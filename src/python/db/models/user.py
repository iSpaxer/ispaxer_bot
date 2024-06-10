from sqlalchemy import Column, func, String, BigInteger, DateTime

from src.python.db.base import Base


class User(Base):

    __tablename__ = "user"

    id = Column(
        BigInteger,
        primary_key=True,
        unique=True,
        autoincrement=False,
        comment="Уникальный индетификатор пользователя"
    )

    username = Column(
        String(32),
        nullable=True,
        unique=True,
        comment="Имя пользователя"
    )

    creation_date_time = Column(
        DateTime(),
        nullable=False,
        comment="Дата создания пользователя",
        server_default=func.now()
    )
