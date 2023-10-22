from django import template
from django.utils import timezone

register = template.Library()

@register.filter(name='expired')
def expired(value):
    print(value)
    now = timezone.now()
    print(now)
    try:
        result = value <= now
    except Exception as e:
        print(e.args)
    print(result)
    return result