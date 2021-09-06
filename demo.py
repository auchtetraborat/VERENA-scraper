from VerenaScraper import VerenaScraper

with open("out.json", "w") as o:
    o.write(VerenaScraper.scrape_to_json())