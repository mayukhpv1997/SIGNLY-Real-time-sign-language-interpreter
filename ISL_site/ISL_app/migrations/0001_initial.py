# Generated by Django 2.2.5 on 2021-04-28 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Signup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
                ('confirmpassword', models.CharField(max_length=30)),
            ],
        ),
    ]
