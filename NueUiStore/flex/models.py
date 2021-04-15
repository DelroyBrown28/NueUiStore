from django.db import models

from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel, PageChooserPanel
from wagtail.core.models import Page
from wagtail.core.fields import StreamField

from blocks import blocks


class FlexPage(Page):
    template = 'flex/flex_page.html'

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
    page_title = models.CharField(max_length=100, blank=True, null=True)

    content_panels = Page.content_panels + [
        FieldPanel('page_title'),
        StreamFieldPanel('all_block_content'),
    ]

    class Meta:
        verbose_name = 'Flex Page'
        verbose_name_plural = 'Flex Pages'
