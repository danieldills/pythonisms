import pytest
from deco import decorate

def test_greeting():
    text = "Daniel"
    res = decorate(text)
    assert res == 'Hello, Goodbye "Daniel"'
