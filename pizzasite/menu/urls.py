
from django.urls import path
from .views import *

urlpatterns = [
    path("", home_view, name="home"),

    path('menu/', pizza_list, name='pizza_list'),

    path('cart/', cart_view, name='cart_view'),

    path('order/', order_view, name='order'),

    path('contact/', contact_view, name='contact' ),

    path("order/form/", order_form_view, name="order_form"),

    path("order/confirmation/", order_confirmation_view, name="order_confirmation"),
]