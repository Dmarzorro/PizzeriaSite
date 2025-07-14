from django import forms

from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ["name", "phone_number", "city", 'zip_code', "street",]
        labels = {
            'phone_number': 'Numer telefonu',
            'name': 'Imię i nazwisko',
            'city': 'Miasto',
            'zip_code': 'Kod pocztowy',
            'street': 'Ulica',
        }

class ContactForm(forms.Form):
    imie = forms.CharField(label="Imię", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    telefon = forms.CharField(label="Numer telefonu", required=False, max_length=20, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label="Email", widget=forms.EmailInput(attrs={'class': 'form-control'}))
    tresc = forms.CharField(label="Treść", widget=forms.Textarea(attrs={'class': 'form-control'}))