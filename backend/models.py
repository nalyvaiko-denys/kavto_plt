from sqlalchemy import Column, Integer, String, Float, Text, Boolean
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Car(Base):
    __tablename__ = 'cars'

    id = Column(Integer, primary_key=True)
    brand = Column(String)
    model = Column(String)
    vin = Column(String, unique=True)
    description = Column(Text)


    price_purchase = Column(Float)  # цена без наценок (видит только админ)
    price_sale = Column(Float)  # цена продажи (видит клиент)

    is_sold = Column(Boolean, default=False)