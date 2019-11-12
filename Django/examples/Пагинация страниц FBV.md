# Пагинация на основе FunctionBaseView (FBV)

## В файле `views.py`

```python
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
def home(request):
    postList = Post.objects.filter(visible='1')
    paginator = Paginator(postList, 4) # 4 поста на страницу
    page = request.GET.get('page')
    try:
        querysetGoods = paginator.get_page(page)
    except PageNotAnInteger:
        querysetGoods = paginator.page(1)
    except EmptyPage:
        querysetGoods = paginator.page(paginator.num_pages)

    return render(request, "partial/home.html", {'posts': querysetGoods})
```

## В шаблоне

```python
<div class="pagination">
    {% if posts.has_previous %}
        <a href="?page={{ posts.previous_page_number }}">Older</a>
    {% endif %}
 
    {% for num in posts.paginator.page_range %}
        {% if num == posts.number %}
            <span class="current"><b>{{ num }}</b></span>
        {% else %}
            <a href="?page={{ num }}"> {{ num }}</a>
        {% endif %} 
    {% endfor %}
 
    {% if posts.has_next %}
        <a href="?page={{ posts.next_page_number }}">Newer</a>
    {% endif %}
</div>
```
