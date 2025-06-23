#A list of questions accessed through an API request that include true/false answers

#Import requests
import requests

#Define parameters for API request
parameters = {
    "amount":10,
    "type":"boolean"
}

#Request data from API, and show an error if error code is returned
response = requests.get(url = "https://opentdb.com/api.php", params = parameters)
response.raise_for_status()
#Open data as a json file
data = response.json()
question_data = data["results"]