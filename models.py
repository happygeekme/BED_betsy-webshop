# Models go here
from peewee import Model, SqliteDatabase, CharField, ForeignKeyField, IntegerField, DecimalField


db = SqliteDatabase('database.db', pragmas={'foreign_keys': 1})


class BaseModel(Model):
    class Meta:
        database = db


class User(BaseModel):
    name = CharField()
    address = CharField()


class Product(BaseModel):
    name = CharField()
    price_per_item = DecimalField(10, 2, auto_round=True)
    quantity = IntegerField()
    description = CharField()
    owner = ForeignKeyField(User, backref='products')

    class Meta:
        indexes = (
            (('name', 'price_per_item', 'quantity', 'description', 'owner'), True),
        )


class Tag(BaseModel):
    name = CharField()


class ProductTag(BaseModel):
    tag = ForeignKeyField(Tag, backref='products')
    product = ForeignKeyField(Product, backref='tags')


class Transaction(BaseModel):
    product = ForeignKeyField(Product)
    quantity = IntegerField()
    buyer = ForeignKeyField(User, backref='buys')
