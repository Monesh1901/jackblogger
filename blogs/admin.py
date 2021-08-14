from detail.views import blog
from django.contrib import admin
from .models import Images, Info
from .models import Blog
from .models import Comment
from .models import Images
admin.site.register(Info)
admin.site.register(Blog)
admin.site.register(Comment)
admin.site.register(Images)

