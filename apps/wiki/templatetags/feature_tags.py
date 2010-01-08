from django import template

register = template.Library()

from wiki.models import *

@register.inclusion_tag('wiki/welcome_message.html')
def show_welcome():
    article = Article.objects.all().get_by("WelcomeMessage", None)
    return {'article': article}

