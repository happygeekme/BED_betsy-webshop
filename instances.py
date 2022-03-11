from models import User, Product, ProductTag, Tag, db, Transaction



def create_users_and_products():
    job = User.create(
        name='job',
        address='dorpsweg 1, het dorp')
    fleur = User.create(
        name='fleur',
        address='stadsweg 2, de stad')
    mila = User.create(
        name='mila',
        address='straatweg 103, straten')
    fiore = User.create(
        name='fiore',
        address='kleiweg 45, kleien')
    kick = User.create(
        name='kick',
        address='kloosterweg 21, kloosteren')

    vaas = Product.create(
        name='vaas',
        price_per_item=25,
        quantity=10,
        description='een vaas om bloemen in te zetten of voor decoratie',
        owner=job
    )

    mok = Product.create(
        name='mok',
        price_per_item=10,
        quantity=7,
        description='een mok om warme dranken uit te drinken',
        owner=job
    )

    armband = Product.create(
        name='armband',
        price_per_item=5,
        quantity=15,
        description='een armbandje met kralen in regenboogkleuren',
        owner=fleur
    )

    ketting = Product.create(
        name='ketting',
        price_per_item=10,
        quantity=15,
        description='een ketting met kralen en bedels',
        owner=fleur
    )

    cupcake = Product.create(
        name='cupcake',
        price_per_item=2.50,
        quantity=10,
        description='cupcake met blauwe bessen',
        owner=mila
    )

    appeltaart = Product.create(
        name='appeltaart',
        price_per_item=11.95,
        quantity=4,
        description='vers gebakken appeltaart',
        owner=mila
    )

    sokken = Product.create(
        name='sokken',
        price_per_item=7.50,
        quantity=10,
        description='gebreide sokken',
        owner=fiore
    )

    trui = Product.create(
        name='trui',
        price_per_item=35,
        quantity=6,
        description='gebreide trui',
        owner=fiore
    )

    tafel = Product.create(
        name='tafel',
        price_per_item=40,
        quantity=4,
        description='houten tafel',
        owner=kick
    )

    kast = Product.create(
        name='kast',
        price_per_item=50,
        quantity=2,
        description='houten kast',
        owner=kick
    )

    aardewerk = Tag.create(name='aardewerk')
    houtwerk = Tag.create(name='houtwerk')
    handwerk = Tag.create(name='handwerk')
    kleding = Tag.create(name='kleding')
    sierraad = Tag.create(name='sierraad')
    gebak = Tag.create(name='gebak')

    ProductTag.create(product=vaas, tag=aardewerk)
    ProductTag.create(product=mok, tag=aardewerk)
    ProductTag.create(product=armband, tag=sierraad)
    ProductTag.create(product=ketting, tag=sierraad)
    ProductTag.create(product=mok, tag=handwerk)
    ProductTag.create(product=vaas, tag=handwerk)
    ProductTag.create(product=armband, tag=handwerk)
    ProductTag.create(product=ketting, tag=handwerk)
    ProductTag.create(product=sokken, tag=handwerk)
    ProductTag.create(product=trui, tag=handwerk)
    ProductTag.create(product=tafel, tag=handwerk)
    ProductTag.create(product=kast, tag=handwerk)
    ProductTag.create(product=tafel, tag=houtwerk)
    ProductTag.create(product=kast, tag=houtwerk)
    ProductTag.create(product=ketting, tag=kleding)
    ProductTag.create(product=sokken, tag=kleding)
    ProductTag.create(product=cupcake, tag=gebak)
    ProductTag.create(product=appeltaart, tag=gebak)


db.create_tables([User, Product, Tag, ProductTag, Transaction])

create_users_and_products()
