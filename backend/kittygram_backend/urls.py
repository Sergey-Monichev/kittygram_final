from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from cats.views import AchievementViewSet, CatViewSet

router = routers.DefaultRouter()
router.register(r'cats', CatViewSet)
router.register(r'achievements', AchievementViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),  # Основные эндпоинты
    path('api/auth/', include('djoser.urls')),  # Работа с пользователями и токенами
    path('api/auth/token/', include('djoser.urls.authtoken')),  # Работа с токенами отдельно
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
