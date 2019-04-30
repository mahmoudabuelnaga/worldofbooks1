# Generated by Django 2.1 on 2019-04-21 04:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('catalog', '0013_auto_20190420_2120'),
    ]

    operations = [
        migrations.CreateModel(
            name='Authers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('img', models.ImageField(upload_to='auther_image/')),
                ('date_of_publication', models.DateField(auto_now=True)),
            ],
            options={
                'ordering': ['-date_of_publication'],
            },
        ),
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('cover', models.ImageField(upload_to='book_img/')),
                ('pdf', models.FileField(upload_to='file_pdf/')),
                ('summary', models.TextField()),
                ('language', models.CharField(max_length=100)),
                ('genre', models.CharField(max_length=100)),
                ('date_of_publication', models.DateField(auto_now=True)),
                ('famous_books', models.BooleanField(default=False)),
                ('auther', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.Authers')),
            ],
            options={
                'ordering': ['-date_of_publication'],
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('img', models.ImageField(upload_to='team_img/')),
                ('specialty', models.CharField(max_length=300)),
            ],
        ),
    ]