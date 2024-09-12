# store/cart.py

class Cart:
    def __init__(self, request):
        self.session = request.session
        self.cart = self.session.get('cart', {})
        if 'cart' not in self.session:
            self.session['cart'] = {}
            self.cart = self.session['cart']

    def add(self, product_id, quantity=1):
        product_id = str(product_id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0}
        self.cart[product_id]['quantity'] += quantity
        self.save()

    def remove(self, product_id):
        product_id = str(product_id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def get_total_price(self):
        total_price = 0
        for item_id, item_data in self.cart.items():
            product_price = self.get_product_price(item_id)  # Replace with actual price lookup
            quantity = item_data.get('quantity', 0)
            total_price += quantity * product_price
        return total_price

    def get_product_price(self, product_id):
        # Replace with actual product price lookup
        # This function should return the price of the product
        # For demonstration, we're returning a fixed price of $10
        return 10

    def save(self):
        self.session['cart'] = self.cart
        self.session.modified = True

    def clear(self):
        self.session['cart'] = {}
        self.session.modified = True
