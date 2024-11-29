from django.shortcuts import render,get_object_or_404
from .models import card,Category



def index(request):
    cards = card.objects.all()  # Get all card objects
    return render(request, 'index.html', {'cards': cards})

def category_products(request, category_id):
    try:
        category = Category.objects.get(id=category_id)
        cards = card.objects.filter(category=category)
        return render(request, 'products.html', {
            'category': category,
            'cards': cards  
        })
    except Category.DoesNotExist:
        return render(request, 'error_page.html', {'message': 'Category not found'})
