# Generated by Django 3.1.7 on 2021-08-03 06:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_category_cat'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='cat',
        ),
        migrations.AddField(
            model_name='subcategory',
            name='cat',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='shop.category', verbose_name='Подкатегория'),
        ),
    ]
