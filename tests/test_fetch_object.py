import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app import fetch_object
from app.config import CURRENT_DIRECTORY


def test_fetch_object_returns_expected_results():
    results = fetch_object(CURRENT_DIRECTORY)
    assert ['vizitka.cdr', './example/test_archive/Saqo/vizitkeq/karmir/vizitka.cdr'] in results
    assert ['new.txt', 'bad_formatting'] in results
    assert ['iore.tio', 'bad_formatting'] in results
