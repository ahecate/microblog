"""new fields in user model

Revision ID: 0b92b77f5d6d
Revises: 0e84ebbc01ec
Create Date: 2019-12-26 22:32:54.295669

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0b92b77f5d6d'
down_revision = '0e84ebbc01ec'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('about_me', sa.String(length=140), nullable=True))
    op.add_column('user', sa.Column('last_seen', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'last_seen')
    op.drop_column('user', 'about_me')
    # ### end Alembic commands ###
