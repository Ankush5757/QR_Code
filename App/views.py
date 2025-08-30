from django.shortcuts import render
from .forms import QRCodeForm
import qrcode
import os
from io import BytesIO
from django.conf import settings
import base64


# Create your views here.

def generate_qr(request):
    if request.method == 'POST':
        form = QRCodeForm(request.POST)
        if form.is_valid():
            rest_name = form.cleaned_data['restraurant_name']
            url = form.cleaned_data['url']
            print(rest_name, url)
        
            # Generate QR Code
            qr = qrcode.make(url)
            file_name = rest_name.replace(" ", "_").lower() + "_.png"
            
            # Convert to Base64
            buffer = BytesIO()
            qr.save(buffer, format='PNG')
            qr_image_base64 = base64.b64encode(buffer.getvalue()).decode()
            qr_url = f"data:image/png;base64,{qr_image_base64}"
            
            context = { 
                'rest_name': rest_name,
                'qr_url': qr_url,
                'file_name': file_name,
            }
            return render(request, 'Qr_Result.html', context)
    else:
        form = QRCodeForm()
        context = {'form': form}
        return render(request, 'Generate_QR.html', context)