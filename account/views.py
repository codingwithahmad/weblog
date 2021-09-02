from django.shortcuts import render, redirect
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
    success_url = reverse_lazy('account:profile')
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

from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from .forms import SignupForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.core.mail import EmailMessage

class Register(CreateView):
    form_class = SignupForm
    template_name = "registration/create_account.html"
    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = False
        user.save(  )
        current_site = get_current_site(self.request)
        mail_subject = 'فعال سازی حساب کاربری'
        message = render_to_string('registration/account_active.html', {
            'user': user,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': account_activation_token.make_token(user)
        })
        to_email = form.cleaned_data.get('email')
        email = EmailMessage(
            mail_subject,message,to=[to_email]
        )
        email.send()
        return HttpResponse('لین ک فعال سازی حساب کاربری به ایمیل شما ارسال شد. یرای ورود <a href="/login" > کلیک </a> کنید.')
    
def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None 
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True 
        user.save()
        return HttpResponse("حساب کاربری شما فعال شد. برای ورود <a href='/login' > کلیک </a> کنید")
    else:
        return HttpResponse('لینک فعال سازی حساب کاربری منقضی شده است، برای ارسال مجدد <a href="/register" > کلیک </a> کنید.')