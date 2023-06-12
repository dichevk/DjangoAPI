from django.urls import path
from django.contrib import admin
from views.viewsets.item_viewset import ItemViewSet, OrderViewSet
from views.contact_view import ContactAPIView
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token


router = routers.DefaultRouter()
router.register(r'item', ItemViewSet, basename='item')
router.register(r'order', OrderViewSet, basename='order')

urlpatterns = router.urls

urlpatterns += [
    path('admin/', admin.site.urls),
    path('contact/', ContactAPIView.as_view()),
    path('api-token-auth/', obtain_auth_token),
]