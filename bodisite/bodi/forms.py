from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Record


class SignUpForm(UserCreationForm):
    """Форма регістрації Bootstrap"""
    email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email Адреса'}))
    first_name = forms.CharField(label="", max_length = 100 , widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Ім'я"}))
    last_name = forms.CharField(label="", max_length = 100 , widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Прізвище'}))


    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    
    def __init__ (self, *args, **kwargs):
        super(SignUpForm, self). __init__ (*args, **kwargs)
        
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Логін'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<span class="form-text text-muted"><small> Увага. Не більше 150 символів. Лише літери, цифри та @/./+/-/_.</small></span>'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Пароль'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Ваш пароль не може бути дуже схожим на вашу іншу особисту інформацію.</li><li>Ваш пароль має містити не менше 8 символів.</li><li>Ваш пароль не може бути типовим паролем.</li><li>Ваш пароль не може бути повністю цифровим.</li></ul>'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Підтвердьте пароль'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Для підтвердження введіть той самий пароль, що й раніше.</small></span>'


# Форма створити
class AddRecordForm(forms.ModelForm):
    first_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "Ім'я", "class": "form-control" }), label="")
    last_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "Прізвище", "class": "form-control" }), label="")
    email = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "Email", "class": "form-control" }), label="")
    phone = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "Телефон", "class": "form-control" }), label="")
    address = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "Адреса", "class": "form-control" }), label="")
    sity = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "Місто", "class": "form-control" }), label="")
    state = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "Країна", "class": "form-control" }), label="")
    zipcode = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "Індекс", "class": "form-control" }), label="")

    class Meta:
        model = Record
        exclude = ('user',)

