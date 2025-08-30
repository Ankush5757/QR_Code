from django import forms


class QRCodeForm(forms.Form):
    restraurant_name = forms.CharField(max_length=50, label='Enter Name', 
                        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Name of the QR'}))
    url = forms.URLField(max_length=200, label='Enter URL',
                         widget=forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Enter URL of the QR'}))