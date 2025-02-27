import requests

create_user_params = {
    "token" : "asbd1yw91hrsjfdb19",
    "username": "saladin",
    "agreeTermsOfService": "yes",
    "notMinor" : "yes"
}

url = "https://pixe.la/v1/users"

response = requests.post(url,json=create_user_params)
print(response.text)