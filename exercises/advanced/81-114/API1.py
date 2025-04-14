
def fecth_data(endpoint, filters={}):
    import requests
    url = f'https://rickandmortyapi.com/api/{endpoint}'
    response = requests.get(url, params=filters)

    return response.json() if response.status_code == 200 else None

    
characters = fecth_data('character', 'name=Rick')

if characters:
    print(characters)
else:
    print('Failed to fecth data')
    