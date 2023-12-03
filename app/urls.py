from django.contrib import admin
from django.urls import path
from games import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Home.as_view(), name='home'),
    path('new/game/', views.NewGame.as_view(), name='new-game'),
    path('game/<int:pk>/', views.GameDetailView.as_view(), name='view'),
    path('update/<int:pk>/', views.GameUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', views.GameDeleteView.as_view(), name='delete'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
