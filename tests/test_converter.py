"""
Unit tests for Tigrinya number converter.

Tests for: cardinals, ordinals, currency, date, time, phone numbers.
"""

import pytest

from tigrinya_numbers import num_to_currency, num_to_date, num_to_ordinal, num_to_phone, num_to_tigrinya, num_to_time

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
        # Compound multiplier: scale becomes separate part
        assert num_to_tigrinya(25000) == "ዕስራን ሓሙሽተን ሽሕን"

    def test_hundred_thousand(self):
        # 100 is a simple multiplier (single part), so combines with scale
        assert num_to_tigrinya(100000) == "ሓደ ሚእቲ ሽሕ"

    def test_two_hundred_thousand(self):
        # 200 is also simple (round hundred)
        assert num_to_tigrinya(200000) == "ክልተ ሚእቲ ሽሕ"

    def test_one_hundred_one_thousand(self):
        # 101 is compound (hundred + one), so scale becomes separate
        assert num_to_tigrinya(101000) == "ሓደ ሚእትን ሓደን ሽሕን"


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


class TestComplexNumbers:
    """Test complex multi-part numbers."""

    def test_1234567(self):
        # User's example: 1,234,567
        expected = "ሓደ ሚልዮንን ክልተ ሚእትን ሰላሳን ኣርባዕተን ሽሕን ሓሙሽተ ሚእትን ሱሳን ሸውዓተን"
        assert num_to_tigrinya(1_234_567) == expected

    def test_1_000_001(self):
        assert num_to_tigrinya(1_000_001) == "ሓደ ሚልዮንን ሓደን"

    def test_1_001_000(self):
        assert num_to_tigrinya(1_001_000) == "ሓደ ሚልዮንን ሓደ ሽሕን"

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
        # No hour: minute marker is mandatory
        assert num_to_time(minute=30) == "ሰላሳ ደቒቕን"
        assert num_to_time(minute=45) == "ኣርብዓን ሓሙሽተን ደቒቕን"


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

    def test_seconds_without_minutes_raises_error(self):
        # Cannot skip middle value
        with pytest.raises(ValueError, match="Cannot provide seconds without minutes"):
            num_to_time(5, second=30)


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


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
