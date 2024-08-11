from django.views.generic import CreateView, ListView
from .models import Recipe
from .forms import RecipeForm

# to check if user is logged in first
from django.contrib.auth.mixins import LoginRequiredMixin


class AddRecipe(LoginRequiredMixin, CreateView):
    # addimng the frecipe view
    template_name = "recipes/add_recipe.html"
    model = Recipe
    form_class = RecipeForm
    success_url = "/recipes/"

    def form_valid(self, form):
        # setting insatnce user to person who is logged in.
        form.instance.user = self.request.user
        return super(AddRecipe, self).form_valid(form)


class Recipes(ListView):
    # avoid Recipe to avoid further problems
    template_name = "recipes/recipes.html"
    model = Recipe
    context_object_name = "recipes"
