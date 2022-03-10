# Models go here
from ast import For
from itertools import product
from peewee import Model, SqliteDatabase, CharField, ManyToManyField, ForeignKeyField, IntegerField, DecimalField


db = SqliteDatabase('database.db', pragmas={'foreign_keys': 1})

class User(Model):
    name = CharField()
    address = CharField()
    
    class Meta:
        database = db

class Product(Model):
    name = CharField()    
    price_per_item = DecimalField(10, 2, auto_round=True)
    quantity = IntegerField()
    description = CharField()
    seller = ForeignKeyField(User)
    tags = ManyToManyField()

    class Meta:
        database = db

class Tag(Model):
    name = CharField()

    class Meta:
        database = db

class ProductTag(Model):
    tag = ForeignKeyField(Tag)
    product = ForeignKeyField(Product)

    class Meta:
        database = db

class Transaction(Model):
    product = ForeignKeyField(Product)
    quantity = IntegerField()
    Buyer = ForeignKeyField(User)
    Seller = ForeignKeyField(User)

    class Meta:
        database = db

# cd .\OneDrive\Documenten\Winc_Academy\BED\Winc\betsy-webshop\