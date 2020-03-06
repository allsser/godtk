from django import template

register = template.Library()

@register.filter
def hashtag_link(godtk):
  tag = godtk.tag + ' '
  hashtag = godtk.hashtag.all()

  for hashtag in hashtag:
    tag = tag.replace(
      hashtag.tag + ' ',
      f'<a href="/godtk/{hashtag.pk}/hashtag/">{hashtag.tag}</a> '
    )
  return tag