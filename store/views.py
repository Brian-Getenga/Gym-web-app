from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Product, Order, OrderItem
from .cart import Cart

def product_list(request):
    """
    View function to list all products with optional search functionality.
    """
    query = request.GET.get('q')  # Get the search query from the GET request
    if query:
        # Filter products based on the search query
        products = Product.objects.filter(name__icontains=query)
    else:
        # Get all products if no search query is provided
        products = Product.objects.all()

    return render(request, 'store/product_list.html', {'products': products})


def product_detail(request, pk):
    """
    View function to display the details of a specific product.
    """
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'store/product_detail.html', {'product': product})

@login_required
def add_to_cart(request, product_id):
    """
    View function to add a product to the cart.
    """
    product = get_object_or_404(Product, id=product_id)
    cart = request.session.get('cart', {})

    # Increase quantity if product is already in the cart, otherwise add it
    if product_id in cart:
        cart[product_id] += 1
    else:
        cart[product_id] = 1

    request.session['cart'] = cart
    messages.success(request, f'Added {product.name} to your cart!')
    return redirect('product_list')

@login_required
def view_cart(request):
    cart = request.session.get('cart', {})
    products = Product.objects.filter(id__in=cart.keys())
    cart_items = [{'product': product, 'quantity': cart[str(product.id)]} for product in products]

    if request.method == 'POST':
        # Handle quantity updates
        for item in cart_items:
            product_id = str(item['product'].id)
            quantity = int(request.POST.get(f'quantity_{product_id}', 0))
            if quantity > 0:
                cart[product_id] = quantity
            else:
                cart.pop(product_id, None)
        request.session['cart'] = cart
        messages.success(request, 'Cart updated successfully!')
        return redirect('cart')

    # Calculate total price for each item
    for item in cart_items:
        item['total_price'] = item['product'].price * item['quantity']

    return render(request, 'store/cart.html', {'cart_items': cart_items})




@login_required
def remove_from_cart(request, product_id):
    cart = request.session.get('cart', {})
    product_id_str = str(product_id)

    if product_id_str in cart:
        cart.pop(product_id_str)
        request.session['cart'] = cart
        messages.success(request, 'Item removed from cart.')
    else:
        messages.error(request, 'Item not found in cart.')

    return redirect('cart')

def checkout(request):
    cart = Cart(request)
    if request.method == 'POST':
        total_price = cart.get_total_price()
        
        if total_price <= 0:
            messages.error(request, "Cart is empty or has invalid items.")
            return redirect('cart')

        order = Order(
            user=request.user,
            total_price=total_price
        )
        order.save()

        # Clear the cart after successful order creation
        cart.clear()
        
        messages.success(request, 'Order placed successfully!')
        return redirect('order_confirmation')  # Replace with your confirmation URL
    else:
        total_price = cart.get_total_price()
        return render(request, 'store/checkout.html', {'total_price': total_price})


@login_required
def order_confirmation(request, order_id):
    """
    View function to display the order confirmation page.
    """
    order = get_object_or_404(Order, id=order_id, user=request.user)
    order_items = OrderItem.objects.filter(order=order)
    return render(request, 'store/order_confirmation.html', {'order': order, 'order_items': order_items})