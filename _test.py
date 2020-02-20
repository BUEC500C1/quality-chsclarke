import pytest
import convertToRoman

def test_4():
    assert convertToRoman.convert(4) == "IV"

def test_5():
    assert convertToRoman.convert(5) == "V"

def test_10():
	assert convertToRoman.convert(10) == "X"

def test_35():
	assert convertToRoman.convert(35) == "XXXV"

def test_994():
	assert convertToRoman.convert(994) == "CMXCIV"

def test_1995():
	assert convertToRoman.convert(1995) == "MCMXCV"

def test_str():
	assert convertToRoman.convert("asdf") == -1

def test_bool():
	assert convertToRoman.convert(True) == -1

def test_bool():
	assert convertToRoman.convert(1.2) == -1