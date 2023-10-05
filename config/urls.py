from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static

from home.views import home, portfolio_details
from blog.views import blog, blog_single

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", home),
    path("portfolio-details/<int:id>/", portfolio_details),
    path("blog/", blog),
    path("blog-single/<int:id>/", blog_single)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
