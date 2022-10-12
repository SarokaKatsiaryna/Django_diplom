# Generated by Django 4.1 on 2022-10-11 16:29

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
            name='OrgEducatuion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_org', models.CharField(max_length=100, verbose_name='Название')),
                ('description_org', models.TextField(verbose_name='Описание')),
                ('address_org', models.CharField(max_length=256, verbose_name='Адрес')),
                ('phone_org', models.CharField(max_length=15, verbose_name='Телефон')),
                ('logo', models.ImageField(blank=True, null=True, upload_to='logo/', verbose_name='Логотип')),
            ],
            options={
                'db_table': 'org_educatuion',
            },
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_org', models.CharField(max_length=100, verbose_name='Название')),
                ('description_org', models.TextField(verbose_name='Описание')),
                ('address_org', models.CharField(max_length=256, verbose_name='Адрес')),
                ('phone_org', models.CharField(max_length=15, verbose_name='Телефон')),
                ('viber', models.CharField(blank=True, max_length=15, null=True, verbose_name='Viber')),
                ('telegtam', models.CharField(blank=True, max_length=50, null=True, verbose_name='Telegram')),
                ('instagram', models.CharField(blank=True, max_length=50, null=True, verbose_name='Instagram')),
                ('logo', models.ImageField(blank=True, null=True, upload_to='logo/', verbose_name='Логотип')),
                ('created', models.DateField(auto_now=True, verbose_name='Дата регистрации')),
                ('publication', models.BooleanField(default=False, verbose_name='Публикация')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'organization',
                'unique_together': {('name_org', 'address_org')},
            },
        ),
    ]
