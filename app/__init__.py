import falcon
from falcon_cors import CORS, CORSMiddleware
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .api.recipes import RecipeResource
from .models.recipe import Base, Recipe
from .settings import DATABASE_URL
from .services.recipe_service import RecipeService
from .utils import prepopulate_db


class App(falcon.API):
    def __init__(self):
        super().__init__(middleware=[
            CORSMiddleware(cors=CORS())
        ])

        engine = create_engine(DATABASE_URL)
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)

        self.recipe_service = RecipeService(Session)
        self.recipe_service.clear_all()

        prepopulate_db(self.recipe_service)

        resource = RecipeResource(self.recipe_service)

        self.add_route('/recipes', resource)
        self.add_route('/recipes/{id}', resource)