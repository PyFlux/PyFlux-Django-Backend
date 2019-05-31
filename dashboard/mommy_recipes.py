from model_mommy.recipe import Recipe
from dashboard.models import Users

user = Recipe(
    Users,
    first_name = 'John Doe',
    username = 'joedoe',    
)
