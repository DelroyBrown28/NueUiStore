from wagtail.core import blocks
from wagtail.core.templatetags.wagtailcore_tags import richtext
from wagtail.images.blocks import ImageChooserBlock


class TitleAndTextBlock(blocks.StructBlock):
    """Title and text."""

    title = blocks.CharBlock(required=True, help_text='Add a title')
    text = blocks.TextBlock(required=True, help_text='Additional Text')

    class Meta:
        template = 'blocks/title_and_text_block.html'
        icon = "edit"
        label = 'Title & Text'
        


class RichtextBlock(blocks.RichTextBlock):


    class Meta:
        template = 'blocks/richtext_block.html'
        icon = 'doc-full'
        label = 'Full Richtext'

        

class ArtBlock(blocks.StructBlock):
    # title_of_picture = blocks.RichTextBlock(required=True)

    art_cards = blocks.ListBlock(
        blocks.StructBlock(
            [
                ('title_of_picture', blocks.CharBlock(required=True, max_length=40, help_text="Name of Art Piece")),
                ('image', ImageChooserBlock(required=True)),
                ('picture_description', blocks.RichTextBlock(required=True, max_length=200)),
                ('button_to_site_page', blocks.PageChooserBlock(required=False)),
                ('button_to_external_URL', blocks.URLBlock(required=False, help_text='Here, you can link to an external website')),
                ('button_text', blocks.CharBlock(required=True, max_length=25, help_text='Text that will be displayed on the button')),

            ]
        )
    )

    class Meta:
        template = "blocks/art_block.html"
        icon = 'pencil'
        label = 'Art cards'


class CTABlock(blocks.StructBlock):
    title = blocks.CharBlock(required=True, max_length=100)
    text = blocks.RichTextBlock(required=True, features=['bold', 'italic'])
    button_page = blocks.PageChooserBlock(required=False) 
    button_url = blocks.URLBlock(required=False)
    button_text = blocks.CharBlock(required=False, default='Learn More', max_length=40)



    class Meta:
        template = 'blocks/cta_block.html'
        icon = 'placeholder'
        label = 'Call To Action'


