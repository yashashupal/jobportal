from django.urls import path
from job import views
from django.contrib.auth import views as auth_views 
urlpatterns = [
    path('',views.index,name='index'),
    path('contact/',views.contact,name='contact'),
    path('about/',views.about,name='about'),
    path('myaccount/',views.myaccount,name='myaccount'),
    path('category/',views.category,name='category'),
    path('404/',views.eror,name='404'),
    path('job-detail/<int:id>/',views.job_detail,name='job-detail'),
    path('updatejob/<int:id>/',views.updatejob,name='updatejob'),
    
    # path('job-detail1/',views.job_detail1,name='job-detail1'),
    path('job-list/',views.job_list,name='job-list'),
    path('testimonial/',views.testimonial,name='testimonial'),
    path('userlogin/',views.userlogin,name='userlogin'),
    path('ragister/',views.ragister,name='ragister'),
    path('logout/',views.Logout,name='logout'),
    path('header/',views.header,name='header'),
    path('internship/',views.internship,name='internship'),
    path('applicationjob/',views.applicationjob,name='applicationjob'),
    path('postjob/',views.postjob,name='postjob'),
    path('clinteragister/',views.clinteragister1,name='clinteragister'),
    path('heade1/',views.heade1,name='heade1'),
    # path('changepassword/<token>/',views.changepassword,name='changepassword'),
    # path('forgetpass/',views.forgetpass,name='forgetpass'),

    
     path('delete_post/<int:id>/',views.delete_post),


    path('password_reset/',auth_views.PasswordResetView.as_view(),name='password_reset'),

    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),

    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),

    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),







    
    path('postdashboard1/',views.postdashboard1,name='postdashboard1'),
    path('postdashboard2/',views.postdashboard2,name='postdashboard2'),
    path('postjob/',views.postdashboard3,name='postdashboard3'),
    path('postdashboard4/',views.postdashboard4,name='postdashboard4'),
    path('postdashboard5/',views.postdashboard5,name='postdashboard5'),
    path('postdashboard6/',views.postdashboard6,name='postdashboard6'),
]
