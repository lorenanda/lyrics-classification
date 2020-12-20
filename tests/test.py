import pytest
import main

def test_always_passes():
    assert True

def test_lowercase():
    assert "ARTIST".lower() == "artist"

def test_reversed():
    assert list(reversed(songs_urls)) == songs_urls

def test_some_primes():
    assert 37 in {
        num
        for num in range(1, 50)
        if num != 1 and not any([num % div == 0 for div in range(2, num)])
    }
