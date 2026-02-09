from sqlalchemy import Column, Integer, String, Boolean, Text, BigInteger
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Bot(Base):
    __tablename__ = "Bot"

    id = Column(Integer, primary_key=True)
    ownerId = Column(Integer)
    templateId = Column(Integer)
    token = Column(String)
    isActive = Column(Boolean)


class BotText(Base):
    __tablename__ = "BotText"

    id = Column(Integer, primary_key=True)
    botId = Column(Integer)
    key = Column(String)
    text = Column(Text)


class TemplateText(Base):
    __tablename__ = "TemplateText"

    id = Column(Integer, primary_key=True)
    templateId = Column(Integer)
    key = Column(String)
    text = Column(Text)


class Session(Base):
    __tablename__ = "Session"

    id = Column(Integer, primary_key=True)
    botId = Column(Integer)
    userId = Column(BigInteger)
    path = Column(Text)
