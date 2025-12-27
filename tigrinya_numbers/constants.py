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
    6: "ሽድሽተ",
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
HUNDRED = "ሚእት"  # Used in compounds (before ን)
HUNDRED_STANDALONE = "ሚእቲ"  # Used when standing alone

# Large number scales (descending order for processing)
SCALES = [
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
