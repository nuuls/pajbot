from sqlalchemy import Column, Integer, String, Text

from pajbot.managers.db import Base


class WebContent(Base):
    __tablename__ = 'tb_web_content'

    id = Column(Integer, primary_key=True)
    page = Column(String(64), nullable=False)
    content = Column(Text, nullable=True)
