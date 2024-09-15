# Generated by Django 5.1.1 on 2024-09-15 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BearerToken',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=255)),
                ('user_id', models.IntegerField()),
                ('issued_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
