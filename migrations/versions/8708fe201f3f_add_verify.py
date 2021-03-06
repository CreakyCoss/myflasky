"""add verify

Revision ID: 8708fe201f3f
Revises: 9e38bf250abd
Create Date: 2018-02-14 23:28:50.627029

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8708fe201f3f'
down_revision = '9e38bf250abd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('email', sa.String(length=64), nullable=True))
    op.add_column('users', sa.Column('password_hash', sa.String(length=128), nullable=True))
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_column('users', 'password_hash')
    op.drop_column('users', 'email')
    # ### end Alembic commands ###
