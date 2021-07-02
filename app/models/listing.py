from sqlalchemy import Column, Integer, String, Boolean, DateTime, Text
from app.core.database import EntityModel as Base, d


class Listing(Base):
	__table_name__ = 'listing_tab'
	id = Column(Integer, primary_key=True, autoincrement=True)
	title = Column(String(50))
	description = Column(String(255))
	price = Column(Interger)
	username = Column(String(50))
	category = Column(String(50))
	create_time = Column(DateTime)
	update_time = Column(DateTime)
