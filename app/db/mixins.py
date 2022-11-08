from datetime import datetime

import sqlalchemy as sa


class PrimaryKeyMixin:
    """
    Add a primakry key to the model that inherits from this class.
    """

    __abstract__ = True
    id = sa.Column(sa.Integer, primary_key=True)


class TimestampsMixin:
    """
    Add the fields created_at/updated_at to the model that inherits from this class.
    """

    __abstract__ = True

    created_at = sa.Column(
        "created_at",
        sa.TIMESTAMP(timezone=False),
        server_default=sa.text("now()"),
        default=datetime.utcnow,
        nullable=False,
    )

    updated_at = sa.Column(
        "updated_at",
        sa.TIMESTAMP(timezone=False),
        server_default=sa.text("now()"),
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
        nullable=False,
    )


class BaseFeaturesMixin(PrimaryKeyMixin, TimestampsMixin):
    __abstract__ = True
