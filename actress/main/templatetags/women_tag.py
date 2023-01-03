from django import template
from main.models import *

register = template.Library()

@register.simple_tag()
def get_categories(filter=None):
    if not filter:
        return Category.objects.all()
    else:
        return Category.objects.filter(pk=filter)
@register.inclusion_tag('list_categories.html')
def show_cats():
    cats = Category.objects.all()
    return({"cats":cats})