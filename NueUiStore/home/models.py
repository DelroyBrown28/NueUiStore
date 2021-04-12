from django.db import models

from blocks import blocks
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField, StreamField
from wagtail.admin.edit_handlers import (FieldPanel, PageChooserPanel,
                                            MultiFieldPanel,
                                            StreamFieldPanel,
                                            InlinePanel,
                                            FieldRowPanel)
from wagtail.images.edit_handlers import ImageChooserPanel


class HomePage(Page):
    templates = "home/home_page.html"
    max_count = 1

    page_title = models.CharField(max_length=100, blank=False, null=True)
    page_subtitle = RichTextField(default='Page Subtitle', blank=True, null=True, features=["bold", "italic"])
    page_description = RichTextField(default='Place description here', null=True, blank=True)
    home_page_background_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="+"
    )
    home_page_CTA_button = models.ForeignKey(
        "wagtailcore.Page",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+"
   )
    home_page_cta_button_label = models.CharField(max_length=25, blank=False, null=False)

    """Navbar Stuff."""
    navbar_logo = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="+"
    )
    navbar_link_1 = models.ForeignKey(
        "wagtailcore.Page",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+"
    )
    navbar_link_text_1 = models.CharField(max_length=25, help_text='Navbar Text', blank=True, null=True, default='Nav Text 1')
    navbar_link_2 = models.ForeignKey(
        "wagtailcore.Page",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+"
    )
    navbar_link_text_2 = models.CharField(max_length=25, help_text='Navbar Text', blank=True, null=True, default='Nav Text 2')
    navbar_link_3 = models.ForeignKey(
        "wagtailcore.Page",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+"
    )
    navbar_link_text_3 = models.CharField(max_length=25, help_text='Navbar Text', blank=True, null=True, default='Nav Text 3')
    navbar_link_4 = models.ForeignKey(
        "wagtailcore.Page",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+"
    )
    navbar_link_text_4 = models.CharField(max_length=25, help_text='Navbar Text', blank=True, null=True, default='Nav Text 4')
    
    all_block_content = StreamField(
        [
            ('title_and_text', blocks.TitleAndTextBlock()),
            ('full_richtext', blocks.RichtextBlock()),
            ('art_cards', blocks.ArtBlock()),
            ('cta', blocks.CTABlock()),
        ],
        null=True,
        blank=True
    )
    art_card_content = StreamField(
        [
            ("full_richtext", blocks.RichtextBlock()),
            ("art_cards", blocks.ArtBlock()),
            
        ],
        null=True,
        blank=True
    )
    content_panels = Page.content_panels + [
        FieldPanel("page_title"),
        FieldPanel("page_subtitle"),
        FieldPanel("page_description"),
        ImageChooserPanel("home_page_background_image"),
        PageChooserPanel("home_page_CTA_button"),
        FieldPanel("home_page_cta_button_label"),
        StreamFieldPanel("art_card_content"),
        # Navbar Stuff
        ImageChooserPanel('navbar_logo'),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('navbar_link_text_1', classname='col12'),
                PageChooserPanel('navbar_link_1'),
            ]),
            FieldRowPanel([
                FieldPanel('navbar_link_text_2', classname='col12'),
                PageChooserPanel('navbar_link_2'),
            ]),
            FieldRowPanel([
                FieldPanel('navbar_link_text_3', classname='col12'),
                PageChooserPanel('navbar_link_3'),
            ]),
            FieldRowPanel([
                FieldPanel('navbar_link_text_4', classname='col12'),
                PageChooserPanel('navbar_link_4'),
            ]),
        ], heading='Navbar Links'),
            StreamFieldPanel("all_block_content"),

    ]

    class Meta:
        verbose_name = "Home Page"
        verbose_name_plural = "Home Pages"

