# Generated by Django 2.2.9 on 2020-01-21 18:22

from django.db import migrations
import markdownx.models


class Migration(migrations.Migration):

    dependencies = [
        ('tasker', '0006_auto_20200122_0229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='summary',
            name='summary',
            field=markdownx.models.MarkdownxField(help_text='Markdown形式で書いてください。', verbose_name='本文'),
        ),
    ]
