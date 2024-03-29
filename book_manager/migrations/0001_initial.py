# Generated by Django 2.2.9 on 2020-04-24 19:19

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import mdeditor.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
                ('pri', models.IntegerField(default=0)),
                ('time', models.CharField(default='00:00', max_length=100)),
                ('rgst', models.DateTimeField(default=django.utils.timezone.now)),
                ('status', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Summary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=100)),
                ('summary', mdeditor.fields.MDTextField(verbose_name='')),
                ('rgst', models.DateTimeField(default=django.utils.timezone.now)),
                ('updt', models.DateTimeField(auto_now=True)),
                ('esa_id', models.IntegerField(blank=True, default=0, null=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='summaries', to='book_manager.Book', verbose_name='book')),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='book_manager.Category'),
        ),
    ]
