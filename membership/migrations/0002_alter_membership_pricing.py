# Generated by Django 3.2.3 on 2021-06-16 13:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('membership', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membership',
            name='pricing',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='memberships', to='membership.pricing'),
        ),
    ]
