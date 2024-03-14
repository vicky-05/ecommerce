# Generated by Django 4.2 on 2024-01-25 07:16

from django.db import migrations, models
import shop.models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_topbrands'),
    ]

    operations = [
        migrations.CreateModel(
            name='productCollection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_product', models.CharField(max_length=255)),
                ('image_product', models.ImageField(blank=True, null=True, upload_to=shop.models.getFilename)),
                ('mrp_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('discounted_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('discount_percentage', models.DecimalField(decimal_places=2, editable=False, max_digits=5)),
                ('discount_amount', models.DecimalField(decimal_places=2, editable=False, max_digits=10)),
                ('status', models.BooleanField(default=False, help_text='0=show,1=Hidden')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]