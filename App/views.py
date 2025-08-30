from django.shortcuts import render
from .forms import QRCodeForm
import qrcode
import os
from django.conf import settings


# Create your views here.

def generate_qr(request):
    if request.method == 'POST':
        form = QRCodeForm(request.POST)
        if form.is_valid():
            rest_name = form.cleaned_data['restraurant_name']
            url = form.cleaned_data['url']
            print(rest_name, url)
        
            # Generate QR Coode
            qr = qrcode.make(url)
            file_name = rest_name.replace(" ", "_").lower() + "_.png"
            file_path = os.path.join(settings.MEDIA_ROOT, file_name) #media/rest_name_menu.png
            qr.save(file_path)
            context = {
                'rest_name': rest_name,
            }
        

            qr_url = os.path.join(settings.MEDIA_URL, file_name)
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