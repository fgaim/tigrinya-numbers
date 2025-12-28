"""
Unit tests for Tigrinya number converter.

Tests for: cardinals, ordinals, currency, date, time, phone numbers.
"""

import pytest

from tigrinya_numbers import (
    num_to_currency,
    num_to_date,
    num_to_ordinal,
    num_to_percent,
    num_to_phone,
    num_to_tigrinya,
    num_to_time,
)

# =============================================================================
# CARDINAL NUMBERS (from v1.0)
# =============================================================================


class TestZero:
    """Test zero conversion."""

    def test_zero_default(self):
        assert num_to_tigrinya(0) == "ዜሮ"

    def test_zero_local(self):
        assert num_to_tigrinya(0, use_bado=True) == "ባዶ"


class TestDigits:
    """Test single digits 1-10."""

    def test_one(self):
        assert num_to_tigrinya(1) == "ሓደ"

    def test_two(self):
        assert num_to_tigrinya(2) == "ክልተ"

    def test_three(self):
        assert num_to_tigrinya(3) == "ሰለስተ"

    def test_four(self):
        assert num_to_tigrinya(4) == "ኣርባዕተ"

    def test_five(self):
        assert num_to_tigrinya(5) == "ሓሙሽተ"

    def test_six(self):
        assert num_to_tigrinya(6) == "ሽዱሽተ"

    def test_seven(self):
        assert num_to_tigrinya(7) == "ሸውዓተ"

    def test_eight(self):
        assert num_to_tigrinya(8) == "ሸሞንተ"

    def test_nine(self):
        assert num_to_tigrinya(9) == "ትሽዓተ"

    def test_ten(self):
        assert num_to_tigrinya(10) == "ዓሰርተ"


class TestTeens:
    """Test numbers 11-19 (special teen format, no conjunction)."""

    def test_eleven(self):
        assert num_to_tigrinya(11) == "ዓሰርተ ሓደ"

    def test_twelve(self):
        assert num_to_tigrinya(12) == "ዓሰርተ ክልተ"

    def test_thirteen(self):
        assert num_to_tigrinya(13) == "ዓሰርተ ሰለስተ"

    def test_fourteen(self):
        assert num_to_tigrinya(14) == "ዓሰርተ ኣርባዕተ"

    def test_fifteen(self):
        assert num_to_tigrinya(15) == "ዓሰርተ ሓሙሽተ"

    def test_sixteen(self):
        assert num_to_tigrinya(16) == "ዓሰርተ ሽዱሽተ"

    def test_seventeen(self):
        assert num_to_tigrinya(17) == "ዓሰርተ ሸውዓተ"

    def test_eighteen(self):
        assert num_to_tigrinya(18) == "ዓሰርተ ሸሞንተ"

    def test_nineteen(self):
        assert num_to_tigrinya(19) == "ዓሰርተ ትሽዓተ"


class TestTens:
    """Test multiples of ten (standalone, no conjunction)."""

    def test_twenty(self):
        assert num_to_tigrinya(20) == "ዕስራ"

    def test_thirty(self):
        assert num_to_tigrinya(30) == "ሰላሳ"

    def test_forty(self):
        assert num_to_tigrinya(40) == "ኣርብዓ"

    def test_fifty(self):
        assert num_to_tigrinya(50) == "ሓምሳ"

    def test_sixty(self):
        assert num_to_tigrinya(60) == "ሱሳ"

    def test_seventy(self):
        assert num_to_tigrinya(70) == "ሰብዓ"

    def test_eighty(self):
        assert num_to_tigrinya(80) == "ሰማንያ"

    def test_ninety(self):
        assert num_to_tigrinya(90) == "ቴስዓ"


class TestCompoundTens:
    """Test compound numbers 21-99 (with conjunction)."""

    def test_twenty_one(self):
        assert num_to_tigrinya(21) == "ዕስራን ሓደን"

    def test_twenty_five(self):
        assert num_to_tigrinya(25) == "ዕስራን ሓሙሽተን"

    def test_thirty_seven(self):
        assert num_to_tigrinya(37) == "ሰላሳን ሸውዓተን"

    def test_forty_two(self):
        assert num_to_tigrinya(42) == "ኣርብዓን ክልተን"

    def test_sixty_nine(self):
        assert num_to_tigrinya(69) == "ሱሳን ትሽዓተን"

    def test_ninety_nine(self):
        assert num_to_tigrinya(99) == "ቴስዓን ትሽዓተን"


class TestHundreds:
    """Test hundreds."""

    def test_hundred_standalone(self):
        # Standalone uses ሚእቲ form
        assert num_to_tigrinya(100) == "ሓደ ሚእቲ"

    def test_hundred_without_one(self):
        assert num_to_tigrinya(100, add_hade=False) == "ሚእቲ"

    def test_two_hundred(self):
        assert num_to_tigrinya(200) == "ክልተ ሚእቲ"

    def test_five_hundred(self):
        assert num_to_tigrinya(500) == "ሓሙሽተ ሚእቲ"

    def test_nine_hundred(self):
        assert num_to_tigrinya(900) == "ትሽዓተ ሚእቲ"


