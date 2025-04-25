# Import specific helper functions from your Flask app module
from app import get_available_products, get_product_by_id, get_all_categories

# Test function to verify available products are returned correctly
def test_get_available_products():
    products = get_available_products()

    # Check that there are exactly 3 products in the list
    assert len(products) == 3
    # Ensure each product has all the expected keys
    assert all('id' in p and 'name' in p and 'description' in p and 
               'base_price' in p and 'image' in p and 'category' in p 
               for p in products)
    
    # Test that filtering by category 'funny' returns exactly 2 products
    assert len(get_available_products('funny')) == 2

# Test function to validate product retrieval by ID
def test_get_product_by_id():
    product = get_product_by_id(1)
    assert product and product['id'] == 1 and product['name'] == 'Meme Lord'
    assert get_product_by_id(999) is None   # Test invalid ID (should return None)

# Test function to verify category list
def test_get_all_categories():
    categories = get_all_categories()
    assert len(categories) == 2  # Ensure there are exactly 2 categories
    assert 'funny' in categories and 'school' in categories

def test_empty_cart_checkout_redirect():
    """Test that users with empty carts are redirected from checkout"""

    # Create a test client
    from app import app  # Import here to avoid circular imports
    with app.test_client() as client:

        # Set up an empty cart in the session
        with client.session_transaction() as session:
            session['cart'] = []

        # Try to access checkout page
        response = client.get('/checkout', follow_redirects=True)

        # Should redirect to home page
        assert response.request.path == '/'