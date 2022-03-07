from django.contrib import admin

# Register your models here.
from .models import *

# Register each table
admin.site.register(Bitcoin)
admin.site.register(Ethereum)
admin.site.register(Tether)
admin.site.register(Helium)
admin.site.register(Doge)
admin.site.register(Litecoin)
admin.site.register(Polkadot)
admin.site.register(Cardano)
admin.site.register(ShibaInu)
