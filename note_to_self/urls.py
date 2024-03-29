from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.contrib.auth import views
from django.urls import path, include
from django.views.decorators.cache import cache_control
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sw.js', (TemplateView.as_view(template_name="book_manager/sw.js", content_type='application/javascript', )), name='sw.js'),
    path('', include('book_manager.urls')),
    path('accounts/login/', views.LoginView.as_view(), name='login'),
    path('accounts/logout/', views.LogoutView.as_view(next_page='/'), name='logout'),
    path('mdeditor/', include('mdeditor.urls')),
]

urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)