from django.shortcuts import render

from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from .forms import StoreForm, QRCodeForm, ImageForm
from .models import Store, QRCode
from a_home.models import Image

@require_http_methods(["GET", "POST"])
def create_store(request):
    store_form = StoreForm()
    qr_form = QRCodeForm()
    image_form = ImageForm()

    if request.method == 'POST':
        if 'store_submit' in request.POST:
            store_form = StoreForm(request.POST)
            if store_form.is_valid():
                store = store_form.save()
                return HttpResponse(f"<div id='store-{store.id}'>{store.name} creado exitosamente!</div>")
        elif 'qr_submit' in request.POST:
            qr_form = QRCodeForm(request.POST)
            if qr_form.is_valid():
                qr = qr_form.save()
                return HttpResponse(f"<div id='qr-{qr.id}'>QR Code para {qr.store.name} creado exitosamente!</div>")
        elif 'image_submit' in request.POST:
            image_form = ImageForm(request.POST, request.FILES)
            if image_form.is_valid():
                image = image_form.save()
                return HttpResponse(f'<option value="{image.id}">{image.file.name}</option>')
    
    return render(request, 'stores/create_store.html', {
        'store_form': store_form,
        'qr_form': qr_form,
        'image_form': image_form
    })

def store_list(request):
    stores = Store.objects.all()
    return render(request, 'stores/store_list.html', {'stores': stores})
