import pytest
from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker, Session
from app.models.cart import Cart, CartItem
from app.core.database import Base
from sqlalchemy.exc import IntegrityError
# Repository #
from app.repositories.cart import *
# Schema #
from app.schemas.cart import *

from tests.test_db import db_session
from tests.test_db import setup_database  # IGNORE

# Fixtures #

@pytest.fixture(scope='module')
def valid_cart():
    return CartCreate(
        user_id=1,
        status_id=1
    )

@pytest.fixture(scope='module')
def valid_cart_item():
    return CartItemCreate(
        cart_id=1,
        product_id=1,
        unit_price=19.99,
        quantity=2,
    )

@pytest.fixture(scope='module')
def another_valid_cart_item():
    return CartItemCreate(
        cart_id=1,
        product_id=2,
        unit_price=19.99,
        quantity=1,
    )

@pytest.mark.usefixtures("db_session")
class TestCartItemRepository:

    def test_create_cart_item(self, valid_cart_item):
        # use the session provided by the `db_session` fixture on the test class
        cart_item_repo = CartItemRepository(db=self.session)
        cart_item_repo.create_cart_item(valid_cart_item)
        cart_id = 1
        product_id = 1
        retrieved_cart_item = self.session.get(CartItem, (cart_id, product_id))
        assert retrieved_cart_item is not None
        assert retrieved_cart_item.cart_id == 1
        assert retrieved_cart_item.product_id == 1
        assert retrieved_cart_item.quantity == 2
        assert float(retrieved_cart_item.subtotal) == 39.98

    def test_get_all_cart_items(self, another_valid_cart_item):
        cart_item_repo = CartItemRepository(db=self.session)
        cart_item_repo.create_cart_item(another_valid_cart_item)
        items = cart_item_repo.get_all_cart_items(1)
        assert len(items) >= 2  # At least the two we added
        assert any(item.product_id == 1 for item in items)
        assert any(item.product_id == 2 for item in items)

    # def test_update_cart_item(self, another_valid_cart_item):
    #     cart_item_repo = CartItemRepository(db=self.session)
    #     cart_item_repo.update_cart_item(1, 2, CartItemUpdate(quantity=3))
    #     retrieved_cart_item = self.session.get(CartItem, (1, 2))
    #     assert retrieved_cart_item is not None
    #     assert retrieved_cart_item.quantity == 3
    #     assert float(retrieved_cart_item.subtotal) == 59.97

    def test_update_cart_item_quantity(self):
        cart_item_repo = CartItemRepository(db=self.session)
        cart_item_repo.update_cart_item_quantity(1, 2, 4)
        retrieved_cart_item = self.session.get(CartItem, (1, 2))
        assert retrieved_cart_item is not None
        assert retrieved_cart_item.quantity == 4
        assert float(retrieved_cart_item.subtotal) == 79.96

    def test_delete_cart_item(self):
        cart_item_repo = CartItemRepository(db=self.session)
        cart_item_repo.delete_cart_item(1, 1)
        retrieved_cart_item = self.session.get(CartItem, (1, 1))
        assert retrieved_cart_item is None

    def test_delete_all_cart_items(self, valid_cart_item):
        cart_item_repo = CartItemRepository(db=self.session)
        # Re-add an item to ensure there's something to delete
        assert len(cart_item_repo.get_all_cart_items(1)) > 0
        cart_item_repo.create_cart_item(valid_cart_item)
        cart_item_repo.delete_all_cart_items(1)
        items = cart_item_repo.get_all_cart_items(1)
        assert len(items) == 0

    # def test_create_cart(self, valid_cart):
    #     # use the session provided by the `db_session` fixture on the test class
    #     cart_repo = CartRepository(db=self.session)
    #     cart_repo.create_cart(valid_cart)
    #     cart_id = 1
    #     retrieved_cart = self.session.get(Cart, cart_id)
    #     assert retrieved_cart is not None
    #     assert retrieved_cart.user_id == 1
    #     assert retrieved_cart.status_id == 1
    #     assert float(retrieved_cart.total_amount) == 0.0

    # def test_create_cart_with_items(self, valid_cart, valid_cart_item, another_valid_cart_item):
    #     cart_repo = CartRepository(db=self.session)
    #     cart = cart_repo.create_cart(valid_cart)
    #     cart_id = cart.cart_id

    #     cart_item1 = CartItem(**valid_cart_item.model_dump())
    #     cart_item2 = CartItem(**another_valid_cart_item.model_dump())
    #     self.session.add_all([cart_item1, cart_item2])
    #     self.session.commit()

    #     retrieved_cart = self.session.get(Cart, cart_id)
    #     assert retrieved_cart is not None

    #     item1 = self.session.get(CartItem, (cart_id, valid_cart_item.product_id))
    #     item2 = self.session.get(CartItem, (cart_id, another_valid_cart_item.product_id))

    #     assert item1 is not None
    #     assert item1.quantity == valid_cart_item.quantity
    #     assert float(item1.subtotal) == valid_cart_item.subtotal

    #     assert item2 is not None
    #     assert item2.quantity == another_valid_cart_item.quantity
    #     assert float(item2.subtotal) == another_valid_cart_item.subtotal

@pytest.mark.usefixtures("db_session")
class TestCartRepository:

    def test_create_cart(self, valid_cart):
        cart_repo = CartRepository(db=self.session)
        cart_repo.create_cart(valid_cart)
        cart_id = 1
        retrieved_cart = self.session.get(Cart, cart_id)
        assert retrieved_cart is not None
        assert retrieved_cart.user_id == 1
        assert retrieved_cart.status_id == 1
        assert float(retrieved_cart.total_amount) == 0.0

    def test_get_all_carts(self):
        cart_repo = CartRepository(db=self.session)
        carts = cart_repo.get_all_carts()
        assert len(carts) >= 1  # At least the one we added
        assert any(cart.user_id == 1 for cart in carts)

    def test_get_cart(self):
        cart_repo = CartRepository(db=self.session)
        cart = cart_repo.get_cart(1)
        assert cart is not None
        assert cart.cart_id == 1
        assert cart.user_id == 1
    
    def test_update_cart(self):
        cart_repo = CartRepository(db=self.session)
        cart_repo.update_cart(1, CartUpdate(total_amount=49.99, status_id=2))
        retrieved_cart = self.session.get(Cart, 1)
        assert retrieved_cart is not None
        assert float(retrieved_cart.total_amount) == 49.99
        assert retrieved_cart.status_id == 2

    def test_delete_cart(self):
        cart_repo = CartRepository(db=self.session)
        cart_repo.delete_cart(1)
        retrieved_cart = self.session.get(Cart, 1)
        assert retrieved_cart is None

@pytest.mark.usefixtures("db_session")
class TestCartStatusRepository:

    def test_create_cart_status(self):
        cart_status_repo = CartStatusRepository(db=self.session)
        status = CartStatusCreate(status_name="Pending")
        cart_status_repo.create_cart_status(status)
        status_id = 1
        retrieved_status = self.session.get(CartStatus, status_id)
        assert retrieved_status is not None
        assert retrieved_status.status_name == "Pending"

    def test_get_all_cart_statuses(self):
        cart_status_repo = CartStatusRepository(db=self.session)
        statuses = cart_status_repo.get_all_cart_statuses()
        assert len(statuses) >= 1  # At least the one we added
        assert any(status.status_name == "Pending" for status in statuses)

    def test_get_cart_status(self):
        cart_status_repo = CartStatusRepository(db=self.session)
        status = cart_status_repo.get_cart_status(1)
        assert status is not None
        assert status.status_id == 1
        assert status.status_name == "Pending"