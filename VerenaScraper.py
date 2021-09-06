from VerenaDownloader import VerenaDownloader
from VerenaExtractor import VerenaExtractor
import json

class VerenaScraper:

    def scrape_to_json():
        result = []
        scraped_pages = VerenaDownloader().scrape()
        for page in scraped_pages:
            result = result + VerenaExtractor(page).extract()
        return json.dumps(result)
    
    

