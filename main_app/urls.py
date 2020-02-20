from django.urls import path
from django.conf.urls import url
# from django.views.generic import TemplateView
# from .views import HomePageView
# from .views import CreateGameView
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.show, name = 'home'),
    # path('', HomePageView.as_view(), name='home'),
    # path('add_game/', CreateGameView.as_view(), name='add_game')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
