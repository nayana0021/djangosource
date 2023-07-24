from django.db import models

"""
photo 앱에서 사용할 테이블 정의
클래스로 정의 - ORM(클래스 == 테이블)
python manage.py makemigrations(class 파일 => sql 코드로 변환)
python manage.py migrate (sql 코드 변환 => 테이블 생성)
"""

class Photo(models.Model):
    """
    create table photo(
        title varchar2(20) not null,
    ) 이 코드와 동일한 작업을 하는것임

    pk 에 해당하는 컬럼은 자동으로 생성
    not null 컬럼으로 생성됨(기본적으로)
    """
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    image = models.CharField(max_length=200)
    description = models.TextField()
    price = models.IntegerField()