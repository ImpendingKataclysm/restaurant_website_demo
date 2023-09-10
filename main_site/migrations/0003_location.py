# Generated by Django 4.2.5 on 2023-09-10 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_site', '0002_alter_menuitem_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street_address', models.CharField(blank=True, max_length=100, null=True)),
                ('city', models.CharField(blank=True, max_length=100, null=True)),
                ('postal', models.CharField(blank=True, max_length=6, null=True)),
                ('province', models.CharField(blank=True, max_length=100, null=True)),
                ('phone', models.CharField(max_length=10)),
                ('image', models.ImageField(blank=True, null=True, upload_to='main_site')),
            ],
        ),
    ]
