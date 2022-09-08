1. python3 manage.py runserver
1. 	http://localhost:8000/
1. 	http://localhost:8000/admin/
1. 	http://localhost:8000/blog/index/                 
1. 	http://localhost:8000/users/register/
1. 	http://localhost:8000/users/login/
1. 	http://localhost:8000/users/logout-user/
1. 	http://localhost:8000/users/profile/roblero/
1. 	http://localhost:8000/users/profile/andy/
1. 	http://localhost:8000/blog/create/
1.
1. https://docs.djangoproject.com/en/4.1/topics/auth/default/#authenticating-users

1. `python3 manage.py makemigrations `
1. `python3 manage.py makemigrations` blog_app when adding something new to models
1. `python3 manage.py migrate`
1. `pipenv install docutils==0.19`
1. `pipenv shell`
1. python3 manage.py createsuperuser

print(request.POST)  

``` 
<QueryDict: {
    'csrfmiddlewaretoken': ['Ypr99DGa3fgyGV8d3VBjDZBTaBALbovbXelIIwfwq5cjvcnZMUeOTaMgkpzoRtoP'],
    'username': ['andy'],
    'password': ['123']
    }>
```

1. ./manage.py showmigrations my_app see all migrations
1. ./manage.py migrate my_app zero to reverse all migrations
1. [reverse()](https://docs.djangoproject.com/en/4.1/ref/urlresolvers/#reverse)