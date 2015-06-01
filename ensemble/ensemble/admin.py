from django.contrib import admin
from .models import *

class WorkScoreInline(admin.TabularInline):
    model = Score
    extra = 1

class WorkComposerInline(admin.TabularInline):
    model = WorkComposer
    extra = 1

class WorkArrangerInline(admin.TabularInline):
    model = WorkArranger
    extra = 1

class WorkPlayerInline(admin.TabularInline):
    model = Player
    extra = 8

class WorkMusicCategoryInline(admin.TabularInline):
    model = WorkMusicCategory
    extra = 1

class WorkMovementInline(admin.TabularInline):
    model = Movement
    extra = 1

class WorkAdmin(admin.ModelAdmin):
    list_display = ('title', 'title_jp')
    inlines = [WorkMusicCategoryInline,
               WorkMovementInline,
               WorkScoreInline,
               WorkComposerInline,
               WorkArrangerInline,
               WorkPlayerInline]

class CDTrackInline(admin.TabularInline):
    model = Track
    extra = 10

class CDAdmin(admin.ModelAdmin):
    inlines = [CDTrackInline]

admin.site.register(Work, WorkAdmin)
admin.site.register(Writer)
admin.site.register(MusicCategory)
admin.site.register(InstrumentType)
admin.site.register(Instrument)
admin.site.register(CD, CDAdmin)
admin.site.register(Publisher)
