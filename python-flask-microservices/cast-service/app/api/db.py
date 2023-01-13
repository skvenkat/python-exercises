# cast-service/app/api/db.py

import os

from sqlalchemy import (Column, Integer, MetaData, String, Table, ARRAY, create_engine)
from databases import Database


DATABASE_URI = os.getenv("DATABASE_URI")

engine = create_engine(DATABASE_URI)
metadata = MetaData()

casts = Table(
    'casts',
    metadata,
    Column('id', Integer, primary_key=true),
    Column('name', String(30)),
    Column('nationality', String(30)),
)

database = Database(DATABASE_URI)
