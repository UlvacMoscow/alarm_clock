"""empty message

Revision ID: e0923ade0f00
Revises: 
Create Date: 2020-08-26 16:00:25.629064

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e0923ade0f00'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('alarm_clock',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('ring_time', sa.DateTime(), nullable=False),
    sa.Column('worked', sa.Boolean(), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('alarm_clock')
    # ### end Alembic commands ###
