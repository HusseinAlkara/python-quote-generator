import requests
category = 'life'
api_url = 'https://api.api-ninjas.com/v1/quotes?category={}'.format(category)
response = requests.get(api_url, headers={'X-Api-Key': 'eg/0zFfA/wVdjUm8fmjRPA==FFOMj1DH8PmLvW6w'})
if response.status_code == 200:
    print(response.text)
else:
    print("Error",response.status_code, response.text)