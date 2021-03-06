# Generated by Django 3.2.2 on 2021-05-13 14:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeveloperUserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(max_length=180)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='developer_profile', to='users.developeruser')),
            ],
        ),
    ]
