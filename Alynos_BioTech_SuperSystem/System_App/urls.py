from django.urls import path

from . import views


app_name = "BioTech_App"

urlpatterns = [

    path('', views.index, name="index"),
    path('about/', views.about, name="about"),
    path('appointment/', views.appointment, name="appointment"),
    path('appointment_view/', views.appointment_view, name="appointment_view"),
    path('blog_sidebar/', views.blog_sidebar, name="blog_sidebar"),
    path('blog_single/<int:blog_id>/', views.blog_single, name="blog_single"),
    path('confirmation/', views.confirmation, name="confirmation"),
    path('department/', views.department, name="department"),
    path('department_single/<int:department_id>/', views.department_single, name="department_single"),
    path('doctor/', views.doctor, name="doctor"),
    path('doctor_single/<int:doctor_id>/', views.doctor_single, name="doctor_single"),
    path('contact/', views.contact, name="contact"),
    path('products/', views.product_list, name="product_list"),
    path('product_detail/<int:product_id>/', views.product_detail, name="product_detail"),
    path('view_cart/', views.view_cart, name='view_cart'),
    path('add_cart/<int:product_id>/', views.add_cart, name='add_cart'),
    path('remove_from_cart/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('payment/', views.payment_process, name='payment'),
    path('payment_page/', views.payment_page, name='payment_page'),
    path('payment_success/', views.payment_success, name='payment_success'),
    path('payment_failed/', views.payment_failed, name='payment_failed'),
    path('submit_message/', views.submit_message, name='submit_message'),
    path('message_confirmation', views.message_confirmation, name='message_confirmation')
    ]