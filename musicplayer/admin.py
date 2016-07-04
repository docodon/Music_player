from django.contrib import admin
from musicplayer.models import Tracks,Genre_id,Id_genre

# Register your models here.
admin.site.register(Tracks)
admin.site.register(Genre_id)
admin.site.register(Id_genre)
