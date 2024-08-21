from django.urls import path
from .views import SensorListCreateView, SensorRetrieveUpdateView, SensorDetailView, MeasurementListCreateView

urlpatterns = [
    path('sensors/', SensorListCreateView.as_view(), name='sensor-list-create'),
    path('sensors/<pk>/', SensorRetrieveUpdateView.as_view(), name='sensor-retrieve-update'),
    path('sensors/<pk>/detail/', SensorDetailView.as_view(), name='sensor-detail'),
    path('measurements/', MeasurementListCreateView.as_view(), name='measurement-list-create'),
]
