#### Ejercicio: crear un programa para registrar productos y total de ventas

class CashRegister:

    def __init__(self, cashier_name):
        self.cashier_name = cashier_name
        self.product_list = {}

    def print_products(self):
        print(self.product_list)

    def add_products(self, product, pieces=1, price = 0.0):
        if isinstance(product, str) and isinstance(pieces, int) and isinstance(price, float):
            values_to_add = {product: {
                    'pieces': pieces,
                    'price': price}
            }
            self.product_list.update(values_to_add)
        else:
            print("Please enter valid values.")

    def remove_product(self, product):
        if product in self.product_list:
            del self.product_list[product]
        else:
            print("That product is not in the purchase list.")

    def update_price(self, product, new_price):
        if product in self.product_list and isinstance(new_price, float):
            self.product_list[product]["price"] = new_price
        else:
            print("Enter a valid product or new price.")

    def calculate_subtotal(self):
        subtotal = 0.0
        for i in self.product_list.keys():
            print(i, self.product_list[i]["price"] * self.product_list[i]["pieces"])
            subtotal += self.product_list[i]["price"] * self.product_list[i]["pieces"]
        print("El subtotal de la orden es:",subtotal)
        return subtotal

    def add_taxes(self):
        subtotal = self.calculate_subtotal()
        total_final = round(subtotal*.05 + subtotal,2)
        print(total_final)
        return total_final


obj1 = CashRegister("Juanchito")
obj1.print_products()
obj1.add_products("Leche 1LT")
obj1.print_products()
obj1.add_products("Galletas",2)
obj1.print_products()
obj1.remove_product("Leche 1LT")
obj1.print_products()
obj1.update_price("Galletas", 5.50)
obj1.add_products("Leche 1LT")
obj1.update_price("Leche 1LT", 34.23)
obj1.print_products()
obj1.calculate_subtotal()
obj1.add_taxes()


