from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    'porridge': {
        'молоко, л': 0.3,
        'геркулес, кг': 0.15,
        'соль, г': 5,
    }
}

def multiply(dict,portion):
    dict_new = {}
    for key, value in dict.items():
        dict_new[key]= round(dict[key]*portion,3)
    return dict_new

def index_view(request):
    meal = request.GET.get("meal", None)
    portion = request.GET.get("portion", 1)
    if meal != None:
        if int(portion) > 1:
            recipe = multiply(DATA[meal],int(portion))
        else:
            recipe = DATA[meal]
        context = {"portion": portion, "meal": meal, "recipe": recipe}
    else:
        context = {"portion": portion, "meal": meal}

    return render(request, "calculator/index.html", context=context)

def home_view(request):
    return HttpResponse(f"Привет, если вам нужны рецепты <a href={reverse('index')}> Рецепты </a>")
