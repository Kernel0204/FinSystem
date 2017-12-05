from analyzeViewer.models import *
from django.contrib import admin

#管理画面で管理するモデルを登録
admin.site.register(users)
admin.site.register(membertype)
admin.site.register(incomecategory)
admin.site.register(expensecategory)
admin.site.register(paidstatuse)
admin.site.register(delayornot)
admin.site.register(groups)
admin.site.register(jobtypes)