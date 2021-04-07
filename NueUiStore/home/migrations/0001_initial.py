# Generated by Django 3.1.8 on 2021-04-07 16:27

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailimages', '0023_add_choose_permissions'),
        ('wagtailcore', '0061_auto_20210407_1453'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomePage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('page_title', models.CharField(max_length=100, null=True)),
                ('page_subtitle', wagtail.core.fields.RichTextField(blank=True, default='Page Subtitle', null=True)),
                ('page_description', wagtail.core.fields.RichTextField(blank=True, default='Place description here', null=True)),
                ('home_page_cta_button_label', models.CharField(max_length=25)),
                ('navbar_link_text_1', models.CharField(blank=True, default='Nav Text 1', help_text='Navbar Text', max_length=25, null=True)),
                ('navbar_link_text_2', models.CharField(blank=True, default='Nav Text 2', help_text='Navbar Text', max_length=25, null=True)),
                ('navbar_link_text_3', models.CharField(blank=True, default='Nav Text 3', help_text='Navbar Text', max_length=25, null=True)),
                ('navbar_link_text_4', models.CharField(blank=True, default='Nav Text 4', help_text='Navbar Text', max_length=25, null=True)),
                ('home_page_CTA_button', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.page')),
                ('home_page_background_image', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image')),
                ('navbar_link_1', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.page')),
                ('navbar_link_2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.page')),
                ('navbar_link_3', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.page')),
                ('navbar_link_4', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.page')),
                ('navbar_logo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image')),
            ],
            options={
                'verbose_name': 'Home Page',
                'verbose_name_plural': 'Home Pages',
            },
            bases=('wagtailcore.page',),
        ),
    ]
