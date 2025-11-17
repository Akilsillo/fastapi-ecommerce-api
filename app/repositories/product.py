from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.product import Product, Category
from app.schemas.product import ProductCreate, ProductUpdate, CategoryCreate

class CategoryRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_category(self, category: CategoryCreate):
        db_category = Category(**category.model_dump())
        self.db.add(db_category)
        self.db.commit()
        self.db.refresh(db_category)
        return db_category
    
    def get_category(self, category_id: int):
        return self.db.scalar(select(Category).where(Category.cat_id == category_id))
    
    def get_all_categories(self):
        return self.db.execute(select(Category).all())
    
class ProductRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_product(self, product: ProductCreate, category_id: int):
        db_product = Product(**product.model_dump())
        db_product.cat_id = category_id
        self.db.add(db_product)
        self.db.commit()
        self.db.refresh(db_product)
        return db_product
    
    def get_product(self, product_id: int):
        return self.db.scalar(select(Product).where(Product.product_id == product_id))

    def get_all_products(self):
        return self.db.scalars(select(Product)).all()
    
    def get_products_by_category(self, category_id: int):
        return self.db.scalars(select(Product).where(Product.cat_id == category_id)).all()

    def update_product(self, product_id: int, product_update: ProductUpdate):
        db_product = self.get_product(product_id)
        if db_product:
            for key, value in product_update.model_dump(exclude_unset=True).items():
                setattr(db_product, key, value)
            self.db.commit()
            self.db.refresh(db_product)
        return db_product

    def delete_product(self, product_id: int):
        db_product = self.get_product(product_id)
        if db_product:
            self.db.delete(db_product)
            self.db.commit()
        return db_product
    
