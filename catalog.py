class Product:
    id: int
    title: str
    price: float
    count: int
    category: int

    def __init__(self, id, title, price, count, category):
        self.id = id
        self.title = title
        self.price = price
        self.count = count
        self.category = category

    def __bool__(self):
        """
        Проверяет есть ли товар в наличии
        """
        return bool(self.count > 0)

    def __len__(self):
        """
        Возвращает количество товара на складе
        """
        return self.count


class Category:
    id: int
    title: str
    description: str
    products: list

    def __init__(self, id, title, description, products):
        self.id = id
        self.title = title
        self.description = description
        self.products = products

    def __bool__(self):
        """
        Проверяет есть ли товары в категории
        """
        return bool(len(self.products))
        # return bool(any([True for x in self.products if x.title in x])) # есть ли конкретный товар в категории

    def __len__(self):
        """
        Возвращает количество наименований товаров, у которых есть наличие на складе
        """
        return sum([1 for product in self.products if product.count > 0])


if __name__ == '__main__':
    p1 = Product(1, 'апельсин', 34.5, 15, 1)
    p2 = Product(2, 'мандарин', 47.5, 26, 1)
    p3 = Product(2, 'банан', 25.3, 0, 1)
    assert bool(p3) is False  # товара р3 нет в наличии на складе
    assert len(p2) == 26  # товара p2 на складе 26 штук
    P = Category(1, 'фрукты', 'вкусные', [p1, p2, p3])
    assert bool(P) is True  # есть товары в данной категории
    assert len(P) == 2  # количество различных товаров, из данной категории, которые есть на складе в данный момент
