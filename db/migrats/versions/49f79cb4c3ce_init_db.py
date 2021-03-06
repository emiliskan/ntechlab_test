"""init db

Revision ID: 49f79cb4c3ce
Revises: 
Create Date: 2021-08-30 21:29:48.947446

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '49f79cb4c3ce'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('x', sa.Float(), nullable=True),
    sa.Column('y', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_users_id'), 'users', ['id'], unique=False)
    op.create_index(op.f('ix_users_x'), 'users', ['x'], unique=False)
    op.create_index(op.f('ix_users_y'), 'users', ['y'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_users_y'), table_name='users')
    op.drop_index(op.f('ix_users_x'), table_name='users')
    op.drop_index(op.f('ix_users_id'), table_name='users')
    op.drop_table('users')
    # ### end Alembic commands ###
