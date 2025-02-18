"""add content column to posts table

Revision ID: 9743d0c61250
Revises: 86f16a886cc0
Create Date: 2025-02-18 11:53:35.377361

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9743d0c61250'
down_revision: Union[str, None] = '86f16a886cc0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
