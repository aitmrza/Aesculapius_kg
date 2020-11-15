# Generated by Django 3.1.2 on 2020-11-15 10:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('clinic', '0012_auto_20201114_1330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clinic',
            name='medical_departments',
            field=models.ManyToManyField(related_name='clinics', to='clinic.MedicalDepartment'),
        ),
        migrations.AlterField(
            model_name='review',
            name='clinic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='clinic.clinic'),
        ),
        migrations.AlterField(
            model_name='review',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to=settings.AUTH_USER_MODEL),
        ),
    ]