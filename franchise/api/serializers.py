from rest_framework import serializers

from franchise.models import Ward
from franchise.models import Franchise
from franchise.models import Panchayat


class PanchayatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Panchayat
        fields = [
            "name",
            "id",
        ]


class BlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ward
        fields = [
            "name",
            "id"
        ]


class FranchiseSerializer(serializers.ModelSerializer):
    status = serializers.CharField(source="get_status_display")

    class Meta:
        model = Franchise
        fields = [
            "name",
            "id",
            "status",
        ]
