"""TranscriptWebsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.static import serve
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from rest_framework.urlpatterns import format_suffix_patterns
from user.api import UserListView, PurchaseListView, ProductList, LoginList, UserAuthentication,Getting_Started_SectionList,Getting_Started_Affiliate_LinkListView,Model_Content_Affiliate_LinkListView,Model_Content_SectionList,Customize_Content_SectionList,Customize_Content_Affiliate_LinkListView,Publish_Affiliate_LinkListView,Publish_SectionList,Resources_Affiliate_LinkListView,Resources_SectionList
urlpatterns = [
    path('', include('home.urls')),
    path('user/', include('user.urls')),
    path('payment/', include('payments.urls')),
    path('password-reset/',
         auth_views.PasswordResetView.as_view(template_name='password_reset.html'), name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),
    path('api/user/', UserListView.as_view(), name='user_api'),
    url(r'api/auth/$', UserAuthentication.as_view(),
        name='User_Authentication_API'),
    url(r'^api/login/(?P<user_id>\d+)/$', LoginList.as_view(), name='login_api'),
    path('api/purchase/', PurchaseListView.as_view()),
    path('api/product/', ProductList.as_view()),
    path('api/getting_started_section/', Getting_Started_SectionList.as_view()),
    path('api/getting_started_affiliate_link/', Getting_Started_Affiliate_LinkListView.as_view()),
    path('api/model_content_section/', Model_Content_SectionList.as_view()),
    path('api/model_content_affiliate_link/', Model_Content_Affiliate_LinkListView.as_view()),
    path('api/customize_content_section/', Customize_Content_SectionList.as_view()),
    path('api/customize_content_affiliate_link/', Customize_Content_Affiliate_LinkListView.as_view()),
    path('api/publish_section/', Publish_SectionList.as_view()),
    path('api/publish_affiliate_link/', Publish_Affiliate_LinkListView.as_view()),
    path('api/resources_section/', Resources_SectionList.as_view()),
    path('api/resources_affiliate_link/', Resources_Affiliate_LinkListView.as_view()),
    url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG==False:
    handler404 = 'user.views.handler404'
    handler500 = 'user.views.handler500'
    handler400 = 'user.views.handler400'
    handler403 = 'user.views.handler403'