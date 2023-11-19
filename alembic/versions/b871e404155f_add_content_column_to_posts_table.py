"""add_content_column_to_posts_table

Revision ID: b871e404155f
Revises: a720b067e826
Create Date: 2023-11-19 21:30:50.340619

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b871e404155f'
down_revision: Union[str, None] = 'a720b067e826'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass