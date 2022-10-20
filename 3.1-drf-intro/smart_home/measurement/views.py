# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.decorators import api_view
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.response import Response

from measurement.models import Sensor, Measurement
from measurement.serializers import SensorDetailSerializer, MeasurementSerializer


# class SensorView(APIView):
#     def get(self, request):
#         sensor = Sensor.objects.all()
#         ser = SensorDetailSerializer(sensor, many=True)
#         return Response(ser.data)

class SensorView(ListCreateAPIView):
        queryset = Sensor.objects.all()
        serializer_class = SensorDetailSerializer


class MetaView(RetrieveUpdateAPIView):
        queryset = Sensor.objects.all()
        serializer_class = SensorDetailSerializer


class NewTemp(CreateAPIView):
        queryset = Measurement.objects.all()
        serializer_class = MeasurementSerializer

