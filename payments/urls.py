
from django.urls import path
from . import views
from django.urls import path


urlpatterns = [
    path('<str:pname>/<int:id>/', views.payment, name='payment'),
    path('stripe/<str:pname>/<int:id>/',
         views.payment_stripe, name='payment_stripe'),
    path('paypal/<str:pname>/<int:id>/',
         views.payment_paypal, name='payment_paypal'),
    # path('charge/<int:amount>/', views.charge, name="charge"),
    path('success/<str:pname>/<int:id>/<int:amt>/<str:through>',
         views.successMsg, name='success'),
]
