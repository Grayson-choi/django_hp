from django.urls import path
from . import views

app_name = 'pages'

urlpatterns = [
    path('index/', views.index, name='index'),
    path('dtl/', views.dtl, name='dtl'),
    path('question/', views.question, name='question'),
    path('answer/', views.answer, name='answer'),
    path('lotto/', views.lotto, name='lotto'),
    path('dinner/<str:menu>/<int:number>', views.dinner, name='dinner'),
]
