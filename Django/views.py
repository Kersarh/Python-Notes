from django.shortcuts import render
from django.views.generic import View, ListView, DetailView, FormView
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.shortcuts import get_list_or_404

from blog.models import Post, Comment, StaticPage, BlogTags
from .forms import CommentForm
from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector, TrigramSimilarity


class ListAll(ListView):
	""" Return all posts """
	model = Post
	paginate_by = 5
	template_name = 'blog/partial/list.html'

	def get_queryset(self):
		list_filter = Post.objects.filter(active=1)
		return list_filter


class DetailPost(DetailView):
	model = Post
	template_name = 'blog/partial/detail.html'

	def get_context_data(self, **kwargs):
		# Отобразить форму
		context = super(DetailPost, self).get_context_data(**kwargs)
		context['comment_form'] = CommentForm()
		# Фильтр для коментов
		context['comments'] = self.object.comments.filter(active=True)
		return context

	def get(self, request, *args, **kwargs):
		# Счетчик просмотров
		self.object = self.get_object()
		self.object.post_views += 1
		self.object.save()
		context = self.get_context_data(object=self.object)
		return self.render_to_response(context)

	def post(self, request, *args, **kwargs):
		# Обработка формы POST запрос
		self.object = self.get_object()
		context = super(DetailPost, self).get_context_data(**kwargs)
		context['comment_form'] = CommentForm()
		comment_form = CommentForm(data=request.POST)
		if comment_form.is_valid():
			new_comment = comment_form.save(commit=False)
			new_comment.post = self.object
			new_comment.save()
			return HttpResponseRedirect(self.object.get_absolute_url())
		else:
			comment_form = CommentForm()
			return self.render_to_response(context)


def static_pages(request, slug=None):
	""" Static Pages """
	page = get_object_or_404(StaticPage.objects.filter(slug=slug))
	return render(request, "blog/partial/static_page.html", {'object': page})


class ListTags(ListView):
	""" Список тегов """
	model = BlogTags
	paginate_by = 5
	template_name = 'blog/partial/list.html'

	def get_queryset(self):
		idd = self.kwargs['id']  # site.com/tag/1/
		# id = self.request.GET.get("id", 2)  # site.com/tag/?id=1
		q = Post.objects.filter(tags=idd)
		if not q:
			self.template_name = "blog/partial/not_found.html"
			return ["Not Found!"]
		elif q:
			return q


class Search(ListView):
	""" Для поиска требуется POSTGRESQL!!! """
	model = Post
	paginate_by = 10
	template_name = 'blog/partial/search.html'

	def get_queryset(self):
		queryset = super(Search, self).get_queryset()
		q = self.request.GET.get("q")
		if q:
			vector = SearchVector('title',
			                      'content',
			                      raw=True,
			                      fields=('title'))
			vector_trgm = TrigramSimilarity(
			    'title', q, raw=True, fields=('title')) + TrigramSimilarity(
			        'content', q, raw=True, fields=('content'))
			a = queryset.annotate(search=vector).order_by('title').filter(
			    search=q) or queryset.annotate(similarity=vector_trgm).filter(
			        similarity__gt=0.1).order_by('title')
			if not a:  # Если НЕ найдено
				self.template_name = "blog/partial/not_found.html"
				return ["Not Found!"]
			else:  # если НАЙДЕНО
				return a
		elif not q:  # Если ПУСТОЙ запрос
			self.template_name = "blog/partial/not_found.html"
			return ["Empty Search String."]

	def get_context_data(self, **kwargs):
		""" Добавляет в контекст параметр q из Get запроса
        Необходим для корректной работы пагинации в поиске """
		context = super().get_context_data(**kwargs)
		context['q'] = self.request.GET.get('q', 2)
		return context
