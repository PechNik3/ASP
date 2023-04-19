# Generated by Django 4.2 on 2023-04-19 00:16

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('year', models.IntegerField()),
            ],
            options={
                'unique_together': {('name', 'year')},
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.TextField()),
                ('first_name', models.TextField()),
                ('courses', models.ManyToManyField(blank=True, to='warehouse_app.course')),
            ],
            options={
                'verbose_name_plural': 'People',
            },
        ),
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='warehouse_app.course')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='warehouse_app.person')),
            ],
        ),
    ]
