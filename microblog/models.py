from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.orm import relationship

from core.db import Base


class Post(Base):
    __tablename__ = 'Posts'

    posts_id = Column(Integer, primary_key=True)
    posts_user = relationship('Users', foreign_keys='users_id')
    posts_text = Column(String(350))
    posts_date = Column(DateTime)
