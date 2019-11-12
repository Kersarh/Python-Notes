# отображение HTML в шаблоне

## Тег `autoescape`

```python
{% autoescape off %}
...
{% endautoescape %}
```

Если off в этом промежутке будет поддерживаться HTML код.  
Если on html код будет выводиться как есть.  
Использовать с осторожностью только для кода которому доверяете.  
Не нужно оборачивать так пользовательский ввод из за возможности эксплойтов.

### examples

```python
{% autoescape off %}
<h1>Hello World!</h1>
{{ post.content|linebreaksbr }}
{% endautoescape %}
```
