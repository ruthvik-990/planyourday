# Generated by Django 3.0 on 2020-05-30 17:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0005_auto_20200530_2238'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='middle',
        ),
        migrations.AddField(
            model_name='task',
            name='profile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='tasks.Profile'),
        ),
        migrations.DeleteModel(
            name='Middle',
        ),
    ]
