from django.contrib import admin
from job.models import studentuser,userpost,clinteragister,userpostreplay,news


admin.site.site_header="InternSpire job"
# Register your models here.
admin.site.register(studentuser)
admin.site.register(userpost)
admin.site.register(clinteragister)
admin.site.register(userpostreplay)


class news_admin(admin.ModelAdmin):
    list_display=('news_title','news_dec')
    
admin.site.register(news,news_admin)
