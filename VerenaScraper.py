from VerenaDownloader import VerenaDownloader
from VerenaExtractor import VerenaExtractor
import json

class VerenaScraper:

    def scrape_to_json():
        result = []
        scraped_pages = VerenaDownloader().scrape()
        for idx, page in enumerate(scraped_pages):
            extract = VerenaExtractor(page).extract()
            print("Page" + str(idx+1) + " : " + str(len(extract)) + " entries")
            result = result + extract
        return json.dumps(result)
    
    

