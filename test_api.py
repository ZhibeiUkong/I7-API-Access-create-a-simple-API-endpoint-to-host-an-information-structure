import requests

base_url = "https://upfront-snort-concur.ngrok-free.dev"

print(requests.get(base_url + "/").text)

foods_response = requests.get(base_url + "/api/foods")
print(foods_response.json())

one_food_response = requests.get(base_url + "/api/foods/FS-001")
print(one_food_response.json())

search_response = requests.get(base_url + "/api/foods/search?status=Safe")
print(search_response.json())