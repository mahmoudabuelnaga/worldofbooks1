# Generated by Django 2.1 on 2019-04-15 16:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_auto_20190415_0836'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='auther',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.Authers'),
        ),
    ]