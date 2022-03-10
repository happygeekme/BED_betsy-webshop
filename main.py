__winc_id__ = "d7b474e9b3a54d23bca54879a4f1855b"
__human_name__ = "Betsy Webshop"

from models import User, Product, Transaction, Tag


def search(term):
    items = Product.select().where(Product.name.contains(term))
    if len(items) > 0:
        return [item.name for item in items]
    else:
        return(f'No items available for {term}')


def list_user_products(user_id):
    user = User.select().where(User.id == user_id)
    products = Product.select().where(Product.seller == user).join(User)
    if len(products) > 0:
        return [product.name for product in products]
    else:
        return(f'{user.name} has no products availale')


def list_products_per_tag(tag_id):
    products = Product.select().where()


def add_product_to_catalog(user_id, product):
    ...


def update_stock(product_id, new_quantity):
    ...


def purchase_product(product_id, buyer_id, quantity):
    ...


def remove_product(product_id):
    ...
