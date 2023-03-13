from django import template

register = template.Library()


@register.simple_tag(takes_context=True)
def has_perm(context, permission_string):
    user = context['user']
    return user.has_perm(permission_string)

