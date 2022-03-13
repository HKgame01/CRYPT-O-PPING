# Generated by Django 3.2.7 on 2021-09-10 22:26

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
            name='Invoicing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('tran_id', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('amount', models.IntegerField(verbose_name='Amount - tinybar (tℏ)')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Invoicing',
                'ordering': ['-timestamp'],
            },
        ),
    ]
