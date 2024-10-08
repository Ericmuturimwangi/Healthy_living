from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
    DeleteView,
    UpdateView,
)
from .models import Recipe
from .forms import RecipeForm
from django.db.models import Q  # allows to write complex db operations.

# to check if user is logged in first
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin


class EditeRecipe(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = "recipes/edit_recipe.html"
    model = Recipe
    form_class = RecipeForm
    success_url = "/recipes/recipes/"

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

    def get_queryset(self, **kwargs):
        query = self.request.GET.get("q")
        if query:
            recipes = self.model.objects.filter(
                Q(title__icontains=query)
                | Q(description__icontains=query)
                | Q(instructions__icontains=query)
                | Q(cuisine_types__icontains=query)
            )
        else:
            recipes = self.model.objects.all()
        return recipes


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
