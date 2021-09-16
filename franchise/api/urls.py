from django.urls import path

from franchise.api.views import BlockListAPIView
from franchise.api.views import PanchayatListAPIView

urlpatterns = [
    path('panchayat/', PanchayatListAPIView.as_view()),
    path('block/', BlockListAPIView.as_view()),
]
