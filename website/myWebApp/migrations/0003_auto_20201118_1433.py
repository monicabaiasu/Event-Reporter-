# Generated by Django 3.0.5 on 2020-11-18 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myWebApp', '0002_auto_20201110_1155'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventReported',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.DeleteModel(
            name='ExampleModel',
        ),
    ]
