# Generated by Django 3.1.8 on 2021-04-09 12:20

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('flex', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='flexpage',
            name='content',
            field=wagtail.core.fields.StreamField([('title_and_text', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Add a title', required=True)), ('text', wagtail.core.blocks.TextBlock(help_text='Additional Text', required=True))]))], blank=True, null=True),
        ),
    ]
