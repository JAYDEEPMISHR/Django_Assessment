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
    
    # Chairman 
    path('chairmanhome/',views.chairmanhome,name='chairmanhome'),
    path('chairmanprofile/',views.chairmanprofile,name='chairmanprofile'),
    path('chairmancomplain/',views.chairmancomplain,name='chairmancomplain'),
    path('chairmanseecomplain/',views.chairmanseecomplain,name='chairmanseecomplain'),
    path('edit-notice/<int:pk>',views.edit_notice,name='edit-notice'),
    path('add-event/',views.add_event,name='add-event'),
    path('event-view/',views.event_view,name='event-view'),
    path('delete/<int:pk>/',views.delete,name='delete'),
    path('delete-notice/<int:pk>/',views.delete_notice,name='delete-notice'),
    path('society-members/',views.society_members,name='society-members'),
    path('pdf/',views.pdf,name='pdf'),
    path('maintainance-amount/',views.maintainance_amount,name='maintainance-amount'),
    #path('edit-amount/',views.edit_amount,name='edit-amount'),

    # Watchman
    path('visitor/',views.visitor,name='visitor'),
    path('watchmanhome/',views.watchmanhome,name='watchmanhome'),
    path('event-view-watchman/',views.event_view_watchman,name='event-view-watchman'),
    path('notice-view/',views.notice_view,name='notice-view'),
    path('notice-view-watchman/',views.notice_view_watchman,name='notice-view-watchman'),
    path('watchmanprofile/',views.watchmanprofile,name='watchmanprofile'),
    path('complain/',views.complain,name='complain'),
    path('view-complain-watchman/',views.view_complain_watchman,name='view-complain-watchman'),
    path('complete-task/',views.complete_task,name='complete-task'),

    # Society Member
    path('member-list/',views.member_list,name='member-list'),
    path('member-profile/',views.member_profile,name='member-profile'),
    path('watchman-details/',views.watchman_details,name='watchman-details'),
    path('raise-complain/',views.raise_complain,name='raise-complain'),
    path('membercomplain/',views.membercomplain,name='membercomplain'),
]