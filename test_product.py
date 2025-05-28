import pytest
from products import Product

def test_creating_prod():
    prod = Product("MacBook Air M2", price=1450, quantity=100)
    assert prod.name == "MacBook Air M2"
    assert prod.price == 1450
    assert prod.quantity == 100
    assert prod.is_active() is True

def test_creating_prod_invalid_details():
    with pytest.raises(ValueError):
        Product("", price=1450, quantity=100)
    with pytest.raises(ValueError):
        Product("MacBook Air M2", price=-10, quantity=100)

def test_prod_becomes_inactive():
    prod = Product("Google Pixel 7", price=500, quantity=1)
    prod.buy(1)
    assert prod.is_active() is False

def test_buy_modifies_quantity():
    prod = Product("Bose Earbuds", price=250, quantity=10)
    total = prod.buy(3)
    assert total == 750  # 3 * 250
    assert prod.quantity == 7

def test_buy_too_much():
    prod = Product("Bose Earbuds", price=250, quantity=5)
    with pytest.raises(ValueError):
        prod.buy(6)
