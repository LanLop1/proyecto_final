from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from django.views.decorators.http import require_http_methods
from a_home.models import Image
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from stores.models import Store  
from stores.forms import StoreForm 
from django.template.loader import render_to_string
from django.shortcuts import  get_object_or_404
from django.http import HttpResponseRedirect

@login_required
@require_http_methods(["GET", "POST"])
def create_or_edit_store(request):
    try:
        # Intenta obtener la tienda existente del usuario
        store = Store.objects.get(owner=request.user)
        # Si existe, estamos editando
        editing = True
    except ObjectDoesNotExist:
        # Si no existe, estamos creando
        store = None
        editing = False

    if request.method == 'POST':
        if editing:
            form = StoreForm(request.POST, instance=store)
        else:
            form = StoreForm(request.POST)

        if form.is_valid():
            if editing:
                form.save()
                messages.success(request, "Tu tienda ha sido actualizada.")
            else:
                store = form.save(commit=False)
                store.owner = request.user
                store.save()
                messages.success(request, "Tu tienda ha sido creada.")
            return redirect('')
    else:
        form = StoreForm(instance=store) if editing else StoreForm()
    
    context = {
        'form': form,
        'editing': editing,
    }
    return render(request, 'stores/create_or_edit_store.html', context)




def store_detail(request, store_id):
    store = get_object_or_404(Store, id=store_id)
    html = render_to_string('store_detail.html', {'store': store})
    return HttpResponse(html)

def store_shop_view(request, id):
    store = get_object_or_404(Store, id=id)

    # Redirigir si la solicitud es HTMX
    if request.headers.get('HX-Request'):
        return HttpResponseRedirect(request.path) 

    return render(request, 'store_shop.html', {'store': store})
