from django import template

register = template.Library()


@register.filter
def format_phone_number(phone_number):
    """
    Formats a phone number to display it in the standard (xxx) xxx-xxxx format
    :param phone_number: The non-formatted phone number
    :return: The formatted phone number
    """
    digits = [char for char in str(phone_number) if char.isdigit()]
    formatted_phone = "({}{}{}) {}{}{}-{}{}{}{}".format(*digits)
    return formatted_phone
