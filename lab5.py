class Sneakers:
    def __init__(self, brand="Unknown", size=0, color="Unknown",
                price=0.0, quantity=0, material="Unknown", 
                number_of_sales=0):

        self.__brand = brand
        self.__size = size
        self.__color = color
        self.__price = price
        self.__quantity = quantity
        self.__material = material
        self.__number_of_sales = number_of_sales

    def __del__(self):
        print(f"Sneakers object {self.__brand} destroyed.")

    def get_brand(self):
        return self.__brand

    def get_size(self):
        return self.__size

    def get_color(self):
        return self.__color

    def get_price(self):
        return self.__price

    def get_quantity(self):
        return self.__quantity

    def get_material(self):
        return self.__material

    def get_number_of_sales(self):
        return self.__number_of_sales

    def set_brand(self, brand):
        self.__brand = brand

    def set_size(self, size):
        self.__size = size

    def set_color(self, color):
        self.__color = color

    def set_price(self, price):
        self.__price = price

    def set_quantity(self, quantity):
        self.__quantity = quantity

    def set_material(self, material):
        self.__material = material

    def set_number_of_sales(self, number_of_sales):
        self.__number_of_sales = number_of_sales

    def __str__(self):
        return (
            f"Brand: {self.__brand}\n"
            f"Size: {self.__size}\n"
            f"Color: {self.__color}\n"
            f"Price: {self.__price}\n"
            f"Quantity: {self.__quantity}\n"
            f"Material: {self.__material}\n"
            f"Number of sales: {self.__number_of_sales}\n"
        )


class SportShoesStore:
    def __init__(self, sneakers=None):
        if sneakers is None:
            self.__sneakers = []
        else:
            self.__sneakers = sneakers

    def __del__(self):
        print("SportShoesStore deleted")

    def get_sneakers(self):
            return self.__sneakers

    def add_sneakers(self, sneakers):
        self.__sneakers.append(sneakers)

    def remove_sneakers(self, brand):
        for sneakers in self.__sneakers:
            if sneakers.get_brand() == brand:
                self.__sneakers.remove(sneakers)
                print(f"{brand} removed from store")
                return

        print(f"{brand} not found.")

    def sort_by_price(self):
        self.__sneakers.sort(
            key=lambda sneakers: sneakers.get_price()
        )
        
    def sort_by_quantity(self):
        self.__sneakers.sort(
            key=lambda sneakers: sneakers.get_quantity()
        )
    
    def show_top_sneakers(self):
        sorted_sneakers = sorted(
            self.__sneakers,
            key=lambda sneakers: sneakers.get_number_of_sales(),
            reverse=True
        )

        print("\nTOP 3 MOST POPULAR SNEAKERS")

        for sneakers in sorted_sneakers[:3]:
            print(sneakers)
            print("--------------------")

    def show_all_sneakers(self):
        for sneakers in self.__sneakers:
            print(sneakers)
            print("--------------------")

def main():
    sneakers1 = Sneakers("Nike", 42, "Black", 4500, 10, "Leather", 150)
    sneakers2 = Sneakers("Adidas", 43, "White", 3800, 15, "Textile", 200)
    sneakers3 = Sneakers("Puma", 41, "Red", 3200, 8, "Suede", 100)
    sneakers4 = Sneakers("New Balance", 44, "Grey", 5200, 12, "Mesh", 250)
    sneakers5 = Sneakers("Reebok", 42, "Blue", 2900, 20, "Leather", 80)

    store = SportShoesStore()

    store.add_sneakers(sneakers1)
    store.add_sneakers(sneakers2)
    store.add_sneakers(sneakers3)
    store.add_sneakers(sneakers4)
    store.add_sneakers(sneakers5)


    for sneakers in store.get_sneakers():
        print(
            f"Brand: {sneakers.get_brand()}, "
            f"Color: {sneakers.get_color()}"
        )


    print("\nALL SNEAKERS")
    store.show_all_sneakers()

    print("\nSORT BY PRICE:")
    store.sort_by_price()
    store.show_all_sneakers()

    print("\nSORT BY QUANTITY:")
    store.sort_by_quantity()
    store.show_all_sneakers()

    print("\nTOP POPULAR SNEAKERS:")
    store.show_top_sneakers()

    print("\nREMOVE SNEAKERS:")
    store.remove_sneakers("Puma")

    print("\nUPDATED STORE:")
    store.show_all_sneakers()

    
main()