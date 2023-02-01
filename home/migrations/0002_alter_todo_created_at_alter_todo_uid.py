# Generated by Django 4.1.6 on 2023-02-01 14:19

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='created_at',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='todo',
            name='uid',
            field=models.UUIDField(default=uuid.UUID('00c18d87-84d3-4e2f-838a-dec0f04b7856'), editable=False, primary_key=True, serialize=False),
        ),
    ]