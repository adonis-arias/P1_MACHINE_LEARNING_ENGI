import sys
sys.path.append('/Users/eaariash/desarrollo/MachineLearningEn/practica_n1')
import pytest
from text_preprocessor import TextPreprocessor


@pytest.mark.parametrize("input_text, expected", [
    ("Check out this link: http://example.com", "Check out this link: "),
    ("No links here!", "No links here!"),
    ("Multiple links http://a.com http://b.com", "Multiple links  "),
    ("", ""),
    ("https://example.com is a cool site", " is a cool site"),
])
def test_remove_links(input_text, expected):
    processor = TextPreprocessor(remove_links=True)
    assert processor.remove_links(input_text) == expected

@pytest.mark.parametrize("input_text, expected", [
    ("Hello! How are you?", "Hello How are you"),
    ("No special characters", "No special characters"),
    ("#Hashtags and @mentions", "Hashtags and mentions"),
    ("", ""),
    ("Special!!! **&&^%$", "Special "),
])
def test_remove_characters(input_text, expected):
    processor = TextPreprocessor(remove_characters=True)
    assert processor.remove_characters(input_text) == expected

@pytest.mark.parametrize("input_text, expected", [
    ("ALLCAPS", "allcaps"),
    ("MiXeDCaSe", "mixedcase"),
    ("123", "123"),
    ("", ""),
    ("lower already", "lower already"),
])
def test_convert_to_lowercase(input_text, expected):
    processor = TextPreprocessor(convert_to_lowercase=True)
    assert processor.convert_to_lowercase(input_text) == expected

@pytest.mark.parametrize("input_text, expected", [
    ("Emoji 😂 is here", "Emoji  is here"),
    ("No emojis", "No emojis"),
    ("😂😂😂", ""),
    ("", ""),
    ("Text with emoji 😂 at the end", "Text with emoji  at the end"),
])
def test_remove_emojis(input_text, expected):
    processor = TextPreprocessor(remove_emojis=True)
    assert processor.remove_emojis(input_text) == expected

@pytest.mark.parametrize("input_text, expected", [
    ("123 numbers", " numbers"),
    ("No1numbers2here3", "Nonumbershere"),
    ("1234567890", ""),
    ("", ""),
    ("abc123def456", "abcdef"),
])
def test_remove_numbers(input_text, expected):
    processor = TextPreprocessor(remove_numbers=True)
    assert processor.remove_numbers(input_text) == expected

