"""

Primary playground for API Workshop
    for Clemson University's 
    NASA Space Apps Challenge Hackathon
    hosted by CUHackit
    
By Dr. Alex Adkins
October 4, 2025

"""

import os
from nasa_utils import *

# Set your NASA_API_KEY in your Terminal/Powershell with the following commands
# You will need to do this every time you start your shell session
# Look into environments for long-term storage!
# MacOS/Linux:  export NASA_API_KEY="YOUR_REAL_KEY"
# Windows:      $env:NASA_API_KEY = "YOUR_REAL_KEY"

NASA_API_KEY = os.getenv("NASA_API_KEY") or "DEMO_KEY" #DEMO_KEY is rate limited
print(NASA_API_KEY)

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

