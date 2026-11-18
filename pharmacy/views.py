from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Medicine, Component, Order, Employee, Prescription

# 1. ЛЕКАРСТВА (Medicine)
class MedicineListView(ListView):
    model = Medicine
    template_name = 'pharmacy/medicine_list.html'
    context_object_name = 'items'

class MedicineDetailView(DetailView):
    model = Medicine
    template_name = 'pharmacy/medicine_detail.html'
    context_object_name = 'item'

class MedicineCreateView(CreateView):
    model = Medicine
    template_name = 'pharmacy/medicine_form.html'
    fields = ['name', 'category', 'manufacturer', 'price', 'description', 'photo', 'prescription_required']
    success_url = reverse_lazy('medicine_list')

class MedicineUpdateView(UpdateView):
    model = Medicine
    template_name = 'pharmacy/medicine_form.html'
    fields = ['name', 'category', 'manufacturer', 'price', 'description', 'photo', 'prescription_required']
    success_url = reverse_lazy('medicine_list')

class MedicineDeleteView(DeleteView):
    model = Medicine
    template_name = 'pharmacy/medicine_confirm_delete.html'
    success_url = reverse_lazy('medicine_list')

# 2. КОМПОНЕНТЫ (Component)
class ComponentListView(ListView):
    model = Component
    template_name = 'pharmacy/component_list.html'
    context_object_name = 'items'

class ComponentDetailView(DetailView):
    model = Component
    template_name = 'pharmacy/component_detail.html'
    context_object_name = 'item'

class ComponentCreateView(CreateView):
    model = Component
    template_name = 'pharmacy/component_form.html'
    fields = ['name', 'supplier', 'unit', 'price', 'photo']
    success_url = reverse_lazy('component_list')

class ComponentUpdateView(UpdateView):
    model = Component
    template_name = 'pharmacy/component_form.html'
    fields = ['name', 'supplier', 'unit', 'price', 'photo']
    success_url = reverse_lazy('component_list')

class ComponentDeleteView(DeleteView):
    model = Component
    template_name = 'pharmacy/component_confirm_delete.html'
    success_url = reverse_lazy('component_list')

# 3. ЗАКАЗЫ (Order)
class OrderListView(ListView):
    model = Order
    template_name = 'pharmacy/order_list.html'
    context_object_name = 'items'

class OrderDetailView(DetailView):
    model = Order
    template_name = 'pharmacy/order_detail.html'
    context_object_name = 'item'

class OrderCreateView(CreateView):
    model = Order
    template_name = 'pharmacy/order_form.html'
    fields = ['medicine', 'employee', 'status']
    success_url = reverse_lazy('order_list')

class OrderUpdateView(UpdateView):
    model = Order
    template_name = 'pharmacy/order_form.html'
    fields = ['medicine', 'employee', 'status']
    success_url = reverse_lazy('order_list')

class OrderDeleteView(DeleteView):
    model = Order
    template_name = 'pharmacy/order_confirm_delete.html'
    success_url = reverse_lazy('order_list')

# 4. СОТРУДНИКИ (Employee)
class EmployeeListView(ListView):
    model = Employee
    template_name = 'pharmacy/employee_list.html'
    context_object_name = 'items'

class EmployeeDetailView(DetailView):
    model = Employee
    template_name = 'pharmacy/employee_detail.html'
    context_object_name = 'item'

class EmployeeCreateView(CreateView):
    model = Employee
    template_name = 'pharmacy/employee_form.html'
    fields = ['last_name', 'first_name', 'position']
    success_url = reverse_lazy('employee_list')

class EmployeeUpdateView(UpdateView):
    model = Employee
    template_name = 'pharmacy/employee_form.html'
    fields = ['last_name', 'first_name', 'position']
    success_url = reverse_lazy('employee_list')

class EmployeeDeleteView(DeleteView):
    model = Employee
    template_name = 'pharmacy/employee_confirm_delete.html'
    success_url = reverse_lazy('employee_list')

# 5. РЕЦЕПТЫ (Prescription)
class PrescriptionListView(ListView):
    model = Prescription
    template_name = 'pharmacy/prescription_list.html'
    context_object_name = 'items'

class PrescriptionDetailView(DetailView):
    model = Prescription
    template_name = 'pharmacy/prescription_detail.html'
    context_object_name = 'item'

class PrescriptionCreateView(CreateView):
    model = Prescription
    template_name = 'pharmacy/prescription_form.html'
    fields = ['number', 'doctor_name', 'patient_name', 'medicine', 'issued_at']
    success_url = reverse_lazy('prescription_list')

class PrescriptionUpdateView(UpdateView):
    model = Prescription
    template_name = 'pharmacy/prescription_form.html'
    fields = ['number', 'doctor_name', 'patient_name', 'medicine', 'issued_at']
    success_url = reverse_lazy('prescription_list')

class PrescriptionDeleteView(DeleteView):
    model = Prescription
    template_name = 'pharmacy/prescription_confirm_delete.html'
    success_url = reverse_lazy('prescription_list')