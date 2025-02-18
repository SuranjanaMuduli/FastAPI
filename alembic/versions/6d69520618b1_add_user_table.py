"""add user table

Revision ID: 6d69520618b1
Revises: 1f88f108f174
Create Date: 2025-02-18 01:32:46.183314

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6d69520618b1'
down_revision: Union[str, None] = '1f88f108f174'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
