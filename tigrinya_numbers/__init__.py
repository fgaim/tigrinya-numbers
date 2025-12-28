"""
Tigrinya Numbers - Convert integers to Tigrinya words.

A clean Python package for converting numbers to their Tigrinya word representation.

Example:
    >>> from tigrinya_numbers import num_to_tigrinya
    >>> num_to_tigrinya(127)
    'ሓደ ሚእትን ዕስራን ሸውዓተን'

    >>> from tigrinya_numbers import num_to_ordinal
    >>> num_to_ordinal(1)
    'ቀዳማይ'

    >>> from tigrinya_numbers import num_to_currency
    >>> num_to_currency(5.50)
    'ሓሙሽተ ናቕፋን ሓምሳ ሳንቲምን'
"""

from .constants import (
    CURRENCIES,
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
    YEAR_ERA,
    ZERO_DEFAULT,
    ZERO_LOCAL,
)
from .converter import (
    num_to_cardinal,
    num_to_currency,
    num_to_date,
    num_to_ordinal,
    num_to_percent,
    num_to_phone,
    num_to_tigrinya,
    num_to_time,
)

__version__ = "0.2.0"
__all__ = [
    # Functions
    "num_to_cardinal",
    "num_to_tigrinya",
    "num_to_ordinal",
    "num_to_percent",
    "num_to_currency",
    "num_to_date",
    "num_to_time",
    "num_to_phone",
    # Constants
    "DIGITS",
    "TENS",
    "HUNDRED_COMPOUND",
    "HUNDRED_STANDALONE",
    "SCALES",
    "ZERO_DEFAULT",
    "ZERO_LOCAL",
    "PERCENT",
    "ORDINALS_MASCULINE",
    "ORDINALS_FEMININE",
    "ORDINAL_PREFIX",
    "CURRENCIES",
    "DEFAULT_CURRENCY",
    "MONTHS",
    "TIME_HOUR",
    "TIME_MINUTE",
    "YEAR_ERA",
]
