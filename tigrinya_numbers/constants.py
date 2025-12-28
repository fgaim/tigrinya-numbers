"""
Tigrinya number word constants.

The default use of words aligns with the Eritrean dialect of Tigrinya.
"""

# Basic digits 1-10
DIGITS = {
    1: "ሓደ",
    2: "ክልተ",
    3: "ሰለስተ",
    4: "ኣርባዕተ",
    5: "ሓሙሽተ",
    6: "ሽዱሽተ",
    7: "ሸውዓተ",
    8: "ሸሞንተ",
    9: "ትሽዓተ",
    10: "ዓሰርተ",
}

# Tens 20-90
TENS = {
    20: "ዕስራ",
    30: "ሰላሳ",
    40: "ኣርብዓ",
    50: "ሓምሳ",
    60: "ሱሳ",
    70: "ሰብዓ",
    80: "ሰማንያ",
    90: "ቴስዓ",
}

# Hundred forms
HUNDRED_COMPOUND = "ሚእት"  # Used in compounds (before ን)
HUNDRED_STANDALONE = "ሚእቲ"  # Used when standing alone

# Large number scales (descending order for processing)
SCALES = [
    (10**24, "ሰፕቲልዮን"),
    (10**21, "ሰክስቲልዮን"),
    (10**18, "ኵንቲልዮን"),
    (10**15, "ኳድሪልዮን"),
    (10**12, "ትሪልዮን"),
    (10**9, "ቢልዮን"),
    (10**6, "ሚልዮን"),
    (10**3, "ሽሕ"),
]

# Zero words
ZERO_DEFAULT = "ዜሮ"  # Loan word (default)
ZERO_LOCAL = "ባዶ"  # Local word

# Conjunction suffix
CONJUNCTION = "ን"

# Decimal point
DECIMAL_POINT = "ነጥቢ"

# Percent
PERCENT = "ሚእታዊት"

# =============================================================================
# ORDINALS
# =============================================================================

# Ordinals 1st-10th (masculine)
ORDINALS_MASCULINE = {
    1: "ቀዳማይ",
    2: "ካልኣይ",
    3: "ሳልሳይ",
    4: "ራብዓይ",
    5: "ሓሙሻይ",
    6: "ሻድሻይ",
    7: "ሻውዓይ",
    8: "ሻምናይ",
    9: "ታሽዓይ",
    10: "ዓስራይ",
}

# Ordinals 1st-10th (feminine)
ORDINALS_FEMININE = {
    1: "ቀዳመይቲ",
    2: "ካልአይቲ",
    3: "ሳልሰይቲ",
    4: "ራብዐይቲ",
    5: "ሓሙሸይቲ",
    6: "ሻድሸይቲ",
    7: "ሻውዐይቲ",
    8: "ሻምነይቲ",
    9: "ታሽዐይቲ",
    10: "ዓስረይቲ",
}

# Prefix for ordinals 11th and above
ORDINAL_PREFIX = "መበል"

# =============================================================================
# CURRENCY
# =============================================================================

# Currency definitions: (main_unit, subunit, subunits_per_main)
CURRENCIES = {
    "ERN": ("ናቕፋ", "ሳንቲም", 100),  # Eritrean Nakfa (default)
    "ETB": ("ብር", "ሳንቲም", 100),  # Ethiopian Birr
    "USD": ("ዶላር", "ሳንቲም", 100),  # US Dollar
    "EUR": ("ዩሮ", "ሳንቲም", 100),  # Euro
}

DEFAULT_CURRENCY = "ERN"

# =============================================================================
# DATE AND TIME
# =============================================================================

# Gregorian month names (1-12)
MONTHS = {
    1: "ጥሪ",
    2: "ለካቲት",
    3: "መጋቢት",
    4: "ሚያዝያ",
    5: "ግንቦት",
    6: "ሰነ",
    7: "ሓምለ",
    8: "ነሓሰ",
    9: "መስከረም",
    10: "ጥቅምቲ",
    11: "ሕዳር",
    12: "ታሕሳስ",
}

# Time words
TIME_HOUR = "ሰዓት"
TIME_MINUTE = "ደቒቕ"
TIME_SECOND = "ካልኢት"

# Date markers (for numeric format)
DATE_DAY = "ዕለት"
DATE_MONTH = "ወርሒ"

# Year era (AD)
YEAR_ERA = "ሓባራዊ ዘመን"
