from django.contrib.admin import TabularInline, StackedInline, ModelAdmin, site
from super_inlines.admin import SuperInlineModelAdmin, SuperModelAdmin

from .models import *

class PlayerInstrumentInline(SuperInlineModelAdmin, TabularInline):
    model = PlayerInstrument
    extra = 1

class WorkScoreShopInline(SuperInlineModelAdmin, TabularInline):
    model = ScoreShop
    extra = 1

class WorkComposerInline(SuperInlineModelAdmin, TabularInline):
    model = WorkComposer
    extra = 1

class WorkArrangerInline(SuperInlineModelAdmin, TabularInline):
    model = WorkArranger
    extra = 1

class WorkPlayerInline(SuperInlineModelAdmin, StackedInline):
    model = Player
    extra = 1
    inlines = [PlayerInstrumentInline]

class WorkMusicCategoryInline(SuperInlineModelAdmin, TabularInline):
    model = WorkMusicCategory
    extra = 1

class WorkMovementInline(SuperInlineModelAdmin, TabularInline):
    model = Movement
    extra = 1

class WorkAdmin(SuperModelAdmin):
    list_display = ('title', 'title_jp')
    inlines = [WorkMusicCategoryInline,
               WorkMovementInline,
               WorkScoreShopInline,
               WorkComposerInline,
               WorkArrangerInline,
               WorkPlayerInline]

class CDShopInline(SuperInlineModelAdmin, TabularInline):
    model = CDShop
    extra = 1

class CDTrackInline(SuperInlineModelAdmin, TabularInline):
    model = Track
    extra = 10

class CDAdmin(SuperModelAdmin):
    inlines = [CDTrackInline]

site.register(Work, WorkAdmin)
site.register(Writer)
site.register(MusicCategory)
site.register(InstrumentType)
site.register(Instrument)
site.register(CD, CDAdmin)
site.register(Publisher)
site.register(Shop)
