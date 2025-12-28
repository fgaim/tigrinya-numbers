"""
Tigrinya number to words converter.

Converts integers to their Tigrinya word representation.
"""

from typing import List, Optional, Union

from .constants import (
    CONJUNCTION,
    CURRENCIES,
    DATE_DAY,
    DATE_MONTH,
    DECIMAL_POINT,
    DEFAULT_CURRENCY,
    DIGITS,
    HUNDRED_COMPOUND,
    HUNDRED_STANDALONE,
    MONTHS,
    ORDINAL_PREFIX,
    ORDINALS_FEMININE,
    ORDINALS_MASCULINE,
    PERCENT,
    SCALES,
    TENS,
    TIME_HOUR,
    TIME_MINUTE,
    TIME_SECOND,
    ZERO_DEFAULT,
    ZERO_LOCAL,
)


def num_to_cardinal(n: Union[int, float], add_hade: bool = True, use_bado: bool = False, feminine: bool = False) -> str:
    """
    Convert a number to Tigrinya cardinal words.

    Supports integers and decimal numbers. For decimals, the integer part is
    read normally, followed by ነጥቢ (point), then each digit of the mantissa
    is read individually.

    Args:
        n: The number to convert (integer or float).
        add_hade: If True, say "ሓደ ሚእቲ" for 100; if False, say "ሚእቲ".
                     Same applies to 1000, 1000000, etc.
        use_bado: If True, use "ባዶ" for zero; if False, use "ዜሮ".
        feminine: If True, use feminine form for 1.

    Returns:
        The Tigrinya word representation of the number.

    Examples:
        >>> num_to_cardinal(0)
        'ዜሮ'
        >>> num_to_cardinal(7)
        'ሸውዓተ'
        >>> num_to_cardinal(15)
        'ዓሰርተ ሓሙሽተ'
        >>> num_to_cardinal(25)
        'ዕስራን ሓሙሽተን'
        >>> num_to_cardinal(127)
        'ሓደ ሚእትን ዕስራን ሸውዓተን'
        >>> num_to_cardinal(5.05)
        'ሓሙሽተ ነጥቢ ዜሮ ሓሙሽተ'
        >>> num_to_cardinal(3.14159)
        'ሰለስተ ነጥቢ ሓደ ኣርባዕተ ሓደ ሓሙሽተ ትሽዓተ'
    """
    # Cardinals have only one instance where gender applies if the number is exactly 1
    if feminine and n == 1:
        return "ሓንቲ"

    # Handle decimals
    if isinstance(n, float) and not n.is_integer():
        str_n = str(n)
        if "." in str_n:
            int_part, dec_part = str_n.split(".")
            int_val = int(int_part)

            # Convert integer part
            int_words = _convert_integer(int_val, add_hade, use_bado)

            # Convert each decimal digit individually
            zero_word = ZERO_LOCAL if use_bado else ZERO_DEFAULT
            dec_digits = []
            for digit in dec_part:
                if digit == "0":
                    dec_digits.append(zero_word)
                else:
                    dec_digits.append(DIGITS[int(digit)])

            return f"{int_words} {DECIMAL_POINT} {' '.join(dec_digits)}"

    # Integer handling
    return _convert_integer(int(n), add_hade, use_bado)


def _convert_integer(n: int, add_hade: bool, use_bado: bool) -> str:
    """Convert an integer to Tigrinya words."""
    if n < 0:
        return "ኣሉታ " + _convert_integer(-n, add_hade, use_bado)

    if n == 0:
        return ZERO_LOCAL if use_bado else ZERO_DEFAULT

    parts = _build_parts(n, add_hade)

    if len(parts) == 1:
        # Standalone: convert ሚእት to ሚእቲ (no conjunction needed)
        return parts[0].replace(HUNDRED_COMPOUND, HUNDRED_STANDALONE)

    # Compound: add ን suffix to each part
    # Key rule: scale words at the end don't get conjunction ONLY if the entire
    # number is a single scale level (standalone). If multiple scale levels are
    # present, ALL scales get conjunction (they're linked parts of a compound).
    result_parts = []
    scale_words = {s[1] for s in SCALES}

    # Count how many distinct scale levels appear in parts
    # If > 1, it's a multi-scale compound and all scales get conjunction
    scales_in_parts = [p for p in parts if any(p.endswith(s) for s in scale_words)]
    is_multi_scale = len(scales_in_parts) > 1

    for i, p in enumerate(parts):
        is_last = i == len(parts) - 1
        if is_last:
            # Final part: check if it's a scale word
            is_scale = any(p.endswith(s) for s in scale_words)
            if is_scale and not is_multi_scale:
                # Single-scale number ending in scale: no conjunction (standalone)
                result_parts.append(p)
            else:
                # Multi-scale, or non-scale final part: add conjunction
                result_parts.append(_add_conjunction(p))
        else:
            result_parts.append(_add_conjunction(p))

    return " ".join(result_parts)


