from django.shortcuts import render, redirect
import requests
from .models import ObjectInfo
from .forms import CityForm


def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=5aa8273002e15c2c4a8d36bddaa1e027'
    #url2 = 'http://api.openweathermap.org/data/2.5/weather?id={}&appid=cb718ae80779c2c4242d37314a76d398'
    err_msg = ''
    message = ''
    message_class = ''
    #city_id = 3099778

   # while city_id < 3100883:
    #    c = requests.get(url2.format(city_id)).json()
     #   if c['cod'] == 200:
      #      b = ObjectInfo(cityName=c['name'])
       #     b.save()
        #city_id = city_id + 5

    if request.method == 'POST':
        form = CityForm(request.POST)

        if form.is_valid():
            new_city = form.cleaned_data['cityName']
            existing_city_count = ObjectInfo.objects.filter(cityName = new_city).count()

            if existing_city_count == 0:
                r = requests.get(url.format(new_city)).json()
                if r['cod'] == 200:
                    form.save()
                else:
                    err_msg = 'city doesnt exists'
            else:
                err_msg = 'City already exists'
        if err_msg:
            message = err_msg
            message_class = 'is-danger'
        else:
            message = 'city added'
            message_class = 'is-success'


    form = CityForm()

    cites = ObjectInfo.objects.all()

    wheather_data = []

    for city in cites:

        r = requests.get(url.format(city)).json()

        city_wheather = {
            'city':  city.cityName,
            'temperature': r['main']['temp'],
            'humidity': r['main']['humidity'],
            'speed': r['wind']['speed'],
            'icon': r['weather'][0]['icon']
        }
        wheather_data.append(city_wheather)

    context = {'wheather_data': wheather_data,
               'form': form,
               'message': message,
               'message_class': message_class
               }
    return render(request, 'wheather/wheather.html', context)

def delete_city(request, city_name):
    ObjectInfo.objects.get(cityName=city_name).delete()

    return redirect('home')