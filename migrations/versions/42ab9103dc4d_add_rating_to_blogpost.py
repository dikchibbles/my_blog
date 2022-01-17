"""Add rating to Blogpost

Revision ID: 42ab9103dc4d
Revises: 
Create Date: 2022-01-17 21:01:35.734597

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '42ab9103dc4d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('blog_posts', sa.Column('rating', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('blog_posts', 'rating')
    # ### end Alembic commands ###
