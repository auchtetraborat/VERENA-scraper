from verenascraper.verenascraper import VerenaScraper


def test_verena():
    v = VerenaScraper()
    res = v.get()
    assert (
        len(res) > 0
    ), "Scraping and extracting all pages of the VERENA portal eturned 0 results. It very likely shouldn't."
