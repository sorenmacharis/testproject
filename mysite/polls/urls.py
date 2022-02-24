from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('numberofpolls/', views.numberofpolls, name='numberofpolls'),
    path('numberofvotes/', views.numberofvotes, name='numberofvotes'),
    path('about/', views.about, name="about"),
]