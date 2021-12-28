# Generated by Django 3.2.9 on 2021-12-25 15:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hotel', '0004_auto_20211225_1759'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderroom',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ordered_room', to='hotel.room', verbose_name='комнаты'),
        ),
        migrations.AlterField(
            model_name='orderroom',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ordered_user', to=settings.AUTH_USER_MODEL, verbose_name='клиент'),
        ),
    ]