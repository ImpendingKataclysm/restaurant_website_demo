from django import template

register = template.Library()


@register.filter
def format_phone_number(phone_number):
    digits = [char for char in str(phone_number) if char.isdigit()]
    formatted_phone = "({}{}{}) {}{}{}-{}{}{}{}".format(*digits)
    return formatted_phone
