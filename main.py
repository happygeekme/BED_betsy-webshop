__winc_id__ = "d7b474e9b3a54d23bca54879a4f1855b"
__human_name__ = "Betsy Webshop"

from models import User, Product, Transaction, ProductTag, Tag


def search(term):
    products = Product.select().where(
        (Product.name ** f'%{term}%') | (Product.description ** f'%{term}%'))
    if len(products) > 0:
        print('Beschikbare producten:')
        for product in products:
            print(
                f'Product: {product.name}, prijs per stuk: {product.price_per_item}, beschikbaarheid: {product.quantity}')
    else:
        print(f'Geen beschikbaarheid gevonden voor {term}')


def list_user_products(user_id):
    try:
        user = User.get_by_id(user_id)
        products = Product.select().where(Product.owner == user).join(User)
        if len(products) > 0:
            print(f'{user.name} biedt het volgende aan:')
            for product in products:
                print(
                    f'Product: {product.name}, prijs per stuk: {product.price_per_item}, beschikbaarheid: {product.quantity}')
        else:
            print(f'{user.name} heeft geen producten beschikbaar')
    except:
        IndexError
        print('Gebruiker niet gevonden')


def list_products_per_tag(tag_id):
    products = Product.select().join(ProductTag).where(ProductTag.tag == tag_id)
    if len(products) > 0:
        print(f'Beschikbare producten:')
        for product in products:
            print(
                f'Product: {product.name}, prijs per stuk: {product.price_per_item}, beschikbaarheid: {product.quantity}')
    else:
        print('Geen producten gevonden')


def add_product_to_catalog(user_id, product):
    Product.create(
        name=product['name'],
        price_per_item=product['price_per_item'],
        quantity=product['quantity'],
        description=product['description'],
        owner=user_id),
    print(
        f'We hebben {product["quantity"]} stuks {product["name"]} aan uw producten toegevoegd')


def update_stock(product_id, new_quantity):
    try:
        update = (Product
                  .update({Product.quantity: new_quantity})
                  .where(Product.id == product_id))
        update.execute()
        print(
            f'De voorraad van het product {Product.get_by_id(product_id).name} is aangepast naar {new_quantity}')
    except:
        IndexError
        print('Dit product is niet beschikbaar, voer als nieuw product in')


def purchase_product(product_id, buyer_id, quantity):
    try:
        product = Product.get_by_id(product_id)
        old_quantity = product.quantity

        if quantity <= old_quantity:
            Transaction.create(
                product=product_id,
                quantity=quantity,
                buyer=buyer_id)

            new_quantity = (old_quantity - quantity)
            print(
                f'U koopt {quantity} x {product.name} voor {product.price_per_item} per stuk')
            update_stock(product_id, new_quantity)
        else:
            print(
                f'Er zijn {old_quantity} stuks {product.name} beschikbaar, pas het aantal aan alstublieft')
    except:
        IndexError
        print('Dit product is niet beschikbaar')


def remove_product(product_id):
    try:
        product = Product.get_by_id(product_id)
        product.delete_instance(recursive=True)
        print(f'{product.name} is verwijderd')

    except:
        IndexError
        print(f'Geen product beschikbaar met id {product_id}')
