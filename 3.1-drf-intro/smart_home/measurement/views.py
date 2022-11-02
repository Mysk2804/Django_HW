# # TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# # TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView

from measurement.models import Sensor, Measurement
from measurement.serializers import SensorDetailSerializer, MeasurementSerializer, SensorSerializer, MeasurementUpSerializer


class SensorView(ListAPIView):
        queryset = Sensor.objects.all()
        serializer_class = SensorSerializer


class MetaView(RetrieveAPIView):
        queryset = Sensor.objects.all()
        serializer_class = SensorDetailSerializer


class NewTemp(CreateAPIView):
        queryset = Measurement.objects.all()
        serializer_class = MeasurementUpSerializer

