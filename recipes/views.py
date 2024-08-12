from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
    DeleteView,
    UpdateView,
)
from .models import Recipe
from .forms import RecipeForm

# to check if user is logged in first
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin


class EditeRecipe(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = "recipes/edit_recipe.html"
    model = Recipe
    form_class = RecipeForm
    success_url = "/recipes/"

    def test_func(self):
        return self.request.user == self.get_object().user


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


class RecipeDetail(DetailView):
    # view single recipe
    # install pip install black to make it public compliant.
    # python -m black recipes -  specifying the recipes directory.
    template_name = "recipes/recipe_detail.html"
    model = Recipe
    context_object_name = "recipes"


# the mixin helps to check if they are logged in
class DeleteRecipe(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    # delete recipe
    model = Recipe
    success_url = "/recipes/"
