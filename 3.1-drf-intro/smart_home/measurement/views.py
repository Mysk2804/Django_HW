# # TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# # TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.generics import CreateAPIView, ListCreateAPIView, RetrieveUpdateAPIView

from measurement.models import Sensor, Measurement
from measurement.serializers import SensorDetailSerializer, SensorSerializer, MeasurementUpSerializer


class SensorView(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class MetaView(RetrieveUpdateAPIView):
    # queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer

    def get_queryset(self):
        return Sensor.objects.all()


class NewTemp(CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementUpSerializer

