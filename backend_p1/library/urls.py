from . import views
from django.urls import path
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', RedirectView.as_view(url='home/', permanent=True)), #redirect home page to new page
    path('home/', views.home),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
