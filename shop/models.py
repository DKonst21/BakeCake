from django.db import models
from django.contrib.auth.models import User


class Layer(models.Model):
    num_layers = models.IntegerField(
        'Количество слоев',
    )
    price = models.DecimalField(
        'Цена',
        max_digits=6,
        decimal_places=2,
        null=True,
        default=0
    )
    image = models.ImageField(
        'Изображение',
        null=True,
        blank=True,
    )
    available = models.BooleanField(
        'Доступно к заказу',
        default=True,
    )

    def orders_count(self):
        return self.orders.count()

    @property
    def int_price(self):
        return int(self.price)

    def __str__(self) -> str:
        return f"{self.num_layers}"

    class Meta:
        verbose_name = 'Опция количества слоев'
        verbose_name_plural = 'Опции количества слоев'


class Shape(models.Model):
    name = models.CharField(
        'Описание формы',
        max_length=100,
    )

    price = models.DecimalField(
        'Цена',
        max_digits=6,
        decimal_places=2,
        null=True,
        default=0
    )
    image = models.ImageField(
        'Изображение',
        null=True,
        blank=True,
    )
    available = models.BooleanField(
        'Доступно к заказу',
        default=True,
    )

    def orders_count(self):
        return self.orders.count()

    @property
    def int_price(self):
        return int(self.price)

    def __str__(self) -> str:
        return f"{self.name}"

    class Meta:
        verbose_name = 'Опция формы'
        verbose_name_plural = 'Опции формы'


class Topping(models.Model):
    name = models.CharField(
        'Описание топпинга',
        max_length=100,
    )

    price = models.DecimalField(
        'Цена',
        max_digits=6,
        decimal_places=2,
        null=True,
        default=0
    )
    image = models.ImageField(
        'Изображение',
        null=True,
        blank=True,
    )
    available = models.BooleanField(
        'Доступно к заказу',
        default=True,
    )

    def orders_count(self):
        return self.orders.count()

    @property
    def int_price(self):
        return int(self.price)

    def __str__(self) -> str:
        return f"{self.name}"

    class Meta:
        verbose_name = 'Опция топпинга'
        verbose_name_plural = 'Опции топпинга'


class Berries(models.Model):
    name = models.CharField(
        'Описание ягод',
        max_length=100,
    )

    price = models.DecimalField(
        'Цена',
        max_digits=6,
        decimal_places=2,
        null=True,
        default=0
    )
    image = models.ImageField(
        'Изображение',
        null=True,
        blank=True,
    )
    available = models.BooleanField(
        'Доступно к заказу',
        default=True,
    )

    def orders_count(self):
        return self.orders.count()

    @property
    def int_price(self):
        return int(self.price)

    def __str__(self) -> str:
        return f"{self.name}"

    class Meta:
        verbose_name = 'Опция ягод'
        verbose_name_plural = 'Опции ягод'


class Decor(models.Model):
    name = models.CharField(
        'Описание украшения',
        max_length=100,
    )

    price = models.DecimalField(
        'Цена',
        max_digits=6,
        decimal_places=2,
        null=True,
        default=0,
    )
    image = models.ImageField(
        'Изображение',
        null=True,
        blank=True,
    )
    available = models.BooleanField(
        'Доступно к заказу',
        default=True,
    )

    def orders_count(self):
        return self.orders.count()

    @property
    def int_price(self):
        return int(self.price)

    def __str__(self) -> str:
        return f"{self.name}"

    class Meta:
        verbose_name = 'Опция украшения'
        verbose_name_plural = 'Опции украшения'


class Words(models.Model):
    word = models.TextField(
        'Надпись',
        max_length=100,
    )

    def __str__(self) -> str:
        return f"{self.word}"

    class Meta:
        verbose_name = 'Надпись на торте'
        verbose_name_plural = 'Надписи на торте'


class Users(models.Model):
    name = models.ForeignKey(
        User,
        verbose_name='Имя заказчика',
        on_delete=models.CASCADE,
        related_name='customer'
    )
    phone = models.TextField('Номер телефона')
    address = models.TextField('Адрес заказчика')


class Orders(models.Model):
    num = models.ForeignKey(
        Layer,
        verbose_name='Уровень',
        on_delete=models.CASCADE
    )
    form = models.ForeignKey(
        Shape,
        verbose_name='Форма',
        on_delete=models.CASCADE
    )
    topping = models.ForeignKey(
        Topping,
        verbose_name='топпинг',
        on_delete=models.CASCADE
    )
    berry = models.ForeignKey(
        Berries,
        verbose_name='Ягоды',
        on_delete=models.CASCADE,
        blank=True
    )
    dekor = models.ForeignKey(
        Decor,
        verbose_name='Декор',
        on_delete=models.CASCADE,
        blank=True
    )
    word = models.ForeignKey(
        Words,
        verbose_name='Надпись',
        on_delete=models.CASCADE,
        blank=True
    )
    comment = models.TextField('Комментарий к заказу', blank=True)
    address = models.ForeignKey(
        Users,
        verbose_name='Надпись',
        on_delete=models.CASCADE
    )
    date_delivery = models.DateField('Дата доставки')
    time_delivery = models.TimeField('Время доставки')