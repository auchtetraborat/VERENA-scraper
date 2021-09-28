from .verenadownloader import VerenaDownloader
from .verenaextractor import VerenaExtractor


class VerenaScraper:
    """
    Downloads and extracts the current job listings from the VERENA portal.
    """
    def get():
        """
        Downloads and extracts the current job listings from the VERENA portal.
        
        Example: [
            {
                "school_id": "99999",
                "desc": "Eine Schule\nSchule der Sekundarstufe II\ndes Landkreis Schuling\n9999 Schulingen",
                "replacement_job_title": "Lehrkraft",
                "subjects": [
                    "Fach 1",
                    "Fach 2"
                ],
                "comments": "Bemerkung zur Stelle: Testbemerkung",
                "duration": "01.01.2021 - 01.01.2022",
                "hours_per_week": "13,5",
                "contact": {
                    "phone": "0172 1111 1111",
                    "fax": "0172 2222 2222",
                    "homepage": "http://www.eine-schule.de",
                    "mail": {
                        "raw": "mailto:bewerbung@eineschule.de?subject=Stellenausschreibung in VERENA",
                        "adress": "bewerbung@eineschule.de",
                        "subject": "Stellenausschreibung in VERENA"
                    }
                },
                "deadline": "17.09.2021",
                "geolocation": {
                    "coord_system": "epsg:25832",
                    "coordinates": [1111111, 1111111],
                    "post_adress": "Eine Stra\u00dfe 1\n99999 Schulingen"
                }
            },
            ...
        ]

        """
        result = []
        scraped_pages = VerenaDownloader().scrape()
        for idx, page in enumerate(scraped_pages):
            extract = VerenaExtractor(page).extract()
            result = result + extract
        return result

if __name__ == "__main__":
    vs = VerenaScraper()
    res = vs.get()
    print(res)