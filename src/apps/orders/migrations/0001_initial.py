# Generated by Django 3.1.4 on 2021-01-04 13:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, verbose_name='имя')),
                ('last_name', models.CharField(max_length=50, verbose_name='фамилия')),
                ('email', models.EmailField(max_length=254, verbose_name='e-mail')),
                ('address', models.CharField(max_length=250, verbose_name='адресс')),
                ('postal_code', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=100, verbose_name='город')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='время оформления')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='изменено')),
                ('paid', models.BooleanField(default=False, verbose_name='оплачено')),
                ('braintree_id', models.CharField(blank=True, max_length=150, verbose_name='идентификатор транзакции')),
            ],
            options={
                'verbose_name': 'заказ',
                'verbose_name_plural': 'заказы',
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='orders.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_items', to='products.product')),
            ],
        ),
    ]
