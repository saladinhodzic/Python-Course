import requests
from datetime import datetime
USERNAME = "saladin"
TOKEN = "asbd1yw91hrsjfdb19"
create_user_params = {
    "token" : TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor" : "yes"
}

url = "https://pixe.la/v1/users"

# response = requests.post(url,json=create_user_params)
# print(response.text)

graph_endpoint = f"{url}/{USERNAME}/graphs"

graph_config = {
    "id":"sakkka1",
    "name":"Walking",
    "unit":"km",
    "type":"float",
    "color":"sora"
}

headers = {
    "X-USER-TOKEN":TOKEN
}

# make_graph = requests.post(graph_endpoint,json=graph_config,headers=headers)

pixel_endpoint = f"{url}/{USERNAME}/graphs/sakkka1"

today = datetime.now()
pixel_config = {
    "date" : today.strftime("%Y%m%d"),
    "quantity": "3"
}
# post_pixel = requests.post(url = pixel_endpoint,json=pixel_config, headers = headers)

pixel_update_endpoint = f"{pixel_endpoint}/20250227"

pixel_update = requests.put(pixel_update_endpoint,json={"quantity":"0.5"},headers=headers)