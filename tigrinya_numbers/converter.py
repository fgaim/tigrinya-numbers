"""
Tigrinya number to words converter.

Converts integers to their Tigrinya word representation.
"""

from .constants import CONJUNCTION, DIGITS, HUNDRED, HUNDRED_STANDALONE, SCALES, TENS, ZERO_DEFAULT, ZERO_LOCAL


def num_to_tigrinya(
    n: int,
    add_hade: bool = True,
    use_bado: bool = False,
) -> str:
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
        raise ValueError("Negative numbers are not supported")

    if n == 0:
        return ZERO_LOCAL if use_bado else ZERO_DEFAULT

    parts = _build_parts(n, add_hade)

    if len(parts) == 1:
        # Standalone: convert ሚእት to ሚእቲ (no conjunction needed)
        return parts[0].replace(HUNDRED, HUNDRED_STANDALONE)
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
            parts.append(HUNDRED)
        else:
            parts.append(f"{DIGITS[h]} {HUNDRED}")

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
