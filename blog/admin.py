# 모델링 한 글들을 장고 관리자에서 추가, 수정, 삭제하기
from django.contrib import admin
from .models import Post


# 관리자 페이지에서 만든 모델 보기
admin.site.register(Post)
