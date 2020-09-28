# SiteMaps Для Django

###  в  **`settings.py`** 

```python
SITE_ID = 1

INSTALLED_APPS = (
    # ...
    'django.contrib.sites',
    'django.contrib.sitemaps',
)
```

Выполнить  

 `python manage.py migrate`

 ###  Sitemaps.py

Создайте новый файл в каталоге приложения и назовите его `sitemaps.py` 

и добавить в него следующий код

```python
from django.contrib.sitemaps import Sitemap
from .models import Post

class PostSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return Post.objects.filter(active=1)

    def lastmod(self, obj):
        return obj.created
```

в **models.py** должен быть задан  **get_absolute_url()** 

###  urls.py

```python
from django.contrib.sitemaps.views import sitemap
from blog.sitemaps import PostSitemap

sitemaps = {
    'posts': PostSitemap,
}

urlpatterns = [
    url("sitemap.xml", sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
]
```

### Настраиваем сайт в админ панели 

 `http://127.0.0.1:8000/admin/sites/site/ `

### и проверяем итог

 `http://127.0.0.1:8000/sitemap.xml `