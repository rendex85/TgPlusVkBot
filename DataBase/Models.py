import os.path

from peewee import *

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "PublicDB.db")
conn = SqliteDatabase(db_path)


def closeConnect():
    conn.close()


class BaseModel(Model):
    conn.connect()

    class Meta:
        database = conn


class Publics(BaseModel):
    public_id = IntegerField(column_name='public_id', primary_key=True)
    public_url = TextField(column_name='public_url')
    last_post_id = IntegerField(column_name='last_post_id')
    public_name = TextField(column_name='public_name')

    class Meta:
        database = conn
        table_name = 'Publics'
