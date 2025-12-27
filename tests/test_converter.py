"""
Unit tests for Tigrinya number converter.
"""

import pytest

from tigrinya_numbers import num_to_tigrinya


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
        assert num_to_tigrinya(6) == "ሽድሽተ"

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
        assert num_to_tigrinya(16) == "ዓሰርተ ሽድሽተ"

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


class TestEdgeCases:
    """Test edge cases and error handling."""

    def test_negative_raises_error(self):
        with pytest.raises(ValueError, match="Negative numbers"):
            num_to_tigrinya(-1)

    def test_negative_large_raises_error(self):
        with pytest.raises(ValueError, match="Negative numbers"):
            num_to_tigrinya(-1_000_000)

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


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
