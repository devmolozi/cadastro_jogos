from django.contrib import admin
from django.urls import path
from games import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Home.as_view(), name='home'),
    path('new/game/', views.NewGame.as_view(), name='new-game'),
    path('update/<int:pk>/', views.GameUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', views.GameDeleteView.as_view(), name='delete'),

]
