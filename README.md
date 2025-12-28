# Tigrinya Number Verbalizer: Convert Numbers to Spoken Words

[![PyPI](https://img.shields.io/pypi/v/tigrinya-numbers.svg)](https://pypi.org/project/tigrinya-numbers/)
[![License: CC BY-SA 4.0](https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-sa/4.0/)
![GitHub issues](https://img.shields.io/github/issues/fgaim/tigrinya-numbers.svg)
[![Python Versions](https://img.shields.io/pypi/pyversions/tigrinya-numbers.svg)](https://pypi.org/project/tigrinya-numbers/)
[![Paper](https://img.shields.io/badge/Paper-Tigrinya%20Numbers%20to%20Words-blue)](https://arxiv.org/abs/2601.03403)

A Python package to convert numbers to spoken Tigrinya words.

See the paper [**Tigrinya Number Verbalization: Rules, Algorithm, and Implementation**](https://arxiv.org/abs/2601.03403) for details.

## Features

- **Cardinal numbers**: Convert integers and decimals to words (e.g., 127 → ሓደ ሚእትን ዕስራን ሸውዓተን)
- **Ordinal numbers**: 1st-10th with gender support, 11th+ with መበል prefix
- **Percentages**: Cardinal + ሚእታዊት suffix (e.g., 40% → ኣርብዓ ሚእታዊት)
- **Currency**: Nakfa (ERN), Birr (ETB), Dollar (USD), Euro (EUR)
- **Dates**: Read dates with numeric or proper month names (e.g., 24/5 → ግንቦት ዕስራን ኣርባዕተን)
- **Time**: Hour, minute, and second verbalization
- **Phone numbers**: Pair-wise or single-digit reading

### Functions

| Feature | Example Function Call | Example Output |
| ------- | --------------------- | -------------- |
| Cardinals | `num_to_tigrinya(127)` | ሓደ ሚእትን ዕስራን ሸውዓተን |
| Ordinals | `num_to_ordinal(1)` | ቀዳማይ, 25th → መበል ዕስራን ሓሙሽተን |
| Currency | `num_to_currency(5.50)` | ሓሙሽተ ናቕፋን ሓምሳ ሳንቲምን |
| Dates | `num_to_date(25, 12)` | ታሕሳስ ዕስራን ሓሙሽተን |
| Time | `num_to_time(3, 45)` | ሰዓት ሰለስተን ኣርብዓን ሓሙሽተን ደቒቕን |
| Phone | `num_to_phone("07123456")` | ዜሮ ሸውዓተ ዓሰርተ ክልተ ሰላሳን ኣርባዕተን ሓምሳን ሽድሽተን |
| Percent | `num_to_percent(40.5)` | ኣርብዓ ነጥቢ ሓሙሽተ ሚእታዊት |

## Installation

Install package from PyPI:

```bash
pip install tigrinya-numbers

# or using uv

uv pip install tigrinya-numbers
```

Or install from source after cloning the repository:

```bash
pip install -e .

# or using uv

uv sync  # then activate the virtual environment to use package
```

## Usage

### Cardinal Numbers

```python
from tigrinya_numbers import num_to_tigrinya
# The num_to_tigrinya function is an alias for num_to_cardinal

# Basic numbers
num_to_tigrinya(7)      # → 'ሸውዓተ'
num_to_tigrinya(15)     # → 'ዓሰርተ ሓሙሽተ'
num_to_tigrinya(25)     # → 'ዕስራን ሓሙሽተን'
num_to_tigrinya(127)    # → 'ሓደ ሚእትን ዕስራን ሸውዓተን'

# Large numbers
num_to_tigrinya(1_234_567)
# → 'ሓደ ሚልዮንን ክልተ ሚእትን ሰላሳን ኣርባዕተን ሽሕን ሓሙሽተ ሚእትን ሱሳን ሸውዓተን'

# Negative numbers (prefix: ኣሉታ)
num_to_tigrinya(-5)        # → 'ኣሉታ ሓሙሽተ'
num_to_tigrinya(-127)      # → 'ኣሉታ ሓደ ሚእትን ዕስራን ሸውዓተን'

# Decimals (ነጥቢ = point, mantissa digit-by-digit)
num_to_tigrinya(5.05)      # → 'ሓሙሽተ ነጥቢ ዜሮ ሓሙሽተ'
num_to_tigrinya(3.14159)   # → 'ሰለስተ ነጥቢ ሓደ ኣርባዕተ ሓደ ሓሙሽተ ትሽዓተ'

# Options
num_to_tigrinya(0)                     # → 'ዜሮ' (loan word, default)
num_to_tigrinya(0, use_bado=True)      # → 'ባዶ' (local word)

num_to_tigrinya(100)                   # → 'ሓደ ሚእቲ'
num_to_tigrinya(100, add_hade=False)   # → 'ሚእቲ'

# Standalone gender support for 'one'
num_to_tigrinya(1)                  # → 'ሓደ' (masculine)
num_to_tigrinya(1, feminine=True)   # → 'ሓንቲ' (feminine)

# Compounds always use the default form
num_to_tigrinya(21, feminine=True)  # → 'ዕስራን ሓደን'
```

### Ordinal Numbers

```python
from tigrinya_numbers import num_to_ordinal

# Masculine (default)
num_to_ordinal(1)    # → 'ቀዳማይ'
num_to_ordinal(5)    # → 'ሓሙሻይ'
num_to_ordinal(10)   # → 'ዓስራይ'

# Feminine
num_to_ordinal(1, feminine=True)   # → 'ቀዳመይቲ'
num_to_ordinal(3, feminine=True)   # → 'ሳልሰይቲ'

# 11th and above use መበል prefix
num_to_ordinal(11)   # → 'መበል ዓሰርተ ሓደ'
num_to_ordinal(25)   # → 'መበል ዕስራን ሓሙሽተን'
num_to_ordinal(100)  # → 'መበል ሓደ ሚእቲ'
```

### Percentages

```python
from tigrinya_numbers import num_to_percent

# Basic percentages
num_to_percent(40)      # → 'ኣርብዓ ሚእታዊት'
num_to_percent(100)     # → 'ሓደ ሚእቲ ሚእታዊት'

# Compound percentages
num_to_percent(25)      # → 'ዕስራን ሓሙሽተን ሚእታዊት'

# Decimal percentages
num_to_percent(25.5)    # → 'ዕስራን ሓሙሽተን ነጥቢ ሓሙሽተ ሚእታዊት'

# use_bado: Use ባዶ for zero instead of ዜሮ
num_to_percent(0)                    # → 'ዜሮ ሚእታዊት'
num_to_percent(0, use_bado=True)     # → 'ባዶ ሚእታዊት'
```

### Currency

```python
from tigrinya_numbers import num_to_currency

# Eritrean Nakfa (default)
num_to_currency(100)      # → 'ሓደ ሚእቲ ናቕፋ'
num_to_currency(5.50)     # → 'ሓሙሽተ ናቕፋን ሓምሳ ሳንቲምን'
num_to_currency(0.25)     # → 'ዕስራን ሓሙሽተን ሳንቲም'

# Ethiopian Birr
num_to_currency(50, currency="ETB")    # → 'ሓምሳ ብር'

# Other currencies
num_to_currency(1, currency="USD")     # → 'ሓደ ዶላር'
num_to_currency(2, currency="EUR")     # → 'ክልተ ዩሮ'
```

### Dates

```python
from tigrinya_numbers import num_to_date

# Default format: Month-name Day [Year]
num_to_date(25, 12)        # → 'ታሕሳስ ዕስራን ሓሙሽተን'
num_to_date(15, 6)         # → 'ሰነ ዓሰርተ ሓሙሽተ'
num_to_date(24, 5, 1991)   # → 'ግንቦት ዕስራን ኣርባዕተን ሽሕን ትሽዓተ ሚእትን ቴስዓን ሓደን'

# add_hade: Include ሓደ before 1000 in year
num_to_date(24, 5, 1991, add_hade=True)
# → 'ግንቦት ዕስራን ኣርባዕተን ሓደ ሽሕን ትሽዓተ ሚእትን ቴስዓን ሓደን'

# use_numeric: Numeric format with ዕለት (day) and ወርሒ (month) markers
num_to_date(24, 5, 1991, use_numeric=True)
# → 'ዕለት ዕስራን ኣርባዕተን ወርሒ ሓሙሽተ ሽሕን ትሽዓተ ሚእትን ቴስዓን ሓደን'

# month_first: Put day before month name (calendar format only)
num_to_date(10, 11)                      # → 'ሕዳር ዓሰርተ' (default: month first)
num_to_date(10, 11, month_first=False)   # → 'ዓሰርተ ሕዳር' (day first)
```

### Time

```python
from tigrinya_numbers import num_to_time

# On the hour
num_to_time(3)    # → 'ሰዓት ሰለስተ'
num_to_time(12)   # → 'ሰዓት ዓሰርተ ክልተ'

# With minutes
num_to_time(3, 45)   # → 'ሰዓት ሰለስተን ኣርብዓን ሓሙሽተን ደቒቕን'
num_to_time(12, 30)  # → 'ሰዓት ዓሰርተ ክልተን ሰላሳ ደቒቕን'

# With minutes and seconds
num_to_time(3, 30, 15)   # → 'ሰዓት ሰለስተን ሰላሳ ደቒቕን ዓሰርተ ሓሙሽተ ካልኢትን'

# Minutes and seconds only
num_to_time(minute=30, second=15)  # → 'ሰላሳ ደቒቕን ዓሰርተ ሓሙሽተ ካልኢትን'

# add_deqiq: Omit minute marker (ደቒቕ)
num_to_time(12, 30, add_deqiq=False)  # → 'ሰዓት ዓሰርተ ክልተን ሰላሳን'

# add_seat: Omit hour prefix (ሰዓት)
num_to_time(3, add_seat=False)        # → 'ሰለስተ'
num_to_time(3, 45, add_seat=False)    # → 'ሰለስተን ኣርብዓን ሓሙሽተን ደቒቕን'
```

### Phone Numbers

```python
from tigrinya_numbers import num_to_phone

# Default: Pairs starting with 0 are read digit-by-digit
num_to_phone("07")         # → 'ዜሮ ሸውዓተ'

# Other pairs are read as two-digit numbers
num_to_phone("12")         # → 'ዓሰርተ ክልተ'
num_to_phone("34")         # → 'ሰላሳን ኣርባዕተን'

# Full phone number
num_to_phone("07123456")   # → 'ዜሮ ሸውዓተ ዓሰርተ ክልተ ሰላሳን ኣርባዕተን ሓምሳን ሽዱሽተን'

# Separators are ignored
num_to_phone("07-12-34-56")   # Same as "07123456"

# use_singles: Read all digits individually (not as pairs)
num_to_phone("1234", use_singles=True)  # → 'ሓደ ክልተ ሰለስተ ኣርባዕተ'
num_to_phone("07123456", use_singles=True)
# → 'ዜሮ ሸውዓተ ሓደ ክልተ ሰለስተ ኣርባዕተ ሓሙሽተ ሽዱሽተ'

# use_bado: Use ባዶ for zero instead of ዜሮ
num_to_phone("07", use_bado=True)  # → 'ባዶ ሸውዓተ'

# Combined flags
num_to_phone("07-34", use_singles=True, use_bado=True)
# → 'ባዶ ሸውዓተ ሰለስተ ኣርባዕተ'
```

## Tigrinya Number System Rules

This package implements Tigrinya number verbalization following these rules:

### Basic Structure

| Range | Format | Example |
|-------|--------|---------|
| 1-10 | Single words | 7 → ሸውዓተ |
| 11-19 | ዓሰርተ + digit (no conjunction) | 15 → ዓሰርተ ሓሙሽተ |
| 20-90 | Unique words | 30 → ሰላሳ |
| 21-99 | Tens + ones (with ን) | 25 → ዕስራን ሓሙሽተን |
| 100+ | Scale + cardinal | 127 → ሓደ ሚእትን ዕስራን ሸውዓተን |

### Conjunction (ን)

The suffix **ን** ("and") connects parts in compound numbers:

- **Standalone numbers** have no ን: `7 → ሸውዓተ`
- **Compound numbers** add ን to each part: `25 → ዕስራን ሓሙሽተን`
- **Exception:** Teens (11-19) don't take internal ን but do at the end in compounds: `115 → ሓደ ሚእትን ዓሰርተ ሓሙሽተን`

### Scales Supported

| Value | Word |
|-------|------|
| 100 | ሚእቲ / ሚእት |
| 1,000 | ሽሕ |
| 10⁶ | ሚልዮን |
| 10⁹  | ቢልዮን |
| 10¹² | ትሪልዮን |
| 10¹⁵ | ኳድሪልዮን |
| 10¹⁸ | ኵንቲልዮን |
| 10²¹ | ሰክስቲልዮን |
| 10²⁴ | ሰፕቲልዮን |

### Hundred Forms

- **ሚእቲ** when standalone: `200 → ክልተ ሚእቲ`
- **ሚእት** before ን: `203 → ክልተ ሚእትን ሰለስተን`

### Ordinals 1st-10th

| # | Masculine | Feminine |
|---|-----------|----------|
| 1st | ቀዳማይ | ቀዳመይቲ |
| 2nd | ካልኣይ | ካልአይቲ |
| 3rd | ሳልሳይ | ሳልሰይቲ |
| 4th | ራብዓይ | ራብዐይቲ |
| 5th | ሓሙሻይ | ሓሙሸይቲ |
| 6th | ሻድሻይ | ሻድሸይቲ |
| 7th | ሻውዓይ | ሻውዐይቲ |
| 8th | ሻምናይ | ሻምነይቲ |
| 9th | ታሽዓይ | ታሽዐይቲ |
| 10th | ዓስራይ | ዓስረይቲ |

### Month Names

| # | Tigrinya |
|---|----------|
| 1 | ጥሪ |
| 2 | ለካቲት |
| 3 | መጋቢት |
| 4 | ሚያዝያ |
| 5 | ግንቦት |
| 6 | ሰነ |
| 7 | ሓምለ |
| 8 | ነሓሰ |
| 9 | መስከረም |
| 10 | ጥቅምቲ |
| 11 | ሕዳር |
| 12 | ታሕሳስ |

## API Reference

### `num_to_tigrinya(n, add_hade=True, use_bado=False, feminine=False)`

Convert a number (integer, negative, or decimal) to Tigrinya words.

**Parameters:**

- `n` (int | float): The number to convert
- `add_hade` (bool): If `True`, include "ሓደ" before scales (e.g., "ሓደ ሚእቲ" for 100). Default: `True`
- `use_bado` (bool): If `True`, use "ባዶ" for zero; if `False`, use "ዜሮ". Default: `False`
- `feminine` (bool): If `True` and n=1, return "ሓንቲ" instead of "ሓደ". Default: `False`

**Returns:** `str` - The Tigrinya representation

---

### `num_to_ordinal(n, feminine=False)`

Convert a number to its ordinal form (1st-10th suppletive, 11th+ with መበል prefix).

**Parameters:**

- `n` (int): The number to convert (must be ≥ 1)
- `feminine` (bool): If `True`, use feminine forms (e.g., ቀዳመይቲ instead of ቀዳማይ). Default: `False`

**Returns:** `str` - The Tigrinya ordinal

---

### `num_to_currency(amount, currency="ERN")`

Convert an amount to Tigrinya currency words.

**Parameters:**

- `amount` (float): The monetary amount
- `currency` (str): Currency code - "ERN" (Nakfa), "ETB" (Birr), "USD", "EUR". Default: `"ERN"`

**Returns:** `str` - The Tigrinya currency expression

---

### `num_to_date(day, month, year=None, add_hade=False, use_numeric=False, month_first=True)`

Convert a date to Tigrinya words.

**Parameters:**

- `day` (int): Day of month (1-31)
- `month` (int): Month number (1-12)
- `year` (int | None): Optional year (Gregorian)
- `add_hade` (bool): Include "ሓደ" before 1000 in year. Default: `False`
- `use_numeric` (bool): Use numeric format with ዕለት/ወርሒ markers. Default: `False`
- `month_first` (bool): Put month name before day (calendar format only). Default: `True`

**Returns:** `str` - The Tigrinya date expression

---

### `num_to_time(hour=None, minute=None, second=None, add_deqiq=True, add_seat=True)`

Convert time to Tigrinya words.

**Parameters:**

- `hour` (int | None): Hour (0-23, where 0 displays as 12)
- `minute` (int | None): Minute (0-59)
- `second` (int | None): Second (0-59)
- `add_deqiq` (bool): Include minute marker "ደቒቕ". Default: `True`
- `add_seat` (bool): Include hour prefix "ሰዓት". Default: `True`

**Returns:** `str` - The Tigrinya time expression

---

### `num_to_phone(phone, use_singles=False, use_bado=False)`

Convert a phone number to Tigrinya words.

**Parameters:**

- `phone` (str): Phone number string (digits, with optional separators)
- `use_singles` (bool): Read all digits individually instead of pairs. Default: `False`
- `use_bado` (bool): Use "ባዶ" for zero instead of "ዜሮ". Default: `False`

**Returns:** `str` - The Tigrinya phone number verbalization

---

### `num_to_percent(n, use_bado=False)`

Convert a number to its Tigrinya percentage form.

**Parameters:**

- `n` (int | float): The percentage value to convert
- `use_bado` (bool): Use "ባዶ" for zero instead of "ዜሮ". Default: `False`

**Returns:** `str` - The Tigrinya percentage expression (cardinal + ሚእታዊት)

## Running Tests

```bash
pip install -e ".[dev]"
pytest tests/ -v
```

Or using `uv`:

```bash
uv sync --extra dev
uv run pytest tests/ -v
```

## Citation

If you use this package for your research, you can cite as follows:

```bibtex
@misc{gaim-2026-tigrinya-numbers,
    title={{Tigrinya Number Verbalization: Rules, Algorithm, and Implementation}}, 
    author={Fitsum Gaim and Issayas Tesfamariam},
    year={2026},
    eprint={2601.03403},
    archivePrefix={arXiv},
    primaryClass={cs.CL},
    url={https://arxiv.org/abs/2601.03403},
}
```

## License

This work is licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/).
