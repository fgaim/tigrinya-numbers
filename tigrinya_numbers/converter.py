"""
Tigrinya number to words converter.

Converts integers to their Tigrinya word representation.
"""

from .constants import (
    CONJUNCTION,
    CURRENCIES,
    DEFAULT_CURRENCY,
    DIGITS,
    HUNDRED_COMPOUND,
    HUNDRED_STANDALONE,
    MONTHS,
    ORDINAL_PREFIX,
    ORDINALS_FEMININE,
    ORDINALS_MASCULINE,
    SCALES,
    TENS,
    TIME_HOUR,
    TIME_MINUTE,
    ZERO_DEFAULT,
    ZERO_LOCAL,
)

# =============================================================================
# CARDINAL NUMBERS
# =============================================================================


def num_to_tigrinya(n: int, add_hade: bool = True, use_bado: bool = False) -> str:
    """
    Convert a number to Tigrinya words.

    Args:
        n: The number to convert (must be non-negative).
        add_hade: If True, say "ሓደ ሚእቲ" for 100; if False, say "ሚእቲ".
                     Same applies to 1000, 1000000, etc.
        use_bado: If True, use "ባዶ" for zero; if False, use "ዜሮ".

    Returns:
        The Tigrinya word representation of the number.

    Raises:
        ValueError: If n is negative.

    Examples:
        >>> num_to_tigrinya(0)
        'ዜሮ'
        >>> num_to_tigrinya(7)
        'ሸውዓተ'
        >>> num_to_tigrinya(15)
        'ዓሰርተ ሓሙሽተ'
        >>> num_to_tigrinya(25)
        'ዕስራን ሓሙሽተን'
        >>> num_to_tigrinya(127)
        'ሓደ ሚእትን ዕስራን ሸውዓተን'
    """
    if n < 0:
        return "ኣሉታ " + num_to_tigrinya(-n, add_hade, use_bado)

    if n == 0:
        return ZERO_LOCAL if use_bado else ZERO_DEFAULT

    parts = _build_parts(n, add_hade)

    if len(parts) == 1:
        # Standalone: convert ሚእት to ሚእቲ (no conjunction needed)
        return parts[0].replace(HUNDRED_COMPOUND, HUNDRED_STANDALONE)
    else:
        # Compound: add ን suffix to each part
        return " ".join(_add_conjunction(p) for p in parts)


def _build_parts(n: int, add_hade: bool) -> list[str]:
    """
    Build list of parts for a number.

    A "part" is a unit that receives the conjunction suffix ን when
    the number is compound (has multiple parts).

    Rules:
    - Simple multipliers (1-19, round tens, round hundreds) combine
      with their scale word as a single part.
    - Compound multipliers (like 25, 127) produce multiple parts,
      and the scale word becomes its own separate part.
    """
    parts = []

    # Process each scale from largest to smallest
    for scale_value, scale_word in SCALES:
        if n >= scale_value:
            multiplier = n // scale_value
            n = n % scale_value

            mult_parts = _convert_under_1000(multiplier, add_hade)

            if _is_simple(multiplier):
                # Simple multiplier: combine with scale as ONE part
                # e.g., 2000 → "ክልተ ሽሕ" (one part)
                # e.g., 15000 → "ዓሰርተ ሓሙሽተ ሽሕ" (one part)
                if multiplier == 1 and not add_hade:
                    parts.append(scale_word)
                else:
                    parts.append(mult_parts[0] + " " + scale_word)
            else:
                # Compound multiplier: scale becomes SEPARATE part
                # e.g., 25000 → ["ዕስራ", "ሓሙሽተ", "ሽሕ"] (three parts)
                parts.extend(mult_parts)
                parts.append(scale_word)

    # Process remainder (1-999)
    if n > 0:
        parts.extend(_convert_under_1000(n, add_hade))

    return parts


