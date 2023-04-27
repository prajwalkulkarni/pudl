"""Add both service_territories df.

Revision ID: ebb079231a85
Revises: 354850730883
Create Date: 2023-04-27 16:14:14.738052
"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "ebb079231a85"
down_revision = "354850730883"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "compiled_geometry_balancing_authority_eia861",
        sa.Column(
            "county_id_fips",
            sa.Text(),
            nullable=True,
            comment="County ID from the Federal Information Processing Standard Publication 6-4.",
        ),
        sa.Column(
            "county_name_census",
            sa.Text(),
            nullable=True,
            comment="County name as specified in Census DP1 Data.",
        ),
        sa.Column(
            "population",
            sa.Float(),
            nullable=True,
            comment="County population, sourced from Census DP1 data.",
        ),
        sa.Column("area_km2", sa.Float(), nullable=True, comment="County area in km2."),
        sa.Column("report_date", sa.Date(), nullable=True, comment="Date reported."),
        sa.Column(
            "balancing_authority_id_eia",
            sa.Integer(),
            nullable=True,
            comment="EIA balancing authority ID. This is often (but not always!) the same as the utility ID associated with the same legal entity.",
        ),
        sa.Column(
            "state",
            sa.Text(),
            nullable=True,
            comment="Two letter US state abbreviation.",
        ),
        sa.Column("county", sa.Text(), nullable=True, comment="County name."),
        sa.Column(
            "state_id_fips",
            sa.Text(),
            nullable=True,
            comment="Two digit state FIPS code.",
        ),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("compiled_geometry_balancing_authority_eia861")
    # ### end Alembic commands ###
