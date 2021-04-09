from django.db import models

from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.core.fields import StreamField
from wagtail.core.models import Page
from wagtail.images.edit_handlers import ImageChooserPanel

from blocks import blocks


class ProductListingPage(Page):
    """Product listing page will display all of the Product Detail pages."""

    template = 'products/product_listing_page.html'


    custom_title = models.CharField(
        max_length=100,
        blank=False,
        null=False,
        help_text='Overwrite the default title'
    )
    content_panels = Page.content_panels + [
        FieldPanel('custom_title'),
    ]

    
    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context['products'] = ProductDetailPage.objects.live().public()
        return context


class ProductDetailPage(Page):
    """Products detail page."""

    custom_title = models.CharField(
        max_length=100,
        blank=False,
        null=False,
        help_text='Overwrite the default title'
    )
    product_image = models.ForeignKey(
        "wagtailimages.Image",
        blank=False,
        null=True,
        related_name='+',
        on_delete=models.SET_NULL
    )
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
    content_panels = Page.content_panels + [
        FieldPanel('custom_title'),
        ImageChooserPanel('product_image'),
        StreamFieldPanel('all_block_content'),
    ]



