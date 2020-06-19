"""Create database and insert data from the API."""

from sqlalchemy import Column, Integer, String


class Product(Base):
    """Store data for products, nutriscore and url"""

    __tablename__ = 'product'
    id = Column(Integer, primary_key=True, autoincrement=False)
    product_name = Column(String)
    nutriscore_grade = Column(String)
    url = Column(String)

    def __repr__(self):
        """Render Product object in a readable way"""
        return f"{product_name} {nutriscore_grade} {url}"


class Store(Base):
    """Store data for the store related to a product"""

    __tablename__ = 'store'
    id = Column(Integer, primary_key=True)
    store_name = Column(String(80), unique=True)

    def __repr__(self):
        """Render Store object in a readable way"""
        return f"{store_name}"

class Category(Base):
    """Store data for the category related to a product"""

    __tablename__ = 'category'
    id = Column(Integer, primary_key=True)
    category_name = Column(String(100), unique=True)
    
    def __repr__(self):
        """Render Category object in a readable way"""
        return f"{category_name}"