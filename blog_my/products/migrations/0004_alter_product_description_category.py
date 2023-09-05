# Generated by Django 4.2.4 on 2023-09-04 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_remove_product_product_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description_category',
            field=models.CharField(choices=[('technice', 'th'), ('book', 'bk'), ('phone', 'ph'), ('food', 'fd'), ('cloth', 'cl'), ('other', 'ot')], default='other', max_length=15),
        ),
    ]
