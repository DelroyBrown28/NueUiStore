# Generated by Django 3.1.8 on 2021-04-12 11:36

import blocks.blocks
from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('flex', '0005_auto_20210411_0134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flexpage',
            name='all_block_content',
            field=wagtail.core.fields.StreamField([('title_and_text', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Add a title', required=True)), ('text', wagtail.core.blocks.TextBlock(help_text='Additional Text', required=True))])), ('full_richtext', blocks.blocks.RichtextBlock()), ('art_cards', wagtail.core.blocks.StructBlock([('gallery_block_title', wagtail.core.blocks.RichTextBlock(required=True)), ('art_cards', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('title_of_picture', wagtail.core.blocks.CharBlock(help_text='Name of Art Piece', max_length=40, required=True)), ('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('picture_description', wagtail.core.blocks.RichTextBlock(max_length=200, required=True)), ('button_to_site_page', wagtail.core.blocks.PageChooserBlock(required=False)), ('button_to_external_URL', wagtail.core.blocks.URLBlock(help_text='Here, you can link to an external website', required=False)), ('button_text', wagtail.core.blocks.CharBlock(help_text='Text that will be displayed on the button', max_length=25, required=True))])))])), ('cta', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(max_length=100, required=True)), ('text', wagtail.core.blocks.RichTextBlock(features=['bold', 'italic'], required=True)), ('cta_image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('button_page', wagtail.core.blocks.PageChooserBlock(required=False)), ('button_url', wagtail.core.blocks.URLBlock(required=False)), ('button_text', wagtail.core.blocks.CharBlock(default='Learn More', max_length=40, required=False))]))], blank=True, null=True),
        ),
    ]
