from rest_framework.generics import ListAPIView

from franchise.api.serializers import BlockSerializer
from franchise.api.serializers import PanchayatSerializer
from franchise.models import Panchayat
from franchise.models import Ward


class PanchayatListAPIView(ListAPIView):
    permission_classes = ()
    serializer_class = PanchayatSerializer
    queryset = Panchayat.objects.all()


class BlockListAPIView(ListAPIView):
    permission_classes = ()
    serializer_class = BlockSerializer
    queryset = Ward.objects.all()
    filterset_fields = ['panchayat']
