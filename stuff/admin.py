from django.contrib import admin
from .models import Feature, Value, FeatureValue

# Register your models here.
admin.site.register(Feature)
admin.site.register(Value)
admin.site.register(FeatureValue)