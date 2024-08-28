
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Cart, CartItem, Product, Order, OrderItem

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart, created = Cart.objects.get_or_create(usuario=request.user.profile)
    cart_item, item_created = CartItem.objects.get_or_create(cart=cart, product=product)
    
    if not item_created:
        cart_item.quantity += 1
        cart_item.save()
    
    return redirect('cart_detail')

@login_required
def cart_detail(request):
    cart, created = Cart.objects.get_or_create(usuario=request.user.profile)
    return render(request, 'orders/cart_detail.html', {'cart': cart})

@login_required
def checkout(request):
    cart = get_object_or_404(Cart, usuario=request.user.profile)
    
    if request.method == 'POST':
        # Crear un nuevo pedido
        order = Order.objects.create(
            usuario=request.user.profile,
            store=cart.items.first().product.store,  # Asumiendo que todos los productos son de la misma tienda
            totalamount=sum(item.quantity * item.price for item in cart.items.all()),
            orderstatus='Pending'
        )
        
        # Crear OrderItems
        for cart_item in cart.items.all():
            OrderItem.objects.create(
                order=order,
                product=cart_item.product,
                quantity=cart_item.quantity,
                price=cart_item.price
            )
        
        # Limpiar el carrito
        cart.items.all().delete()
        
        return redirect('order_confirmation', order_id=order.id)
    
    return render(request, 'orders/checkout.html', {'cart': cart})
# Create your views here.
