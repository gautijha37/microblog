"""Added language column to posts db

Revision ID: 8fe1963bdb6e
Revises: b753e6b179dd
Create Date: 2022-02-07 12:28:58.336330

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8fe1963bdb6e'
down_revision = 'b753e6b179dd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('language', sa.String(length=5), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('post', 'language')
    # ### end Alembic commands ###
