import requests

#Se ocupa la api de OMD se debe conseguir una key para usarlo.

base_url = 'http://www.omdbapi.com/'


def Main():
    title = input("Ingrese un titulo: ")
    params = {
        'apikey':'',
        't': title
    }
    
    response = requests.get(base_url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        
        titleAPI = data["Title"]
        yearAPI = data["Year"]
        runtimeAPI = data["Runtime"]
        
        print("La pelicula es:",titleAPI,"del año",yearAPI,"con una duración de",runtimeAPI)
    else:
        print(f'Error: {response.status_code}')


if __name__=="__main__":
    Main()