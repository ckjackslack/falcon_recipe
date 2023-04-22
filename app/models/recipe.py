from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Recipe(Base):
    __tablename__ = 'recipes'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    category = Column(String)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'category': self.category,
        }

    @classmethod
    def from_dict(cls, data, instance=None):
        if instance is None:
            instance = cls()
        instance.name = data.get('name', instance.name)
        instance.description = data.get('description', instance.description)
        instance.category = data.get('category', instance.category)
        return instance
