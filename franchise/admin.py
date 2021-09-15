from django.contrib import admin

from franchise.models import Block
from franchise.models import Franchise
from franchise.models import Panchayat

admin.site.register(Panchayat)
admin.site.register(Block)
admin.site.register(Franchise)
