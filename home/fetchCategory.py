from home.models import Category

def all_categories():
    category = Category.objects.all()
    return category