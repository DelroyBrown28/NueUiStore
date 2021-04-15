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

#     home_page_background_image = models.ForeignKey(
#         "wagtailimages.Image",
#         null=True,
#         blank=False,
#         on_delete=models.SET_NULL,
#         related_name="+"
#     )
#     home_page_CTA_button = models.ForeignKey(
#         "wagtailcore.Page",
#         null=True,
#         blank=True,
#         on_delete=models.SET_NULL,
#         related_name="+"
#    )
#     home_page_cta_button_label = models.CharField(max_length=25, blank=False, null=False)

    

    all_block_content = StreamField(
        [
            ('title_and_text', blocks.TitleAndTextBlock()),
            ('full_richtext', blocks.RichtextBlock()),
            ('art_cards', blocks.ArtBlock()),
            ('cta', blocks.CTABlock()),
            ('large_jumbotron', blocks.LargeJumbotronBlock()),
            ('navbar', blocks.NavbarBlock()),


        ],
        null=True,
        blank=True
    )
    homepage_content = StreamField(
        [
            ('navbar', blocks.NavbarBlock()),
            ('homepage_cta', blocks.CTABlock()),
            ('home_page_title', blocks.TitleAndTextBlock()),
            ('home_page_subtitle', blocks.TitleAndTextBlock()),
            ('home_page_description', blocks.RichtextBlock()),
            ('home_page_background_image', blocks.ImageChooserBlock()),
            ('art_cards', blocks.ArtBlock()),


        ],
        null=True,
        blank=True
    )

    content_panels = Page.content_panels + [
        # ImageChooserPanel("home_page_background_image"),
        # PageChooserPanel("home_page_CTA_button"),
        # FieldPanel("home_page_cta_button_label"),
        StreamFieldPanel("homepage_content"),
        StreamFieldPanel("all_block_content"),
    ]

    

    class Meta:
        verbose_name = "Home Page"
        verbose_name_plural = "Home Pages"


