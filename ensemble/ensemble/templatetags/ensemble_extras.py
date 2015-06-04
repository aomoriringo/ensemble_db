from django import template

register = template.Library()

def get_field_val_set(objects, field):
    field_list = field.split(".")
    objs = objects
    for field in field_list:
        objs = [getattr(o, field, '') for o in objs]
    return objs

@register.simple_tag
def obj_join(objects, s, field):
    field_list = field.split(".")
    objs = objects
    for field in field_list:
        objs = [getattr(o, field, '') for o in objs]
    return s.join(objs)

@register.inclusion_tag('parts/obj_join_with_link.html')
def obj_join_with_link(objects, separater, field, link_field, linkname):
    vals = get_field_val_set(objects, field)
    links = get_field_val_set(objects, link_field)

    obj_data = []
    for val, link in zip(vals, links):
        obj_data.append({'val': val,
                         'link': link})
    print(obj_data)
    return {'objects': obj_data,
            'separater': separater,
            'linkname': linkname}

@register.inclusion_tag('parts/work_table.html')
def work_table(works, field=''):
    if field:
        works = get_field_val_set(works, field)
    return {'works': works}

@register.inclusion_tag('parts/writer_table.html')
def writer_table(writers, field=''):
    return {'writers': writers}


