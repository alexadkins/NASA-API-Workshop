"""

Utility code for API Workshop
    for Clemson University's 
    NASA Space Apps Challenge Hackathon
    hosted by CUHackit
    
By Dr. Alex Adkins
October 4, 2025

"""

import json, requests

methods = {
    "GET": requests.get,
    "POST": requests.post,
    "PUT": requests.put,
    "PATCH": requests.patch,
    "DELETE": requests.delete
}

def print_json(json_obj: dict):
    """
    Pretty-print a JSON object with indentation.

    Args:
        json_obj (dict | list | str): 
            The JSON object to print. Can be a dictionary, list of objects,
            or a JSON-formatted string.

    Notes:
        - Dictionaries and lists will be formatted with 2-space indentation.
        - Strings will be parsed as JSON before formatting.
        - If the input type is unsupported, a warning message is printed.
    """
    
    if isinstance(json_obj, dict):
        print(json.dumps(json_obj, indent=2))
    elif isinstance(json_obj, str):
        print(json.dumps(json.loads(json_obj), indent=2))
    elif isinstance(json_obj, list):
        for obj in json_obj:
            print_json(obj)
    else:
        print(f"Failed to print object of type {type(json_obj)} to json format.")
        
def send_request(method, url, params = None, headers = None, body = None, suppress_output = False): 
    """
    Send an HTTP request using the requests library.

    Args:
        method (str):
            The HTTP method (e.g., 'GET', 'POST', 'PUT', 'PATCH', 'DELETE').
        url (str):
            The target URL.
        params (dict, optional):
            Query parameters to append to the URL.
        headers (dict, optional):
            HTTP headers to include in the request.
        body (str | dict, optional):
            Request payload for methods like POST, PUT, or PATCH.
            If a dictionary is provided, it will be sent as form data.
        suppress_output (bool, default=False):
            If True, suppresses printing success messages.

    Returns:
        Any:
            Parsed JSON response if the request is successful.

    Raises:
        requests.HTTPError:
            If the request fails with a status code >= 300.

    Example:
        >>> response = send_request(
        ...     "GET",
        ...     "https://eonet.gsfc.nasa.gov/api/v2.1/events",
        ...     params = {"days": 2},
        ...     headers = {"api_key": NASA_API_KEY}
        ... )
        >>> print_json(response)
    """
    
    r = methods[method.upper()](url, params=params, headers=headers, data=body)
    
    if r.status_code < 300:
        if not suppress_output:
            print(f"Successful {method} to {url}")
        return r.json()
    else:
        print(f"Failed to {method} from {url}: \n"
              "\t{r.status_code} Error: {r.text}"
        )
        r.raise_for_status()
        