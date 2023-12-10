from django import forms
from . import models


class ReservationForm(forms.ModelForm):
    """
    Models the Reservation Form based on the Reservation DB model.
    """
    party_name = forms.CharField(
        max_length=models.NAME_MAX_LEN,
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter the name of your party',
            'class': 'form-control',
        })
    )

    party_size = forms.IntegerField(
        max_value=100,
        required=True,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
        })
    )

    phone = forms.CharField(
        max_length=models.MAX_NUM,
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'Your phone number',
            'class': 'form-control',
        })
    )

    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'placeholder': 'Your email address',
            'class': 'form-control',
        }),
    )

    location = forms.ModelChoiceField(
        queryset=models.Location.objects.order_by('city'),
        widget=forms.RadioSelect,
        required=True,
    )

    date = forms.DateField(
        widget=forms.DateInput(attrs={
            'type': 'date',
            'class': 'form-control',
        }),
    )

    time = forms.TimeField(
        widget=forms.TimeInput(attrs={
            'type': 'time',
            'class': 'form-control',
        }),
    )

    class Meta:
        model = models.Reservation
        fields = (
            'party_name',
            'party_size',
            'phone',
            'email',
            'location',
            'date',
            'time',
        )
