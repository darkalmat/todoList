# Generated by Django 2.1 on 2018-08-15 05:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200)),
                ('image', models.ImageField(null=True, upload_to='uploads/%Y/%m/%d/')),
                ('text', models.TextField(blank=True)),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TodoList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deadline', models.DateTimeField()),
                ('note', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='todos.Note')),
            ],
        ),
        migrations.CreateModel(
            name='TodoThing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('done', models.BooleanField()),
                ('positionIndex', models.IntegerField(default=0)),
                ('todoList', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todos.TodoList')),
            ],
        ),
    ]
