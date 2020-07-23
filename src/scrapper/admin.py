from django.contrib import admin
from .models import City
from .models import Language
from .models import Jobs
from .models import Error
# Register your models here.
admin.site.register(City)
admin.site.register(Language)
admin.site.register(Jobs)
admin.site.register(Error)
