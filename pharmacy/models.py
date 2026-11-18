from django.db import models

MAX_LENGTH = 255

# 1. Категория
class Category(models.Model):
    name = models.CharField(max_length=MAX_LENGTH, verbose_name='Наименование категории')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')
    def __str__(self): return self.name
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

# 2. Производитель
class Manufacturer(models.Model):
    name = models.CharField(max_length=MAX_LENGTH, verbose_name='Наименование производителя')
    country = models.CharField(max_length=100, null=True, blank=True, verbose_name='Страна')
    def __str__(self): return self.name
    class Meta:
        verbose_name = 'Производитель'
        verbose_name_plural = 'Производители'

# 3. Поставщик
class Supplier(models.Model):
    name = models.CharField(max_length=MAX_LENGTH, verbose_name='Наименование поставщика')
    phone = models.CharField(max_length=20, null=True, blank=True, verbose_name='Телефон')
    def __str__(self): return self.name
    class Meta:
        verbose_name = 'Поставщик'
        verbose_name_plural = 'Поставщики'

# 4. Лекарство (С ФОТО)
class Medicine(models.Model):
    name = models.CharField(max_length=MAX_LENGTH, verbose_name='Наименование лекарства')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Производитель')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')
    photo = models.ImageField(upload_to='medicines/', null=True, blank=True, verbose_name='Фото')
    prescription_required = models.BooleanField(default=False, verbose_name='По рецепту')
    def __str__(self): return self.name
    class Meta:
        verbose_name = 'Лекарство'
        verbose_name_plural = 'Лекарства'

# 5. Компонент (С ФОТО)
class Component(models.Model):
    name = models.CharField(max_length=MAX_LENGTH, verbose_name='Наименование компонента')
    supplier = models.ForeignKey(Supplier, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Поставщик')
    unit = models.CharField(max_length=20, default='г', verbose_name='Единица измерения')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена за единицу')
    photo = models.ImageField(upload_to='components/', null=True, blank=True, verbose_name='Фото')
    def __str__(self): return self.name
    class Meta:
        verbose_name = 'Компонент'
        verbose_name_plural = 'Компоненты'

# 6. Сотрудник
class Employee(models.Model):
    last_name = models.CharField(max_length=50, verbose_name='Фамилия')
    first_name = models.CharField(max_length=50, verbose_name='Имя')
    position = models.CharField(max_length=100, verbose_name='Должность')
    def __str__(self): return f'{self.last_name} {self.first_name}'
    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'

# 7. Заказ
class Order(models.Model):
    STATUS_CHOICES = [
        ('ВОбработке', 'В обработке'),
        ('ВПроизводстве', 'В производстве'),
        ('Готов', 'Готов'),
        ('Выдан', 'Выдан'),
    ]
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE, verbose_name='Лекарство')
    employee = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Сотрудник')
    status = models.CharField(max_length=40, choices=STATUS_CHOICES, default='ВОбработке', verbose_name='Статус')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    def __str__(self): return f'Заказ #{self.pk} — {self.medicine}'
    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

# 8. Рецепт
class Prescription(models.Model):
    number = models.CharField(max_length=50, verbose_name='Номер рецепта')
    doctor_name = models.CharField(max_length=MAX_LENGTH, verbose_name='Врач')
    patient_name = models.CharField(max_length=MAX_LENGTH, verbose_name='Пациент')
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE, verbose_name='Лекарство')
    issued_at = models.DateField(verbose_name='Дата выдачи')
    def __str__(self): return f'Рецепт №{self.number}'
    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'