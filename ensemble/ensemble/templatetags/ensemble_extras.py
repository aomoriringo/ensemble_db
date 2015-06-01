from django import template

register = template.Library()

@register.filter
def instruments(player):
    instrument_names = [str(i.instrument.name) for i in player.playerinstrument_set.all()]
    return "/".join(instrument_names)

@register.simple_tag
def obj_join(objects, s, fields):
    field_list = fields.split(".")
    objs = objects
    for field in field_list:
        objs = [getattr(o, field, '') for o in objs]
    return s.join(objs)
