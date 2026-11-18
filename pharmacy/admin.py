from django.contrib import admin
from .models import Category, Manufacturer, Supplier, Medicine, Component, Employee, Order, Prescription

admin.site.register(Category)
admin.site.register(Manufacturer)
admin.site.register(Supplier)
admin.site.register(Medicine)
admin.site.register(Component)
admin.site.register(Employee)
admin.site.register(Order)
admin.site.register(Prescription)