import pytest
from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker, Session
from app.models.product import Product, Category
from app.core.database import Base
# from tests.test_db import TEST_ENGINE
from decimal import Decimal

# Models #

from sqlalchemy import Column, Integer, String
from sqlalchemy.pool import StaticPool
from sqlalchemy.exc import IntegrityError

# Schema #
from app.schemas.product import ProductCreate, ProductUpdate, CategoryCreate

TEST_SQLITE_URL = 'sqlite:///:memory:'
TEST_ENGINE = create_engine(TEST_SQLITE_URL, connect_args={'check_same_thread': False}, poolclass=StaticPool)

# Using the project's declarative `Base` from app.core.database so
# model classes imported from `app.models` share the same metadata.


# Tests #

@pytest.fixture(scope='module', autouse=True)
def setup_database():
    # Create the database tables
    Base.metadata.create_all(bind=TEST_ENGINE)
    TestingSession = sessionmaker(autoflush=False, bind=TEST_ENGINE)
    yield TestingSession
    # Drop the database tables after tests
    Base.metadata.drop_all(bind=TEST_ENGINE)

@pytest.fixture(scope='module')
def valid_category():
    return Category(
        name="Plantin"
    )

@pytest.fixture(scope='module')
def valid_product(valid_category):
    return ProductCreate(
        name="Aloe Vera",
        description="A succulent plant species of the genus Aloe.",
        price=15.99,
        stock=50,
        cat_id=1  # Assuming the category ID will be 1
    )

class TestProductModel:

    # Assertion tests for Product model
    
    # def test_category_creation(self, setup_database, valid_category):
    #     session = setup_database()
    #     session.add(valid_category)
    #     session.commit()
    #     plantin_category = session.query(Category).filter_by(name="Plantin").first()
    #     assert plantin_category is not None
    #     assert plantin_category.name == "Plantin"
    #     assert plantin_category.cat_id == 1

    # def test_product_creation(self, setup_database, valid_product):
    #     session = setup_database()
    #     #session.add(valid_product.category)  # Ensure category is added first
    #     session.add(valid_product)
    #     session.commit()
    #     aloe_product = session.scalar(select(Product).where(Product.name == 'Aloe Vera'))
    #     assert aloe_product is not None
    #     assert aloe_product.name == "Aloe Vera"
    #     assert aloe_product.description == "A succulent plant species of the genus Aloe."
    #     assert float(aloe_product.price) == 15.99 #Decimal('15.99')
    #     assert aloe_product.stock == 50
    #     assert aloe_product.category.name == "Plantin"

    # Integrity tests for Category model

    # @pytest.mark.xfail(raises=IntegrityError)
    # def test_category_no_name(self, setup_database):
    #     session = setup_database()
    #     invalid_category = Category(
    #         name=None
    #     )
    #     session.add(invalid_category)
    #     session.commit()
    pass

# Testing repositories #
from app.repositories.product import ProductRepository



class TestProductRepository:

    def test_create_product(self, setup_database, valid_product, valid_category):
        
        session = setup_database()
        session.add(valid_category)
        session.commit()
        product_repo = ProductRepository(db=session)
        product_repo.create_product(valid_product, category_id=1)
        product_id = 1
        retrieved_product = session.get(Product, product_id)
        assert retrieved_product is not None
        assert retrieved_product.name == "Aloe Vera"
        assert retrieved_product.description == "A succulent plant species of the genus Aloe."
        assert float(retrieved_product.price) == 15.99
        assert retrieved_product.stock == 50
        assert retrieved_product.cat_id == 1
        assert retrieved_product.category.name == "Plantin"
