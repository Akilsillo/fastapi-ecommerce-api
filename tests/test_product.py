import pytest
from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker, Session
from app.models.product import Product, Category
from app.core.database import Base

from sqlalchemy.pool import StaticPool
from sqlalchemy.exc import IntegrityError

# Schema #
from app.schemas.product import ProductCreate, ProductUpdate, CategoryCreate

from tests.test_db import db_session
from tests.test_db import setup_database  # IGNORE

TEST_SQLITE_URL = 'sqlite:///:memory:'
TEST_ENGINE = create_engine(TEST_SQLITE_URL, connect_args={'check_same_thread': False}, poolclass=StaticPool)

# Tests #


@pytest.fixture(scope='module')
def valid_category():
    return Category(
        name="Plantin"
    )

@pytest.fixture(scope='module')
def valid_product():
    return ProductCreate(
        name="Aloe Vera",
        description="A succulent plant species of the genus Aloe.",
        price=15.99,
        stock=50,
        cat_id=1  # Assuming the category ID will be 1
    )



# Testing repositories #
from app.repositories.product import ProductRepository



@pytest.mark.usefixtures("db_session")
class TestProductRepository:

    def test_create_product(self, valid_product, valid_category):
        # use the session provided by the `db_session` fixture on the test class
        self.session.add(valid_category)
        self.session.commit()
        product_repo = ProductRepository(db=self.session)
        product_repo.create_product(valid_product, category_id=1)
        product_id = 1
        retrieved_product = self.session.get(Product, product_id)
        assert retrieved_product is not None
        assert retrieved_product.name == "Aloe Vera"
        assert retrieved_product.description == "A succulent plant species of the genus Aloe."
        assert float(retrieved_product.price) == 15.99
        assert retrieved_product.stock == 50
        assert retrieved_product.cat_id == 1
        assert retrieved_product.category.name == "Plantin"

    def test_get_product(self):
        product_repo = ProductRepository(db=self.session)
        retrieved_product = product_repo.get_product(1)
        assert retrieved_product is not None
        assert retrieved_product.name == "Aloe Vera"

    def test_get_product_by_category(self):
        product_repo = ProductRepository(db=self.session)
        products_in_category = product_repo.get_products_by_category(1)
        assert len(products_in_category) == 1
        assert products_in_category[0].name == "Aloe Vera"

    def test_update_product(self):
        product_repo = ProductRepository(db=self.session)
        product_update = ProductUpdate(
            price=12.99,
            stock=30
        )
        updated_product = product_repo.update_product(1, product_update)
        assert updated_product is not None
        assert float(updated_product.price) == 12.99
        assert updated_product.stock == 30

    def test_delete_product(self):
        product_repo = ProductRepository(db=self.session)
        deleted_product = product_repo.delete_product(1)
        assert deleted_product is not None
        assert deleted_product.name == "Aloe Vera"
        # Verify deletion
        should_be_none = product_repo.get_product(1)
        assert should_be_none is None