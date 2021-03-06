# Generated by Django 2.2 on 2021-04-05 19:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Priority',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(help_text='Description priority', max_length=100, unique=True)),
                ('order', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='TodoList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(help_text='Description todo', max_length=100, unique=True)),
                ('done', models.BooleanField(default=True)),
                ('priority', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todolist_app.Priority')),
            ],
        ),
    ]
