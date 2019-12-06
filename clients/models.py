from django.db import models

#use for case ClientType.is_active=True 
def choices_type_client_active():
    return {'is_active': True}

class ClientType(models.Model):
    name_type = models.CharField(max_length=50, verbose_name="Тип клиента")
    short_name_type = models.CharField(max_length=20, blank=True, null=True, default=None, verbose_name="Коротко")
    is_active = models.BooleanField(default=True, verbose_name="Активный")
    created = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Создание")
    updated = models.DateTimeField(auto_now_add=False, auto_now=True, verbose_name="Обновление")        
    
    def __str__(self):
        return "{}".format(self.name_type)

    class Meta:
        verbose_name = "Тип клиента" 
        verbose_name_plural = "Типы клиентов"
        ordering = ['name_type']


class Client(models.Model):
    name = models.CharField(max_length=250, verbose_name="Имя")
    short_name = models.CharField(max_length=100, blank=True, null=True, default=None, verbose_name="Короткое имя")
    code_client = models.IntegerField(default=0, verbose_name="Код (ЕРДПО)")
    client_type = models.ForeignKey(ClientType, limit_choices_to=choices_type_client_active, blank=True, null=True, default=None, on_delete=models.PROTECT, verbose_name='Тип клиента')
    email = models.EmailField(blank=True, null=True, default=None)
    phone = models.CharField(max_length=50, blank=True, null=True, default=None)
    address = models.CharField(max_length=120, blank=True, null=True, default=None, verbose_name="Адрес")        
    comment = models.TextField(blank=True, null=True, default=None, verbose_name="Примечание")
    is_customer = models.BooleanField(default=True, verbose_name="Заказчик")
    is_povider = models.BooleanField(default=True, verbose_name="Поставщик")
    is_agent = models.BooleanField(default=True, verbose_name="Перевозчик")
    is_active = models.BooleanField(default=True, verbose_name="Активный")    
    created = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Создание")
    updated = models.DateTimeField(auto_now_add=False, auto_now=True, verbose_name="Обновление")        

    def __str__(self):
        return "{} ({})".format(self.name, self.code_client)
    
    class Meta:
        verbose_name = "Клиент" 
        verbose_name_plural = "Клиенты"
        ordering = ['name']
