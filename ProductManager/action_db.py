from models import Product, Company

'''Компанія'''

def add_company(name: str, password: str):
    Company.create(name=name, password=password)

def company_exists(name: str) -> bool:
    return Company.select().where(Company.name == name).exists()

def get_company_by_name(name: str):
    return Company.get_or_none(Company.name == name)


'''Товар'''
# отримання
def get_all_products():
    return Product.select()


def get_product_by_category(category: str):
    return Product.select().where(Product.category == category)


def get_all_categories():
    return Product.select(Product.category).distinct().order_by(Product.category)


def product_exist(name) -> bool:
    return Product.select().where(Product.name == name).exists()


# додавання
def add_product(name: str, price: float, category: str):
    Product.create(name=name, price=price, category=category)

def get_product_by_name(name):
    return Product.get_or_none(Product.name == name)


def update_product(name, price, category):
    product = Product.get_or_none(Product.name == name)
    if product:
        product.price = price
        product.category = category
        product.save()