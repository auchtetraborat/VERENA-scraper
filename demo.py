from VerenaScraper import VerenaScraper

with open("output.json", "w") as o:
    o.write(VerenaScraper.scrape_to_json())