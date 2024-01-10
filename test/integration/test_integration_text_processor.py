import sys
sys.path.append('/Users/eaariash/desarrollo/MachineLearningEn/practica_n1')
import pytest
from text_preprocessor import TextPreprocessor

@pytest.mark.parametrize("input_text, remove_links, remove_hashtags, convert_to_lowercase, expected", [
    ("Check this #hashtag and http://example.com", True, True, True, "check this  and "),
    ("SOME TEXT with #hashtag and a @mention", False, True, True, "some text with  and a @mention"),
    ("Another #example with a link http://example.com", True, False, False, "Another #example with a link "),
    ("MIXEDcase TEXT without processing", False, False, False, "MIXEDcase TEXT without processing"),
    ("123 numbers and emojis 😂 are here", False, False, False, "123 numbers and emojis 😂 are here"),
])
def test_full_preprocessing(input_text, remove_links, remove_hashtags, convert_to_lowercase, expected):
    processor = TextPreprocessor(remove_links=remove_links, remove_hastags=remove_hashtags,
                                 convert_to_lowercase=convert_to_lowercase)
    result = processor.preprocess_text(input_text)
    assert result == expected

@pytest.mark.parametrize("input_text, remove_links, remove_hashtags, remove_emojis, expected", [
    ("#Python is #awesome http://python.org 😃", True, True, True, "is  "),
    ("Visit #PyCon at http://pycon.com 😃", True, True, False, "Visit  at  😃"),
    ("#Coding in #Python 😃", False, True, True, "in  "),
    ("Learning #Python at http://python.org", False, False, False, "Learning #Python at http://python.org"),
    ("Python is fun 😃", False, False, True, "Python is fun "),
])
def test_different_flags(input_text, remove_links, remove_hashtags, remove_emojis, expected):
    processor = TextPreprocessor(remove_links=remove_links, remove_hastags=remove_hashtags,
                                 remove_emojis=remove_emojis)
    result = processor.preprocess_text(input_text)
    assert result == expected


