from django.db import migrations


def seed_products(apps, schema_editor):
    Products = apps.get_model('api', 'Products')
    sample_products = [
        ('Phone', 29999),
        ('Laptop', 65999),
    ]

    for name, price in sample_products:
        Products.objects.get_or_create(name=name, defaults={'price': price})


def remove_seed_products(apps, schema_editor):
    Products = apps.get_model('api', 'Products')
    Products.objects.filter(name__in=['Phone', 'Laptop']).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(seed_products, remove_seed_products),
    ]
