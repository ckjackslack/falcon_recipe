import falcon
from sqlalchemy.orm.exc import NoResultFound

from ..models.recipe import Recipe
from ..services.recipe_service import RecipeService


class RecipeResource:
    def __init__(self, service: RecipeService):
        self.service = service

    def on_get(self, req, resp, id=None):
        if id is not None:
            try:
                recipe = self.service.get_recipe_by_id(id)
            except NoResultFound:
                raise falcon.HTTPNotFound()
            resp.media = recipe.to_dict()
        else:
            name = req.get_param('name')
            category = req.get_param('category')
            recipes = self.service.get_recipes(name=name, category=category)
            resp.media = [recipe.to_dict() for recipe in recipes]

    def on_post(self, req, resp):
        data = req.media
        recipe = Recipe.from_dict(data)
        recipe = self.service.create_recipe(recipe)
        resp.status = falcon.HTTP_CREATED
        resp.media = recipe.to_dict()

    def on_put(self, req, resp, id):
        data = req.media
        try:
            recipe = self.service.get_recipe_by_id(id)
        except NoResultFound:
            raise falcon.HTTPNotFound()
        recipe = Recipe.from_dict(data, instance=recipe)
        recipe = self.service.update_recipe(recipe)
        resp.media = recipe.to_dict()

    def on_delete(self, req, resp, id):
        try:
            recipe = self.service.get_recipe_by_id(id)
        except NoResultFound:
            raise falcon.HTTPNotFound()
        self.service.delete_recipe(recipe)
        resp.status = falcon.HTTP_NO_CONTENT