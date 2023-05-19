from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('signup/',views.signup,name='signup'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('profile/',views.profile,name='profile'),
    path('forgot-password/',views.forgot_password,name='forgot-password'),
    path('verify-otp/',views.verify_otp,name="verify-otp"),
    path('new-password/',views.new_password,name='new-password'),
    path('notice/',views.notice,name='notice'),
    path('notice-view/',views.notice_view,name='notice-view'),
    path('chairmanhome/',views.chairmanhome,name='chairmanhome'),
    path('edit-notice/',views.edit_notice,name='edit-notice'),
    path('add-event/',views.add_event,name='add-event'),
    path('event-view/',views.event_view,name='event-view'),
]