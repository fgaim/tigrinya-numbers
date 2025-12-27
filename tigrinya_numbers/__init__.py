"""
Tigrinya Numbers - Convert integers to Tigrinya words.

A clean Python package for converting numbers to their Tigrinya word representation.

Example:
    >>> from tigrinya_numbers import num_to_tigrinya
    >>> num_to_tigrinya(127)
    'ሓደ ሚእትን ዕስራን ሸውዓተን'
"""

from .constants import DIGITS, HUNDRED, HUNDRED_STANDALONE, SCALES, TENS, ZERO_DEFAULT, ZERO_LOCAL
from .converter import num_to_tigrinya

__version__ = "1.0.0"
__all__ = [
    "num_to_tigrinya",
    "DIGITS",
    "TENS",
    "HUNDRED",
    "HUNDRED_STANDALONE",
    "SCALES",
    "ZERO_DEFAULT",
    "ZERO_LOCAL",
]
