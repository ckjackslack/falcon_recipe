from sqlalchemy.orm import Session

from ..models.recipe import Recipe


class RecipeService:
    def __init__(self, session: Session):
        self.Session = session

    def create_recipe(self, recipe):
        with self.session() as db:
            db.add(recipe)
            db.commit()
            db.refresh(recipe)
            return recipe

    def get_recipe_by_id(self, id):
        with self.session() as db:
            return db.query(Recipe).filter(Recipe.id == id).one()

    def get_recipes(self, name=None, category=None):
        with self.session() as db:
            query = db.query(Recipe)
            if name is not None:
                query = query.filter(Recipe.name.like(f'%{name}%'))
            if category is not None:
                query = query.filter(Recipe.category == category)
            return query.all()

    def update_recipe(self, recipe):
        with self.session() as db:
            db.add(recipe)
            db.commit()
            db.refresh(recipe)
            return recipe

    def delete_recipe(self, recipe):
        with self.session() as db:
            db.delete(recipe)
            db.commit()

    def clear_all(self):
        with self.session() as db:
            db.query(Recipe).delete()
            db.commit()

    def session(self):
        return self.Session()
