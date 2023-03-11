from django.core.paginator import Paginator
from django.shortcuts import render, reverse
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
    # можете добавить свои рецепты ;)
}


def home_view(request):
    template_name = 'calculator/home.html'
    pages = DATA
    context = {
        'pages': pages
    }
    print(context)
    return render(request, template_name, context)

def dish(request, name):
    template_name = 'calculator/index.html'
    dish = {}
    for key, value in DATA.items():
        if key == name:
            dish = DATA[name]
    servings = int(request.GET.get("servings", 1))
    recipe = {}
    for key, value in dish.items():
        recipe[key] = round(value * servings, 2)
    context = {'recipe': recipe}
    return render(request, template_name, context)

# _____________________________________________________________
# CONTENT = [str(i) for i in range(10000)]
#
# def pagi(request):
#     page_number = int(request.GET.get("page", 1))
#     paginator = Paginator(CONTENT, 10)
#     page = paginator.get_page(page_number)
#     context = {
#         'page': page
#     }
#     return render(request, 'calculator/pagi.html', context)
#
# def hello(request):
#     # name = request.GET.get("name", 'уважаемый')
#     # age = int(request.GET.get("age", 99))
#     # print(age)
#     # return HttpResponse(f'hehe, dj {name} {age*2}')
#     context = {
#         'test': 5,
#         'data': [1,7,9,11],
#         'val': "hello!",
#     }
#     return render(request, 'calculator/demo.html', context)
#
# def sum(request, a, b):
#     return HttpResponse(f'ass {a} & {b}')