from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.cart import Cart, CartItem, CartStatus
from app.schemas.cart import *

class CartRepository:
    def _init__(self, db: Session):
        self.db = db

    def create_cart(self, cart: CartCreate):
        db_cart = Cart(**cart.model_dump())
        self.db.add(db_cart)
        self.db.commit()
        self.db.refresh(db_cart)
        return db_cart

    def get_cart(self, cart_id: int):
        return self.db.scalar(select(Cart).where(Cart.id == cart_id))
    
    def get_all_carts(self):
        return self.db.scalars(select(Cart)).all()
    
    def update_cart(self, cart_id: int, cart_update: CartUpdate):
        db_cart = self.get_cart(cart_id)
        if db_cart:
            for key, value in cart_update.model_dump(exclude_unset=True).items():
                setattr(db_cart, key, value)
            self.db.commit()
            self.db.refresh(db_cart)
        return db_cart

    def delete_cart(self, cart_id: int):
        db_cart = self.get_cart(cart_id)
        if db_cart:
            self.db.delete(db_cart)
            self.db.commit()
        return db_cart
    
class CartStatusRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_cart_status(self, status: CartStatusCreate):
        db_status = CartStatus(**status.model_dump())
        self.db.add(db_status)
        self.db.commit()
        self.db.refresh(db_status)
        return db_status

    def get_cart_status(self, status_id: int):
        return self.db.scalar(select(CartStatus).where(CartStatus.id == status_id))
    
    def get_all_cart_statuses(self):
        return self.db.scalars(select(CartStatus)).all()
    
class CartItemRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_cart_item(self, cart_item: CartItemCreate):
        db_cart_item = CartItem(**cart_item.model_dump())
        self.db.add(db_cart_item)
        self.db.commit()
        self.db.refresh(db_cart_item)
        return db_cart_item

    def get_cart_item(self, cart_id: int, product_id: int):
        return self.db.scalar(select(CartItem).where(CartItem.cart_id == cart_id, CartItem.product_id == product_id))
    
    def get_all_cart_items(self, cart_id: int):
        return self.db.scalars(select(CartItem).where(CartItem.cart_id == cart_id)).all()
    
    def update_cart_item(self, cart_id: int, product_id: int, cart_item_update: CartItemUpdate):
        db_cart_item = self.get_cart_item(cart_id, product_id)
        if db_cart_item:
            for key, value in cart_item_update.model_dump(exclude_unset=True).items():
                setattr(db_cart_item, key, value)
            self.db.commit()
            self.db.refresh(db_cart_item)
        return db_cart_item
    
    def delete_cart_item(self, cart_id: int, product_id: int):
        db_cart_item = self.get_cart_item(cart_id, product_id)
        if db_cart_item:
            self.db.delete(db_cart_item)
            self.db.commit()
        return db_cart_item
    
    def delete_all_cart_items(self, cart_id: int):
        db_cart_items = self.get_all_cart_items(cart_id)
        for item in db_cart_items:
            self.db.delete(item)
        self.db.commit()
        return db_cart_items
    