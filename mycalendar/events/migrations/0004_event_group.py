# Generated by Django 5.0.2 on 2024-07-15 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_alter_event_fio_alter_event_email_alter_event_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='group',
            field=models.CharField(blank=True, help_text='Группа', max_length=255, null=True, verbose_name='Группа'),
        ),
    ]
