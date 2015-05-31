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
    title_jp_reading = models.CharField(max_length=CHAR_FIELD_MAX_LEN, blank=True)
    subtitle = models.CharField(max_length=CHAR_FIELD_MAX_LEN, blank=True)
    subtitle_jp = models.CharField(max_length=CHAR_FIELD_MAX_LEN, blank=True)
    time = models.IntegerField(null=True, blank=True)
    parent = models.ForeignKey('self', null=True, blank=True)
    order = models.IntegerField(null=True, blank=True)

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
    pubulisher = models.ForeignKey(Publisher)
    amazon_url = models.URLField(max_length=URL_FIELD_MAX_LEN)

class WorkComposer(models.Model):
    work = models.ForeignKey(Work)
    composer = models.ForeignKey(Writer)

class WorkArranger(models.Model):
    work = models.ForeignKey(Work)
    arranger = models.ForeignKey(Writer)

class MusicCategory(models.Model):
    name = models.CharField(max_length=CHAR_FIELD_MAX_LEN)
    name_jp = models.CharField(max_length=CHAR_FIELD_MAX_LEN)

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
    name_jp = models.CharField(max_length=CHAR_FIELD_MAX_LEN)
    instrument_type = models.ForeignKey(InstrumentType)

    def __unicode__(self):
        return self.name_jp

class Player(models.Model):
    work = models.ForeignKey(Work)
    order = models.IntegerField()
    instrument = models.ForeignKey(Instrument)
    number = models.IntegerField()

    def __unicode__(self):
        return unicode(self.work) + ":" + unicode(self.order)
    class Meta:
        unique_together=(("work", "order", "instrument"))

class CD(models.Model):
    title = models.CharField(max_length=CHAR_FIELD_MAX_LEN)
    title_jp = models.CharField(max_length=CHAR_FIELD_MAX_LEN)
    amazon_url = models.URLField(max_length=URL_FIELD_MAX_LEN)
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


