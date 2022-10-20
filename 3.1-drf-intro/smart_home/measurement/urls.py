from django.urls import path

from measurement.views import SensorView, MetaView, NewTemp

urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path('sensors/', SensorView.as_view()),
    path('sensors/<pk>', MetaView.as_view()),
    path('measurements/', NewTemp.as_view()),
]
