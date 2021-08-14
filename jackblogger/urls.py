from django.contrib import admin
from django.urls import path
from detail import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    
    path('about/', views.about, name='about'),
    path('blog/', views.blog, name='blog'),
    path('comment/', views.comment, name='comment'),
    path('contact/', views.contact, name='contact'),
    path('marketing/', views.marketing, name='marketing'),
    path('base/', views.base, name='base'),
    
    #------------------------------------------------------->
    path('calendar/', views.calendar, name='calendar'),
    path('comments/', views.comments, name='comments'),
    path('charts/', views.charts, name='charts'),
    path('contact1/', views.contact1, name='contact1'),
    path('dashboard_2/', views.dashboard_2, name='dashboard_2'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('email/', views.email, name='email'),
    path('general_elements/', views.general_elements, name='general_elements'),
    path('invoice/', views.invoice, name='invoice'),
    path('icons/', views.icons, name='icons'),
    path('index1/', views.index1, name='index1'),
    path('login/', views.login, name='login'),
    path('map/', views.map, name='map'),
    path('media_gallery/', views.media_gallery, name='media_gallery'),
    path('price/', views.price, name='price'),
    path('profile/', views.profile, name='profile'),
    path('settings/', views.settings, name='settings'),

    path('blogs1/', views.blogs1,name='blogs1'),
    path('edit_blog/<int:id>',views.edit_blog, name='edit_blog'), 
    path('delete_blog/<int:id>',views.delete_blog, name='delete_blog' ),
    path('add_blog/',views.add_blog,name='add_blog'),

    path('images/', views.images,name='images'),
    path('edit_1/<int:id>',views.edit_1, name='edit_1'), 
    path('delete_1/<int:id>',views.delete_1, name='delete_1' ),
    path('add_1/',views.add_1,name='add_1'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

