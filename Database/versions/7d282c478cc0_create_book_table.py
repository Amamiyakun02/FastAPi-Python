"""create_book_table

Revision ID: 7d282c478cc0
Revises: 
Create Date: 2023-08-31 08:54:15.119041

"""
from typing import Sequence, Union

from alembic import op
from sqlalchemy import Column, String,Integer


# revision identifiers, used by Alembic.
revision: str = '7d282c478cc0'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'book',
        Column('id', Integer,primary_key=True),
        Column('name',String(255), nullable=False),
        Column('pengarang', String(255),nullable=True),
        Column('id_penerbit', Integer, nullable=True)
    )


def downgrade() -> None:
    op.drop_table('book')
