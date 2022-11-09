from typing import AsyncIterator

from sqlalchemy import Column, ForeignKey, Integer, Table
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.base import Base
from app.db.session import async_session


async def get_db() -> AsyncIterator[AsyncSession]:
    async with async_session() as db:
        yield db


def reference_col(
    tablename: str,
    nullable=False,
    pk_name="id",
    ondelete: str | None = None,
    use_alter=False,
    **kwargs,
) -> Column:
    """
    Column that adds the reference of the primary key to the foreign key.

    Usage:
        user_id = reference_col(User.__tablename__)
        profile = relationship("Profile", back_populates="user")

    :param tablename:
    :param nullable:
    :param pk_name:
    :param ondelete:
    :param use_alter:
    :param kwargs:
    :return: Column
    """
    return Column(
        ForeignKey(f"{tablename}.{pk_name}", ondelete=ondelete, use_alter=use_alter),
        nullable=nullable,
        **kwargs,
    )


def pivot_table(
    table_name, left: str | dict[str, str], right: str | dict[str, str]
) -> Table:
    """
    Creates a pivot table to be able to create a many-to-many relationship
    Simplifies the boiler plate code
    :param table_name:
    :param left: name of the first table to reference or options for the left column
    :param right: name of the second table to reference or options for the right column
    :return:
    """

    if isinstance(left, str):
        left = {"table": left}
    if isinstance(right, str):
        right = {"table": right}

    left_table = left.pop("table")
    right_table = right.pop("table")
    if left_table is None or right_table is None:
        raise Exception(
            f"Pivot table creation failed left: {left_table}, right: {right_table}"
        )

    left_type = left.pop("type", Integer)
    right_type = right.pop("type", Integer)

    left_ref = left.pop("ref", f"{left_table}.id")
    right_ref = right.pop("ref", f"{right_table}.id")
    left_name = left.pop("name", f"{left_table}_id")
    right_name = right.pop("name", f"{right_table}_id")

    left_delete = left.pop("ondelete", None)
    right_delete = right.pop("ondelete", None)

    return Table(
        table_name,
        Base.metadata,
        Column(
            left_name,
            left_type,
            ForeignKey(left_ref, ondelete=left_delete),
            primary_key=True,
        ),
        Column(
            right_name,
            right_type,
            ForeignKey(right_ref, ondelete=right_delete),
            primary_key=True,
        ),
    )
