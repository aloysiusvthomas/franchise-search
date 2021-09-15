from rest_framework import filters
from rest_framework.generics import ListAPIView

from franchise.api.serializers import BlockSerializer
from franchise.api.serializers import FranchiseSerializer
from franchise.api.serializers import PanchayatSerializer
from franchise.models import Ward
from franchise.models import Franchise
from franchise.models import Panchayat


class PanchayatListAPIView(ListAPIView):
    permission_classes = ()
    serializer_class = PanchayatSerializer
    queryset = Panchayat.objects.all()


class BlockListAPIView(ListAPIView):
    permission_classes = ()
    serializer_class = BlockSerializer
    queryset = Ward.objects.all()
    filterset_fields = ['panchayat']


class FranchiseListAPIView(ListAPIView):
    permission_classes = ()
    serializer_class = FranchiseSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']

    def get_queryset(self, *args, **kwargs):
        print(self.request.GET.get)
        block = self.request.GET.get("block")
        return Franchise.objects.filter(block=block)
