from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.APIRootView = views.ExamplePluginRootView

router.register(r"animals", views.AnimalViewSet)

app_name = "netbox_example_plugin-api"
urlpatterns = router.urls