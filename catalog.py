from connector import Connector


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

    def __str__(self):
        return f'Продукт: {self.title}. Осталось {self.count} штук. Цена: {self.price} за кг.'

    def __repr__(self):
        return f'Продукт: {self.title}. Осталось {self.count} штук. Цена: {self.price} за кг.'

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

    def __init__(self, id, title, description, products=[]):
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


class Shop:
    """
    Класс для работы с магазином
    """

    # products: list
    # categories: list

    def __init__(self, *args, **kwargs):
        pass

    def get_categories(self):
        """
        Показать все категории пользователю в произвольном виде, главное, чтобы пользователь
        мог видеть идентификаторы (id) каждой категории
        """
        our_category_connector = Connector('categories.json')
        all_category = our_category_connector.select(dict())
        for category in all_category:
            print(f'Номер категории: {category["id"]}')
            print(f'Название категории: {category["title"]}')
            print(f'Описание категории: {category["description"]}', end='\n\n')

    def get_products(self):
        """
        Запросить номер категории и вывести все товары, которые относятся к этой категории
        Обработать вариант отсутствия введенного номера
        """
        try:
            id_category = int(input('Введит номер категории о товарах которой вы хотите узнать: '))
            our_category_connector = Connector('products.json')
            all_products = our_category_connector.select({"category": (id_category)})
            if all_products:
                for product_ in all_products:
                    print(f'Продукт: {product_["title"]}.'
                          f' Осталось {product_["count"]} штук.'
                          f' Цена: {product_["price"]} р. за кг.')
            else:
                print('Такой категории у нас нет!')
        except ValueError:
            print('Такой категории у нас нет!')
        print()

    def get_product(self):
        """
        Запросить ввод номера товара и вывести всю информацию по нему в произвольном виде
        Обработать вариант отсутствия введенного номера
        """
        id_product = input('Введите номер товара по которому хотите узнать информацию: ')
        our_product_connector = Connector('products.json')
        try:  # если номер не в нашем диапазоне или не число, то выводим что номера нет такого, иначе отчёт по товару
            product_ = our_product_connector.select({"id": int(id_product)})[0]
            print(
                f'Продукт: {product_["title"]}. Осталось {product_["count"]} штук. Цена: {product_["price"]} р. за кг.')
        except IndexError:
            print('Товара с таким номером нет!')
        except ValueError:
            print('Товара с таким номером нет!')
        print()  # Просто чтобы не "слиплось"


if __name__ == '__main__':
    my_shop = Shop()
    my_shop.get_product()
    my_shop.get_categories()
    my_shop.get_products()
