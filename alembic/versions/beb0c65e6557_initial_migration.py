"""Initial migration

Revision ID: beb0c65e6557
Revises: ea4887199e8f
Create Date: 2025-03-28 15:52:27.542695

"""

from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "beb0c65e6557"
down_revision: Union[str, None] = "ea4887199e8f"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("balances", sa.Column("tron_address", sa.String(), nullable=False))
    op.drop_column("balances", "tron_adress")
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "balances",
        sa.Column("tron_adress", sa.VARCHAR(), autoincrement=False, nullable=False),
    )
    op.drop_column("balances", "tron_address")
    # ### end Alembic commands ###
