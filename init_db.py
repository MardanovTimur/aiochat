from sqlalchemy import create_engine, MetaData

from chatapp.settings import config
from chatapp.models import user, friends
from aiopg.sa.engine import aiopg

DSN = 'postgresql://{user}:{password}@{host}:{port}/{database}'


def create_tables(engine):
    """ Initialize the database
    """
    meta = MetaData()
    meta.create_all(bind=engine, tables=[user, friends])


def sample_data(engine):
    """ Creates the sample data in database
    """
    conn = engine.connect()
    conn.execute(user.insert(), [
        {
            'username': 'timurmardanov97',
        },
        {
            'username': 'jax02',
        },
    ])
    conn.close()


async def init_pg(app):
    conf = app['config']['postgres']
    engine = await aiopg.sa.create_engine(**conf)
    app['db'] = engine


async def close_pg(app):
    app['db'].close()
    await app['db'].wait_closed()


if __name__ == '__main__':
    db_url = DSN.format(**config['postgres'])
    engine = create_engine(db_url)

    create_tables(engine)
    sample_data(engine)
