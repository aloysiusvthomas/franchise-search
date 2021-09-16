from django.contrib import admin

from franchise.models import Ward
from franchise.models import Panchayat

admin.site.register(Panchayat)
admin.site.register(Ward)
