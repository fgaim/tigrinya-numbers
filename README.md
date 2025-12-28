# Tigrinya Numbers to Words

A Python package to convert numbers to Tigrinya words.

## Features

- **Cardinal numbers**: Convert integers to words (e.g., 127 → ሓደ ሚእትን ዕስራን ሸውዓተን)
- **Ordinal numbers**: 1st-10th with gender support, 11th+ with መበል prefix
- **Currency**: Nakfa (ERN), Birr (ETB), Dollar (USD), Euro (EUR)
- **Dates**: Gregorian calendar with Tigrinya month names
- **Time**: Hour and minute verbalization
- **Phone numbers**: Pair-based reading with special handling for leading zeros

### Functions

| Feature | Function Call | Example Output |
|---------|----------|---------|
| Cardinals | `num_to_tigrinya(127)` | ሓደ ሚእትን ዕስራን ሸውዓተን |
| Ordinals | `num_to_ordinal(1)` | ቀዳማይ, 25th → መበል ዕስራን ሓሙሽተን |
| Currency | `num_to_currency(5.50)` | ሓሙሽተ ናቕፋን ሓምሳ ሳንቲምን |
| Dates | `num_to_date(25, 12)` | ታሕሳስ ዕስራን ሓሙሽተን |
| Time | `num_to_time(3, 45)` | ሰዓት ሰለስተን ኣርብዓን ሓሙሽተን ደቒቕን |
| Phone | `num_to_phone("07123456")` | ዜሮ ሸውዓተ ዓሰርተ ክልተ ሰላሳን ኣርባዕተን ሓምሳን ሽድሽተን |

## Installation

Install package from PyPI:

```bash
pip install tigrinya-numbers

# or

uv pip install tigrinya-numbers
```

Or install from source after cloning the repository:

```bash
pip install -e .

# or

uv sync  # then activate the virtual environment to use packagex
```

## Usage

### Cardinal Numbers

```python
from tigrinya_numbers import num_to_tigrinya

# Basic numbers
num_to_tigrinya(7)      # → 'ሸውዓተ'
num_to_tigrinya(15)     # → 'ዓሰርተ ሓሙሽተ'
num_to_tigrinya(25)     # → 'ዕስራን ሓሙሽተን'
num_to_tigrinya(127)    # → 'ሓደ ሚእትን ዕስራን ሸውዓተን'

# Large numbers
num_to_tigrinya(1_234_567)
# → 'ሓደ ሚልዮንን ክልተ ሚእትን ሰላሳን ኣርባዕተን ሽሕን ሓሙሽተ ሚእትን ሱሳን ሸውዓተን'

# Options
num_to_tigrinya(0)                     # → 'ዜሮ' (loan word, default)
num_to_tigrinya(0, use_bado=True)      # → 'ባዶ' (local word)

num_to_tigrinya(100)                   # → 'ሓደ ሚእቲ'
num_to_tigrinya(100, add_hade=False)   # → 'ሚእቲ'
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

# Format: Month Day
num_to_date(25, 12)        # → 'ታሕሳስ ዕስራን ሓሙሽተን'
num_to_date(1, 1)          # → 'ጥሪ ሓደ'
num_to_date(15, 6)         # → 'ሰነ ዓሰርተ ሓሙሽተ'

# With year
num_to_date(1, 1, 2025)    # → 'ጥሪ ሓደ ክልተ ሽሕን ዕስራን ሓሙሽተን'
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
num_to_time(12, 30, add_deqiq=False)  # → 'ሰዓት ዓሰርተ ክልተን ሰላሳን'

# With minutes and seconds
num_to_time(3, 30, 15)   # → 'ሰዓት ሰለስተን ሰላሳ ደቒቕን ዓሰርተ ሓሙሽተ ካልኢትን'

# Minutes and seconds
num_to_time(minute=30, second=15)  # → 'ሰላሳ ደቒቕን ዓሰርተ ሓሙሽተ ካልኢትን'
```

### Phone Numbers

```python
from tigrinya_numbers import num_to_phone

# Pairs starting with 0 are read digit-by-digit
num_to_phone("07")         # → 'ዜሮ ሸውዓተ'

# Other pairs are read as two-digit numbers
num_to_phone("12")         # → 'ዓሰርተ ክልተ'
num_to_phone("34")         # → 'ሰላሳን ኣርባዕተን'

# Full phone number
num_to_phone("07123456")   # → 'ዜሮ ሸውዓተ ዓሰርተ ክልተ ሰላሳን ኣርባዕተን ሓምሳን ሽዱሽተን'

# Separators are ignored
num_to_phone("07-12-34-56")   # Same as "07123456"
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

### `num_to_tigrinya(n, add_hade=True, use_bado=False)`

Convert a non-negative integer to Tigrinya words.

**Parameters:**

- `n` (int): The number to convert (must be ≥ 0)
- `add_hade` (bool): If `True`, say "ሓደ ሚእቲ" for 100; if `False`, say "ሚእቲ". Default: `True`
- `use_bado` (bool): If `True`, use "ባዶ" for zero; if `False`, use "ዜሮ". Default: `False`

**Returns:** `str` - The Tigrinya representation

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
@misc{gaim-2025-tigrinya-numbers,
    title={{Tigrinya Numbers Verbalization: Rules, Algorithm, and Implementation}}, 
    author={Fitsum Gaim},
    month={December},
    year={2025},
    url={https://github.com/fgaim/tigrinya-numbers}
}
```

## License

This work is licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/).
