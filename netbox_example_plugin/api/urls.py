from rest_framework import routers
from . import views

router = routers.DefaultRouter()

router.register('animals', views.AnimalViewSet)

urlpatterns = router.urls