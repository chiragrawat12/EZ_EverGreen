from django.template import Library

register = Library()


@register.filter(name='addclass')
def addclass(field, class_attr):
    return field.as_widget(attrs={'class': class_attr, 'placeholder': 'Email'})


@register.filter(name='pwd1')
def pwd1(field, class_attr):
    return field.as_widget(attrs={'class': class_attr, 'placeholder': 'New Password'})


@register.filter(name='pwd2')
def pwd2(field, class_attr):
    return field.as_widget(attrs={'class': class_attr, 'placeholder': 'Confirm Password'})