class TestHundredsWithRemainder:
    """Test hundreds with remainder (compound, with conjunction)."""

    def test_hundred_one(self):
        assert num_to_tigrinya(101) == "ሓደ ሚእትን ሓደን"

    def test_hundred_ten(self):
        assert num_to_tigrinya(110) == "ሓደ ሚእትን ዓሰርተን"

    def test_hundred_fifteen(self):
        # Teen in compound: ን at end only
        assert num_to_tigrinya(115) == "ሓደ ሚእትን ዓሰርተ ሓሙሽተን"

    def test_hundred_twenty(self):
        assert num_to_tigrinya(120) == "ሓደ ሚእትን ዕስራን"

    def test_hundred_twenty_seven(self):
        assert num_to_tigrinya(127) == "ሓደ ሚእትን ዕስራን ሸውዓተን"

    def test_two_hundred_three(self):
        assert num_to_tigrinya(203) == "ክልተ ሚእትን ሰለስተን"

    def test_three_hundred_forty_five(self):
        assert num_to_tigrinya(345) == "ሰለስተ ሚእትን ኣርብዓን ሓሙሽተን"

    def test_nine_hundred_ninety_nine(self):
        assert num_to_tigrinya(999) == "ትሽዓተ ሚእትን ቴስዓን ትሽዓተን"


class TestThousands:
    """Test thousands."""

    def test_one_thousand(self):
        assert num_to_tigrinya(1000) == "ሓደ ሽሕ"

    def test_one_thousand_without_one(self):
        assert num_to_tigrinya(1000, add_hade=False) == "ሽሕ"

    def test_two_thousand(self):
        # Simple multiplier: single part, no conjunction
        assert num_to_tigrinya(2000) == "ክልተ ሽሕ"

    def test_ten_thousand(self):
        assert num_to_tigrinya(10000) == "ዓሰርተ ሽሕ"

    def test_fifteen_thousand(self):
        # Teen multiplier: still single part
        assert num_to_tigrinya(15000) == "ዓሰርተ ሓሙሽተ ሽሕ"

    def test_twenty_thousand(self):
        # Round tens multiplier: single part
        assert num_to_tigrinya(20000) == "ዕስራ ሽሕ"

    def test_twenty_five_thousand(self):
        # Compound multiplier: scale becomes separate part, but no trailing conjunction
        assert num_to_tigrinya(25000) == "ዕስራን ሓሙሽተን ሽሕ"

    def test_hundred_thousand(self):
        # 100 is a simple multiplier (single part), so combines with scale
        assert num_to_tigrinya(100000) == "ሓደ ሚእቲ ሽሕ"
        assert num_to_tigrinya(100000, add_hade=False) == "ሚእቲ ሽሕ"

    def test_two_hundred_thousand(self):
        # 200 is also simple (round hundred)
        assert num_to_tigrinya(200000) == "ክልተ ሚእቲ ሽሕ"

    def test_one_hundred_one_thousand(self):
        # 101 is compound (hundred + one), so scale becomes separate, no trailing conjunction
        assert num_to_tigrinya(101000) == "ሓደ ሚእትን ሓደን ሽሕ"


class TestThousandsWithRemainder:
    """Test thousands with remainder."""

    def test_two_thousand_one(self):
        assert num_to_tigrinya(2001) == "ክልተ ሽሕን ሓደን"

    def test_two_thousand_fifteen(self):
        assert num_to_tigrinya(2015) == "ክልተ ሽሕን ዓሰርተ ሓሙሽተን"

    def test_two_thousand_twenty(self):
        assert num_to_tigrinya(2020) == "ክልተ ሽሕን ዕስራን"

    def test_two_thousand_twenty_five(self):
        assert num_to_tigrinya(2025) == "ክልተ ሽሕን ዕስራን ሓሙሽተን"

    def test_five_thousand_five_hundred_fifty_five(self):
        assert num_to_tigrinya(5555) == "ሓሙሽተ ሽሕን ሓሙሽተ ሚእትን ሓምሳን ሓሙሽተን"