def _convert_under_1000(n: int, add_hade: bool) -> list[str]:
    """
    Convert a number 1-999 to a list of parts.

    Returns:
        List of parts. Each part is a string that will receive ן
        when in a compound number.

    Examples:
        7   → ["ሸውዓተ"]
        15  → ["ዓሰርተ ሓሙሽተ"]  (teen: single part, space-separated)
        25  → ["ዕስራ", "ሓሙሽተ"]
        127 → ["ሓደ ሚእት", "ዕስራ", "ሸውዓተ"]
    """
    if n <= 0:
        return []

    parts = []

    # Handle hundreds
    if n >= 100:
        h = n // 100
        n = n % 100
        if h == 1 and not add_hade:
            parts.append(HUNDRED_COMPOUND)
        else:
            parts.append(f"{DIGITS[h]} {HUNDRED_COMPOUND}")

    # Handle remainder (1-99)
    if n > 0:
        if n <= 10:
            # Single digit
            parts.append(DIGITS[n])
        elif n <= 19:
            # Teen (11-19): single part with space, NO internal conjunction
            # e.g., 15 → "ዓሰርተ ሓሙሽተ"
            parts.append(f"{DIGITS[10]} {DIGITS[n - 10]}")
        else:
            # Compound tens (20-99)
            tens_digit = (n // 10) * 10
            ones_digit = n % 10
            parts.append(TENS[tens_digit])
            if ones_digit > 0:
                parts.append(DIGITS[ones_digit])

    return parts


def _is_simple(n: int) -> bool:
    """
    Check if n (1-999) produces a single part.

    Simple numbers combine with scale words as one unit.
    Compound numbers cause the scale word to become a separate part.

    Simple: 1-19, 20/30/.../90, 100/200/.../900
    Compound: everything else (21-29, 31-39, ..., 101-999 except round hundreds)
    """
    if n <= 0:
        return False
    if n <= 19:
        # Digits and teens
        return True
    if n < 100 and n % 10 == 0:
        # Round tens: 20, 30, ..., 90
        return True
    if n % 100 == 0:
        # Round hundreds: 100, 200, ..., 900
        return True
    return False


def _add_conjunction(part: str) -> str:
    """Add the conjunction suffix ን to a part."""
    return part + CONJUNCTION


# =============================================================================
# ORDINAL NUMBERS
# =============================================================================


def num_to_ordinal(n: int, feminine: bool = False) -> str:
    """
    Convert a number to Tigrinya ordinal words.

    Args:
        n: The number to convert (must be positive).
        feminine: If True, use feminine form; if False, use masculine (default).

    Returns:
        The Tigrinya ordinal word representation.

    Raises:
        ValueError: If n is less than 1.

    Examples:
        >>> num_to_ordinal(1)
        'ቀዳማይ'
        >>> num_to_ordinal(1, feminine=True)
        'ቀዳመይቲ'
        >>> num_to_ordinal(10)
        'ዓስራይ'
        >>> num_to_ordinal(25)
        'መበል ዕስራን ሓሙሽተን'
    """
    if n < 1:
        raise ValueError("Ordinal numbers must be positive (>= 1)")

    # 1st-10th have unique forms
    if n <= 10:
        if feminine:
            return ORDINALS_FEMININE[n]
        else:
            return ORDINALS_MASCULINE[n]

    # 11th and above: መበል + cardinal
    cardinal = num_to_tigrinya(n)
    return f"{ORDINAL_PREFIX} {cardinal}"


# =============================================================================
# CURRENCY
# =============================================================================


def num_to_currency(amount: float, currency: str = DEFAULT_CURRENCY) -> str:
    """
    Convert a monetary amount to Tigrinya words.

    Args:
        amount: The amount to convert (must be non-negative).
        currency: Currency code ("ERN", "ETB", "USD", "EUR"). Default is "ERN" (Nakfa).

    Returns:
        The Tigrinya currency word representation.

    Raises:
        ValueError: If amount is negative or currency is unsupported.

    Examples:
        >>> num_to_currency(5.50)
        'ሓሙሽተ ናቕፋን ሓምሳ ሳንቲምን'
        >>> num_to_currency(100)
        'ሓደ ሚእቲ ናቕፋ'
        >>> num_to_currency(0.25)
        'ዕስራን ሓሙሽተን ሳንቲም'
    """
    if amount < 0:
        raise ValueError("Amount cannot be negative")

    if currency not in CURRENCIES:
        raise ValueError(f"Unsupported currency: {currency}. Supported: {list(CURRENCIES.keys())}")

    main_unit, subunit, subunits_per_main = CURRENCIES[currency]

    # Split into main and sub amounts
    main_amount = int(amount)
    sub_amount = round((amount - main_amount) * subunits_per_main)

    # Handle rounding edge case
    if sub_amount >= subunits_per_main:
        main_amount += 1
        sub_amount = 0

    parts = []

    # Main amount
    if main_amount > 0:
        main_words = num_to_tigrinya(main_amount)
        parts.append((main_words, main_unit))

    # Subunit amount
    if sub_amount > 0:
        sub_words = num_to_tigrinya(sub_amount)
        parts.append((sub_words, subunit))

    # Handle zero amount
    if not parts:
        return f"{ZERO_DEFAULT} {main_unit}"

    # Format output
    if len(parts) == 1:
        # Single part: no conjunction
        words, unit = parts[0]
        return f"{words} {unit}"
    else:
        # Multiple parts: add conjunction
        # Format: Xን main_unitን Yን subunitን
        main_words, main_unit = parts[0]
        sub_words, subunit = parts[1]
        return f"{_add_conjunction(main_words)} {_add_conjunction(main_unit)} {_add_conjunction(sub_words)} {_add_conjunction(subunit)}"


# =============================================================================
# DATE
# =============================================================================


def num_to_date(day: int, month: int, year: int | None = None) -> str:
    """
    Convert a date to Tigrinya words.

    Format: Month Day [Year] (e.g., ታሕሳስ ዕስራን ሓሙሽተን)

    Args:
        day: Day of month (1-31).
        month: Month number (1-12).
        year: Optional year (Gregorian).

    Returns:
        The Tigrinya date word representation.

    Raises:
        ValueError: If day or month is out of range.

    Examples:
        >>> num_to_date(25, 12)
        'ታሕሳስ ዕስራን ሓሙሽተን'
        >>> num_to_date(1, 1, 2025)
        'ጥሪ ሓደ ክልተ ሽሕን ዕስራን ሓሙሽተን'
        >>> num_to_date(15, 6)
        'ሰነ ዓሰርተ ሓሙሽተ'
    """
    if not (1 <= month <= 12):
        raise ValueError(f"Month must be 1-12, got {month}")
    if not (1 <= day <= 31):
        raise ValueError(f"Day must be 1-31, got {day}")

    month_name = MONTHS[month]
    day_words = num_to_tigrinya(day)

    if year is not None:
        year_words = num_to_tigrinya(year)
        return f"{month_name} {day_words} {year_words}"
    else:
        return f"{month_name} {day_words}"


# =============================================================================
# TIME
# =============================================================================


def num_to_time(hour: int, minute: int = 0) -> str:
    """
    Convert a time to Tigrinya words.

    Format: ሰዓት X [Yን ደቒቕን] (e.g., ሰዓት ሰለስተን ኣርብዓን ሓሙሽተን ደቒቕን)

    Args:
        hour: Hour (0-23 or 1-12).
        minute: Minute (0-59). Default is 0.

    Returns:
        The Tigrinya time word representation.

    Raises:
        ValueError: If hour or minute is out of range.

    Examples:
        >>> num_to_time(3, 0)
        'ሰዓት ሰለስተ'
        >>> num_to_time(3, 45)
        'ሰዓት ሰለስተን ኣርብዓን ሓሙሽተን ደቒቕን'
        >>> num_to_time(12, 30)
        'ሰዓት ዓሰርተ ክልተን ሰላሳን ደቒቕን'
    """
    if not (0 <= hour <= 23):
        raise ValueError(f"Hour must be 0-23, got {hour}")
    if not (0 <= minute <= 59):
        raise ValueError(f"Minute must be 0-59, got {minute}")

    # Handle hour 0 as 12
    display_hour = hour if hour != 0 else 12

    hour_words = num_to_tigrinya(display_hour)

    if minute == 0:
        # On the hour: ሰዓት X
        return f"{TIME_HOUR} {hour_words}"
    else:
        # With minutes: ሰዓት Xን Yን ደቒቕን
        minute_words = num_to_tigrinya(minute)
        # If minute_words is compound (has spaces and ends with ן), don't add another
        if " " in minute_words and minute_words.endswith(CONJUNCTION):
            minute_with_conj = minute_words
        else:
            minute_with_conj = _add_conjunction(minute_words)
        return f"{TIME_HOUR} {_add_conjunction(hour_words)} {minute_with_conj} {_add_conjunction(TIME_MINUTE)}"


# =============================================================================
# PHONE NUMBERS
# =============================================================================


def num_to_phone(phone: str) -> str:
    """
    Convert a phone number to Tigrinya words.

    Phone numbers are read in pairs. If a pair starts with 0, it's read
    digit-by-digit; otherwise, it's read as a two-digit number (teens/tens).

    Args:
        phone: Phone number string (digits only, or with common separators).

    Returns:
        The Tigrinya phone number word representation.

    Examples:
        >>> num_to_phone("07123456")
        'ዜሮ ሸውዓተ ዓሰርተ ክልተ ሰላሳን ኣርባዕተን ሓምሳን ሽድሽተን'
        >>> num_to_phone("07-12-34-56")
        'ዜሮ ሸውዓተ ዓሰርተ ክልተ ሰላሳን ኣርባዕተን ሓምሳን ሽድሽተን'
    """
    # Remove common separators
    digits = "".join(c for c in phone if c.isdigit())

    if not digits:
        raise ValueError("Phone number must contain at least one digit")

    parts = []

    i = 0
    while i < len(digits):
        if i + 1 < len(digits):
            # We have a pair
            pair = digits[i : i + 2]
            if pair[0] == "0":
                # Starts with 0: read digit-by-digit
                parts.append(ZERO_DEFAULT)
                parts.append(DIGITS[int(pair[1])])
            else:
                # Read as two-digit number
                num = int(pair)
                parts.append(num_to_tigrinya(num))
            i += 2
        else:
            # Single remaining digit
            parts.append(DIGITS[int(digits[i])])
            i += 1

    return " ".join(parts)
