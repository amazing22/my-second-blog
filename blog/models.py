# 블로그 글 모델 설정하기.
# from, import로 시작하는 부분은 다른 파일에 있는 것을 추가하라는 뜻
from django.db import models
from django.utils import timezone

# 모델을 정의하는 코드
# 모델 = 객체(object)
# class는 객체를 정의한다,
# post는 모델의 이름
# models는 post가 장고 모델임을 의미한다. -> 장고는 post가 데이터베이스에 저장되어야 한다고 알려됨
# models.CharField - 글자 수가 제한된 텍스트를 정의할 때 사용.(글 제목같이 짧은 문자열 정보를 저장할 때 사용)
# models.TextField - 글자 수에 제한이 없는 긴 텍스트를 위한 속성, 블로그 콘텐츠를 담기좋다.
# models.DateTimeField - 날짜와 시간을 의미한다.
# models.ForeignKey - 다른 모델에 대한 링크 의미
class Post(models.Model): # class Post(models.Model) : 부모 클래스
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
