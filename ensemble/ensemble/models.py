from django.db import models

CHAR_FIELD_MAX_LEN = 1024
URL_FIELD_MAX_LEN = 10000

class Writer(models.Model):
    name = models.CharField(max_length=CHAR_FIELD_MAX_LEN)
    name_jp = models.CharField(max_length=CHAR_FIELD_MAX_LEN)

class Work(models.Model):
    title = models.CharField(max_length=CHAR_FIELD_MAX_LEN)
    title_jp = models.CharField(max_length=CHAR_FIELD_MAX_LEN)
    composer = models.ForeignKey(Writer, related_name="work_composers")
    arranger = models.ForeignKey(Writer, related_name="work_arrangers", null=True)
    time = models.IntegerField()
    parent = models.ForeignKey('self', null=True)
    order = models.IntegerField()

class MusicCategory(models.Model):
    name = models.CharField(max_length=CHAR_FIELD_MAX_LEN)
    name_jp = models.CharField(max_length=CHAR_FIELD_MAX_LEN)

class InstrumentType(models.Model):
    name = models.CharField(max_length=CHAR_FIELD_MAX_LEN)
    name_jp = models.CharField(max_length=CHAR_FIELD_MAX_LEN)

class Instrument(models.Model):
    name = models.CharField(max_length=CHAR_FIELD_MAX_LEN)
    name_jp = models.CharField(max_length=CHAR_FIELD_MAX_LEN)
    instrument_type = models.ForeignKey(InstrumentType)
    number = models.IntegerField()

class Player(models.Model):
    work = models.ForeignKey(Work, unique=True)
    order = models.IntegerField(primary_key=True)
    instrument = models.ForeignKey(Instrument, unique=True)

class CD(models.Model):
    title = models.CharField(max_length=CHAR_FIELD_MAX_LEN)
    title_jp = models.CharField(max_length=CHAR_FIELD_MAX_LEN)
    amazon_url = models.URLField(max_length=URL_FIELD_MAX_LEN)

class Track(models.Model):
    CD = models.ForeignKey(CD)
    order = models.IntegerField()
    work = models.ForeignKey(Work, null=True)
    title = models.CharField(max_length=CHAR_FIELD_MAX_LEN)
    title_jp = models.CharField(max_length=CHAR_FIELD_MAX_LEN)
    composer_name = models.CharField(max_length=CHAR_FIELD_MAX_LEN)
    composer_name_jp = models.CharField(max_length=CHAR_FIELD_MAX_LEN)
    arranger_name = models.CharField(max_length=CHAR_FIELD_MAX_LEN)
    arranger_name_jp = models.CharField(max_length=CHAR_FIELD_MAX_LEN)


