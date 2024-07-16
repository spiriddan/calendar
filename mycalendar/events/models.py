from __future__ import unicode_literals

from django.db import models
from django.core.exceptions import ValidationError


class Event(models.Model):
    day = models.DateField(u'Дата консультации', help_text=u'Дата консультации')
    FIO = models.CharField(u'ФИО', help_text=u'ФИО', blank=True, null=True, max_length=255)
    phone = models.CharField(u'Телефон', help_text=u'Телефон', blank=True, null=True, max_length=255)
    email = models.EmailField(u'Электронная почта', help_text=u'Электронная почта', blank=True, null=True)
    group = models.CharField(u'Группа', help_text=u'Группа', blank=True, null=True, max_length=255)
    is_marked_10 = models.BooleanField(default=False, verbose_name='10:00-11:00')
    is_marked_11 = models.BooleanField(default=False, verbose_name='11:00-12:00')
    is_marked_12 = models.BooleanField(default=False, verbose_name='12:00-13:00')
    is_marked_13 = models.BooleanField(default=False, verbose_name='13:00-14:00')
    is_marked_14 = models.BooleanField(default=False, verbose_name='14:00-15:00')
    is_marked_16 = models.BooleanField(default=False, verbose_name='16:00-17:00')

    class Meta:
        verbose_name = u'Запись на консультацию'
        verbose_name_plural = u'Записи на консультации'

    def validate_unique(self, exclude=None):
        super(Event, self).validate_unique(exclude)

        if Event.objects.filter(day=self.day, is_marked_10=True).exists():
            if self.is_marked_10:
                raise ValidationError(u'Запись на консультацию уже существует')
        if Event.objects.filter(day=self.day, is_marked_11=True).exists():
            if self.is_marked_11:
                raise ValidationError(u'Запись на консультацию уже существует')
        if Event.objects.filter(day=self.day, is_marked_12=True).exists():
            if self.is_marked_12:
                raise ValidationError(u'Запись на консультацию уже существует')
        if Event.objects.filter(day=self.day, is_marked_13=True).exists():
            if self.is_marked_13:
                raise ValidationError(u'Запись на консультацию уже существует')
        if Event.objects.filter(day=self.day, is_marked_14=True).exists():
            if self.is_marked_14:
                raise ValidationError(u'Запись на консультацию уже существует')
        if Event.objects.filter(day=self.day, is_marked_16=True).exists():
            if self.is_marked_16:
                raise ValidationError(u'Запись на консультацию уже существует')
