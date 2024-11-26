from django.shortcuts import render
import requests
# Create your views here.
def main(req):
    city='kochi'
    if req.method=='POST':
        city=req.POST['city']
        api_key='360e4bc3865e745ec844bd7ec054ca11'
        url=f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
        try:
            data=requests.get(url)
            weather_data=data.json()
            data={
                'city':city,
                'dis':weather_data['weather'][0]['description']
            }
        except:
            city='kochi'
    api_key='360e4bc3865e745ec844bd7ec054ca11'
    url=f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
    data=requests.get(url)
    weather_data=data.json()
    data={
        'city':city,
        'dis':weather_data['weather'][0]['description']
        }
    return render(req,'index.html',{'data':data})
        