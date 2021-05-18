# Generated by Django 3.2.2 on 2021-05-18 20:50

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_remove_user_uuid'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
    ]
