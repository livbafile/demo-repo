import requests

url = "https://v2.jokeapi.dev/joke/Any"

response = requests.get(url)


if response.status_code == 200:
    
    
    
    if 'joke' in response.json():
        
        print(response.json()['joke'])
        #print('\n')
        print(response.json()['delivery'])
    else:
        print(response.json()['setup'])
        #print('\n')
        print(response.json()['delivery'])
    
    
    
    
else:
    
    print("Oops! Something went wrong.")