from django.contrib import admin
from .models import Invoice, InvoiceDetail

class InvoiceDetailInline(admin.TabularInline):
    model = InvoiceDetail
    extra = 1

class InvoiceAdmin(admin.ModelAdmin):
    inlines = [InvoiceDetailInline]

admin.site.register(Invoice, InvoiceAdmin)
