from __future__ import absolute_import, unicode_literals

from django.db import models
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import datetime

from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailadmin.edit_handlers import FieldPanel, FieldRowPanel, InlinePanel, MultiFieldPanel, PageChooserPanel
from wagtail.wagtailsnippets.edit_handlers import SnippetChooserPanel
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailsnippets.models import register_snippet
from wagtail.wagtailforms.models import AbstractEmailForm, AbstractFormField
from wagtail.wagtailforms.edit_handlers import FormSubmissionsPanel
from modelcluster.fields import ParentalKey


@register_snippet
class SermonDay(models.Model):
    sermon_day = models.CharField(max_length=50, default="Lord's Day")

    def __str__(self):
        return self.sermon_day


@register_snippet
class SermonVideo(models.Model):
    sermon_day = models.ForeignKey(
        "home.SermonDay",
        null=True,
        blank=False,
        related_name='+',
        on_delete=models.SET_NULL,
    )
    sermon_title = models.TextField(default="Sermon Title")
    sermon_date = models.CharField(max_length=50, default="May 23 2017")
    sermon_chapter = models.CharField(max_length=80, default="Act 22:1-2")
    sermon_thumbnail_image = models.ForeignKey(
        "wagtailimages.Image",
        blank=False,
        null=True,
        related_name='+',
        on_delete=models.SET_NULL,
        help_text="Sermon Thumbnail Image"
    )
    sermon_link = models.TextField(default="www.youtube.com")
    sermon_share_code = models.CharField(max_length=80, default="LHJowUFSKMA")
    upload_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} - {}".format(self.sermon_title, self.sermon_date)


@register_snippet
class Author(models.Model):
    author_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text="75x75 pixel"
    )
    author_name = models.CharField(max_length=30, default="Pastor Kim")
    author_title = models.CharField(max_length=60, default="Eastern Church Senior Pastor")

    def __str__(self):
        return self.author_name


