"""Add metrics to block_runs

Revision ID: ec5df57a1c60
Revises: 8971d4cd5b39
Create Date: 2022-12-04 22:18:55.232804

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ec5df57a1c60'
down_revision = '8971d4cd5b39'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('block_run', sa.Column('metrics', sa.JSON(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('block_run', 'metrics')
    # ### end Alembic commands ###