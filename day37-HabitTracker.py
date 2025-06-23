#Habit Tracker
#Ashlynn Ward, June 16, 2025
#This program uses the Pixela API to maintain a habit tracker. It allows the user to update it  with their daily accomplishments.\
#To use this program, add in your own token and username. Creating an account and graph are commented out at the moment because they have
#already been run.

#Import requests module, and os and datetime libraries
import requests
import os
import datetime as dt

#Define endpoint and parameters for Pixela API
PIXELA_ENDPOINT = "https://pixe.la/v1/users"
TOKEN = "ENTER TOKEN HERE"
USERNAME = "ENTER USERNAME HERE"
GRAPH_NAME = "graph1"
user_params = {
    "token":TOKEN,
    "username":USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes"
}

#Created an account on Pixela - commented out because it has been done
#response = requests.post(url = PIXELA_ENDPOINT, json = user_params)

#Define parameters for graph
graph_config = {
    "id":GRAPH_NAME,
    "name":"Coding Graph",
    "unit":"minutes",
    "type":"int",
    "color":"ajisai"
}

headers = {
    "X-USER-TOKEN":TOKEN
}

#Create a graph - commented out because it has been done
graph_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"
#response = requests.post(url = graph_endpoint, json = graph_config, headers = headers)

#Store today's date
today = dt.datetime.now()

#Define pixel parameters
pixel_data = {
    "date":today.strftime("%Y%m%d"),
    "quantity":"60",
}

#Add a pixel to the graph
pixel_creation_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_NAME}"
requests.post(url = pixel_creation_endpoint, json=pixel_data, headers=headers)

#Update a pixel
update_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_NAME}/{pixel_data['date']}"
update_data={
    "quantity":"45"
}
requests.put(url=update_endpoint, json=update_data, headers=headers)

#Delete a pixel
delete_endpoint = update_endpoint
requests.delete(url=delete_endpoint, headers=headers)