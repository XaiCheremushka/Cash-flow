from django.db import models
from django.utils import timezone
from pytils.translit import slugify


def get_currency():
    return Currency.objects.get(code='RUB').pk


class Type(models.Model):
    class Meta:
        db_table = 'cashflow_type'
        verbose_name = 'Тип денежного потока'
        verbose_name_plural = 'Типы денежных потоков'

    name = models.CharField(verbose_name='type', null=False, blank=False)
    slug = models.SlugField(verbose_name='slug', null=False, blank=False)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Category(models.Model):
    class Meta:
        db_table = 'cashflow_category'
        verbose_name = 'Категория денежного потока'
        verbose_name_plural = 'Категории денежных потоков'

    name = models.CharField(verbose_name='Категория', null=False, blank=False)
    type = models.ForeignKey(
        Type,
        verbose_name='Тип',
        related_name='category',
        null=False,
        blank=False,
        on_delete=models.CASCADE
    )
    slug = models.SlugField(verbose_name='slug', null=False, blank=False)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Subcategory(models.Model):
    class Meta:
        db_table = 'cashflow_subcategory'
        verbose_name = 'Подкатегория денежного потока'
        verbose_name_plural = 'Подкатегории денежных потоков'

    name = models.CharField(verbose_name='Подкатегория', null=False, blank=False)
    category = models.ForeignKey(Category,
                                 verbose_name='Категория',
                                 related_name='subcategory',
                                 null=False,
                                 blank=False,
                                 on_delete=models.CASCADE)
    slug = models.SlugField(verbose_name='slug', null=False, blank=False)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Status(models.Model):
    class Meta:
        db_table = 'cashflow_status'
        verbose_name = 'Статус денежного потока'
        verbose_name_plural = 'Статусы денежных потоков'

    name = models.CharField(verbose_name='status', null=False, blank=False)
    slug = models.SlugField(verbose_name='slug', null=False, blank=False)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Currency(models.Model):
    class Meta:
        db_table = 'currency'
        verbose_name = 'Валюта'
        verbose_name_plural = 'Валюты'

    name = models.CharField(max_length=50, verbose_name='Название', help_text='Полное название валюты')
    # Код валюты (например: USD, EUR, RUB)
    code = models.CharField(max_length=3, unique=True, verbose_name='Код валюты', help_text='Трехбуквенный код валюты')
    symbol = models.CharField(max_length=5, verbose_name='Символ', help_text='Символ валюты ($, €, ₽ и т.д.)')

    def __str__(self):
        return self.name


class CashFlow(models.Model):
    class Meta:
        db_table = 'cashflow'
        verbose_name = 'Денежный поток'
        verbose_name_plural = 'Денежные потоки'

    category = models.ForeignKey(Category, verbose_name='Категория', null=False, blank=False, on_delete=models.PROTECT)
    subcategory = models.ForeignKey(Subcategory, verbose_name='Подкатегория', null=False, blank=False,
                                    on_delete=models.PROTECT, default=1)
    type = models.ForeignKey(Type, verbose_name='Тип', null=False, blank=False, on_delete=models.PROTECT)
    status = models.ForeignKey(Status, verbose_name='Статус', null=False, blank=False, on_delete=models.PROTECT)
    amount = models.DecimalField(verbose_name="Сумма", max_digits=10, decimal_places=2)
    currency = models.ForeignKey(Currency,
                                 verbose_name="Валюта",
                                 default=get_currency,
                                 null=False,
                                 blank=False,
                                 on_delete=models.PROTECT)
    comment = models.TextField(verbose_name="Комментарий", null=True, blank=True)
    date_created = models.DateField(verbose_name='Дата создания', null=False, blank=True)

    def save(self, *args, **kwargs):
        if not self.date_created:
            self.date_created = timezone.now().date()
        super().save(*args, **kwargs)
