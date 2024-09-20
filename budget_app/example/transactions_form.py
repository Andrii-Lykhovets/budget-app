from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator


class TransactionForm(forms.Form):
    income = forms.FloatField(
        label='Income',
        validators=[MinValueValidator(0), MaxValueValidator(99999999.99)],
    )
    expenditure = forms.FloatField(
        label='Expenditure',
        validators=[MinValueValidator(-99999999.99), MaxValueValidator(0)],
    )
    description = forms.CharField(
        label='Description',
        max_length=255,  # must be the same value as in the DB
    )
    date_time = forms.DateTimeField(
        label='Date and Time'
    )
    company_id = forms.IntegerField(
        label='Company ID'
    )
