from django.db import models

# Create your models here.

class Ingredients(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nazwa składnika")

    def __str__(self):
        return self.name


class Pizza(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nazwa")
    description = models.TextField(blank=True, null=True, verbose_name="Opis")
    price = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Cena")
    is_available = models.BooleanField(default=True, verbose_name="Dostępność")
    ingredients = models.ManyToManyField(Ingredients, verbose_name="Składniki")

    def __str__(self):
        return self.name

class Cart(models.Model):
    pizzas = models.ManyToManyField(Pizza, verbose_name="Pizze w koszyku")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Data utworzenia")

class CartItem(models.Model):
    cart = models.ForeignKey('Cart', on_delete=models.CASCADE, verbose_name="Koszyk")
    pizza = models.ForeignKey('Pizza', on_delete=models.CASCADE, verbose_name="Pizza")
    quantity = models.PositiveIntegerField(default=1, verbose_name="Ilość")

class Order(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, verbose_name="Koszyk")
    name = models.CharField(max_length=20, verbose_name="Imię i nazwisko")
    phone_number = models.CharField(max_length=20, verbose_name="Numer telefonu")
    zip_code = models.CharField(max_length=10, default="", blank=True, verbose_name="Kod pocztowy")
    street = models.CharField(max_length=50, verbose_name="Ulica")
    city = models.CharField(max_length=15, verbose_name="Miasto")
    status = models.CharField(max_length=20,
                              choices=[
                                  ("pending", "Oczekuje"),
                                  ("completed", "Gotowe"),
                                  ("delivered", "Dostarczone")
                              ],
                              default="pending",
                              verbose_name="Status zamówienia"
                              )

    def __str__(self):
        return f"Zamówienie dla {self.name} ({self.status})"
