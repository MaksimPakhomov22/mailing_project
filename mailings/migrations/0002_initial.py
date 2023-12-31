# Generated by Django 4.2.6 on 2023-10-25 21:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('mailings', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
        migrations.AddField(
            model_name='mailings',
            name='clients',
            field=models.ManyToManyField(to='mailings.client', verbose_name='Получатели'),
        ),
        migrations.AddField(
            model_name='mailings',
            name='message',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mailings.message', verbose_name='Сообщение'),
        ),
        migrations.AddField(
            model_name='mailings',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
        migrations.AddField(
            model_name='log',
            name='message',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='mailings.message', verbose_name='Письмо'),
        ),
        migrations.AddField(
            model_name='log',
            name='newsletter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mailings.mailings', verbose_name='Рассылка'),
        ),
        migrations.AddField(
            model_name='client',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Клиент'),
        ),
    ]
