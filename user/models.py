from sqlalchemy import Column, String, Integer, DateTime, Boolean

from core.db import Base


class User(Base):
    __tablename__ = 'Users'

    users_id = Column(Integer, primary_key=True, index=True, unique=True)
    users_name = Column(String, unique=True)
    users_email = Column(String, unique=True)
    users_password = Column(String)
    users_date = Column(DateTime)
    users_status = Column(Boolean)
    users_is_admin = Column(Boolean, default=False)
