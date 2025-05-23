"""add Product Table

Revision ID: d2a80ecd1ede
Revises: 
Create Date: 2025-05-09 13:38:32.110751

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = 'd2a80ecd1ede'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('th_products',
    sa.Column('id', mysql.INTEGER(unsigned=True), autoincrement=True, nullable=False, comment='제품 테이블 Primary Key'),
    sa.Column('code', sa.String(length=8), nullable=False, comment='제품 고유 코드'),
    sa.Column('name', sa.String(length=100), nullable=False, comment='제품명'),
    sa.Column('price', mysql.INTEGER(unsigned=True), nullable=False, comment='제품 가격'),
    sa.Column('use_flag', mysql.TINYINT(display_width=1), nullable=False, comment='현재 판매 또는 사용중인 제품'),
    sa.Column('created_user', sa.String(length=50), server_default=sa.text("'system'"), nullable=False, comment='등록자 - 아이디 정보 생성시 아이디+이름으로 표기 예정'),
    sa.Column('created_datetime', sa.DateTime(), server_default=sa.text('now()'), nullable=False, comment='등록시각'),
    sa.Column('updated_user', sa.String(length=50), nullable=True, comment='수정자 - 아이디 정보 생성시 아이디+이름으로 표기 예정'),
    sa.Column('updated_datetime', sa.DateTime(), nullable=True, comment='수정시각'),
    sa.Column('deleted_user', sa.String(length=50), nullable=True, comment='삭제자 - 아이디 정보 생성시 아이디+이름으로 표기 예정'),
    sa.Column('deleted_datetime', sa.DateTime(), nullable=True, comment='삭제시각'),
    sa.PrimaryKeyConstraint('id'),
    comment='제품 기본정보 테이블'
    )
    op.create_index(op.f('ix_th_products_code'), 'th_products', ['code'], unique=False)
    op.create_index(op.f('ix_th_products_name'), 'th_products', ['name'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_th_products_name'), table_name='th_products')
    op.drop_index(op.f('ix_th_products_code'), table_name='th_products')
    op.drop_table('th_products')
    # ### end Alembic commands ###
