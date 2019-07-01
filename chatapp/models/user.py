import datetime
from sqlalchemy import (
    PrimaryKeyConstraint,
    Boolean,
    DateTime,
    UniqueConstraint,
    ForeignKey,
    MetaData,
    Table,
    Column,
    ForeignKey,
    Integer,
    String,
    Date,
)

from . import meta

# TODO: type on declarative style

friends = Table('friends', meta,
                Column('user_1', Integer, ForeignKey('user.id'), comment='Subscriber'),
                Column('user_2', Integer, ForeignKey('user.id'), comment='User to subscribe'),
                Column('created_on', DateTime(), default=datetime.datetime.utcnow),
                Column('is_approved', Boolean(), default=False),
                PrimaryKeyConstraint('user_1', 'user_2', name='user_1_user_2_pk'),
                )

user = Table('user', meta,
             Column('id', Integer, primary_key=True),
             Column('username', String(200), nullable=False, index=True),
             Column('phone', String(14), nullable=True),
             Column('last_seen', DateTime(), nullable=False, default=datetime.datetime.utcnow),
             UniqueConstraint('username', 'phone', name='username_phone_uniq_constraint'),
             )
