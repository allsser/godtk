from django.db import models
from django.conf import settings

class Hashtag(models.Model):
  tag = models.TextField(unique=True)

  # 객체 표현 방식
  def __str__(self):
    return self.tag 

class Godtk(models.Model):
  company_name = models.CharField(max_length=40, blank=True)   # 업체이름
  event_title = models.CharField(max_length=40)                # 행사 타이틀
  start_date = models.TextField(null=True, blank=True)         # 행사 시작 날짜
  end_date = models.TextField(null=True, blank=True)           # 행사 끝나는 날짜
  content = models.TextField(null=True, blank=True)            # 행사 소개
  event_url = models.TextField(null=True, blank=True)          # 행사 url
  img_path = models.ImageField(blank=True)                     # 행사 이미지
  tag = models.TextField(null=True, blank=True)                # 태그

  hashtag = models.ManyToManyField(Hashtag, blank=True)        # 해시태그

  def __str__(self):
    return f'[{self.pk}] {self.event_title}|{self.content}'