class TestLargeNumbers:
    """Test millions, billions, and beyond."""

    def test_standalone_scales(self):
        assert num_to_tigrinya(10_000) == "ዓሰርተ ሽሕ"
        assert num_to_tigrinya(34_000) == "ሰላሳን ኣርባዕተን ሽሕ"
        assert num_to_tigrinya(34_000_000) == "ሰላሳን ኣርባዕተን ሚልዮን"
        assert num_to_tigrinya(34_000_000_000) == "ሰላሳን ኣርባዕተን ቢልዮን"
        assert num_to_tigrinya(134_000_000_000) == "ሓደ ሚእትን ሰላሳን ኣርባዕተን ቢልዮን"
        assert num_to_tigrinya(134_000_000_000, add_hade=False) == "ሚእትን ሰላሳን ኣርባዕተን ቢልዮን"

    def test_compound_ending_in_hundred(self):
        assert num_to_tigrinya(34_700) == "ሰላሳን ኣርባዕተን ሽሕን ሸውዓተ ሚእትን"
        assert num_to_tigrinya(34_000_700) == "ሰላሳን ኣርባዕተን ሚልዮንን ሸውዓተ ሚእትን"
        assert num_to_tigrinya(34_000_000_700) == "ሰላሳን ኣርባዕተን ቢልዮንን ሸውዓተ ሚእትን"

    def test_one_million(self):
        assert num_to_tigrinya(1_000_000) == "ሓደ ሚልዮን"

    def test_two_million(self):
        assert num_to_tigrinya(2_000_000) == "ክልተ ሚልዮን"

    def test_one_billion(self):
        assert num_to_tigrinya(1_000_000_000) == "ሓደ ቢልዮን"

    def test_one_trillion(self):
        assert num_to_tigrinya(1_000_000_000_000) == "ሓደ ትሪልዮን"

    def test_one_quadrillion(self):
        assert num_to_tigrinya(10**15) == "ሓደ ኳድሪልዮን"

    def test_one_quintillion(self):
        assert num_to_tigrinya(10**18) == "ሓደ ኵንቲልዮን"

    def test_one_sextillion(self):
        assert num_to_tigrinya(10**21) == "ሓደ ሰክስቲልዮን"

    def test_one_septillion(self):
        assert num_to_tigrinya(10**24) == "ሓደ ሰፕቲልዮን"


class TestComplexNumbers:
    """Test complex multi-part numbers."""

    def test_1234567(self):
        # ሚልዮን gets conjunction (ሚልዮንን) when followed by more parts
        expected = "ሓደ ሚልዮንን ክልተ ሚእትን ሰላሳን ኣርባዕተን ሽሕን ሓሙሽተ ሚእትን ሱሳን ሸውዓተን"
        assert num_to_tigrinya(1_234_567) == expected

    def test_1_000_001(self):
        assert num_to_tigrinya(1_000_001) == "ሓደ ሚልዮንን ሓደን"

    def test_1_001_000(self):
        # Multi-scale number (millions + thousands): both scales get conjunction
        assert num_to_tigrinya(1_001_000) == "ሓደ ሚልዮንን ሓደ ሽሕን"

    def test_trailing_scale_conjunction(self):
        # 84,000 -> 84 thousand (scale at end, no conjunction)
        assert num_to_tigrinya(84_000) == "ሰማንያን ኣርባዕተን ሽሕ"

        # 84,001 -> 84 thousand and one (scale in middle, keeps conjunction)
        assert num_to_tigrinya(84_001) == "ሰማንያን ኣርባዕተን ሽሕን ሓደን"

        # 147,000 -> 147 thousand (scale at end, no conjunction)
        assert num_to_tigrinya(147_000) == "ሓደ ሚእትን ኣርብዓን ሸውዓተን ሽሕ"

    def test_12_345(self):
        # 12 thousand + 345
        assert num_to_tigrinya(12_345) == "ዓሰርተ ክልተ ሽሕን ሰለስተ ሚእትን ኣርብዓን ሓሙሽተን"

    def test_111_111(self):
        # 111 thousand + 111
        expected = "ሓደ ሚእትን ዓሰርተ ሓደን ሽሕን ሓደ ሚእትን ዓሰርተ ሓደን"
        assert num_to_tigrinya(111_111) == expected


class TestCardinalEdgeCases:
    """Test cardinal edge cases."""

    def test_negative_raises_error(self):
        result = num_to_tigrinya(-1)
        assert "ኣሉታ" in result

    def test_negative_large_raises_error(self):
        result = num_to_tigrinya(-1_000_000)
        assert "ኣሉታ" in result

    def test_very_large_number(self):
        # Sextillions
        n = 5 * 10**21 + 3 * 10**18
        result = num_to_tigrinya(n)
        assert "ሰክስቲልዮን" in result
        assert "ኵንቲልዮን" in result


