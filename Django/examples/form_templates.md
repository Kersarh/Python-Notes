# Set up the layout for Django forms in templates

When you pass a Django form -- unbound or bound -- to a template there are many options to generate its layout. You can use one of Django's pre-built HTML helpers to quickly generate a form's output or granularly output each field to create an advanced form layout (e.g. responsive design[[3\]](https://www.webforefront.com/django/formtemplatelayout.html#footnote-3)).In addition, there can also be many ways to output form errors (e.g. besides the fields themselves or at the top of a form). Up next, I'll describe the various options to output Django forms in templates.

Listing 6-19 shows the Django form I'll use throughout the remaining layout sections -- which is the same form used throughout this chapter.



#### Listing 6-19. Django form class definition

```
from django import forms

class ContactForm(forms.Form):
      name = forms.CharField(required=False)
      email = forms.EmailField(label='Your email')  
      comment = forms.CharField(widget=forms.Textarea) 
```

## Output form fields: form.as_table, form.as_p, form.as_ul & granularly by field

Django forms offer three helper methods to simplify the output of all form fields. The syntax `form.as_table` outputs a form's fields to accommodate an HTML `` as illustrated in listing 6-20. The syntax `form.as_p` outputs a form's fields with HTML `` tags as illustrated in listing 6-21. Where as the syntax `form.as_ul` outputs a form's fields to accommodate an HTML `` list tag, as illustrated in listing 6-22.

>  **Caution** If you use form.as_table, form.as_p, form.as_ul you must declare opening/closing HTML tags, a wrapping <form> tag, a Django {% csrf_token %} tag and an <input type="submit"> button, as described in the initial section of this chapter ['Functional web form syntax for Django forms'](https://www.webforefront.com/django/setupdjangoforms.html#functionalform)



#### Listing 6-20. Django form output with form.as_table

```
<tr>
    <th><label for="id_name">Name:</label></th>
    <td><input id="id_name" name="name" type="text" /></td>
</tr>\n
<tr>
    <th><label for="id_email">Your email:</label></th>
    <td><input id="id_email" name="email" type="email" required/></td>
</tr>\n
<tr>
    <th><label for="id_comment">Comment:</label></th>
    <td><textarea cols="40" id="id_comment" name="comment" rows="10" required>\r\n</textarea></td>
</tr>
```



#### Listing 6-21. Django form output with form.as_p

```
<p>
    <label for="id_name">Name:</label>
    <input id="id_name" name="name" type="text" />
</p>\n
<p>
    <label for="id_email">Your email:</label>
    <input id="id_email" name="email" type="email" required/>
</p>\n
<p>
    <label for="id_comment">Comment:</label>
    <textarea cols="40" id="id_comment" name="comment" rows="10" required>\r\n</textarea>
</p>'
```



#### Listing 6-22 Django form output with form.as_ul

```
<li>
    <label for="id_name">Name:</label>
    <input id="id_name" name="name" type="text" />
</li>\n
<li>
    <label for="id_email">Your email:</label>
    <input id="id_email" name="email" type="email" required/>
</li>\n
    <li><label for="id_comment">Comment:</label>
    <textarea cols="40" id="id_comment" name="comment" rows="10" required>\r\n</textarea>
</li>
```

>  **Tip** The `form.as_table`, `form.as_p` & `form.as_ul` output can be made less verbose -- omitting label tags and id attributes -- by [initializing the form with `auto_id=False`](https://www.webforefront.com/django/formprocessing.html#listing-6-12). In addition, you can also change the symbol that separates label names (by default `:`) with another symbol by initializing the form with the [`label_suffix` variable](https://www.webforefront.com/django/formprocessing.html#label-suffix). It's also possible to use the [`field_order` option](https://www.webforefront.com/django/formprocessing.html#field-order) to alter the output field order.

Under certain circumstances, none of the previous helper methods may be sufficient to achieve certain form layouts. For example, to create a responsive design you'll need to output each of field manually to accommodate specific layout requirement (e.g. Bootstrap CSS grid columns). To achieve the custom output of fields, every form instance permits access to its fields through the `form.` syntax using the attributes in table 6-4.



#### Table 6-4. Django form field attributes accessible in templates

| **Attribute name**                                           | **Description**                                              |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| {{form.<field_name>}} (i.e. No attribute, just the field name by itself) | Outputs the HTML form tag -- technically known as the Django widget -- associated with the field (e.g. <input type="text">) |
| {{form.<field_name>.name}}                                   | Outputs the name of a field, as defined in the form class.   |
| {{form.<field_name>.value}}                                  | Outputs the value of the field assigned with initial or user provided data. Useful if you need to separately output the HTML form tag's value attribute (e.g. for <input type="text" name="name" value="John Doe">, {{form.name.value}} outputs John Doe) |
| {{form.<field_name>.label}}                                  | Outputs the label of a field, which by default uses the syntax "Your <field_name>" (e.g. for the email field, {{form.email.label}} outputs Your email). |
| {{form.<field_name>.id_for_label}}                           | Outputs the label id of a field, which by default uses the syntax id_<field_name> (e.g. for the email field, {{form.email.id_for_label}} outputs id_email). |
| {{form.<field_name>.auto_id}}                                | Outputs the auto id of a field, which by default uses the syntax id_<field_name> (e.g. for the email field, {{form.email.auto_id}} outputs id_email). |
| {{form.<field_name>.label_tag}}                              | Helper method to output the HTML <label> tag along with id_for_label and label(e.g. for the email field, {{form.email.label_tag}} outputs <label for="id_email">Your email:</label>). |
| {{form.<field_name>.help_text}}                              | Outputs the help text associated with a field.               |
| {{form.<field_name>.errors}}                                 | Outputs the errors associated with a field.                  |
| {{form.<field_name>.css_classes}}                            | Outputs the CSS classes associated with a field.             |
| {{form.<field_name>.as_hidden}}                              | Outputs the HTML of a field as a hidden HTML field (e.g. <input type="hidden" >) |
| {{form.<field_name>.is_hidden}}                              | Boolean result of a field's hidden status.                   |
| {{form.<field_name>.as_text}}                                | Outputs the HTML of a field as a text HTML field (e.g. <input type="text">) |
| {{form.<field_name>.as_textarea}}                            | Outputs the HTML of a field as a textarea HTML field (e.g. <textarea></textarea>) |
| {{form.<field_name>.as_widget}}                              | Outputs the Django widget associated with a field; technically produces the same output as calling the standalone field with the syntax {{form.<field_name>}} -- shown at the top of this table. |

>  **Tip** You can override the default output for `{{form..label}}`, the suffix for `{{form..label_tag}}` and the default output for `{{form..help_text}}` in [table 6-4](https://www.webforefront.com/django/formtemplatelayout.html#table-6-4), by using the `label`, `label_suffix` and `help_text` options on form fields. This process is described in the previous section on ['Django form field types: Widgets, options and validations'](https://www.webforefront.com/django/formfieldtypesandvalidation.html).

As you can see in [table 6-4](https://www.webforefront.com/django/formtemplatelayout.html#table-6-4), there are many field attributes available to customize the layout of a form. Just be careful that if you output form fields granularly you don't miss a field, because if you do miss a field, the most likely outcome is Django won't be able to process the form as it won't receive values from missing fields.

Listing 6-23 illustrates a standard `{% for %}` loop which ensures you don't miss any field and provides more flexibility than the previous `form.as_table`, `form.as_p` & `form.as_ul` methods.



#### Listing 6-23 Django form {% for %} loop over all fields

```
{% for field in form %}
    <div class="row">
       <div class="col-md-2">    
        {{ field.label_tag }}
        {% if field.help_text %}
          <sup>{{ field.help_text }}</sup>
        {% endif %}
        {{ field.errors }}
       </div><div class="col-md-10 pull-left">
         {{ field }}
       </div>
    </div>
 {% endfor %}
```

In listing 6-23, a loop is created over the `form` reference to ensure no fields are missed. If you want to avoid presenting a field in certain form layouts, then I recommend you use the `{{field.as_hidden}}` vs. `{{field}}`, as this ensures the field still forms part of the form for validation purposes and is simply hidden from a user -- more details about this scenario are provided in the upcoming section on [advanced form processing and partial forms](https://www.webforefront.com/django/formadvancedprocessing.html).

 

## Output field order: field_order and order_fields.

If you use any of the techniques presented in listings [6-20](https://www.webforefront.com/django/formtemplatelayout.html#listing-6-20), [6-21](https://www.webforefront.com/django/formtemplatelayout.html#listing-6-21), [6-22](https://www.webforefront.com/django/formtemplatelayout.html#listing-6-22) or [6-23](https://www.webforefront.com/django/formtemplatelayout.html#listing-6-23), the form fields are output in the same order as they're declared in the form class in [listing 6-19](https://www.webforefront.com/django/formtemplatelayout.html#listing-6-19) (i.e. name,email,comment). However, you can use several techniques to alter the order in which form fields are output.

The first and obvious approach is to change the form field order directly in the form class definition. Because this last technique requires altering a form's source code, Django also offers the `field_order` option. The `field_order` option accepts a list of form field names in the order you want them output (e.g. `field_order=['email','name','comment']` outputs the `email` field first, followed by `name` and `comment`). The `field_order` option is flexible enough that you can provide a partial list of form fields (e.g. `field_order=['email']` outputs the email field first and the remaining form fields in their declared order) as well as declare non-existent field names which are ignored and is helpful when using form inheritance.

The `field_order` option can be declared in two locations. First, it can be declared as part of a form class definition, as illustrated in listing 6-24.



#### Listing 6-24 Django form field_order option to enforce field order

```
from django import forms

class ContactForm(forms.Form):
      name = forms.CharField(required=False)
      email = forms.EmailField(label='Your email')
      comment = forms.CharField(widget=forms.Textarea)
      field_order = ['email','comment','name']
```

As you can see in listing 6-24, `field_order` is declared as any other form field and assigned a list of field names to ensure the fields are output in the order: email, comment and name. It's also possible to use the `field_order` option as part of a form's initialization processes -- described in detail in the form processing section. It's worth mentioning that if you use the `field_order` option on both the class definition -- as shown in listing 6-24 -- and form instance initialization, the latter value takes precedence over the former.

In addition to the `field_order` option, Django also offers `order_fields` which also expects a list of field names to alter a form's output field order. But unlike the `field_order` option which must be declared in a form class or as part of the initialization of a form instance, `order_fields` can be called directly on a form instance which makes it a good option to use in a view method or template (e.g. `form.order_fields(['email'])`).

## Output CSS classes, styles & field attributes: error_css_class, required_css_class, widget customization and various form field options.

By default, when you output form fields and labels there are no CSS classes or styles associated with them. Django offers several mechanisms to associate CSS classes with form fields. The first two approaches are the `error_css_class` and `required_css_class` fields which are declared directly in a Django form, as illustrated in listing 6-25.



#### Listing 6-25. Django form error_css_class and required_css_class fields to apply CSS formatting

```
from django import forms

class ContactForm(forms.Form):
      name = forms.CharField(required=False)
      email = forms.EmailField(label='Your email')
      comment = forms.CharField(widget=forms.Textarea)
      error_css_class = 'error'
      required_css_class = 'bold'      
```

As you can see in listing 6-25, the `error_css_class` and `required_css_class` fields are added just like regular form fields. When a field associated with a form instance of this kind is rendered on a template, Django adds the `error` CSS class to all fields marked with an error and adds the `bold` CSS class to all fields marked as required.

For example, all form fields are treated as required except when they explicitly use `required=False`. This means if you output an unbound form instance from listing 6-25 using `form.as_p`, the comment field is output as `Comment: \r\n` -- note the `class` in the `` tag. Similarly, if a field associated with a bound form instance from listing 6-25 raises an error, Django adds the `error` CSS class to the field (e.g. if the email field value is not valid, the email field is output as `Your email: `, note the `bold` CSS class remains because the form field is also required).

As helpful as the `error_css_class` and `required_css_class` fields are, they still offer limited CSS formatting functionality. To gain full control over CSS class output, you'll need to either use some of the more granular output options for fields in [table 6-4](https://www.webforefront.com/django/formtemplatelayout.html#table-6-4) or customize a form field's widget as illustrated in listing 6-26.



#### Listing 6-26. Django form with inline widget definition to add custom CSS class

```
from django import forms

class ContactForm(forms.Form):
      name = forms.CharField(required=False)
      email = forms.EmailField(label='Your email', widget=forms.TextInput(attrs={'class' : 'myemailclass'}))
      comment = forms.CharField(widget=forms.Textarea)
```

Notice in listing 6-26 how the email field is declared with the `widget=forms.TextInput(attrs={'class' : 'myemailclass'})` argument. This last statement tells Django that when it outputs the `email` field, it use the custom `forms.TextInput` widget which declares the CSS `class` attribute with the `myemailclass` value.

By using the form definition in listing 6-26, the `email` field is output as ``. If you don't know what a Django widget is, see the earlier section entitled ['The relationship between widgets and form fields'](https://www.webforefront.com/django/formfieldtypesandvalidation.html#relationship).

The approach presented in listing 6-26 is a powerful technique, because just as you can declare the CSS `class` attribute, you can also declare any other form field HTML attribute. For example, if you wanted to declare custom HTML attributes -- such as those used by frameworks like jQuery or Bootstrap -- you can easily use this same technique (e.g.`widget=forms.TextInput(attrs={'role' : 'dialog'})` would output ``).

However, a word of caution now that you know how easy it's to output any HTML attribute alongside a Django form field. Be aware that nearly all Django form field data types come with built-in options that get translated into HTML attributes. For example, the `forms.CharField(max_length=25)` statement gets output to ``, which means the form field `max_length` option automatically generates the HTML `maxlength="25"` attribute. So be careful to start adding HTML attributes indiscriminately using the approach in listing 6-26, as they may already be supported through built-in data type options. See the previous section on ['Django form field types: Widgets, options and validations'](https://www.webforefront.com/django/formfieldtypesandvalidation.html) for more details on these built-in data type options.

 

## Output form field errors: form.<field_name>.errors, form.errors, form.non_field_errors

Just as form fields can be output in different ways, form field errors can also be output in different ways. Toward the end of the first section in [listing 6-23](https://www.webforefront.com/django/formtemplatelayout.html#listing-6-23), you can see how we use the `{{field.errors}}` syntax to output errors associated with a particular field. However, an important thing to keep in mind when outputting a field's `errors` value in this manner is the output is generated as an HTML formatted list:

```
<ul class="errorlist">
    <li>Name is required.</li>
</ul>
```

As you can see in listing 6-27, the `{{fields.errors}}` value is list with the `errorlist` CSS class -- which allows you to provide CSS behaviors like a background color or borders -- and the values are pre-wrapped as list elements.

If you want to strip these wrapping HTML list tags to gain more control over the error layout (e.g. creating a responsive design or CSV list) you can do so creating a loop on each `field.errors` as illustrated in listing 6-27.



#### Listing 6-27. Django loop over form.<field_name>.errors

```
 {% for field in form %}
    <div class="row">
      <div class="col-md-2">
        {{ field.label_tag }}
        {% if field.help_text %}
          <sup>{{ field.help_text }}</sup>
          {% endif %}
          {% for error in field.errors %}
           <div class="row">
             <div class="alert alert-danger">{{error}}</div>
           </div>
          {% endfor %}
       </div><div class="col-md-10 pull-left">
         {{ field }}
       </div>
    </div>
  {% endfor %}
```

You can see in listing 6-27 that inside the loop for each field, another loop is made on the `field.errors` reference to granularly output and assign custom markup to each field error.

As granular as the error output in 6-27 is, this type of layout assumes you want to display a form's error messages besides each field, in addition to requiring a loop over a form's fields. But what if you want to display a form's errors at the top or besides the main form ? Or if you want to keep using Django's short-cut methods (i.e. `form.as_table`, `form.as_p` & `form.as_ul`) and still display errors ?

Besides the `form..errors` syntax in listing 6-27 to access field errors, Django also can output form's errors with the `errors` and `non_field_errors` dictionaries as illustrated in listing 6-28.



#### Listing 6-28. Django form.errors and form.non_field_errors with custom HTML output

```
<!-- Field errors -->
 {% if form.errors %}
  <div class="row">
    {% for field_with_error,error_messages in form.errors.items %}
        <div class="alert alert-danger">{{field_with_error}}  {{error_messages}}</div>
    {% endfor %}
  </div>
  {% endif %}
<!-- Non-field errors --> {% if form.non_field_errors %}
  <div class="row">
    {% for error in form.non_field_errors %}
    <div class="alert alert-danger">{{error}}</div>
    {% endfor %}
  </div>
  {% endif %}
```

As you can see in listing 6-28, the `form.errors` dictionary provides an aggregated version of all the `form..errors`, where each dictionary key represents the form field name and the value is a list of error messages with error code (e.g. `required`) to further filter the error list. If you want to output every form error at the top of a form/page, require error filtering by code type or want to keep using Django's shortcut output form methods (e.g. `form.as_table`) and obtain form errors, then using `form.errors` on a template is the way to go.

In addition, notice toward the top of listing 6-28 the loop over the `form.non_field_errors` dictionary. The `form.non_field_errors` contains errors that don't belong to a specific form field -- as discussed earlier in the ['Error form values: errors'](https://www.webforefront.com/django/formprocessing.html#errors) section and the special error placeholder field named `__all__`. Because non-field errors don't apply to a specific form field, it's common to output these type of errors at the top of a form accessing the `non_field_errors` dictionary.

Be aware that if you use `form.errors` or `form.non_field_errors` to output errors, by default the error reference -- `{{error_messages}}` and `{{error}}` in listing 6-28 -- are wrapped as an HTML formatted list (e.g. `...`) but you can add an additional for loop to the error list -- as in [listing 6-27](https://www.webforefront.com/django/formtemplatelayout.html#listing-6-27) -- to create a custom HTML error layout.

Finally, it's worth mentioning there are a series of auxiliary methods designed to facilitate error output (e.g. in JSON format), [table 6-1](https://www.webforefront.com/django/formprocessing.html#table-6-1) in the Django form processing section describes these methods.