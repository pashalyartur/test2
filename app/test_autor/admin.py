from django.contrib import admin
from .models import Result,Test,Question,Answer, CorrectAnswer


admin.site.register(Result)
admin.site.register(Test)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(CorrectAnswer)
