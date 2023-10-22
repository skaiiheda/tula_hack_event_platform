# Generated by Django 4.2 on 2023-10-21 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('city', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=300)),
                ('date', models.DateTimeField()),
                ('end_reg', models.DateTimeField()),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='events/images')),
                ('categories', models.ManyToManyField(to='recommendations.category')),
            ],
        ),
    ]
