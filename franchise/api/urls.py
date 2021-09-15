from django.urls import path

from franchise.api.views import BlockListAPIView
from franchise.api.views import FranchiseListAPIView
from franchise.api.views import PanchayatListAPIView

urlpatterns = [
    path('panchayat/', PanchayatListAPIView.as_view()),
    path('block/', BlockListAPIView.as_view()),
    path('franchise/', FranchiseListAPIView.as_view()),
]
