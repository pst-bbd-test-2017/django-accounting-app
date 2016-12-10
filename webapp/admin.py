from django.contrib import admin
from webapp.models import Partner, Invoice, InvoiceLine, Product, Tax
# Register your models here.

admin.site.register(Partner)
admin.site.register(Invoice)
admin.site.register(InvoiceLine)
admin.site.register(Product)
admin.site.register(Tax)