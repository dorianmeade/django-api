from django.shortcuts import render
import requests 

# Create your views here.
def index(request):
    headers = {
        'Accept': 'application/json' #to return json format
    } 
    response = requests.get(url='https://ec.europa.eu/esco/api/resource/occupation?uri=http://data.europa.eu/esco/occupation/faed411a-f920-4100-86a8-b877928b429c&language=en', headers=headers)
    data = response.json()
    return render(request, 'index.html', {
        'career': data['title'],
        'description' : data['description']['en']['literal']
    })

def career(request, title):
    if title == "developer":
            uri = 'http://data.europa.eu/esco/occupation/c40a2919-48a9-40ea-b506-1f34f693496d'
    elif title == "uidesigner":
        uri = 'http://data.europa.eu/esco/occupation/96e20037-0a25-4bf6-a25e-808d1605d890'
    elif title == "uxdesigner":
        uri = 'http://data.europa.eu/esco/occupation/faed411a-f920-4100-86a8-b877928b429c' 

    response = requests.get(url="https://ec.europa.eu/esco/api/resource/occupation?language=en&uri="+uri, headers={'Accept': 'application/json' })
    data = response.json()

    return render(request, 'index.html', {
        'career': data['title'], 
        'description': data['description']['en']['literal']
    })
    