def _build_parts(n: int, add_hade: bool) -> List[str]:
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


def _convert_under_1000(n: int, add_hade: bool) -> List[str]:
    """
    Convert a number 1-999 to a list of parts.

    Returns:
        List of parts. Each part is a string that will receive ን when in a compound number.

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


def num_to_percent(n: Union[int, float], use_bado: bool = False) -> str:
    """
    Convert a number to Tigrinya percentage form.

    Percentages are formed by appending ሚእታዊት (percent) to the cardinal form.

    Args:
        n: The percentage value to convert.
        use_bado: If True, use "ባዶ" for zero; if False, use "ዜሮ".

    Returns:
        The Tigrinya percentage word representation.

    Examples:
        >>> num_to_percent(40)
        'ኣርብዓ ሚእታዊት'
        >>> num_to_percent(100)
        'ሓደ ሚእቲ ሚእታዊት'
        >>> num_to_percent(0)
        'ዜሮ ሚእታዊት'
        >>> num_to_percent(0, use_bado=True)
        'ባዶ ሚእታዊት'
        >>> num_to_percent(25.5)
        'ዕስራን ሓሙሽተን ነጥቢ ሓሙሽተ ሚእታዊት'
    """
    cardinal = num_to_tigrinya(n, use_bado=use_bado)
    return f"{cardinal} {PERCENT}"


def num_to_currency(amount: float, currency: str = DEFAULT_CURRENCY, add_hade: bool = True) -> str:
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
        main_words = num_to_tigrinya(main_amount, add_hade=add_hade)
        parts.append((main_words, main_unit))

    # Subunit amount
    if sub_amount > 0:
        sub_words = num_to_tigrinya(sub_amount, add_hade=add_hade)
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
        # Multiple parts: add conjunction to units, amounts follow cardinal rules
        # Format: X main_unitን Y subunitን (amounts already have ን if compound)
        main_words, main_unit = parts[0]
        sub_words, subunit = parts[1]
        return f"{main_words} {_add_conjunction(main_unit)} {sub_words} {_add_conjunction(subunit)}"


def num_to_date(
    day: int,
    month: int,
    year: Optional[int] = None,
    add_hade: bool = False,
    use_numeric: bool = False,
    month_first: bool = True,
) -> str:
    """
    Convert a date to Tigrinya words.

    Two formats supported:
    - Calendar names (default): Month-name Day [Year] (e.g., ታሕሳስ ዕስራን ሓሙሽተን)
    - Numeric (use_numeric=True): ዕለት Day ወርሒ Month [Year]

    Args:
        day: Day of month (1-31).
        month: Month number (1-12).
        year: Optional year (Gregorian).
        add_hade: Whether to add ሓደ before 1000 in year (default False).
        use_numeric: If True, use numeric month with day/month markers (default False).
        month_first: If True, put month name first, "ሕዳር ዓሰርተ" vs. "ዓሰርተ ሕዳር" (default True).

    Returns:
        The Tigrinya date word representation.

    Raises:
        ValueError: If day or month is out of range.

    Examples:
        >>> num_to_date(25, 12)
        'ታሕሳስ ዕስራን ሓሙሽተን'
        >>> num_to_date(24, 5, 1991)
        'ግንቦት ዕስራን ኣርባዕተን ሽሕን ትሽዓተ ሚእትን ቴስዓን ሓደን'
        >>> num_to_date(24, 5, 1991, add_hade=True)
        'ግንቦት ዕስራን ኣርባዕተን ሓደ ሽሕን ትሽዓተ ሚእትን ቴስዓን ሓደን'
        >>> num_to_date(24, 5, 1991, use_numeric=True)
        'ዕለት ዕስራን ኣርባዕተን ወርሒ ሓሙሽተ ሽሕን ትሽዓተ ሚእትን ቴስዓን ሓደን'
    """
    if not (1 <= month <= 12):
        raise ValueError(f"Month must be 1-12, got {month}")
    if not (1 <= day <= 31):
        raise ValueError(f"Day must be 1-31, got {day}")

    day_words = num_to_tigrinya(day)

    if use_numeric:
        # Numeric format: ዕለት [day] ወርሒ [month] [year]
        month_words = num_to_tigrinya(month)
        parts = [f"{DATE_DAY} {day_words}", f"{DATE_MONTH} {month_words}"]
        if year is not None:
            year_words = num_to_tigrinya(year, add_hade=add_hade)
            parts.append(year_words)
        return " ".join(parts)
    else:
        # Calendar format: Month-name Day [Year]
        month_name = MONTHS[month]
        if year is not None:
            year_words = num_to_tigrinya(year, add_hade=add_hade)
            if month_first:
                return f"{month_name} {day_words} {year_words}"
            return f"{day_words} {month_name} {year_words}"
        if month_first:
            return f"{month_name} {day_words}"
        return f"{day_words} {month_name}"


def num_to_time(
    hour: Optional[int] = None,
    minute: Optional[int] = None,
    second: Optional[int] = None,
    add_deqiq: bool = True,
    add_seat: bool = True,
) -> str:
    """
    Convert a time to Tigrinya words.

    Linguistic Rules:
        1. Zero values for minute and second are omitted (not expressed).
        2. If seconds are provided with minutes, both markers are mandatory.
        3. If hour is omitted (None), minute marker is mandatory.
        4. The add_deqiq option only applies when expressing hour:minute (no seconds).
        5. Conjunction placement: goes on the marker when present, otherwise on the
           final number (simple numbers only; compound numbers already have it).

    Args:
        hour: Hour (0-23). None to express minutes/seconds only.
        minute: Minute (0-59). None to omit; 0 is omitted in output.
        second: Second (0-59). None to omit; 0 is omitted in output.
        add_deqiq: Whether to add minute marker (ደቒቕ). Only applies when second=None.
        add_seat: Whether to add hour prefix (ሰዓት). Defaults to True.

    Returns:
        The Tigrinya time word representation.

    Raises:
        ValueError: If values are out of range.

    Examples:
        >>> num_to_time(3)
        'ሰዓት ሰለስተ'
        >>> num_to_time(3, add_seat=False)
        'ሰለስተ'
        >>> num_to_time(3, 45)
        'ሰዓት ሰለስተን ኣርብዓን ሓሙሽተን ደቒቕን'
        >>> num_to_time(12, 30)
        'ሰዓት ዓሰርተ ክልተን ሰላሳ ደቒቕን'
        >>> num_to_time(12, 30, add_deqiq=False)
        'ሰዓት ዓሰርተ ክልተን ሰላሳን'
        >>> num_to_time(1, 30, 45)
        'ሰዓት ሓደን ሰላሳ ደቒቕን ኣርብዓን ሓሙሽተን ካልኢትን'
        >>> num_to_time(minute=30)
        'ሰላሳ ደቒቕን'
        >>> num_to_time(minute=30, second=15)
        'ሰላሳ ደቒቕን ዓሰርተ ሓሙሽተ ካልኢትን'
    """
    # Validation (0 is valid input for all)
    if hour is not None and not (0 <= hour <= 23):
        raise ValueError(f"Hour must be 0-23, got {hour}")
    if minute is not None and not (0 <= minute <= 59):
        raise ValueError(f"Minute must be 0-59, got {minute}")
    if second is not None and not (0 <= second <= 59):
        raise ValueError(f"Second must be 0-59, got {second}")

    # Normalize 0 to None for output (linguistically, zero values are omitted)
    if minute == 0:
        minute = None
    if second == 0:
        second = None

    # When seconds are provided, minute marker is mandatory (if minutes present)
    if second is not None and minute is not None:
        add_deqiq = True

    parts = []

    # Process hour
    if hour is not None:
        display_hour = hour if hour != 0 else 12
        hour_words = num_to_tigrinya(display_hour)

        if minute is None and second is None:
            # Hour only: ሰዓት X (no conjunction needed)
            if add_seat:
                return f"{TIME_HOUR} {hour_words}"
            else:
                return hour_words
        else:
            # Hour with more parts: conjunction on hour
            if add_seat:
                parts.append(f"{TIME_HOUR} {_add_conjunction(hour_words)}")
            else:
                parts.append(_add_conjunction(hour_words))

    # Determine if there will be multiple components (for conjunction decision)
    has_multiple_components = sum(x is not None for x in (hour, minute, second)) > 1

    # Process minutes
    if minute is not None:
        minute_words = num_to_tigrinya(minute)
        if add_deqiq:
            # Marker: add conjunction only if multiple components
            marker = _add_conjunction(TIME_MINUTE) if has_multiple_components else TIME_MINUTE
            parts.append(f"{minute_words} {marker}")
        else:
            # No marker: conjunction on the number (if simple)
            if not minute_words.endswith(CONJUNCTION):
                minute_words = _add_conjunction(minute_words)
            parts.append(minute_words)

    # Process seconds
    if second is not None:
        second_words = num_to_tigrinya(second)
        # Marker: add conjunction only if multiple components
        marker = _add_conjunction(TIME_SECOND) if has_multiple_components else TIME_SECOND
        parts.append(f"{second_words} {marker}")

    return " ".join(parts)


def num_to_phone(phone: str, use_singles: bool = False, use_bado: bool = False) -> str:
    """
    Convert a phone number to Tigrinya words.

    Phone numbers are read in pairs by default. If a pair starts with 0, it's read
    digit-by-digit; otherwise, it's read as a two-digit number (teens/tens).
    When use_singles=True, all digits are read individually.

    Args:
        phone: Phone number string (digits only, or with common separators).
        use_singles: If True, read all digits individually instead of pairs.
        use_bado: If True, use ባዶ for zero instead of ዜሮ.

    Returns:
        The Tigrinya phone number word representation.

    Examples:
        >>> num_to_phone("07123456")
        'ዜሮ ሸውዓተ ዓሰርተ ክልተ ሰላሳን ኣርባዕተን ሓምሳን ሽድሽተን'
        >>> num_to_phone("07-12-34-56")
        'ዜሮ ሸውዓተ ዓሰርተ ክልተ ሰላሳን ኣርባዕተን ሓምሳን ሽድሽተን'
        >>> num_to_phone("07123456", use_singles=True)
        'ዜሮ ሸውዓተ ሓደ ክልተ ሰለስተ ኣርባዕተ ሓሙሽተ ሽዱሽተ'
        >>> num_to_phone("07", use_bado=True)
        'ባዶ ሸውዓተ'
    """
    # Remove common separators
    digits = "".join(c for c in phone if c.isdigit())

    if not digits:
        raise ValueError("Phone number must contain at least one digit")

    # Select zero word based on use_bado flag
    zero_word = ZERO_LOCAL if use_bado else ZERO_DEFAULT

    parts = []

    if use_singles:
        # Single-digit mode: read each digit individually
        for d in digits:
            digit = int(d)
            if digit == 0:
                parts.append(zero_word)
            else:
                parts.append(DIGITS[digit])
    else:
        # Pair mode: read in pairs
        i = 0
        while i < len(digits):
            if i + 1 < len(digits):
                # We have a pair
                pair = digits[i : i + 2]
                if pair[0] == "0":
                    # Starts with 0: read digit-by-digit
                    parts.append(zero_word)
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


def num_to_tigrinya(n: Union[int, float], add_hade: bool = True, use_bado: bool = False, feminine: bool = False) -> str:
    """
    Convert a number to Tigrinya words.

    This is the primary entry function for number-to-words conversion. Currently,
    it handles cardinal numbers, negatives, and decimals by forwarding to
    `num_to_cardinal`.

    Args:
        n: The number to convert (integer or float).
        add_hade: If True, say "ሓደ ሚእቲ" for 100; if False, say "ሚእቲ".
                     Same applies to 1000, 1000000, etc. Default: True.
        use_bado: If True, use "ባዶ" for zero; if False, use "ዜሮ". Default: False.
        feminine: If True, use feminine form for 1 ("ሓንቲ"). Default: False.

    Returns:
        The Tigrinya word representation of the number.

    Note:
        Future enhancement: This function is intended to become a unified entry
        point that can auto-detect and handle multiple number types (cardinals,
        ordinals, currency, dates, times, percentages, phone numbers) by parsing
        input strings with pattern recognition. For now, it handles cardinal
        numbers only.

    Examples:
        >>> num_to_tigrinya(0)
        'ዜሮ'
        >>> num_to_tigrinya(127)
        'ሓደ ሚእትን ዕስራን ሸውዓተን'
        >>> num_to_tigrinya(3.14)
        'ሰለስተ ነጥቢ ሓደ ኣርባዕተ'
        >>> num_to_tigrinya(-5)
        'ኣሉታ ሓሙሽተ'
    """
    return num_to_cardinal(n, add_hade=add_hade, use_bado=use_bado, feminine=feminine)
