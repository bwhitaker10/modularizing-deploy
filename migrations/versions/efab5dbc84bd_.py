"""empty message

Revision ID: efab5dbc84bd
Revises: 
Create Date: 2019-03-17 13:05:57.539420

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'efab5dbc84bd'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('dojo',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=45), nullable=False),
    sa.Column('city', sa.String(length=45), nullable=False),
    sa.Column('state', sa.String(length=45), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('ninja',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=45), nullable=False),
    sa.Column('last_name', sa.String(length=45), nullable=False),
    sa.Column('dojo_id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
    sa.ForeignKeyConstraint(['dojo_id'], ['dojo.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('ninja')
    op.drop_table('dojo')
    # ### end Alembic commands ###