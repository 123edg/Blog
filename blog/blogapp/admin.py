from django.contrib import admin
from blogapp.models import Sort,Tages,Article,Comment,Contact,User
# Register your models here.
class BaseModelAdmin(admin.ModelAdmin):
    def __str__(self):
        return self.name
admin.site.register(Sort,BaseModelAdmin)
admin.site.register(Tages,BaseModelAdmin)
admin.site.register(Article)
admin.site.register(Comment)
admin.site.register(Contact)
admin.site.register(User)
class NewsAdmin(admin.ModelAdmin):
    class Media:
        js = ('/js/tinymce/tinymce.min.js', '/js/textareas.js')