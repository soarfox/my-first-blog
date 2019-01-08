# 引入外部程式碼
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.conf import settings

# model名稱為Post, 可以隨意命名但永遠是字首大寫
# models.Model意指此為一個Django的Model, 藉此讓Django知道日後要將此Model的資料存入資料庫內
# 定義所需用的各種資料型態如下
# models.CharField為有上限的字元
# models.TextField為無上限的字串
# models.ateTimeField為為日期與時間
# models.ForeignKey為與其他Model的關聯
class Post(models.Model):
	
    # author = models.ForeignKey(User, on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

# def後續定義的東西是方法, 亦可稱為函數, 故下方publish是一個方法(即一個函數)
# 通常方法通常會return一些東西, 故__str__此方法中,將會取得一個網誌標題的一個字串(string)
    def publish(self):
    	self.published_date = timezone.now()
    	self.save()
    def __str__(self):
    	return self.title


