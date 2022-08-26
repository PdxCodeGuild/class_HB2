from django.urls import path
from .views import register, sign_in, sign_out

from poll import views


app_name = 'poll'
# The manual way
from .views import sign_in, register, sign_out, user_profile
urlpatterns = [
    path('sign_in', sign_in, name='sign_in'),
    path('sign_out', sign_out, name='sign_out'),
    path('register', register, name='register'),
    path('user_profile', user_profile, name='user_profile'),
]
# urlpatterns = [
#     # ex: /polls/
#     path('', views.index, name='index'),
#     # ex: /polls/5/
#     path('<int:question_id>/', views.detail, name='detail'),
#     # ex: /polls/5/results/
#     path('<int:question_id>/results/', views.results, name='results'),
#     # ex: /polls/5/vote/
#     path('<int:question_id>/vote/', views.vote, name='vote'),
#     path('loginUser', views.loginUser, name='loginUser'),
# ]