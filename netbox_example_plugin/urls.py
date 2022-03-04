from django.http import HttpResponse
from django.urls import path
from . import views


def dummy_view(request):
    html = "<html><body>Example plugin.</body></html>"
    return HttpResponse(html)


urlpatterns = [
    path("", views.ListAnimalsView.as_view(), name="animals_list"),
    path("<int:pk>/", views.AnimalView.as_view(), name="animal"),
    path('add_animal/', views.AnimalEditView.as_view(), name='add_animal'),
]
