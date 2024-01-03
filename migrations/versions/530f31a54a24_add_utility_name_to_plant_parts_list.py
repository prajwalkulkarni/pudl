"""add utility name to plant parts list

Revision ID: 530f31a54a24
Revises: 2e5b623ab40b
Create Date: 2024-01-01 20:31:08.389639

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = '530f31a54a24'
down_revision = '2e5b623ab40b'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('out_eia__yearly_plant_parts', schema=None) as batch_op:
        batch_op.add_column(sa.Column('utility_name_eia', sa.Text(), nullable=True, comment='The name of the utility.'))

    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('out_eia__yearly_plant_parts', schema=None) as batch_op:
        batch_op.drop_column('utility_name_eia')

    # ### end Alembic commands ###
