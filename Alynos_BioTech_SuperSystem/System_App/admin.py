from django.contrib import admin

# Register your models here.

from .models import Doctor, DoctorDetails, Department, DepartmentDetails, Products, ProductDetail, CheckoutForm, Appointment, PaymentReport, Blog, Comment, BlogDetail, Purchase, ContactMessage

admin.site.register(Appointment)
admin.site.register(Doctor)
admin.site.register(DoctorDetails)
admin.site.register(Department)
admin.site.register(DepartmentDetails)
admin.site.register(Products)
admin.site.register(ProductDetail)
admin.site.register(PaymentReport)
admin.site.register(Blog)
admin.site.register(Comment)
admin.site.register(BlogDetail)
admin.site.register(ContactMessage)

class PurchaseInline(admin.TabularInline):
    model = Purchase
    extra = 1

class PurchaseAdmin(admin.ModelAdmin):
    list_display = ('checkout_form', 'product', 'quantity')

class CheckoutFormAdmin(admin.ModelAdmin):
    inlines = [PurchaseInline]

admin.site.register(CheckoutForm, CheckoutFormAdmin)
admin.site.register(Purchase, PurchaseAdmin)