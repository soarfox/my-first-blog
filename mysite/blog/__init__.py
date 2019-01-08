# 引入外部程式碼
from django.db import models

# on_delete沒有使用到,但必須要寫出來否則無法跑過程式
on_delete = models.DO_NOTHING