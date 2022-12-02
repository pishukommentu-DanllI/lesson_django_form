from django import forms


class Two_form(forms.Form):
    Name = forms.CharField(widget=forms.TextInput(
        attrs={' placeholder': 'Имя'}
    ))
    SuName = forms.CharField(widget=forms.TextInput(
        attrs={' placeholder': 'Фамилия'}
    ))
    Email = forms.CharField(widget=forms.EmailInput(
        attrs={' placeholder': 'Email'}
    ))
    Adress = forms.CharField(widget=forms.TextInput(
        attrs={' placeholder': 'Адресс'}
    ))


class One_form(forms.Form):

    Name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'contaner__wrap__BlockForm__Form__BlockBtn__input input', 'type': 'text', 'placeholder': 'Name'}
    ))

    Email = forms.CharField(widget=forms.EmailInput(
        attrs={'class': 'contaner__wrap__BlockForm__Form__BlockBtn__input input', 'type': 'email', 'placeholder': 'Email'}
    ))

    Phone = forms.CharField(widget=forms.NumberInput(
        attrs={'class': 'contaner__wrap__BlockForm__Form__BlockBtn__input input', 'type': 'tel', 'placeholder': 'Phone Number'}
    ))

    TextArea = forms.CharField(widget=forms.Textarea(
        attrs={'class': 'contaner__wrap__BlockForm__Form__input input', 'placeholder': 'Tell us about the car needing service(s)'}
    ))

    Select = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'contaner__wrap__BlockForm__Form__BlockBtn__input input', 'type': 'text', 'placeholder': 'Select Service'}
    ))