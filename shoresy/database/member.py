import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class Member(Base):
    """Represents the member table."""

    __tablename__ = "member"

    id: Mapped[int] = mapped_column(sa.Integer, primary_key=True, autoincrement=True)
    guild_id: Mapped[int] = mapped_column("guildID", sa.BigInteger, nullable=False)
    member_id: Mapped[int] = mapped_column("memberID", sa.BigInteger, nullable=False)

    @property
    def mention(self) -> str:
        """Return the member as a mentionable string."""
        return f"<@{self.member_id}>"
