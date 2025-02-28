import requests
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

pixel_config = {
    "date" : "20250227",
    "quantity": "1.1"
}

post_pixel = requests.post(url = pixel_endpoint,json=pixel_config, headers = headers)