class TestDecimalNumbers:
    """Test decimal/fraction number conversion."""

    def test_simple_decimal(self):
        # 5.05 → ሓሙሽተ ነጥቢ ዜሮ ሓሙሽተ
        assert num_to_tigrinya(5.05) == "ሓሙሽተ ነጥቢ ዜሮ ሓሙሽተ"

    def test_pi(self):
        # 3.14159 → ሰለስተ ነጥቢ ሓደ ኣርባዕተ ሓደ ሓሙሽተ ትሽዓተ
        assert num_to_tigrinya(3.14159) == "ሰለስተ ነጥቢ ሓደ ኣርባዕተ ሓደ ሓሙሽተ ትሽዓተ"

    def test_decimal_with_zero_integer(self):
        # 0.5 → ዜሮ ነጥቢ ሓሙሽተ
        assert num_to_tigrinya(0.5) == "ዜሮ ነጥቢ ሓሙሽተ"

    def test_decimal_with_leading_zeros(self):
        # 1.01 → ሓደ ነጥቢ ዜሮ ሓደ
        assert num_to_tigrinya(1.01) == "ሓደ ነጥቢ ዜሮ ሓደ"

    def test_integer_float_treated_as_integer(self):
        # 5.0 should be treated as integer 5
        assert num_to_tigrinya(5.0) == "ሓሙሽተ"


class TestIncludeOneOption:
    """Test the add_hade parameter."""

    def test_hundred_with_one(self):
        assert num_to_tigrinya(100, add_hade=True) == "ሓደ ሚእቲ"

    def test_hundred_without_one(self):
        assert num_to_tigrinya(100, add_hade=False) == "ሚእቲ"

    def test_thousand_with_one(self):
        assert num_to_tigrinya(1000, add_hade=True) == "ሓደ ሽሕ"

    def test_thousand_without_one(self):
        assert num_to_tigrinya(1000, add_hade=False) == "ሽሕ"

    def test_million_without_one(self):
        assert num_to_tigrinya(1_000_000, add_hade=False) == "ሚልዮን"

    def test_compound_hundred_without_one(self):
        # Even with add_hade=False, the pattern should work
        assert num_to_tigrinya(103, add_hade=False) == "ሚእትን ሰለስተን"

    def test_two_hundred_ignores_include_one(self):
        # add_hade=False only affects "1" multipliers
        assert num_to_tigrinya(200, add_hade=False) == "ክልተ ሚእቲ"


# =============================================================================
# ORDINAL NUMBERS
# =============================================================================


class TestOrdinalsMasculine:
    """Test masculine ordinals 1st-10th."""

    def test_first(self):
        assert num_to_ordinal(1) == "ቀዳማይ"

    def test_second(self):
        assert num_to_ordinal(2) == "ካልኣይ"

    def test_third(self):
        assert num_to_ordinal(3) == "ሳልሳይ"

    def test_fourth(self):
        assert num_to_ordinal(4) == "ራብዓይ"

    def test_fifth(self):
        assert num_to_ordinal(5) == "ሓሙሻይ"

    def test_sixth(self):
        assert num_to_ordinal(6) == "ሻድሻይ"

    def test_seventh(self):
        assert num_to_ordinal(7) == "ሻውዓይ"

    def test_eighth(self):
        assert num_to_ordinal(8) == "ሻምናይ"

    def test_ninth(self):
        assert num_to_ordinal(9) == "ታሽዓይ"

    def test_tenth(self):
        assert num_to_ordinal(10) == "ዓስራይ"


class TestOrdinalsFeminine:
    """Test feminine ordinals 1st-10th."""

    def test_first_feminine(self):
        assert num_to_ordinal(1, feminine=True) == "ቀዳመይቲ"

    def test_second_feminine(self):
        assert num_to_ordinal(2, feminine=True) == "ካልአይቲ"

    def test_third_feminine(self):
        assert num_to_ordinal(3, feminine=True) == "ሳልሰይቲ"

    def test_sixth_feminine(self):
        assert num_to_ordinal(6, feminine=True) == "ሻድሸይቲ"

    def test_eighth_feminine(self):
        assert num_to_ordinal(8, feminine=True) == "ሻምነይቲ"

    def test_ninth_feminine(self):
        assert num_to_ordinal(9, feminine=True) == "ታሽዐይቲ"

    def test_tenth_feminine(self):
        assert num_to_ordinal(10, feminine=True) == "ዓስረይቲ"


class TestOrdinalsAboveTen:
    """Test ordinals 11th and above using መበል prefix."""

    def test_eleventh(self):
        assert num_to_ordinal(11) == "መበል ዓሰርተ ሓደ"

    def test_fifteenth(self):
        assert num_to_ordinal(15) == "መበል ዓሰርተ ሓሙሽተ"

    def test_twentieth(self):
        assert num_to_ordinal(20) == "መበል ዕስራ"

    def test_twenty_fifth(self):
        assert num_to_ordinal(25) == "መበል ዕስራን ሓሙሽተን"

    def test_hundredth(self):
        assert num_to_ordinal(100) == "መበል ሓደ ሚእቲ"

    def test_hundred_twenty_seventh(self):
        assert num_to_ordinal(127) == "መበል ሓደ ሚእትን ዕስራን ሸውዓተን"


class TestOrdinalEdgeCases:
    """Test ordinal edge cases."""

    def test_zero_raises_error(self):
        with pytest.raises(ValueError, match="must be positive"):
            num_to_ordinal(0)

    def test_negative_raises_error(self):
        with pytest.raises(ValueError, match="must be positive"):
            num_to_ordinal(-5)


