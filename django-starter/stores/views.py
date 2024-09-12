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
        store = Store.objects.get(owner=request.user)
        editing = True
    except Store.DoesNotExist:
        store = None
        editing = False

    if request.method == 'POST':
        form = StoreForm(request.POST, request.FILES, instance=store)
        if form.is_valid():
            store = form.save(commit=False)
            if not editing:
                store.owner = request.user
            
            # Manejo de imágenes
            for field_name in ['imageStore', 'logoImage', 'bannerImage']:
                if field_name in request.FILES:
                    image_file = request.FILES[field_name]
                    image = Image.objects.create(
                        user=request.user,
                        file=image_file,
                        description=f"{field_name} for {store.name}"
                    )
                    setattr(store, field_name, image)
            
            store.save()
            action = "actualizada" if editing else "creada"
            messages.success(request, f"Tu tienda ha sido {action} exitosamente.")
            return redirect(reverse('stores:create_or_edit_store'))
    else:
        form = StoreForm(instance=store)
    
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
