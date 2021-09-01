from django.http import Http404
from django.shortcuts import get_object_or_404, redirect
from articles.models import Articles

class FieldsMixin():
	def dispatch(self, request, *args, **kwargs):
		self.fields = [
		"title", "slug", 
		"description", "thumbnail", 'is_special', 
		"publish", "status", "category",
		]
		if request.user.is_superuser:
			self.fields.append("author")

		return super().dispatch(request, *args, **kwargs)

class FormValid():
	def form_valid(self, form):
		if self.request.user.is_superuser:
			form.save()
		else:
			self.obj = form.save(commit=False)
			self.obj.author = self.request.user
			if not self.obj.status == "i":
				self.obj.status = "d"

		return super().form_valid(form)
class AuthorAccessMixin():
	def dispatch(self, request, pk, *args, **kwargs):
		articles = get_object_or_404(Articles, pk=pk)
		if articles.author == request.user and articles.status in ['d', 'b'] or request.user.is_superuser:
			return super().dispatch(request, *args, **kwargs)
		else:
			raise Http404("شما دسترسی به این بخش را ندارید")

class SuperUserMixin():
	def dispatch(self, request, pk, *args, **kwargs):
		articles = get_object_or_404(Articles, pk=pk)
		if request.user.is_superuser:
			return super().dispatch(request, *args, **kwargs)
		else:
			raise Http404("شما دسترسی به این بخش را ندارید")

class AuthorsAccessMixin():
	def dispatch(self, request, *args, **kwargs):
		if request.user.is_authenticated:
			if request.user.is_superuser or request.user.is_author:
				return super().dispatch(request, *args, **kwargs)
			else:
				return redirect("profile")
		else:
			return redirect("login")				