class BlogPage(Page):
    blog_title = models.TextField(default="Blog Title")
    blog_date = models.DateTimeField(auto_now_add=True)
    blog_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=False,
        related_name='+',
        on_delete=models.SET_NULL,
        help_text="Blog Image"
    )
    blog_content = RichTextField()

    blog_author = models.ForeignKey(
        "home.Author",
        blank=False,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )

    blog_button_text = models.CharField(max_length=50, default="Read more blog")
    blog_button_link = models.ForeignKey(
        "wagtailcore.Page",
        blank=False,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    parent_page_types = ['home.BlogIndexPage']

    content_panels = Page.content_panels + [
        FieldPanel('blog_title'),
        ImageChooserPanel('blog_image'),
        SnippetChooserPanel('blog_author'),
        FieldPanel('blog_content'),
        FieldPanel('blog_button_text'),
        PageChooserPanel('blog_button_link')
    ]


class BlogIndexPage(Page):
    blog_hero_title = models.TextField(default="Blog")
    blog_hero_subtitle = models.TextField(default="Subtitle for Blog")
    blog_featured_name = models.CharField(max_length=100, default="Featured Blog")

    subpage_types = ['home.BlogPage']

    blogs = BlogPage.objects.all().order_by("-blog_date")

    def get_context(self, request, *args, **kwargs):
        blogs = self.blogs

        paginator = Paginator(blogs, 9)
        page = request.GET.get('page')

        try:
            blogs = paginator.page(page)
        except PageNotAnInteger:
            blogs = paginator.page(1)
        except EmptyPage:
            blogs = paginator.page(paginator.num_pages)

        context = super(BlogIndexPage, self).get_context(request, *args, **kwargs)
        context['blogs'] = blogs

        return context

    content_panels = Page.content_panels + [
        FieldPanel('blog_hero_title'),
        FieldPanel('blog_hero_subtitle'),
        FieldPanel('blog_featured_name'),
    ]



class HomePage(Page):

    # Slide Section
    # First Slide
    first_slide_title = models.TextField(default="Welcome To EPC")
    first_slide_verse = models.CharField(max_length=100, default="Matthew 28:10-20")
    first_slide_scripture = models.TextField(default="Scriptures")
    first_slide_button_text = models.CharField(max_length=70, default="About EPC")
    first_slide_button_link = models.CharField(max_length=70, default="/about/")

    # Second Slide
    second_slide_title = models.TextField(default="Welcome To EPC")
    second_slide_verse = models.CharField(max_length=100, default="Matthew 28:10-20")
    second_slide_scripture = models.TextField(default="Scriptures")
    second_slide_button_text = models.CharField(max_length=70, default="About EPC")
    second_slide_button_link = models.CharField(max_length=70, default="/about/")

    # Third Slide
    third_slide_title = models.TextField(default="Welcome To EPC")
    third_slide_verse = models.CharField(max_length=100, default="Matthew 28:10-20")
    third_slide_scripture = models.TextField(default="Scriptures")
    third_slide_button_text = models.CharField(max_length=70, default="About EPC")
    third_slide_button_link = models.CharField(max_length=70, default="/about/")

    # Fourth Slide
    fourth_slide_title = models.TextField(default="Welcome To EPC")
    fourth_slide_verse = models.CharField(max_length=100, default="Matthew 28:10-20")
    fourth_slide_scripture = models.TextField(default="Scriptures")
    fourth_slide_button_text = models.CharField(max_length=70, default="About EPC")
    fourth_slide_button_link = models.CharField(max_length=70, default="/about/")

    # Confession Section
    confession_main_title = models.CharField(default="Our Confession", max_length=80)

    first_confession_title = models.CharField(max_length=80, default="first confession")
    first_confession_verse = models.CharField(max_length=50, default="Mathew 1:18")
    first_confession_scripture = models.TextField(default="Scripture")
    first_confession_icon = models.ForeignKey(
        "wagtailimages.Image",
        blank=False,
        null=True,
        related_name='+',
        on_delete=models.SET_NULL,
        help_text="64x64 icon"
    )

    second_confession_title = models.CharField(max_length=80, default="second confession")
    second_confession_verse = models.CharField(max_length=50, default="Mathew 1:18")
    second_confession_scripture = models.TextField(default="Scripture")
    second_confession_icon = models.ForeignKey(
        "wagtailimages.Image",
        blank=False,
        null=True,
        related_name='+',
        on_delete=models.SET_NULL,
        help_text="64x64 icon"
    )

    third_confession_title = models.CharField(max_length=80, default="third confession")
    third_confession_verse = models.CharField(max_length=50, default="Mathew 1:18")
    third_confession_scripture = models.TextField(default="Scripture")
    third_confession_icon = models.ForeignKey(
        "wagtailimages.Image",
        blank=False,
        null=True,
        related_name='+',
        on_delete=models.SET_NULL,
        help_text="64x64 icon"
    )

    fourth_confession_title = models.CharField(max_length=80, default="fourth confession")
    fourth_confession_verse = models.CharField(max_length=50, default="Mathew 1:18")
    fourth_confession_scripture = models.TextField(default="Scripture")
    fourth_confession_icon = models.ForeignKey(
        "wagtailimages.Image",
        blank=False,
        null=True,
        related_name='+',
        on_delete=models.SET_NULL,
        help_text="64x64 icon"
    )

    fifth_confession_title = models.CharField(max_length=80, default="fifth confession")
    fifth_confession_verse = models.CharField(max_length=50, default="Mathew 1:18")
    fifth_confession_scripture = models.TextField(default="Scripture")
    fifth_confession_icon = models.ForeignKey(
        "wagtailimages.Image",
        blank=False,
        null=True,
        related_name='+',
        on_delete=models.SET_NULL,
        help_text="64x64 icon"
    )

    # Sermon Videos
    sermon_video_main_title = models.CharField(max_length=80, default="Sermon Video")
    sermon_video_subtitle = models.CharField(max_length=80, default="Recent Sermon Video")
    sermon_video_description = models.TextField(default="Click play to watch video")
    sermon_video_button_text = models.CharField(max_length=30, default="Watch more")
    sermon_video_button_link = models.CharField(max_length=80, default="/watch")

    # Blog
    blog_main_title = models.CharField(max_length=80, default="Blog")
    blog_subtitle = models.CharField(max_length=100, default="Message from pastor")
    blog_description = models.TextField(default="Description for blog section")
    blog_button_text = models.CharField(max_length=50, default="See more blogs")
    blog_button_link = models.ForeignKey(
        "wagtailcore.Page",
        blank=False,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    @property
    def latest_blogs(self):
        latest_blog = BlogPage.objects.all().order_by('-blog_date')
        return latest_blog

    @property
    def latest_sermons(self):
        latest_sermon_video = SermonVideo.objects.all().order_by('-upload_date')
        return latest_sermon_video

    def get_context(self, request, *args, **kwargs):
        sermons = self.latest_sermons
        latest_blog = self.latest_blogs
        context = super(HomePage, self).get_context(request, *args, **kwargs)
        context['sermons'] = sermons
        context['latest_blogs'] = latest_blog

        return context

    # Wagtail Admin
    content_panels = Page.content_panels + [

        # Slide Section
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('first_slide_title', classname="col6"),
                FieldPanel('first_slide_verse', classname="col6"),
            ]),
            FieldRowPanel([
                FieldPanel('first_slide_button_text', classname="col6"),
                FieldPanel('first_slide_button_link', classname="col6"),
            ]),
            FieldPanel('first_slide_scripture')
        ]),

        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('second_slide_title', classname="col6"),
                FieldPanel('second_slide_verse', classname="col6"),
            ]),
            FieldRowPanel([
                FieldPanel('second_slide_button_text', classname="col6"),
                FieldPanel('second_slide_button_link', classname="col6"),
            ]),
            FieldPanel('second_slide_scripture')
        ]),

        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('third_slide_title', classname="col6"),
                FieldPanel('third_slide_verse', classname="col6"),
            ]),
            FieldRowPanel([
                FieldPanel('third_slide_button_text', classname="col6"),
                FieldPanel('third_slide_button_link', classname="col6"),
            ]),
            FieldPanel('third_slide_scripture')
        ]),

        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('fourth_slide_title', classname="col6"),
                FieldPanel('fourth_slide_verse', classname="col6"),
            ]),
            FieldRowPanel([
                FieldPanel('fourth_slide_button_text', classname="col6"),
                FieldPanel('fourth_slide_button_link', classname="col6"),
            ]),
            FieldPanel('fourth_slide_scripture')
        ]),

        # Confession Section
        FieldPanel('confession_main_title'),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('first_confession_title', classname="col6"),
                FieldPanel('first_confession_verse', classname="col6"),
            ]),
            FieldPanel('first_confession_scripture'),
            ImageChooserPanel('first_confession_icon')
        ]),

        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('second_confession_title', classname="col6"),
                FieldPanel('second_confession_verse', classname="col6"),
            ]),
            FieldPanel('second_confession_scripture'),
            ImageChooserPanel('second_confession_icon')
        ]),

        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('third_confession_title', classname="col6"),
                FieldPanel('third_confession_verse', classname="col6"),
            ]),
            FieldPanel('third_confession_scripture'),
            ImageChooserPanel('third_confession_icon')
        ]),

        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('fourth_confession_title', classname="col6"),
                FieldPanel('fourth_confession_verse', classname="col6"),
            ]),
            FieldPanel('fourth_confession_scripture'),
            ImageChooserPanel('fourth_confession_icon')
        ]),

        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('fifth_confession_title', classname="col6"),
                FieldPanel('fifth_confession_verse', classname="col6"),
            ]),
            FieldPanel('fifth_confession_scripture'),
            ImageChooserPanel('fifth_confession_icon')
        ]),

        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('sermon_video_main_title', classname="col6"),
                FieldPanel('sermon_video_subtitle', classname="col6"),
            ]),
            FieldPanel('sermon_video_description'),
            FieldRowPanel([
                FieldPanel('sermon_video_button_text', classname="col6"),
                FieldPanel('sermon_video_button_link', classname="col6"),
            ])
        ]),

        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('blog_main_title', classname="col6"),
                FieldPanel('blog_subtitle', classname="col6")
                ])
        ]),
        FieldPanel('blog_description'),
        FieldPanel('blog_button_text', classname="col6"),
        PageChooserPanel('blog_button_link'),



    ]

