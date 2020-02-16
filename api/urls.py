from rest_framework import routers
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from baner.views import BanerViewSet
from live_camers.views import LiveCamersViewSet,LiveCamersCountryViewSet,CountryViewSet
from news.views import NewsViewSet,CategoryNewsViewSet,NewsFromCategoryViewSet

router = routers.DefaultRouter()
router.register(r'baner', BanerViewSet)
router.register(r'live_camers', LiveCamersViewSet)
router.register(r'live_camers_country', LiveCamersCountryViewSet)
router.register(r'country', CountryViewSet)
router.register(r'news', NewsViewSet)
router.register(r'category_news', CategoryNewsViewSet)
router.register(r'news_from_category', NewsFromCategoryViewSet)
urlpatterns = [
    path('', include(router.urls)),
]\
               + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)\
               + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
