from django.shortcuts import render
from django.http import HttpResponseBadRequest

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'паста, г': 200,
        'сыр, г': 50,
        'масло, г': 20,
    },
    # Добавьте другие рецепты по аналогии
}

def recipe_view(request, recipe_slug):
    servings = int(request.GET.get('servings', 1))
    recipe_data = DATA.get(recipe_slug)
    if not recipe_data:
        return HttpResponseBadRequest('Рецепт не найден')

    context = {
        'recipe_title': recipe_slug.capitalize(),  # Название рецепта в заголовке
        'recipe': {ingredient: amount * servings for ingredient, amount in recipe_data.items()},
    }
    return render(request, 'calculator/index.html', context)

