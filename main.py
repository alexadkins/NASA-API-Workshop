"""

Primary playground for API Workshop
    for Clemson University's 
    NASA Space Apps Challenge Hackathon
    hosted by CUHackit
    
By Dr. Alex Adkins
October 4, 2025

"""

from vars import *
from nasa_utils import *

def main():
    eonet_response = send_request(
                        "GET",
                        "https://eonet.gsfc.nasa.gov/api/v2.1/events",
                        params = {"days": 2}
                    )
    
    neows_response = send_request(
                        "GET",
                        "https://api.nasa.gov/neo/rest/v1/feed",
                        params = {
                            "start_date" : "2025-10-01",
                            "api_key" : NASA_API_KEY
                        }
                    )
    
    print_json(eonet_response)
    print_json(neows_response)

if __name__ == "__main__":
    main()

