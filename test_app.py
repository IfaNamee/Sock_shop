from app import get_available_products, get_product_by_id, get_all_categories

def test_get_available_products():

    products = get_available_products()

    assert len(products) == 3

    assert all('id' in p and 'name' in p and 'description' in p and 

              'base_price' in p and 'image' in p and 'category' in p 

              for p in products)

    assert len(get_available_products('funny')) == 2



def test_get_product_by_id():

    product = get_product_by_id(1)

    assert product and product['id'] == 1 and product['name'] == 'Meme Lord'

    assert get_product_by_id(999) is None



def test_get_all_categories():

    categories = get_all_categories()

    assert len(categories) == 2

    assert 'funny' in categories and 'school' in categories