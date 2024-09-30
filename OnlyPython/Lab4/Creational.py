#Singleton
class Shop:
    instance = None #Unity moment
    def __new__(cls):
        if cls.instance is None:
            cls.instance = super(Shop, cls).__new__(cls)
            cls.instance.products = []
        return cls.instance

    def add_product(self, _p):
        self.products.append(_p)

    def get_books(self):
        return self.products

# Пример использования
shop = Shop()
shop.add_product("Bananas")
shop.add_product("Apples")
another_shop = shop 
another_shop.add_product("Oranges")
print(shop.get_books())
print(another_shop.get_books())
print("equal" if another_shop == shop else "mistake!")
