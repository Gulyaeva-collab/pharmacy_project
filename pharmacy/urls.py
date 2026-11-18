from django.urls import path
from . import views

urlpatterns = [
    # 1. Лекарства
    path('medicines/', views.MedicineListView.as_view(), name='medicine_list'),
    path('medicines/<int:pk>/', views.MedicineDetailView.as_view(), name='medicine_detail'),
    path('medicines/add/', views.MedicineCreateView.as_view(), name='medicine_add'),
    path('medicines/<int:pk>/edit/', views.MedicineUpdateView.as_view(), name='medicine_edit'),
    path('medicines/<int:pk>/delete/', views.MedicineDeleteView.as_view(), name='medicine_delete'),

    # 2. Компоненты
    path('components/', views.ComponentListView.as_view(), name='component_list'),
    path('components/<int:pk>/', views.ComponentDetailView.as_view(), name='component_detail'),
    path('components/add/', views.ComponentCreateView.as_view(), name='component_add'),
    path('components/<int:pk>/edit/', views.ComponentUpdateView.as_view(), name='component_edit'),
    path('components/<int:pk>/delete/', views.ComponentDeleteView.as_view(), name='component_delete'),

    # 3. Заказы
    path('orders/', views.OrderListView.as_view(), name='order_list'),
    path('orders/<int:pk>/', views.OrderDetailView.as_view(), name='order_detail'),
    path('orders/add/', views.OrderCreateView.as_view(), name='order_add'),
    path('orders/<int:pk>/edit/', views.OrderUpdateView.as_view(), name='order_edit'),
    path('orders/<int:pk>/delete/', views.OrderDeleteView.as_view(), name='order_delete'),

    # 4. Сотрудники
    path('employees/', views.EmployeeListView.as_view(), name='employee_list'),
    path('employees/<int:pk>/', views.EmployeeDetailView.as_view(), name='employee_detail'),
    path('employees/add/', views.EmployeeCreateView.as_view(), name='employee_add'),
    path('employees/<int:pk>/edit/', views.EmployeeUpdateView.as_view(), name='employee_edit'),
    path('employees/<int:pk>/delete/', views.EmployeeDeleteView.as_view(), name='employee_delete'),

    # 5. Рецепты
    path('prescriptions/', views.PrescriptionListView.as_view(), name='prescription_list'),
    path('prescriptions/<int:pk>/', views.PrescriptionDetailView.as_view(), name='prescription_detail'),
    path('prescriptions/add/', views.PrescriptionCreateView.as_view(), name='prescription_add'),
    path('prescriptions/<int:pk>/edit/', views.PrescriptionUpdateView.as_view(), name='prescription_edit'),
    path('prescriptions/<int:pk>/delete/', views.PrescriptionDeleteView.as_view(), name='prescription_delete'),
]