from rest_framework import serializers

from franchise.models import Panchayat
from franchise.models import Ward


class PanchayatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Panchayat
        fields = [
            "name",
            "id",
        ]


class BlockSerializer(serializers.ModelSerializer):
    franchise_status = serializers.CharField(source="get_franchise_status_display")

    class Meta:
        model = Ward
        fields = [
            "name",
            "id",
            "franchise_status"
        ]
