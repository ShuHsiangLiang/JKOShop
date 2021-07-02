from sqlalchemy import Column, Integer, String, Boolean, DateTime, Text
from app.core.database import EntityModel as Base, d


class Category(Base):
	__table_name__ = 'categor_tab'
	id = Column(Integer, primary_key=True, autoincrement=True)
	name = Column(String(50))
	listing = Column(String(50))
	description = Column(String(255))
	create_time = Column(DateTime)
	update_time = Column(DateTime)
