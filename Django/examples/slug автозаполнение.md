# Автозаполнение поля slug

Необходимо для генерации автоматического url поста из названия.  

## В `models.py`

```python
class Post(models.Model):
        title = models.CharField(verbose_name='Название', max_length=60)
        slug = models.SlugField(verbose_name='URL')

# Регистрируем в админ панели
class PostAdmin(admin.ModelAdmin):
        # Генерировать на основе поля title
        prepopulated_fields = {"slug": ("title",)}
admin.site.register(Post,PostAdmin)
```
