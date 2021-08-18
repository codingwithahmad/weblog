from django.http import Http404
from django.shortcuts import get_object_or_404
from articles.models import Articles

class FieldsMixin():
	def dispatch(self, request, *args, **kwargs):
		if request.user.is_superuser:
			    self.fields = ["title", "slug", "author", 
				    "description", "thumbnail", 
				    "publish", "status", "category",
			    ]
		elif request.user.is_author:
				self.fields = ["title", "slug", 
				    "description", "thumbnail", 
				    "publish", "category",
			    ]
		else:
			raise Http404("وضعیت نویسندگی شما فعال نیست")

		return super().dispatch(request, *args, **kwargs)

class FormValid():
	def form_valid(self, form):
		if self.request.user.is_superuser:
			form.save()
		else:
			self.obj = form.save(commit=False)
			self.obj.author = self.request.user
			self.obj.status = "d"

		return super().form_valid(form)
class AuthorAccessMixin():
	def dispatch(self, request, pk, *args, **kwargs):
		articles = get_object_or_404(Articles, pk=pk)
		if articles.author == request.user and articles.status == 'd' or request.user.is_superuser:
			return super().dispatch(request, *args, **kwargs)
		else:
			raise Http404("شما دسترسی به این بخش را ندارید")