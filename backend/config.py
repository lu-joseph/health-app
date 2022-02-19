import os


class Config(object):
    SQLALCHEMY_DATABASE_URI = 'postgresql://{user}:{password}@{host}/{name}'.format(
        user=os.getenv('DATABASE_USER'),
        password=os.getenv('DATABASE_PASSWORD'),
        host=os.getenv('DATABASE_HOST'),
        name=os.getenv('DATABASE_NAME')
    )
