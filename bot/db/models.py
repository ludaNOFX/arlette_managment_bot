from bot.db.base import Base

from sqlalchemy import Column, BigInteger, Integer


class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    user_id = Column(BigInteger, unique=True, nullable=False)
    active = Column(Integer, default=1)