# =============================================================================
# CURRENCY
# =============================================================================


class TestCurrencyNakfa:
    """Test Eritrean Nakfa (default currency)."""

    def test_whole_amount(self):
        assert num_to_currency(100) == "ሓደ ሚእቲ ናቕፋ"

    def test_whole_amount_small(self):
        assert num_to_currency(5) == "ሓሙሽተ ናቕፋ"

    def test_with_cents(self):
        # Both amounts follow cardinal rules: simple numbers don't get ን
        assert num_to_currency(5.50) == "ሓሙሽተ ናቕፋን ሓምሳ ሳንቲምን"
        assert num_to_currency(51.51) == "ሓምሳን ሓደን ናቕፋን ሓምሳን ሓደን ሳንቲምን"

    def test_cents_only(self):
        assert num_to_currency(0.25) == "ዕስራን ሓሙሽተን ሳንቲም"

    def test_zero_amount(self):
        assert num_to_currency(0) == "ዜሮ ናቕፋ"

    def test_large_amount(self):
        assert num_to_currency(1234.56) == "ሓደ ሽሕን ክልተ ሚእትን ሰላሳን ኣርባዕተን ናቕፋን ሓምሳን ሽዱሽተን ሳንቲምን"
        assert num_to_currency(1234.56, add_hade=False) == "ሽሕን ክልተ ሚእትን ሰላሳን ኣርባዕተን ናቕፋን ሓምሳን ሽዱሽተን ሳንቲምን"


class TestCurrencyBirr:
    """Test Ethiopian Birr."""

    def test_birr_whole(self):
        assert num_to_currency(50, currency="ETB") == "ሓምሳ ብር"

    def test_birr_with_cents(self):
        assert num_to_currency(10.75, currency="ETB") == "ዓሰርተ ብርን ሰብዓን ሓሙሽተን ሳንቲምን"


class TestCurrencyOther:
    """Test other currencies."""

    def test_usd(self):
        assert num_to_currency(1, currency="USD") == "ሓደ ዶላር"

    def test_eur(self):
        assert num_to_currency(2, currency="EUR") == "ክልተ ዩሮ"


class TestCurrencyEdgeCases:
    """Test currency edge cases."""

    def test_negative_raises_error(self):
        with pytest.raises(ValueError, match="cannot be negative"):
            num_to_currency(-10)

    def test_invalid_currency_raises_error(self):
        with pytest.raises(ValueError, match="Unsupported currency"):
            num_to_currency(10, currency="XYZ")


# =============================================================================
# DATE
# =============================================================================


class TestDateBasic:
    """Test basic date conversion."""

    def test_december_25(self):
        result = num_to_date(25, 12)
        assert result == "ታሕሳስ ዕስራን ሓሙሽተን"

    def test_january_1(self):
        result = num_to_date(1, 1)
        assert result == "ጥሪ ሓደ"

    def test_june_15(self):
        result = num_to_date(15, 6)
        assert result == "ሰነ ዓሰርተ ሓሙሽተ"


class TestDateWithYear:
    """Test date conversion with year."""

    def test_with_year_2025(self):
        result = num_to_date(1, 1, 2025)
        assert "ጥሪ" in result
        assert "ሓደ" in result
        assert "ሽሕ" in result  # part of 2025


