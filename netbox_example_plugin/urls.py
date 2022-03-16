from django.urls import path
from . import views

app_name = 'netbox_example_plugin'

urlpatterns = [
    path("", views.ListAnimalsView.as_view(), name="animal_list"),
    path("<int:pk>/", views.AnimalView.as_view(), name="animal"),
    path('add_animal/', views.AnimalEditView.as_view(), name='add_animal'),
    path("<int:pk>/edit/", views.AnimalEditView.as_view(), name="animal_edit"),
    path("animal_bulk_edit/", views.AnimalBulkEditView.as_view(), name="animal_bulk_edit"),
    path("annimal_bulk_delete/", views.AnimalBulkDeleteView.as_view(), name="animal_bulk_delete"),
    path('<int:pk>/delete/', views.AnimalDeleteView.as_view(), name='animal_delete'),
    path('import_animals/', views.AnimalBulkImportView.as_view(), name='import_animals'),
    path('free_animals/', views.free_animals, name='free_animals'),
    path('busy_animals/', views.busy_animals, name='busy_animals'),
]
