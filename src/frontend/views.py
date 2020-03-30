from django.shortcuts import render
import folium

# Create your views here.

def map(requests):
    # create map object
    map = folium.Map(location=[49.246292, -123.116226], zoom_start=12)

    # map.save('map.html')
    context = {'map': map.get_root().render()}

    return render(requests, 'map.html', context)
