class InputError(Exception):
    pass


# class Product:
#     def __init__(self, price):
#         self.set_price(price)

#     def get_price(self):
#         return self.__price

#     def set_price(self, price):
#         if price < 0:
#             raise InputError("Price not valid")

#         self.__price = price

#     price = property(get_price, set_price)


# p = Product(10)
# p.price = 20

# print(p.price)


# [BETTER WAY]
class Product:
    def __init__(self, price):
        self.__price = price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if price < 0:
            raise InputError("Price not valid")

        self.__price = price


p = Product(10)
p.price = 20

print(p.price)
