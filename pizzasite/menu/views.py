from django.shortcuts import render, redirect
from .models import Pizza, Order
from django.http import JsonResponse
import json
from .forms import ContactForm, OrderForm

def pizza_list(request):
    pizzas = Pizza.objects.all()
    return render(request, 'menu/pizza_list.html', {'pizzas': pizzas})

def cart_view(request):
    return render(request, 'menu/cart.html')

def contact_view(request):
    form = ContactForm()
    return render(request, 'menu/contact.html', {'form': form})


def home_view(request):
    return render(request, 'menu/home.html')

from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from .models import Order, Pizza

from .models import Cart

@csrf_exempt
def order_view(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            cart_data = data.get("cart", {})

            if not cart_data:
                return JsonResponse({"error": "Koszyk jest pusty"}, status=400)

            cart_obj = Cart.objects.create()

            order = Order.objects.create(
                cart=cart_obj,
                name="Anonim",
                phone_number="000-000-000",
                city="Miasto"
            )

            for pizza_id, item in cart_data.items():
                try:
                    pizza = Pizza.objects.get(pk=pizza_id)
                    for _ in range(item["quantity"]):
                        cart_obj.pizzas.add(pizza)
                except Pizza.DoesNotExist:
                    return JsonResponse({"error": f"Nie znaleziono pizzy o ID {pizza_id}"}, status=404)

            return JsonResponse({"message": "Zamówienie zostało złożone!"})
        except json.JSONDecodeError:
            return JsonResponse({"error": "Nieprawidłowe dane JSON"}, status=400)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    return JsonResponse({"error": "Nieprawidłowa metoda żądania"}, status=405)


def order_form_view(request):
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            cart_data_str = request.POST.get("cart_data", "{}")
            try:
                cart_data = json.loads(cart_data_str)
            except json.JSONDecodeError:
                cart_data = {}

            if not cart_data:
                form.add_error(None, "Twój koszyk jest pusty!")
                return render(request, "menu/order.html", {"form": form})

            cart_obj = Cart.objects.create()
            for pizza_id, item in cart_data.items():
                try:
                    pizza = Pizza.objects.get(pk=pizza_id)
                    for _ in range(item["quantity"]):
                        cart_obj.pizzas.add(pizza)
                except Pizza.DoesNotExist:
                    continue

            order = form.save(commit=False)
            order.cart = cart_obj
            order.save()

            return redirect("order_confirmation")
    else:
        form = OrderForm()

    return render(request, "menu/order.html", {"form": form})


def order_confirmation_view(request):
    return render(request, "menu/order_confirmation.html")

