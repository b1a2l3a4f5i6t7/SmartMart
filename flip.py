from 
class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.cart = []
        self.orders = []

    def add_to_cart(self, product):
        self.cart.append(product)

    def place_order(self):
        order = Order(self.cart)
        self.orders.append(order)
        self.cart = []

    def view_orders(self):
        for order in self.orders:
            print(order)

class Product:
    def __init__(self, name, price, description):
        self.name = name
        self.price = price
        self.description = description

    def __str__(self):
        return f"{self.name} - {self.price}$"

class Order:
    def __init__(self, products):
        self.products = products
        self.status = "Pending"

    def update_status(self, new_status):
        self.status = new_status

    def __str__(self):
        product_list = "\n".join([str(product) for product in self.products])
        return f"Status: {self.status}\nProducts:\n{product_list}"

# Sample Usage
if __name__ == "__main__":
    # Create some products
    product1 = Product("Phone", 500, "A smartphone")
    product2 = Product("Headphones", 50, "Noise-canceling headphones")

    # Create a user
    user = User("john", "password")

    # Add products to the user's cart
    user.add_to_cart(product1)
    user.add_to_cart(product2)

    # Place the order
    user.place_order()

    # View the order history
    user.view_orders()