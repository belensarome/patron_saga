"""Compras

Revision ID: 21c511581f4e
Revises: 7b8f030fe03d
Create Date: 2024-10-22 21:26:12.559443

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '21c511581f4e'
down_revision = '7b8f030fe03d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('compras',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('producto_id', sa.Integer(), nullable=False),
    sa.Column('fecha_compra', sa.DateTime(), nullable=False),
    sa.Column('direccion_envio', sa.String(length=120), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('compras')
    # ### end Alembic commands ###