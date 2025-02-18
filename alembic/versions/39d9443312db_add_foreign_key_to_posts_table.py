"""add foreign key to posts table

Revision ID: 39d9443312db
Revises: 6d69520618b1
Create Date: 2025-02-18 11:30:13.048281

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '39d9443312db'
down_revision: Union[str, None] = '6d69520618b1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
