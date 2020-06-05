from core import views
from django.urls import path

urlpatterns = [
    path('api/dapau', views.dapau),
    path('api/login', views.login),
    path('api/logout', views.logout),
    path('api/whoami', views.whoami),
    path('api/settings', views.settings),

    path('api/dashboard', views.dashboard),
    path('api/list_questions', views.list_questions),
    path('api/add_answers', views.add_answers),
]
