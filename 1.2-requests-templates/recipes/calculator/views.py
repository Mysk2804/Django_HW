from django.http import HttpResponse
from django.shortcuts import render
from pprint import pprint

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
    # можете добавить свои рецепты ;)
}

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }

def recipte(request):
    return render(request, 'calculator/recipe.html')


def calculator(request, recipte):
    context = {}
    servings = request.GET.get('servings', 1)
    for recipt, ingridients in DATA.items():
        if recipt == recipte:
            count = {}
            for key, val in ingridients.items():
                coun = {f'{key}': f'{val * int(servings)}'}
                count.update(coun)
            context = {'recipe': count}


    return render(request, 'calculator/index.html', context)


