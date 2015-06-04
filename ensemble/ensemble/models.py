from django.db import models

CHAR_FIELD_MAX_LEN = 1024
URL_FIELD_MAX_LEN = 10000

class Writer(models.Model):
    name = models.CharField(max_length=CHAR_FIELD_MAX_LEN)
    name_reading = models.CharField(max_length=CHAR_FIELD_MAX_LEN)
    name_jp = models.CharField(max_length=CHAR_FIELD_MAX_LEN)
    name_jp_reading = models.CharField(max_length=CHAR_FIELD_MAX_LEN)

    def __unicode__(self):
        return self.name_jp

class Work(models.Model):
    title = models.CharField(max_length=CHAR_FIELD_MAX_LEN)
    title_jp = models.CharField(max_length=CHAR_FIELD_MAX_LEN, blank=True)
    short_title = models.CharField(max_length=CHAR_FIELD_MAX_LEN, blank=True)
    short_title_jp = models.CharField(max_length=CHAR_FIELD_MAX_LEN, blank=True)
    short_title_jp_reading = models.CharField(max_length=CHAR_FIELD_MAX_LEN, blank=True)

    time_minute = models.IntegerField(null=True, blank=True)
    time_second = models.IntegerField(null=True, blank=True)

    def __unicode__(self):
        return self.title_jp

class Movement(models.Model):
    work = models.ForeignKey(Work)
    order = models.IntegerField()
    title = models.CharField(max_length=CHAR_FIELD_MAX_LEN)
    title_jp = models.CharField(max_length=CHAR_FIELD_MAX_LEN, default="")

    time_minute = models.IntegerField(null=True, blank=True)
    time_second = models.IntegerField(null=True, blank=True)

    def __unicode__(self):
        return self.title_jp

class Publisher(models.Model):
    name = models.CharField(max_length=CHAR_FIELD_MAX_LEN)
    name_jp = models.CharField(max_length=CHAR_FIELD_MAX_LEN)
    url = models.URLField(max_length=URL_FIELD_MAX_LEN)

    def __unicode__(self):
        return self.name_jp

class Score(models.Model):
    work = models.ForeignKey(Work)
    publisher = models.ForeignKey(Publisher)
    asin = models.CharField(max_length=10, blank=True)

class WorkComposer(models.Model):
    work = models.ForeignKey(Work)
    composer = models.ForeignKey(Writer)

class WorkArranger(models.Model):
    work = models.ForeignKey(Work)
    arranger = models.ForeignKey(Writer)

class MusicCategory(models.Model):
    name = models.CharField(max_length=CHAR_FIELD_MAX_LEN)
    name_jp = models.CharField(max_length=CHAR_FIELD_MAX_LEN)
    parent = models.ForeignKey('self', null=True, blank=True)
    number = models.IntegerField(null=True, blank=True)

    def __unicode__(self):
        return self.name_jp

class WorkMusicCategory(models.Model):
    work = models.ForeignKey(Work)
    music_category = models.ForeignKey(MusicCategory)

class InstrumentType(models.Model):
    name = models.CharField(max_length=CHAR_FIELD_MAX_LEN)
    name_jp = models.CharField(max_length=CHAR_FIELD_MAX_LEN)

    def __unicode__(self):
        return self.name_jp

class Instrument(models.Model):
    name = models.CharField(max_length=CHAR_FIELD_MAX_LEN)
    short_name = models.CharField(max_length=CHAR_FIELD_MAX_LEN, blank=True)
    name_jp = models.CharField(max_length=CHAR_FIELD_MAX_LEN)
    instrument_type = models.ForeignKey(InstrumentType)

    def __unicode__(self):
        return self.name_jp

class Player(models.Model):
    work = models.ForeignKey(Work)
    order = models.IntegerField(null=True, blank=True)

    def __unicode__(self):
        return unicode(self.work) + ":" + unicode(self.order)
    class Meta:
        unique_together=(("work", "order"))

class PlayerInstrument(models.Model):
    player = models.ForeignKey(Player)
    instrument = models.ForeignKey(Instrument)
    override_description = models.CharField(max_length=CHAR_FIELD_MAX_LEN, blank=True)
    number = models.IntegerField(default=1)

class CD(models.Model):
    title = models.CharField(max_length=CHAR_FIELD_MAX_LEN)
    title_jp = models.CharField(max_length=CHAR_FIELD_MAX_LEN)
    asin = models.CharField(max_length=10, blank=True)
    release = models.DateField(null=True, blank=True)

    def __unicode__(self):
        return self.title

class Track(models.Model):
    CD = models.ForeignKey(CD)
    order = models.IntegerField()
    work = models.ForeignKey(Work, null=True, blank=True)
    title = models.CharField(max_length=CHAR_FIELD_MAX_LEN, blank=True)
    title_jp = models.CharField(max_length=CHAR_FIELD_MAX_LEN, blank=True)
    composer_name = models.CharField(max_length=CHAR_FIELD_MAX_LEN, blank=True)
    composer_name_jp = models.CharField(max_length=CHAR_FIELD_MAX_LEN, blank=True)
    arranger_name = models.CharField(max_length=CHAR_FIELD_MAX_LEN, blank=True)
    arranger_name_jp = models.CharField(max_length=CHAR_FIELD_MAX_LEN, blank=True)

    def __unicode__(self):
        return unicode(self.CD) + ":" + unicode(self.order)


