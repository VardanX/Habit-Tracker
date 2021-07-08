import requests
from datetime import datetime
USERNAME = "your name"
TOKEN = "your api key"
pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token" : TOKEN,
    "username" : USERNAME,
    "agreeTermsOfService" : "yes",
    "notMinor" : "yes",
}
#creating user account
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id" : "graph1",
    "name" : "Pushup Graph",
    "unit" : "pushups",
    "type" : "int",
    "color" : "momiji",

}
headers = {
    "X-USER-TOKEN" : TOKEN
}
#configuring graphs
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)
pixel_creation = f"{pixela_endpoint}/{USERNAME}/graphs/graph1"
today = datetime.now()
pixel_data = {
    "date" : today.strftime("%Y%m%d"),
    "quantity" : input("How many pushups did you do today?"),
}
#chainging date
response = requests.post(url=pixel_creation, json=pixel_data, headers=headers)
print(response.text)
update_endpiont = f"{pixela_endpoint}/{USERNAME}/graphs/graph1/{today.strftime('%Y%m%d')}"
new_pixel_data = {
    "quantity" : "50",

}
#updating
# response = requests.put(url=update_endpiont, json=new_pixel_data, headers=headers)
# print(response.text)

#deleting
# delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1/{today.strftime('%Y%m%d')}"
# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)