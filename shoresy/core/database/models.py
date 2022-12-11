from sqlalchemy import BigInteger, Column, Integer
from sqlalchemy.orm import declarative_base

__all__ = ("Member",)

Base = declarative_base()


class Member(Base):
    """
    Class that represents the 'members' table
    """

    __tablename__ = "members"

    id: int = Column(Integer, primary_key=True)
    guild_id: int = Column(BigInteger, nullable=False, unique=False)
    member_id: int = Column(BigInteger, nullable=False, unique=False)
