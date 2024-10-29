"""add event models

Revision ID: 71a8b872296d
Revises: 64a870953fa5
Create Date: 2024-10-29 20:02:59.248013

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils
from shared.constants import ProtocolIDs

# revision identifiers, used by Alembic.
revision: str = '71a8b872296d'
down_revision: Union[str, None] = '64a870953fa5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('accumulators_sync_event_data',
    sa.Column('token', sa.String(), nullable=False),
    sa.Column('lending_accumulator', sa.Numeric(precision=38, scale=18), nullable=False),
    sa.Column('debt_accumulator', sa.Numeric(precision=38, scale=18), nullable=False),
    sa.Column('event_name', sa.String(), nullable=False),
    sa.Column('block_number', sa.Integer(), nullable=False),
    sa.Column('protocol_id', sqlalchemy_utils.types.choice.ChoiceType(ProtocolIDs), nullable=False),
    sa.Column('id', sa.UUID(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_accumulators_sync_event_data_block_number'), 'accumulators_sync_event_data', ['block_number'], unique=False)
    op.create_index(op.f('ix_accumulators_sync_event_data_event_name'), 'accumulators_sync_event_data', ['event_name'], unique=False)
    op.create_table('liquidation_event_data',
    sa.Column('liquidator', sa.String(), nullable=False),
    sa.Column('user', sa.String(), nullable=False),
    sa.Column('debt_token', sa.String(), nullable=False),
    sa.Column('debt_raw_amount', sa.Numeric(precision=38, scale=18), nullable=False),
    sa.Column('debt_face_amount', sa.Numeric(precision=38, scale=18), nullable=False),
    sa.Column('collateral_token', sa.String(), nullable=False),
    sa.Column('collateral_amount', sa.Numeric(precision=38, scale=18), nullable=False),
    sa.Column('event_name', sa.String(), nullable=False),
    sa.Column('block_number', sa.Integer(), nullable=False),
    sa.Column('protocol_id', sqlalchemy_utils.types.choice.ChoiceType(ProtocolIDs), nullable=False),
    sa.Column('id', sa.UUID(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_liquidation_event_data_block_number'), 'liquidation_event_data', ['block_number'], unique=False)
    op.create_index(op.f('ix_liquidation_event_data_event_name'), 'liquidation_event_data', ['event_name'], unique=False)
    op.drop_index('ix_notification_email', table_name='notification')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_liquidation_event_data_event_name'), table_name='liquidation_event_data')
    op.drop_index(op.f('ix_liquidation_event_data_block_number'), table_name='liquidation_event_data')
    op.drop_table('liquidation_event_data')
    op.drop_index(op.f('ix_accumulators_sync_event_data_event_name'), table_name='accumulators_sync_event_data')
    op.drop_index(op.f('ix_accumulators_sync_event_data_block_number'), table_name='accumulators_sync_event_data')
    op.drop_table('accumulators_sync_event_data')
    # ### end Alembic commands ###