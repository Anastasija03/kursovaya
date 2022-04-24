from os import name
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.Index.as_view(), name="index"),
    path('quiz/', views.QuizList.as_view(), name="quiz_list"),
    path('quiz/<pk>/<quest>', views.QuizPage.as_view(), name="quiz"),
    path('form/', views.FormPage.as_view(), name="form"),
    path('propose/', views.ProposePage.as_view(), name="propose"),
    path('api/createform', views.APICreateUserForm.as_view(), name="api_createform"),
    path('api/getuserforms', views.APIGetUserForms.as_view(), name="api_getuserforms")
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
