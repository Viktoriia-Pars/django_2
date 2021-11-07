from django.shortcuts import render, redirect
from django.urls import reverse
from django.conf import settings
import csv
from django.core.paginator import Paginator

def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    page_number = int(request.GET.get('page', 1))
    elements_per_page = 15

    with open(settings.BUS_STATION_CSV, encoding='utf-8') as file:
        reader = csv.DictReader(file)
        station_list = []
        for r in reader:
            filtered_dict = {}
            for k, v in r.items():
                if k in ('Name', 'Street', 'District'):
                    filtered_dict[k] = v
                    station_list.append(filtered_dict)
        paginator = Paginator(station_list, elements_per_page)
        page = paginator.get_page(page_number)


    context = {
        'bus_stations': bus_stations,
        'page': page,
    }
    return render(request, 'stations/index.html', context)
