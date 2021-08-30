from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from articles.models import Articles
from .mixins import (
    FieldsMixin,
    FormValid,
    AuthorAccessMixin,
    SuperUserMixin,
    AuthorsAccessMixin,
)
from django.contrib.auth.views import PasswordChangeView
from .models import User
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.contrib.auth.views import LoginView
from .forms import ProfileForm

# Create your views here.
class ArticlesList(AuthorsAccessMixin, ListView):
    template_name = "registration/home.html"

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Articles.objects.all()
        else:
            return Articles.objects.filter(author=self.request.user)


class ArticlesCreate(AuthorsAccessMixin, FieldsMixin, FormValid, CreateView):
    model = Articles
    fields = ["title", "slug", "author", "description", "thumbnail", "publish", "status", "category",]
    template_name = "registration/articles_create_update.html"


class ArticlesUpdate(AuthorAccessMixin, FieldsMixin, FormValid, UpdateView):
    model = Articles
    fields = ["title", "slug", "author", "description", "thumbnail", "publish", "status", "category",]
    template_name = "registration/articles_create_update.html"


class ArticlesDelete(SuperUserMixin, DeleteView):
    model = Articles
    success_url = reverse_lazy('account:home')
    template_name = "registration/articles_confirm_delete.html"


class Profile(LoginRequiredMixin, UpdateView):
    model = User
    template_name = "registration/profile.html"
    form_class = ProfileForm
    def get_object(self):
        return User.objects.get(pk= self.request.user.pk)

    def get_form_kwargs(self):
        kwargs = super(Profile, self).get_form_kwargs()
        kwargs.update({
                'user': self.request.user,
        })
        return kwargs

class Login(LoginView):
    def get_success_url(self):
        user = self.request.user

        if user.is_superuser or user.is_author:
            return reverse_lazy("account:home")
        else:
            return reverse_lazy("account:profile")

class PasswordChange(PasswordChangeView):
    success_url = reverse_lazy("account:password_change_done")
    