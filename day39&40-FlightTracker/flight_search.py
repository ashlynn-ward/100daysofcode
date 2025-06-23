#Import requests module
import requests

#This class is responsible for talking to the Flight Search API
class FlightSearch:
    def __init__(self):
        self._api_key = "API KEY"
        self._api_secret = "API SECRET"
        self._token = self._get_new_token()


    #Method get destination code returns the code for the airport 
    def get_destination_code(self, city):
        #Pass each city to the API
        headers = {"Authorization": f"Bearer {self._token}"}
        query = {
            "keyword": city,
            "max": "2",
            "include": "AIRPORTS",
        }
        response = requests.get(url = "https://test.api.amadeus.com/v1/reference-data/locations/cities", headers = headers, params = query)
        #Try to access code and return it
        try:
            code = response.json()["data"][0]["iataCode"]
        except IndexError:
            print(f"Index Error: there is no code for an airport in {query['city']}.")
            return "N/A"
        except KeyError:
            print(f"Key Error: there is no code for an airport in this {query['city']}.")
            return "None"
        return code
    
    #Method get new token rquests a token from Amadeus API
    def _get_new_token(self):
        header = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        token_data = {
            "grant_type":"client_credentials",
            "client_id":self._api_key,
            "client_secret":self._api_secret
        }
        response = requests.post(url = "https://test.api.amadeus.com/v1/security/oauth2/token", headers = header, data = token_data)
        token = response.json()
        return token["access_token"]
    
    #Method check_flights searches the data received from Amadeus API for flight prices
    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time, is_direct = True):
        headers = {"Authorization": f"Bearer {self._token}"}
        query = {
            "originLocationCode": origin_city_code,
            "destinationLocationCode": destination_city_code,
            "departureDate": from_time.strftime("%Y-%m-%d"),
            "returnDate": to_time.strftime("%Y-%m-%d"),
            "adults": 1,
            "nonStop": "true" if is_direct else "false",
            "currencyCode": "GBP",
            "max": "10",
        }
        response = requests.get(url="https://test.api.amadeus.com/v2/shopping/flight-offers", headers=headers, params=query)

        #Print a message if API request returns an error code
        if response.status_code != 200:
            print(f"check_flights() response code: {response.status_code}")
            print("There was a problem with the flight search.\n"
                  "For details on status codes, check the API documentation:\n"
                  "https://developers.amadeus.com/self-service/category/flights/api-doc/flight-offers-search/api"
                  "-reference")
            print("Response body:", response.text)
            return None

        return response.json()