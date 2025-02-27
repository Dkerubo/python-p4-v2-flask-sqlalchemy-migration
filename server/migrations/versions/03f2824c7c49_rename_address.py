"""rename address

Revision ID: 03f2824c7c49
Revises: 3feb4d60ec96
Create Date: 2025-02-27 04:32:08.664923

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '03f2824c7c49'
down_revision = '3feb4d60ec96'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('departments', sa.Column('location', sa.String(), nullable=False))
    op.drop_column('departments', 'address')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('departments', sa.Column('address', sa.VARCHAR(), nullable=True))
    op.drop_column('departments', 'location')
    # ### end Alembic commands ###
