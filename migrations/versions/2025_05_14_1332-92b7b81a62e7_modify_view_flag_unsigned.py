"""modify view_flag unsigned

Revision ID: 92b7b81a62e7
Revises: d2a80ecd1ede
Create Date: 2025-05-14 13:32:50.852822

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = '92b7b81a62e7'
down_revision: Union[str, None] = 'd2a80ecd1ede'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('th_sellers',
    sa.Column('id', mysql.INTEGER(unsigned=True), autoincrement=True, nullable=False, comment='판매자 테이블 Primary Key'),
    sa.Column('business_code', sa.String(length=10), nullable=False, comment='사업자등록번호'),
    sa.Column('owner_name', sa.String(length=50), nullable=False, comment='대표자명'),
    sa.Column('compony_name', sa.String(length=80), nullable=False, comment='업체명'),
    sa.Column('adress', sa.String(length=140), nullable=True, comment='업체주소'),
    sa.Column('tel', sa.String(length=15), nullable=True, comment='전화번호'),
    sa.Column('phone', sa.String(length=15), nullable=True, comment='개인전화'),
    sa.Column('view_flag', mysql.TINYINT(display_width=1, unsigned=True), nullable=False, comment='노출여부'),
    sa.Column('created_user', sa.String(length=50), server_default=sa.text("'system'"), nullable=False, comment='등록자 - 아이디 정보 생성시 아이디+이름으로 표기 예정'),
    sa.Column('created_datetime', sa.DateTime(), server_default=sa.text('now()'), nullable=False, comment='등록시각'),
    sa.Column('updated_user', sa.String(length=50), nullable=True, comment='수정자 - 아이디 정보 생성시 아이디+이름으로 표기 예정'),
    sa.Column('updated_datetime', sa.DateTime(), nullable=True, comment='수정시각'),
    sa.Column('deleted_user', sa.String(length=50), nullable=True, comment='삭제자 - 아이디 정보 생성시 아이디+이름으로 표기 예정'),
    sa.Column('deleted_datetime', sa.DateTime(), nullable=True, comment='삭제시각'),
    sa.PrimaryKeyConstraint('id'),
    comment='판매자 정보 테이블'
    )
    op.create_index(op.f('ix_th_sellers_business_code'), 'th_sellers', ['business_code'], unique=False)
    op.create_index(op.f('ix_th_sellers_compony_name'), 'th_sellers', ['compony_name'], unique=False)
    op.create_index(op.f('ix_th_sellers_owner_name'), 'th_sellers', ['owner_name'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_th_sellers_owner_name'), table_name='th_sellers')
    op.drop_index(op.f('ix_th_sellers_compony_name'), table_name='th_sellers')
    op.drop_index(op.f('ix_th_sellers_business_code'), table_name='th_sellers')
    op.drop_table('th_sellers')
    # ### end Alembic commands ###
