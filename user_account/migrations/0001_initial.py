# Generated by Django 3.1.2 on 2020-10-30 07:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('itn', models.CharField(blank=True, max_length=14, unique=True, verbose_name='ИНН')),
                ('gender', models.CharField(blank=True, choices=[('М', 'Мужчина'), ('Ж', 'Женщина')], max_length=1, verbose_name='Пол')),
                ('birth_date', models.DateField(blank=True, null=True, verbose_name='Дата рождения')),
                ('city', models.CharField(blank=True, choices=[('БК', 'Бишкек'), ('Ош', 'Ош'), ('ДА', 'Джалал-Абад'), ('ТК', 'Токмок'), ('ТС', 'Талас'), ('КЛ', 'Каракол'), ('НН', 'Нарын'), ('БН', 'Баткен')], max_length=2, verbose_name='Город')),
                ('blood_type', models.CharField(blank=True, max_length=30, verbose_name='Группа крови')),
                ('photo', models.ImageField(blank=True, upload_to='users/%Y/%m/%d', verbose_name='Фото')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
