Создаем в папке templates файл `robots.txt`. 

Далее *urls.py*:

```
path('robots.txt', views.robots),
```

 *views.py*

```
def robots(request):
	return render(request, "robots.txt", content_type="text/plain")
```