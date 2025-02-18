"""add last few columns to posts table

Revision ID: 86f16a886cc0
Revises: 39d9443312db
Create Date: 2025-02-18 11:38:47.746873

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '86f16a886cc0'
down_revision: Union[str, None] = '39d9443312db'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
