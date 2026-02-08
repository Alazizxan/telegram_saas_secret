from sqlalchemy import Column, Integer, String, Boolean, Text
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Bot(Base):
    __tablename__ = "bots"
    id = Column(Integer, primary_key=True)
    owner_id = Column(Integer)
    token = Column(String)
    is_active = Column(Boolean, default=True)

class BotText(Base):
    __tablename__ = "bot_texts"
    id = Column(Integer, primary_key=True)
    bot_id = Column(Integer)
    key = Column(String)
    text = Column(Text)

class Session(Base):
    __tablename__ = "sessions"
    id = Column(Integer, primary_key=True)
    bot_id = Column(Integer)
    user_id = Column(Integer)
    path = Column(String)
