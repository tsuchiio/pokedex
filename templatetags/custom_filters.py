from django import template

register = template.Library()

@register.filter
def add_url_param(value, arg):
    return f"{value}?{arg}"