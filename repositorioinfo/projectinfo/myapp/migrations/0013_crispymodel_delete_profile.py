# Generated by Django 4.0.6 on 2022-08-18 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0012_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='CrispyModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('songs', models.CharField(max_length=500)),
                ('name_of_artist', models.CharField(max_length=500)),
                ('number_of_awards', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