class TestDateMonths:
    """Test all month names."""

    def test_all_months(self):
        expected_months = {
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
        for month_num, month_name in expected_months.items():
            result = num_to_date(1, month_num)
            assert month_name in result


class TestDateEdgeCases:
    """Test date edge cases."""

    def test_invalid_month_raises_error(self):
        with pytest.raises(ValueError, match="Month must be 1-12"):
            num_to_date(1, 13)

    def test_invalid_day_raises_error(self):
        with pytest.raises(ValueError, match="Day must be 1-31"):
            num_to_date(32, 1)

    def test_zero_month_raises_error(self):
        with pytest.raises(ValueError, match="Month must be 1-12"):
            num_to_date(1, 0)


class TestDateAddHade:
    """Test the add_hade parameter for date year verbalization."""

    def test_default_no_hade(self):
        # Default: 1991 -> ሽሕን... (no ሓደ before ሽሕ)
        result = num_to_date(24, 5, 1991)
        assert result == "ግንቦት ዕስራን ኣርባዕተን ሽሕን ትሽዓተ ሚእትን ቴስዓን ሓደን"
        assert "ሓደ ሽሕ" not in result

    def test_with_hade(self):
        # add_hade=True: 1991 -> ሓደ ሽሕን... (includes ሓደ)
        result = num_to_date(24, 5, 1991, add_hade=True)
        assert result == "ግንቦት ዕስራን ኣርባዕተን ሓደ ሽሕን ትሽዓተ ሚእትን ቴስዓን ሓደን"
        assert "ሓደ ሽሕ" in result


class TestDateUseNumeric:
    """Test the use_numeric parameter for numeric date format."""

    def test_numeric_format_no_year(self):
        # Numeric: ዕለት [day] ወርሒ [month]
        result = num_to_date(25, 12, use_numeric=True)
        assert result == "ዕለት ዕስራን ሓሙሽተን ወርሒ ዓሰርተ ክልተ"

    def test_numeric_format_with_year(self):
        # Numeric with year
        result = num_to_date(24, 5, 1991, use_numeric=True)
        assert result == "ዕለት ዕስራን ኣርባዕተን ወርሒ ሓሙሽተ ሽሕን ትሽዓተ ሚእትን ቴስዓን ሓደን"

    def test_numeric_with_add_hade(self):
        # Both flags combined
        result = num_to_date(24, 5, 1991, use_numeric=True, add_hade=True)
        assert result == "ዕለት ዕስራን ኣርባዕተን ወርሒ ሓሙሽተ ሓደ ሽሕን ትሽዓተ ሚእትን ቴስዓን ሓደን"

    def test_compare_calendar_vs_numeric(self):
        # Compare both formats for same date
        calendar = num_to_date(25, 12)
        numeric = num_to_date(25, 12, use_numeric=True)
        assert "ታሕሳስ ዕስራን ሓሙሽተን" == calendar  # Month name in calendar
        assert "ዕለት ዕስራን ሓሙሽተን ወርሒ ዓሰርተ ክልተ" == numeric  # Month marker in numeric


class TestDateMonthFirst:
    """Test the month_first parameter for date ordering."""

    def test_default_month_first(self):
        # Default: month comes first
        result = num_to_date(10, 11)
        assert result == "ሕዳር ዓሰርተ"

    def test_day_first_no_year(self):
        # month_first=False: day comes first
        result = num_to_date(10, 11, month_first=False)
        assert result == "ዓሰርተ ሕዳር"

    def test_day_first_with_year(self):
        # month_first=False with year
        result = num_to_date(25, 12, 2025, month_first=False)
        assert result == "ዕስራን ሓሙሽተን ታሕሳስ ክልተ ሽሕን ዕስራን ሓሙሽተን"

    def test_month_first_ignored_in_numeric(self):
        # month_first has no effect in numeric mode (always ዕለት Day ወርሒ Month)
        result_true = num_to_date(10, 11, use_numeric=True, month_first=True)
        result_false = num_to_date(10, 11, use_numeric=True, month_first=False)
        assert result_true == result_false == "ዕለት ዓሰርተ ወርሒ ዓሰርተ ሓደ"


# =============================================================================
# TIME
# =============================================================================


class TestTimeOnTheHour:
    """Test time conversion on the hour (hour only, no minutes)."""

    def test_three_oclock(self):
        # Hour only: use just hour arg (minute=None)
        assert num_to_time(3) == "ሰዓት ሰለስተ"

    def test_twelve_oclock(self):
        assert num_to_time(12) == "ሰዓት ዓሰርተ ክልተ"

    def test_midnight_as_twelve(self):
        # Hour 0 should display as 12
        assert num_to_time(0) == "ሰዓት ዓሰርተ ክልተ"


class TestTimeWithMinutes:
    """Test time conversion with minutes."""

    def test_three_forty_five(self):
        assert num_to_time(3, 45) == "ሰዓት ሰለስተን ኣርብዓን ሓሙሽተን ደቒቕን"

    def test_twelve_thirty(self):
        # 30 is a simple number (round tens), marker carries conjunction
        assert num_to_time(12, 30) == "ሰዓት ዓሰርተ ክልተን ሰላሳ ደቒቕን"
        assert num_to_time(12, 30, add_deqiq=False) == "ሰዓት ዓሰርተ ክልተን ሰላሳን"

    def test_one_fifteen(self):
        # 15 is a teen (simple number), marker carries conjunction
        assert num_to_time(1, 15) == "ሰዓት ሓደን ዓሰርተ ሓሙሽተ ደቒቕን"
        assert num_to_time(1, 15, add_deqiq=False) == "ሰዓት ሓደን ዓሰርተ ሓሙሽተን"

    def test_minute_only(self):
        # No hour: minute marker is mandatory, no conjunction (single component)
        assert num_to_time(minute=30) == "ሰላሳ ደቒቕ"
        assert num_to_time(minute=45) == "ኣርብዓን ሓሙሽተን ደቒቕ"

    def test_second_only(self):
        assert num_to_time(second=5) == "ሓሙሽተ ካልኢት"
        assert num_to_time(second=45) == "ኣርብዓን ሓሙሽተን ካልኢት"

    def test_hour_only(self):
        assert num_to_time(hour=1) == "ሰዓት ሓደ"
        assert num_to_time(hour=12) == "ሰዓት ዓሰርተ ክልተ"


class TestTimeWithSeconds:
    """Test time conversion with seconds."""

    def test_with_minutes_and_seconds(self):
        # 1:30:45 - markers are mandatory when seconds present
        assert num_to_time(1, 30, 45) == "ሰዓት ሓደን ሰላሳ ደቒቕን ኣርብዓን ሓሙሽተን ካልኢትን"

    def test_simple_seconds(self):
        # 3:30:15 - 30 is simple (ሰላሳ), marker carries conjunction
        assert num_to_time(3, 30, 15) == "ሰዓት ሰለስተን ሰላሳ ደቒቕን ዓሰርተ ሓሙሽተ ካልኢትን"

    def test_minute_and_second_only(self):
        # No hour: both markers mandatory
        assert num_to_time(minute=30, second=15) == "ሰላሳ ደቒቕን ዓሰርተ ሓሙሽተ ካልኢትን"

    def test_hour_and_seconds_only(self):
        # Hour with seconds, no minutes (10:00:05)
        assert num_to_time(10, 0, 5) == "ሰዓት ዓሰርተን ሓሙሽተ ካልኢትን"


class TestTimeEdgeCases:
    """Test time edge cases."""

    def test_invalid_hour_raises_error(self):
        with pytest.raises(ValueError, match="Hour must be 0-23"):
            num_to_time(24, 0)

    def test_invalid_minute_raises_error(self):
        with pytest.raises(ValueError, match="Minute must be 0-59"):
            num_to_time(12, 60)

    def test_negative_hour_raises_error(self):
        with pytest.raises(ValueError, match="Hour must be 0-23"):
            num_to_time(-1)

    def test_invalid_second_raises_error(self):
        with pytest.raises(ValueError, match="Second must be 0-59"):
            num_to_time(12, 30, 60)


class TestTimeAddSeat:
    """Test the add_seat parameter for optional hour prefix."""

    def test_hour_only_without_seat(self):
        # Hour without prefix
        assert num_to_time(3, add_seat=False) == "ሰለስተ"
        assert num_to_time(12, add_seat=False) == "ዓሰርተ ክልተ"

    def test_hour_and_minutes_without_seat(self):
        # Hour:minute without prefix
        assert num_to_time(3, 45, add_seat=False) == "ሰለስተን ኣርብዓን ሓሙሽተን ደቒቕን"
        assert num_to_time(7, 30, add_seat=False) == "ሸውዓተን ሰላሳ ደቒቕን"

    def test_hour_minutes_seconds_without_seat(self):
        # Full time without prefix
        assert num_to_time(2, 37, 48, add_seat=False) == "ክልተን ሰላሳን ሸውዓተን ደቒቕን ኣርብዓን ሸሞንተን ካልኢትን"

    def test_combined_options(self):
        # Without prefix and without minute marker
        assert num_to_time(3, 45, add_seat=False, add_deqiq=False) == "ሰለስተን ኣርብዓን ሓሙሽተን"
        # With prefix but without minute marker (default add_seat=True)
        assert num_to_time(3, 45, add_deqiq=False) == "ሰዓት ሰለስተን ኣርብዓን ሓሙሽተን"

    def test_midnight_without_seat(self):
        # Midnight (hour 0 displays as 12) without prefix
        assert num_to_time(0, add_seat=False) == "ዓሰርተ ክልተ"
        assert num_to_time(0, 30, add_seat=False) == "ዓሰርተ ክልተን ሰላሳ ደቒቕን"


# =============================================================================
# PHONE NUMBERS
# =============================================================================


class TestPhoneBasic:
    """Test basic phone number conversion."""

    def test_phone_with_leading_zero(self):
        # Should be digit-by-digit: ዜሮ ሸውዓተ
        assert num_to_phone("07") == "ዜሮ ሸውዓተ"

    def test_phone_pair_twelve(self):
        # Should be read as teen: ዓሰርተ ክልተ
        assert num_to_phone("12") == "ዓሰርተ ክልተ"

    def test_phone_pair_thirty_four(self):
        # Should be read as compound: ሰላሳን ኣርባዕተን
        assert num_to_phone("34") == "ሰላሳን ኣርባዕተን"


class TestPhoneFormatted:
    """Test phone numbers with separators."""

    def test_phone_with_dashes(self):
        assert num_to_phone("07-12-34") == "ዜሮ ሸውዓተ ዓሰርተ ክልተ ሰላሳን ኣርባዕተን"

    def test_phone_with_spaces(self):
        assert num_to_phone("07 12 34") == "ዜሮ ሸውዓተ ዓሰርተ ክልተ ሰላሳን ኣርባዕተን"


class TestPhoneLong:
    """Test full phone numbers."""

    def test_ten_digit_phone(self):
        assert num_to_phone("0712345678") == "ዜሮ ሸውዓተ ዓሰርተ ክልተ ሰላሳን ኣርባዕተን ሓምሳን ሽዱሽተን ሰብዓን ሸሞንተን"


class TestPhoneEdgeCases:
    """Test phone edge cases."""

    def test_empty_raises_error(self):
        with pytest.raises(ValueError, match="at least one digit"):
            num_to_phone("")

    def test_no_digits_raises_error(self):
        with pytest.raises(ValueError, match="at least one digit"):
            num_to_phone("abc")

    def test_single_digit(self):
        result = num_to_phone("5")
        assert result == "ሓሙሽተ"

    def test_odd_number_of_digits(self):
        # 12 as teen, 3 as single; TODO this is not ideal
        assert num_to_phone("123") == "ዓሰርተ ክልተ ሰለስተ"


class TestPhoneUseSingles:
    """Test the use_singles parameter for digit-by-digit reading."""

    def test_basic_singles(self):
        # Each digit read individually
        assert num_to_phone("1234", use_singles=True) == "ሓደ ክልተ ሰለስተ ኣርባዕተ"

    def test_with_zero(self):
        # Zero as individual digit
        assert num_to_phone("07", use_singles=True) == "ዜሮ ሸውዓተ"
        assert num_to_phone("0712", use_singles=True) == "ዜሮ ሸውዓተ ሓደ ክልተ"

    def test_full_phone_singles(self):
        # Full phone number in singles
        assert num_to_phone("07123456", use_singles=True) == "ዜሮ ሸውዓተ ሓደ ክልተ ሰለስተ ኣርባዕተ ሓሙሽተ ሽዱሽተ"

    def test_with_separators_singles(self):
        # Separators should be ignored in singles mode too
        assert num_to_phone("07-12-34", use_singles=True) == "ዜሮ ሸውዓተ ሓደ ክልተ ሰለስተ ኣርባዕተ"

    def test_compare_pairs_vs_singles(self):
        # Compare default (pairs) vs singles
        pairs = num_to_phone("1234")  # "12" -> ዓሰርተ ክልተ, "34" -> ሰላሳን ኣርባዕተን
        singles = num_to_phone("1234", use_singles=True)  # 1 2 3 4 individually
        assert pairs == "ዓሰርተ ክልተ ሰላሳን ኣርባዕተን"
        assert singles == "ሓደ ክልተ ሰለስተ ኣርባዕተ"
        assert pairs != singles


class TestPhoneUseBado:
    """Test the use_bado parameter for zero word selection."""

    def test_pairs_with_bado(self):
        # Pairs mode with ባዶ for zero
        assert num_to_phone("07", use_bado=True) == "ባዶ ሸውዓተ"
        assert num_to_phone("07-12", use_bado=True) == "ባዶ ሸውዓተ ዓሰርተ ክልተ"

    def test_singles_with_bado(self):
        # Singles mode with ባዶ for zero
        assert num_to_phone("07", use_singles=True, use_bado=True) == "ባዶ ሸውዓተ"
        assert num_to_phone("0712", use_singles=True, use_bado=True) == "ባዶ ሸውዓተ ሓደ ክልተ"

    def test_combined_flags(self):
        # All combinations
        phone = "07-34"
        assert num_to_phone(phone) == "ዜሮ ሸውዓተ ሰላሳን ኣርባዕተን"
        assert num_to_phone(phone, use_bado=True) == "ባዶ ሸውዓተ ሰላሳን ኣርባዕተን"
        assert num_to_phone(phone, use_singles=True) == "ዜሮ ሸውዓተ ሰለስተ ኣርባዕተ"
        assert num_to_phone(phone, use_singles=True, use_bado=True) == "ባዶ ሸውዓተ ሰለስተ ኣርባዕተ"


# =============================================================================
# PERCENT
# =============================================================================


class TestPercentBasic:
    """Test basic percentage conversion."""

    def test_zero_percent(self):
        assert num_to_percent(0) == "ዜሮ ሚእታዊት"

    def test_zero_percent_bado(self):
        assert num_to_percent(0, use_bado=True) == "ባዶ ሚእታዊት"

    def test_forty_percent(self):
        assert num_to_percent(40) == "ኣርብዓ ሚእታዊት"

    def test_hundred_percent(self):
        assert num_to_percent(100) == "ሓደ ሚእቲ ሚእታዊት"

    def test_compound_percent(self):
        assert num_to_percent(25) == "ዕስራን ሓሙሽተን ሚእታዊት"


class TestPercentDecimal:
    """Test decimal percentage conversion."""

    def test_decimal_percent(self):
        assert num_to_percent(25.5) == "ዕስራን ሓሙሽተን ነጥቢ ሓሙሽተ ሚእታዊት"

    def test_simple_decimal_percent(self):
        assert num_to_percent(3.14) == "ሰለስተ ነጥቢ ሓደ ኣርባዕተ ሚእታዊት"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
