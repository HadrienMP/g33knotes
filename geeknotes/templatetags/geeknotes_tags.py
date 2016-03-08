from django import template
from django.db.models import Count
from django.core.exceptions import FieldError
from taggit_templatetags.templatetags.taggit_extras import *

register = template.Library()

colors = ["33BBFF", "30C2E4", "2DC9C9", "2AD1AE", "27D893", "24E079"]

@register.filter
def date_to_color(date):
    index = date.month
    
    if index > len(colors):
        index = len(colors) - index % len(colors) - (len(colors) * (index / len(colors) - 1))
    else:
        index -= 1 
        
    return "#" + colors[index]
    
@register.assignment_tag
def tagcloud_qs(queryset):
    try:
        queryset = queryset.annotate(num_times=Count('taggeditem_items'))
    except FieldError:
        queryset = queryset.annotate(num_times=Count('taggit_taggeditem_items'))

    num_times = queryset.values_list('num_times', flat=True)

    try:
        
        weight_fun = get_weight_fun(T_MIN, T_MAX, min(num_times), max(num_times))
        queryset = queryset.order_by('name')
        for tag in queryset:
            tag.weight = weight_fun(tag.num_times)
            
    except (ZeroDivisionError, ValueError) as e :
        pass

    return queryset