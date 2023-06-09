"""empty message

Revision ID: 230d18b13a44
Revises: 
Create Date: 2023-03-12 10:30:40.443152

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '230d18b13a44'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('properties',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('proptitle', sa.String(length=100), nullable=True),
    sa.Column('description', sa.String(length=2048), nullable=True),
    sa.Column('number_of_rooms', sa.Integer(), nullable=True),
    sa.Column('price', sa.Integer(), nullable=True),
    sa.Column('location', sa.String(length=100), nullable=True),
    sa.Column('photo', sa.String(length=255), nullable=True),
    sa.Column('number_of_bathrooms', sa.Integer(), nullable=True),
    sa.Column('property_type', sa.String(length=25), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('properties')
    # ### end Alembic commands ###
