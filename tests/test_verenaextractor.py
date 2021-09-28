import pytest
import json
from verenascraper.verenaextractor import VerenaExtractor


def test_extractor_content():
    with open("tests/ausschreibung_test_input.html", "r") as f:
        with open("tests/ausschreibung_correct_result.json", "r") as correct:
            content = "<html><body>" + f.read() + "</body></html>"
            ve = VerenaExtractor(content)
            res = ve.extract()
            assert len(res) == 1 and res[0] == json.loads(correct.read())


def test_extractor_simple_10():
    with open("tests/ausschreibung_test_input.html", "r") as f:
        content = "<html><body>" + f.read() * 10 + "</body></html>"
        ve = VerenaExtractor(content)
        res = ve.extract()
        assert len(res) == 10
