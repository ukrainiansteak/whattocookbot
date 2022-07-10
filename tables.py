from sqlalchemy import Column, Integer, MetaData, String, Text, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from utilities import create_recipe

engine = create_engine('sqlite:///db.sqlite3', encoding='utf8', connect_args={'check_same_thread': False})
session = sessionmaker(bind=engine)()

Base = declarative_base()


class Recipe(Base):
    __tablename__ = "recipe"
    id = Column(Integer, primary_key=True)
    name = Column(String(length=100))
    description = Column(Text)

    # def __init__(self, id, name, description):
    #     self.id = id
    #     self.name = name
    #     self.description = description


Base.metadata.create_all(engine)
#
# create_recipe(session, Recipe)
