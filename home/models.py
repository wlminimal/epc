from __future__ import absolute_import, unicode_literals

from django.db import models
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import datetime

from wagtail.core.models import Page, PageManager, PageQuerySet, Orderable
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, FieldRowPanel, InlinePanel, MultiFieldPanel, PageChooserPanel
from wagtail.snippets.edit_handlers import SnippetChooserPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.snippets.models import register_snippet
from wagtail.contrib.forms.models import AbstractEmailForm, AbstractFormField
from wagtail.contrib.forms.edit_handlers import FormSubmissionsPanel
from modelcluster.fields import ParentalKey


@register_snippet
class SermonDay(models.Model):
    sermon_day = models.CharField(max_length=50, default="Lord's Day")

    def __str__(self):
        return self.sermon_day


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
    service_date = models.BigIntegerField(default="2018070911")

    class Meta:
        abstract = True
        ordering = ("-service_date",)


@register_snippet
class LordDayMorningSermon(SermonVideo):

    def __str__(self):
        return "{} - {}".format(self.sermon_title, self.sermon_date)


@register_snippet
class LordDayAfternoonSermon(SermonVideo):

    def __str__(self):
        return "{} - {}".format(self.sermon_title, self.sermon_date)


@register_snippet
class RevelationSermon(SermonVideo):
    def __str__(self):
        return "{} - {}".format(self.sermon_title, self.sermon_date)


@register_snippet
class PhilippiansSermon(SermonVideo):
    def __str__(self):
        return "{} - {}".format(self.sermon_title, self.sermon_date)

@register_snippet
class GenesisSermon(SermonVideo):
    def __str__(self):
        return "{} - {}".format(self.sermon_title, self.sermon_date)

@register_snippet
class RomansSermon(SermonVideo):
    def __str__(self):
        return "{} - {}".format(self.sermon_title, self.sermon_date)


@register_snippet
class PsalmsSermon(SermonVideo):
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


# class BlogPageQuerySet(PageQuerySet):
#     def latest_blogs(self):
#         latest_blogs = self.order_by('-blog_date')
#         return latest_blogs
#
# BlogPageManager = PageManager.from_queryset(BlogPageQuerySet)


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

    @property
    def latest_blogs(self):
        latest_blogs = BlogPage.objects.all().order_by('-blog_date')[:3]
        return latest_blogs

    def get_context(self, request, *args, **kwargs):
        latest_blogs = self.latest_blogs
        context = super(BlogPage, self).get_context(request, *args, **kwargs)
        context['latest_blogs'] = latest_blogs
        return context

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


class Event(models.Model):
    event_title = models.CharField(max_length=50, default="Event Title")
    upload_date = models.DateTimeField(auto_now_add=True)
    event_date = models.CharField(max_length=20, default="6월 23일")
    event_time = models.CharField(max_length=20, default="11:00 AM")
    event_description = models.TextField(max_length=150, default="Event Description")

    class Meta:
        abstract = True


@register_snippet
class FeaturedEvent(Event):
    event_image = models.ForeignKey(
        "wagtailimages.Image",
        blank=False,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    def __str__(self):
        return self.event_title + "-" + self.event_date


@register_snippet
class RegularEvent(Event):

    def __str__(self):
        return self.event_title + "-" + self.event_date


class EventIndexPage(Page):
    event_hero_title = models.TextField(default="Event")
    event_hero_subtitle = models.TextField(default="Subtitle for Event")
    event_featured_name = models.CharField(max_length=100, default="Featured Event")

    featured_event = FeaturedEvent.objects.all().order_by("-upload_date")[:2]
    regular_event = RegularEvent.objects.all().order_by("-upload_date")

    def get_context(self, request, *args, **kwargs):
        f_events = self.featured_event
        r_events = self.regular_event

        paginator = Paginator(r_events, 8)
        page = request.GET.get('page')

        try:
            r_events = paginator.page(page)
        except PageNotAnInteger:
            r_events = paginator.page(1)
        except EmptyPage:
            r_events = paginator.page(paginator.num_pages)

        context = super(EventIndexPage, self).get_context(request, *args, **kwargs)
        context['f_events'] = f_events
        context['r_events'] = r_events

        return context

    content_panels = Page.content_panels + [
        FieldPanel('event_hero_title'),
        FieldPanel('event_hero_subtitle'),
        FieldPanel('event_featured_name'),
    ]


class SermonPage(Page):
    subpage_types = ["home.LordDayMorningSermonPage", "home.LordDayAfternoonSermonPage", "home.FridaySermonPage"]


class LordDayMorningSermonPage(Page):
    hero_title = models.CharField(max_length=80, default="주일 설교 영상")
    hero_subtitle = models.TextField(default="성경을 성경으로 해석한다")
    hero_description = RichTextField(default="Description")

    sermon_main_title_1 = models.CharField(max_length=100, default="최신 주일 예배 설교 영상")
    sermon_main_title_2 = models.CharField(max_length=100, default="지난 주일 예배 설교 영상들")

    @property
    def latest_morning_sermons(self):
        latest_morning_sermon_video = LordDayMorningSermon.objects.all().order_by('-service_date')[:2]
        return latest_morning_sermon_video

    @property
    def past_morning_sermons(self):
        past_morning_sermon_video = LordDayMorningSermon.objects.all().order_by('-service_date')[2:]
        return past_morning_sermon_video

    def get_context(self, request, *args, **kwargs):
        latest_sermons = self.latest_morning_sermons
        past_sermons = self.past_morning_sermons

        paginator = Paginator(past_sermons, 8)
        page = request.GET.get('page')

        try:
            past_sermons = paginator.page(page)
        except PageNotAnInteger:
            past_sermons = paginator.page(1)
        except EmptyPage:
            past_sermons = paginator.page(paginator.num_pages)

        context = super(LordDayMorningSermonPage, self).get_context(request, *args, **kwargs)
        context['latest_sermons'] = latest_sermons
        context['past_sermons'] = past_sermons

        return context

    content_panels = Page.content_panels + [
        FieldPanel('hero_title'),
        FieldPanel('hero_subtitle'),
        FieldPanel('hero_description'),
        FieldPanel('sermon_main_title_1'),
        FieldPanel('sermon_main_title_2'),
    ]


class LordDayAfternoonSermonPage(Page):

    hero_title = models.CharField(max_length=80, default="주일 설교 영상")
    hero_subtitle = models.TextField(default="성경을 성경으로 해석한다")
    hero_description = RichTextField(default="Description")

    sermon_main_title_1 = models.CharField(max_length=100, default="최신 주일 예배 설교 영상")
    sermon_main_title_2 = models.CharField(max_length=100, default="지난 주일 예배 설교 영상들")

    @property
    def latest_afternoon_sermons(self):
        latest_afternoon_sermon_video = LordDayAfternoonSermon.objects.all().order_by('-upload_date')[:2]
        return latest_afternoon_sermon_video

    @property
    def past_afternoon_sermons(self):
        past_afternoon_sermon_video = LordDayAfternoonSermon.objects.all().order_by('-upload_date')[2:]
        return past_afternoon_sermon_video

    def get_context(self, request, *args, **kwargs):
        latest_sermons = self.latest_afternoon_sermons
        past_sermons = self.past_afternoon_sermons

        paginator = Paginator(past_sermons, 8)
        page = request.GET.get('page')

        try:
            past_sermons = paginator.page(page)
        except PageNotAnInteger:
            past_sermons = paginator.page(1)
        except EmptyPage:
            past_sermons = paginator.page(paginator.num_pages)

        context = super(LordDayAfternoonSermonPage, self).get_context(request, *args, **kwargs)
        context['latest_sermons'] = latest_sermons
        context['past_sermons'] = past_sermons

        return context

    content_panels = Page.content_panels + [
        FieldPanel('hero_title'),
        FieldPanel('hero_subtitle'),
        FieldPanel('hero_description'),
        FieldPanel('sermon_main_title_1'),
        FieldPanel('sermon_main_title_2'),
    ]


class FridaySermonPage(Page):
    f_sermon_hero_title = models.CharField(max_length=80, default="금요 예배 설교 영상")
    f_sermon_hero_subtitle = models.TextField(default="요한 계시록 강해 / 특별 강사 설교")
    f_sermon_hero_description = RichTextField(default="Description")

    f_sermon_bible_1 = models.CharField(max_length=100, default="요한 계시록")
    f_sermon_bible_1_main_title_1 = models.CharField(max_length=100, default="최신 요한계시록 강해 영상")
    f_sermon_bible_1_main_title_2 = models.CharField(max_length=100, default="지난 요한계시록 강해 영상들")

    f_sermon_bible_2 = models.CharField(max_length=100, default="로마서")
    f_sermon_bible_2_main_title_1 = models.CharField(max_length=100, default="최신 로마서 강해 영상")
    f_sermon_bible_2_main_title_2 = models.CharField(max_length=100, default="지난 로마서 강해 영상들")

    f_sermon_bible_3 = models.CharField(max_length=100, default="빌립보서")
    f_sermon_bible_3_main_title_1 = models.CharField(max_length=100, default="최신 빌립보서 강해 영상")
    f_sermon_bible_3_main_title_2 = models.CharField(max_length=100, default="지난 빌립보서 강해 영상들")

    f_sermon_bible_4 = models.CharField(max_length=100, default="시편")
    f_sermon_bible_4_main_title_1 = models.CharField(max_length=100, default="최신 시편 강해 영상")
    f_sermon_bible_4_main_title_2 = models.CharField(max_length=100, default="지난 시편 강해 영상들")

    @property
    def latest_revelation_sermons(self):
        latest_revelation_video = RevelationSermon.objects.all().order_by('-upload_date')[:2]
        return latest_revelation_video

    @property
    def past_revelation_sermons(self):
        past_revelation_video = RevelationSermon.objects.all().order_by('-upload_date')[2:]
        return past_revelation_video

    @property
    def roman_sermon(self):
        roman_video = RomansSermon.objects.all().order_by('-upload_date')
        return roman_video

    @property
    def philippians_sermon(self):
        philippians_video = PhilippiansSermon.objects.all().order_by('-upload_date')
        return philippians_video

    @property
    def genesis_sermon(self):
        genesis_video = GenesisSermon.objects.all().order_by('-upload_date')
        return genesis_video

    @property
    def psalm_sermon(self):
        psalm_video = PsalmsSermon.objects.all().order_by('-upload_date')
        return psalm_video

    def get_context(self, request, *args, **kwargs):
        latest_revelation_sermons = self.latest_revelation_sermons
        past_revelation_sermons = self.past_revelation_sermons
        roman_sermon = self.roman_sermon
        philippians_sermon = self.philippians_sermon
        psalm_sermon = self.psalm_sermon
        genesis_sermon = self.genesis_sermon

        paginator = Paginator(past_revelation_sermons, 8)
        page = request.GET.get('page')

        try:
            past_revelation_sermons = paginator.page(page)
        except PageNotAnInteger:
            past_revelation_sermons = paginator.page(1)
        except EmptyPage:
            past_revelation_sermons = paginator.page(paginator.num_pages)

        context = super(FridaySermonPage, self).get_context(request, *args, **kwargs)
        context['latest_revelation_sermons'] = latest_revelation_sermons
        context['past_revelation_sermons'] = past_revelation_sermons
        context['latest_roman_sermon'] = roman_sermon[:2]
        context['past_roman_sermon'] = roman_sermon[2:]
        context['latest_philippians_sermon'] = philippians_sermon[:2]
        context['past_philippians_sermon'] = philippians_sermon[2:]
        context['latest_psalm_sermon'] = psalm_sermon[:2]
        context['past_psalm_sermon'] = psalm_sermon[2:]
        context['latest_genesis_sermon'] = genesis_sermon[:2]
        context['past_genesis_sermon'] = genesis_sermon[2:]

        return context

    content_panels = Page.content_panels + [
        FieldPanel('f_sermon_hero_title'),
        FieldPanel('f_sermon_hero_subtitle'),
        FieldPanel('f_sermon_hero_description'),
        FieldPanel('f_sermon_bible_1'),
        FieldPanel('f_sermon_bible_1_main_title_1'),
        FieldPanel('f_sermon_bible_1_main_title_2'),

        FieldPanel('f_sermon_bible_2'),
        FieldPanel('f_sermon_bible_2_main_title_1'),
        FieldPanel('f_sermon_bible_2_main_title_2'),

        # FieldPanel('f_sermon_bible_3'),
        # FieldPanel('f_sermon_bible_3_main_title_1'),
        # FieldPanel('f_sermon_bible_3_main_title_2'),

        # FieldPanel('f_sermon_bible_4'),
        # FieldPanel('f_sermon_bible_4_main_title_1'),
        # FieldPanel('f_sermon_bible_4_main_title_2'),
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

    # Event
    event_main_title = models.CharField(max_length=80, default="Event")
    event_subtitle = models.CharField(max_length=100, default="Church Event")
    event_description = models.TextField(default="Description for Church Event")
    event_button_text = models.CharField(max_length=50, default="See more events")
    event_button_link = models.ForeignKey(
        "wagtailcore.Page",
        blank=False,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    # Service Info
    service_title = models.CharField(max_length=50, default="EPC Worship Service")
    service_scripture = models.TextField(default="Scripture for EPC service section")
    service_verse = models.CharField(max_length=50, default="Hebrew 10:25")
    service_hero_image = models.ForeignKey(
        "wagtailimages.Image",
        blank=False,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    service_subtitle = models.CharField(max_length=50, default="Service Schedule")

    service_lord_day = models.CharField(max_length=50, default="Lord's Day")
    service_lord_day_schedule_1 = models.CharField(max_length=20, default="5:30 AM")
    service_lord_day_schedule_2 = models.CharField(max_length=20, default="9:30 AM")
    service_lord_day_schedule_3 = models.CharField(max_length=20, default="11:00 AM")
    service_lord_day_schedule_4 = models.CharField(max_length=20, default="2:00 PM")

    service_friday_day = models.CharField(max_length=20, default="Friday Day")
    service_friday_day_schedule = models.CharField(max_length=20, default="7:30 PM")

    service_button_text = models.CharField(max_length=50, default="See more Service info")
    service_button_link = models.ForeignKey(
        "wagtailcore.Page",
        blank=False,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    # EPC Mission Section
    mission_main_title = models.CharField(max_length=50, default="EPC Mission")
    mission_scripture = models.TextField(default="Scripture for mission section")
    mission_verse = models.CharField(max_length=50, default="Hebrew 10:25")

    # mission card
    mission_card_image = models.ForeignKey(
        "wagtailimages.Image",
        blank=False,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    mission_card_title = models.CharField(max_length=30, default="Mission")
    mission_card_subtitle = models.CharField(max_length=50, default="Nicaragua")
    mission_card_button_text = models.CharField(max_length=10, default="Learn more")
    mission_card_button_link = models.ForeignKey(
        "wagtailcore.Page",
        blank=False,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    # education card
    education_card_image = models.ForeignKey(
        "wagtailimages.Image",
        blank=False,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    education_card_title = models.CharField(max_length=30, default="Education")
    education_card_subtitle = models.CharField(max_length=50, default="Korean School and TIU")
    education_card_button_text = models.CharField(max_length=10, default="Learn more")
    education_card_button_link = models.ForeignKey(
        "wagtailcore.Page",
        blank=False,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    # Offering card
    offering_card_image = models.ForeignKey(
        "wagtailimages.Image",
        blank=False,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    offering_card_title = models.CharField(max_length=30, default="Offering")
    offering_card_subtitle = models.CharField(max_length=50, default="Offering & Donation")
    offering_card_button_text = models.CharField(max_length=10, default="Learn more")
    offering_card_button_link = models.ForeignKey(
        "wagtailcore.Page",
        blank=False,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    # Contact card
    contact_card_image = models.ForeignKey(
        "wagtailimages.Image",
        blank=False,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    contact_card_title = models.CharField(max_length=30, default="Contact")
    contact_card_subtitle = models.CharField(max_length=50, default="Keep in touch with us")
    contact_card_button_text = models.CharField(max_length=10, default="Learn more")
    contact_card_button_link = models.ForeignKey(
        "wagtailcore.Page",
        blank=False,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )


    @property
    def latest_event(self):
        latest_event = RegularEvent.objects.all().order_by('-upload_date')
        latest_event = latest_event[:4]
        return latest_event

    @property
    def latest_blogs(self):
        latest_blog = BlogPage.objects.all().live().order_by('-blog_date')
        latest_blog = latest_blog[:3]
        return latest_blog

    @property
    def latest_sermons(self):
        latest_sermon_video = LordDayMorningSermon.objects.all().order_by('-upload_date')[:2]
        return latest_sermon_video

    def get_context(self, request, *args, **kwargs):
        sermons = self.latest_sermons
        latest_blog = self.latest_blogs
        latest_event = self.latest_event

        context = super(HomePage, self).get_context(request, *args, **kwargs)
        context['sermons'] = sermons
        context['latest_blogs'] = latest_blog
        context['latest_event'] = latest_event

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

        # Blog
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('blog_main_title', classname="col6"),
                FieldPanel('blog_subtitle', classname="col6")
                ])
        ]),
        FieldPanel('blog_description'),
        FieldPanel('blog_button_text', classname="col6"),
        PageChooserPanel('blog_button_link'),

        # Event
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('event_main_title', classname="col6"),
                FieldPanel('event_subtitle', classname="col6")
            ])
        ]),
        FieldPanel('event_description'),
        FieldPanel('event_button_text', classname="col6"),
        PageChooserPanel('event_button_link'),

        # Service Info
        FieldPanel('service_title'),
        FieldPanel('service_scripture'),
        FieldPanel('service_verse'),
        ImageChooserPanel('service_hero_image'),
        FieldPanel('service_subtitle'),
        FieldPanel('service_lord_day'),

        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('service_lord_day_schedule_1', classname="col3"),
                FieldPanel('service_lord_day_schedule_2', classname="col3"),
                FieldPanel('service_lord_day_schedule_3', classname="col3"),
                FieldPanel('service_lord_day_schedule_4', classname="col3"),
            ])
        ]),

        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('service_friday_day', classname="col6"),
                FieldPanel('service_friday_day_schedule', classname="col6"),
            ])
        ]),

        FieldPanel('service_button_text'),
        PageChooserPanel('service_button_link'),

        # EPC Mission Section

        FieldPanel('mission_main_title'),
        FieldPanel('mission_scripture'),
        FieldPanel('mission_verse'),

        # Mission Card
        ImageChooserPanel('mission_card_image'),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('mission_card_title', classname="col4"),
                FieldPanel('mission_card_subtitle', classname="col4"),
                FieldPanel('mission_card_button_text', classname="col4"),
            ])
        ]),
        PageChooserPanel('mission_card_button_link'),

        # Mission Card
        ImageChooserPanel('education_card_image'),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('education_card_title', classname="col4"),
                FieldPanel('education_card_subtitle', classname="col4"),
                FieldPanel('education_card_button_text', classname="col4"),
            ])
        ]),
        PageChooserPanel('education_card_button_link'),

        # Offering Card
        ImageChooserPanel('offering_card_image'),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('offering_card_title', classname="col4"),
                FieldPanel('offering_card_subtitle', classname="col4"),
                FieldPanel('offering_card_button_text', classname="col4"),
            ])
        ]),
        PageChooserPanel('offering_card_button_link'),

        # Contact Card
        ImageChooserPanel('contact_card_image'),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('contact_card_title', classname="col4"),
                FieldPanel('contact_card_subtitle', classname="col4"),
                FieldPanel('contact_card_button_text', classname="col4"),
            ])
        ]),
        PageChooserPanel('contact_card_button_link')
    ]


class AboutPage(Page):
    about_hero_title_1 = models.CharField(max_length=80, default="경건한 예배")
    about_hero_title_2 = models.CharField(max_length=80, default="성경 중심적 설교")
    about_hero_title_3 = models.CharField(max_length=80, default="이웃을 섬기는 교회")

    about_main_title = models.CharField(max_length=80, default="섬기는 목사님들")

    pastor_picture_1 = models.ForeignKey(
        "wagtailimages.Image",
        blank=False,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    pastor_name_1 = models.CharField(max_length=50, default="김정오 목사")
    pastor_title_1 = models.CharField(max_length=80, default="동부교회 담임목사")
    pastor_message_1 = RichTextField(default="목사님들 인사말씀")

    pastor_picture_2 = models.ForeignKey(
        "wagtailimages.Image",
        blank=False,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    pastor_name_2 = models.CharField(max_length=50, default="나은수 목사")
    pastor_title_2 = models.CharField(max_length=80, default="동부교회 목사")
    pastor_message_2 = RichTextField(default="목사님들 인사말씀")

    # History Section
    history_title = models.CharField(max_length=50, default="교회 연혁")
    history_scripture = models.TextField(default="Scripture for History section")
    history_verse = models.CharField(max_length=80, default="Act 20:28")

    history_card_title = models.TextField(default="history of our church")
    history_content = RichTextField(default="History of our church")

    service_main_title = models.CharField(max_length=80, default="Information about Service")
    service_scripture = models.TextField(default="Scripture for service section")
    service_verse = models.CharField(max_length=80, default="Act 20:28")

    service_day_1 = models.CharField(max_length=50, default="Lord's Day")

    service_gen_1 = models.CharField(max_length=20, default="Adult")
    service_schedule_1 = models.CharField(max_length=20, default="5:30 AM")
    service_schedule_2 = models.CharField(max_length=20, default="9:30 AM")
    service_schedule_3 = models.CharField(max_length=20, default="11:00 AM")
    service_schedule_4 = models.CharField(max_length=20, default="2:00 PM")

    service_gen_2 = models.CharField(max_length=20, default="Youth Group")
    service_schedule_5 = models.CharField(max_length=20, default="10:00 AM")
    service_schedule_6 = models.CharField(max_length=20, default="1:30 PM")

    service_gen_3 = models.CharField(max_length=20, default="Elementary")
    service_schedule_7 = models.CharField(max_length=20, default="11:00 AM")
    service_schedule_8 = models.CharField(max_length=20, default="2:00 PM")

    service_gen_4 = models.CharField(max_length=20, default="Kinder")
    service_schedule_9 = models.CharField(max_length=20, default="11:00 AM")
    service_schedule_10 = models.CharField(max_length=20, default="2:00 PM")

    service_gen_5 = models.CharField(max_length=20, default="Kinder")
    service_schedule_11 = models.CharField(max_length=20, default="11:00 AM")

    service_day_2 = models.CharField(max_length=50, default="Friday Day")
    service_schedule_12 = models.CharField(max_length=20, default="7:30 PM")

    service_day_3 = models.CharField(max_length=50, default="Saturday Day")
    service_schedule_13 = models.CharField(max_length=20, default="5:30 PM")

    content_panels = Page.content_panels + [
        FieldPanel('about_hero_title_1'),
        FieldPanel('about_hero_title_2'),
        FieldPanel('about_hero_title_3'),
        FieldPanel('about_main_title'),

        ImageChooserPanel('pastor_picture_1'),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('pastor_name_1'),
                FieldPanel('pastor_title_1'),
            ])
        ]),

        FieldPanel('pastor_message_1'),

        ImageChooserPanel('pastor_picture_2'),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('pastor_name_2'),
                FieldPanel('pastor_title_2'),
            ])
        ]),

        FieldPanel('pastor_message_2'),

        FieldPanel('history_title'),
        FieldPanel('history_scripture'),
        FieldPanel('history_verse'),

        FieldPanel('history_card_title'),
        FieldPanel('history_content'),

        FieldPanel('service_main_title'),
        FieldPanel('service_scripture'),
        FieldPanel('service_verse'),

        FieldPanel('service_day_1'),
        FieldPanel('service_gen_1'),
        FieldPanel('service_schedule_1'),
        FieldPanel('service_schedule_2'),
        FieldPanel('service_schedule_3'),
        FieldPanel('service_schedule_4'),

        FieldPanel('service_gen_2'),
        FieldPanel('service_schedule_5'),
        FieldPanel('service_schedule_6'),

        FieldPanel('service_gen_3'),
        FieldPanel('service_schedule_7'),
        FieldPanel('service_schedule_8'),

        FieldPanel('service_gen_4'),
        FieldPanel('service_schedule_9'),
        FieldPanel('service_schedule_10'),

        FieldPanel('service_gen_5'),
        FieldPanel('service_schedule_11'),

        FieldPanel('service_day_2'),
        FieldPanel('service_schedule_12'),

        FieldPanel('service_day_3'),
        FieldPanel('service_schedule_13'),

    ]


class GenerationPage(Page):

    subpage_types = ["home.KidsPage", "home.NurseryPage", "home.ElementaryPage", "home.YouthGroupPage", "home.YoungAdultPage"]


class NurseryPage(Page):
    # 영아부 페이지
    nursery_hero_title = models.CharField(max_length=80, default="동부 교회 영아부")
    nursery_here_verse = models.CharField(max_length=80, default="마태복음 18장 2-3절")
    nursery_hero_scripture = models.TextField(default="Scripture for kids page")

    nursery_tab_title_1 = models.CharField(max_length=30, default="영아부")

    nursery_tab_content_title_1 = models.CharField(max_length=30, default="영아부")
    nursery_tab_content_age = models.CharField(max_length=50, default="0세부터 3세")
    nursery_tab_content_info = models.TextField(default="예배 안내: 오전 11:00 23번 방")
    nursery_tab_content = RichTextField(default="Intro to Nursery")
    nursery_tab_image_1 = models.ForeignKey(
        "wagtailimages.Image",
        blank=False,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    nursery_tab_image_2 = models.ForeignKey(
        "wagtailimages.Image",
        blank=False,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    nursery_tab_image_3 = models.ForeignKey(
        "wagtailimages.Image",
        blank=False,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    content_panels = Page.content_panels + [
        FieldPanel('nursery_hero_title'),
        FieldPanel('nursery_here_verse'),
        FieldPanel('nursery_hero_scripture'),

        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('nursery_tab_title_1', classname="full"),
            ])
        ]),

        FieldPanel('nursery_tab_content_title_1'),
        FieldPanel('nursery_tab_content_age'),
        FieldPanel('nursery_tab_content_info'),
        FieldPanel('nursery_tab_content'),
        ImageChooserPanel('nursery_tab_image_1'),
        ImageChooserPanel('nursery_tab_image_2'),
        ImageChooserPanel('nursery_tab_image_3'),

    ]


class KidsPage(Page):
    # 유치부 페이지
    kids_hero_title = models.CharField(max_length=80, default="동부 교회 유치부")
    kids_hero_verse = models.CharField(max_length=80, default="마태복음 18장 2-3절")
    kids_hero_scripture = models.TextField(default="Scripture for kids page")

    kids_tab_title_1 = models.CharField(max_length=30, default="유치부")

    kinder_tab_content_title_1 = models.CharField(max_length=30, default="유치부")
    kinder_tab_content_age = models.CharField(max_length=50, default="0세부터 3세")
    kinder_tab_content_info = models.TextField(default="예배 안내: 오전 11:00 23번 방")
    kinder_tab_content = RichTextField(default="Intro to Kinder")
    kinder_tab_image_1 = models.ForeignKey(
        "wagtailimages.Image",
        blank=False,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    kinder_tab_image_2 = models.ForeignKey(
        "wagtailimages.Image",
        blank=False,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    kinder_tab_image_3 = models.ForeignKey(
        "wagtailimages.Image",
        blank=False,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    content_panels = Page.content_panels + [
        FieldPanel('kids_hero_title'),
        FieldPanel('kids_hero_verse'),
        FieldPanel('kids_hero_scripture'),

        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('kids_tab_title_1', classname="full"),
            ])
        ]),

        FieldPanel('kinder_tab_content_title_1'),
        FieldPanel('kinder_tab_content_age'),
        FieldPanel('kinder_tab_content_info'),
        FieldPanel('kinder_tab_content'),
        ImageChooserPanel('kinder_tab_image_1'),
        ImageChooserPanel('kinder_tab_image_2'),
        ImageChooserPanel('kinder_tab_image_3'),
    ]


class ElementaryPage(Page):
    # 초등부 페이지
    elem_hero_title = models.CharField(max_length=80, default="동부 교회 초등부")
    elem_hero_verse = models.CharField(max_length=80, default="마태복음 18장 2-3절")
    elem_hero_scripture = models.TextField(default="Scripture for kids page")

    elem_tab_title_1 = models.CharField(max_length=30, default="초등부")

    elem_tab_content_title_1 = models.CharField(max_length=30, default="초등부")
    elem_tab_content_age = models.CharField(max_length=50, default="0세부터 3세")
    elem_tab_content_info = models.TextField(default="예배 안내: 오전 11:00 23번 방")
    elem_tab_content = RichTextField(default="Intro to Kinder")
    elem_tab_image_1 = models.ForeignKey(
        "wagtailimages.Image",
        blank=False,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    elem_tab_image_2 = models.ForeignKey(
        "wagtailimages.Image",
        blank=False,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    elem_tab_image_3 = models.ForeignKey(
        "wagtailimages.Image",
        blank=False,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    content_panels = Page.content_panels + [
        FieldPanel('elem_hero_title'),
        FieldPanel('elem_hero_verse'),
        FieldPanel('elem_hero_scripture'),

        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('elem_tab_title_1', classname="full"),
            ])
        ]),

        FieldPanel('elem_tab_content_title_1'),
        FieldPanel('elem_tab_content_age'),
        FieldPanel('elem_tab_content_info'),
        FieldPanel('elem_tab_content'),
        ImageChooserPanel('elem_tab_image_1'),
        ImageChooserPanel('elem_tab_image_2'),
        ImageChooserPanel('elem_tab_image_3'),
    ]


class YouthGroupPage(Page):
    yg_hero_title = models.CharField(max_length=80, default="동부 교회 주일 학교")
    yg_hero_verse = models.CharField(max_length=80, default="마태복음 18장 2-3절")
    yg_hero_scripture = models.TextField(default="Scripture for kids page")

    yg_tab_content_title_1 = models.CharField(max_length=30, default="중고등부")
    yg_tab_content_age = models.CharField(max_length=50, default="6학년부터 12학년까지")
    yg_tab_content_info = models.TextField(default="예배 안내: 주일 오전 10:30분 성경공부 / 오후 2시 예배 (중고등부실)")
    yg_tab_content = RichTextField(default="Intro to YG")
    yg_tab_image_1 = models.ForeignKey(
        "wagtailimages.Image",
        blank=False,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    yg_tab_image_2 = models.ForeignKey(
        "wagtailimages.Image",
        blank=False,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    yg_tab_image_3 = models.ForeignKey(
        "wagtailimages.Image",
        blank=False,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    content_panels = Page.content_panels + [
        FieldPanel('yg_hero_title'),
        FieldPanel('yg_hero_verse'),
        FieldPanel('yg_hero_scripture'),

        FieldPanel('yg_tab_content_title_1'),
        FieldPanel('yg_tab_content_age'),
        FieldPanel('yg_tab_content_info'),
        FieldPanel('yg_tab_content'),
        ImageChooserPanel('yg_tab_image_1'),
        ImageChooserPanel('yg_tab_image_2'),
        ImageChooserPanel('yg_tab_image_3'),
    ]


class YoungAdultPage(Page):
    ya_hero_title = models.CharField(max_length=80, default="청년부")
    ya_hero_verse = models.CharField(max_length=80, default="Psalm 119:9-16")
    ya_hero_scripture = models.TextField(default="Scripture for kids page")

    ya_tab_content_title_1 = models.CharField(max_length=30, default="청년부")
    ya_tab_content_age = models.CharField(max_length=50, default="성인 모든 청년을 대상으로 합니다.")
    ya_tab_content_info = models.TextField(default="예배 안내: 오후 1:00 청년부실")
    ya_tab_content = RichTextField(default="Intro to 청년부")
    ya_tab_image_1 = models.ForeignKey(
        "wagtailimages.Image",
        blank=False,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    ya_tab_image_2 = models.ForeignKey(
        "wagtailimages.Image",
        blank=False,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    ya_tab_image_3 = models.ForeignKey(
        "wagtailimages.Image",
        blank=False,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    content_panels = Page.content_panels + [
        FieldPanel('ya_hero_title'),
        FieldPanel('ya_hero_verse'),
        FieldPanel('ya_hero_scripture'),

        FieldPanel('ya_tab_content_title_1'),
        FieldPanel('ya_tab_content_age'),
        FieldPanel('ya_tab_content_info'),
        FieldPanel('ya_tab_content'),
        ImageChooserPanel('ya_tab_image_1'),
        ImageChooserPanel('ya_tab_image_2'),
        ImageChooserPanel('ya_tab_image_3'),
    ]


class EMPage(Page):
    em_hero_title = models.CharField(max_length=80, default="English Ministry")
    em_hero_verse = models.CharField(max_length=80, default="Psalm 119:9-16")
    em_hero_scripture = models.TextField(default="Scripture for English Ministry")

    em_tab_title_1 = models.CharField(max_length=100, default="English Ministry")
    em_tab_title_2 = models.CharField(max_length=100, default="Pastor & Staffs")
    em_tab_content_title_1 = models.TextField(default="English Ministry")
    em_tab_content_vision = models.TextField(default="English Ministry.")
    em_tab_content_mission = models.TextField(default="예배 안내: 오후 1:00 청년부실")
    em_tab_content_1 = RichTextField(default="Intro to English Ministry")
    em_tab_image_1 = models.ForeignKey(
        "wagtailimages.Image",
        blank=False,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    em_tab_image_2 = models.ForeignKey(
        "wagtailimages.Image",
        blank=False,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    em_tab_image_3 = models.ForeignKey(
        "wagtailimages.Image",
        blank=False,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    em_tab_content_title_2 = models.TextField(default="English Ministry")
    em_tab_content_pastor = models.TextField(default="English Ministry.")
    em_tab_content_pastor_2 = models.TextField(default="예배 안내: 오후 1:00 청년부실")
    em_tab_content_2 = RichTextField(default="Intro to English Ministry")
    em_tab_image_4 = models.ForeignKey(
        "wagtailimages.Image",
        blank=False,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    em_tab_image_5 = models.ForeignKey(
        "wagtailimages.Image",
        blank=False,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    em_tab_image_6 = models.ForeignKey(
        "wagtailimages.Image",
        blank=False,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    content_panels = Page.content_panels + [
        FieldPanel('em_hero_title'),
        FieldPanel('em_hero_verse'),
        FieldPanel('em_hero_scripture'),

        FieldPanel('em_tab_title_1'),
        FieldPanel('em_tab_title_2'),

        FieldPanel('em_tab_content_title_1'),
        FieldPanel('em_tab_content_vision'),
        FieldPanel('em_tab_content_mission'),
        FieldPanel('em_tab_content_1'),
        ImageChooserPanel('em_tab_image_1'),
        ImageChooserPanel('em_tab_image_2'),
        ImageChooserPanel('em_tab_image_3'),

        FieldPanel('em_tab_content_title_2'),
        FieldPanel('em_tab_content_pastor'),
        FieldPanel('em_tab_content_pastor_2'),
        FieldPanel('em_tab_content_2'),
        ImageChooserPanel('em_tab_image_4'),
        ImageChooserPanel('em_tab_image_5'),
        ImageChooserPanel('em_tab_image_6'),
    ]



class MissionPage(Page):
    subpage_types = ["home.NicaraguaPage"]


class NicaraguaPage(Page):
    mission_hero_title = models.CharField(max_length=80, default="동부 교회 선교부")
    mission_hero_verse = models.CharField(max_length=80, default="이사야 6장 8절")
    mission_hero_scripture = models.TextField(default="내가 또 주의 목소리를 들은즉 이르시되 내가 누구를 보내며 누가 우리를 위하여 갈꼬 그 때에 내가 가로되 내가 여기 있나이다 나를 보내소서")

    nicaragua_tab_content_title_1 = models.CharField(max_length=30, default="니카라과 선교지")
    nicaragua_tab_pastor = models.CharField(max_length=50, default="선교사 : 김성헌 목사")
    nicaragua_tab_contact_info = models.TextField(default="연락처 : nicaragua@epcla.org")
    nicaragua_tab_content = RichTextField(default="Intro to English Ministry")
    nicaragua_tab_image_1 = models.ForeignKey(
        "wagtailimages.Image",
        blank=False,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    nicaragua_tab_image_2 = models.ForeignKey(
        "wagtailimages.Image",
        blank=False,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    nicaragua_tab_image_3 = models.ForeignKey(
        "wagtailimages.Image",
        blank=False,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    content_panels = Page.content_panels + [
        FieldPanel('mission_hero_title'),
        FieldPanel('mission_hero_verse'),
        FieldPanel('mission_hero_scripture'),

        FieldPanel('nicaragua_tab_content_title_1'),
        FieldPanel('nicaragua_tab_pastor'),
        FieldPanel('nicaragua_tab_contact_info'),
        FieldPanel('nicaragua_tab_content'),
        ImageChooserPanel('nicaragua_tab_image_1'),
        ImageChooserPanel('nicaragua_tab_image_2'),
        ImageChooserPanel('nicaragua_tab_image_3'),
    ]


class EducationPage(Page):
    subpage_types = ["home.KoreanSchoolPage", "home.TiuPage"]


class KoreanSchoolPage(Page):
    kschool_hero_title = models.CharField(max_length=80, default="동부 교회 한국 학교")
    kschool_hero_verse = models.CharField(max_length=80, default="이사야 6장 8절")
    kschool_hero_scripture = models.TextField(
        default="내가 또 주의 목소리를 들은즉 이르시되 내가 누구를 보내며 누가 우리를 위하여 갈꼬 그 때에 내가 가로되 내가 여기 있나이다 나를 보내소서")

    kschool_tab_content_title_1 = models.CharField(max_length=30, default="동부 교회 한국 학교")
    kschool_tab_pastor = models.CharField(max_length=50, default="교장 : 정 삼숙 박사")
    kschool_tab_contact_info = models.TextField(default="연락처 : koreanschool@epcla.org")
    kschool_tab_content = RichTextField(default="Intro to English Ministry")
    kschool_tab_image_1 = models.ForeignKey(
        "wagtailimages.Image",
        blank=False,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    kschool_tab_image_2 = models.ForeignKey(
        "wagtailimages.Image",
        blank=False,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    kschool_tab_image_3 = models.ForeignKey(
        "wagtailimages.Image",
        blank=False,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    content_panels = Page.content_panels + [
        FieldPanel('kschool_hero_title'),
        FieldPanel('kschool_hero_verse'),
        FieldPanel('kschool_hero_scripture'),

        FieldPanel('kschool_tab_content_title_1'),
        FieldPanel('kschool_tab_pastor'),
        FieldPanel('kschool_tab_contact_info'),
        FieldPanel('kschool_tab_content'),
        ImageChooserPanel('kschool_tab_image_1'),
        ImageChooserPanel('kschool_tab_image_2'),
        ImageChooserPanel('kschool_tab_image_3'),
    ]


class TiuPage(Page):
    tyndale_hero_title = models.CharField(max_length=80, default="틴데일 신학교")
    tyndale_hero_verse = models.CharField(max_length=80, default="이사야 6장 8절")
    tyndale_hero_scripture = models.TextField(
        default="내가 또 주의 목소리를 들은즉 이르시되 내가 누구를 보내며 누가 우리를 위하여 갈꼬 그 때에 내가 가로되 내가 여기 있나이다 나를 보내소서")

    tyndale_tab_content_title_1 = models.CharField(max_length=30, default="틴데일 신학교")
    tyndale_tab_pastor = models.CharField(max_length=50, default="이사장 : 지 창수 목사")
    tyndale_tab_contact_info = models.TextField(default="www.tyndaleinternationaluniversity.com")
    tyndale_tab_content = RichTextField(default="Intro to English Ministry")
    tyndale_tab_image_1 = models.ForeignKey(
        "wagtailimages.Image",
        blank=False,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    content_panels = Page.content_panels + [
        FieldPanel('tyndale_hero_title'),
        FieldPanel('tyndale_hero_verse'),
        FieldPanel('tyndale_hero_scripture'),

        FieldPanel('tyndale_tab_content_title_1'),
        FieldPanel('tyndale_tab_pastor'),
        FieldPanel('tyndale_tab_contact_info'),
        FieldPanel('tyndale_tab_content'),
        ImageChooserPanel('tyndale_tab_image_1'),
    ]


class FormField(AbstractFormField):
    page = ParentalKey('ContactPage', related_name='form_fields')


class ContactPage(AbstractEmailForm):
    contact_hero_title = models.CharField(max_length=100, default="모든 분들의 연락을 기다립니다.")
    contact_hero_subtitle = models.TextField(default="교회와 사역에 질문이 있으시면 아래 연락방법으로 연락하시길 바랍니다.")

    address_title = models.CharField(max_length=30, default="교회 주소")
    address_1 = models.CharField(max_length=50, default="4270 W 6th St")
    address_2 = models.CharField(max_length=50, default="Los Angeles, CA 90020")

    phone_title = models.CharField(max_length=30, default="전화번호")
    phone_number = models.CharField(max_length=50, default="사무실 : (213)383-3261")
    fax_number = models.CharField(max_length=50, default="팩스: (213)383-9467")

    email_title = models.CharField(max_length=30, default="이메일 주소")
    email_address = models.CharField(max_length=50, default="이메일 : info@epcla.org")

    service_title = models.CharField(max_length=30, default="예배 시간")
    service_schedule_1 = models.CharField(max_length=80, default="주일 예배: 9:30 am / 11:00 am / 2:00 pm")
    service_schedule_2 = models.CharField(max_length=80, default="금요예배 : 7:30 pm")

    contact_form_title = models.TextField(default="문의 사항이 있으시면 아래 폼을 작성해서 보내기를 눌러주세요")

    thank_you_text = RichTextField(default="Thank you for contacting us. We will get back to you soon.")

    content_panels = Page.content_panels + [
        FieldPanel('contact_hero_title'),
        FieldPanel('contact_hero_subtitle'),

        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('address_title', classname="col4"),
                FieldPanel('address_1', classname="col4"),
                FieldPanel('address_2', classname="col4"),
            ])
        ]),

        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('phone_title', classname="col4"),
                FieldPanel('phone_number', classname="col4"),
                FieldPanel('fax_number', classname="col4"),
            ])
        ]),

        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('email_title', classname="col6"),
                FieldPanel('email_address', classname="col6"),
            ])
        ]),

        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('service_title', classname="col4"),
                FieldPanel('service_schedule_1', classname="col4"),
                FieldPanel('service_schedule_2', classname="col4"),
            ])
        ]),

        FieldPanel('contact_form_title'),
        FormSubmissionsPanel(),
        InlinePanel('form_fields', label='Contact Form Fields'),
        FieldPanel('thank_you_text', classname='full'),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('from_address', classname="col6"),
                FieldPanel('to_address', classname="col6"),
            ]),
            FieldPanel('subject'),
        ], 'Email'),
    ]


class GivePage(Page):
    give_hero_title = models.TextField(default="구제를 좋아하는 자는 풍족하여질 것이요 남을 윤택하게 하는 자는 윤택하여지리라")
    give_verse = models.CharField(max_length=30, default="잠언 11장 25절")

    offering_title = models.CharField(max_length=20, default="연보")
    offering_subtitle = models.CharField(max_length=80, default="십일조 / 주일연보/ 감사연보")

    mission_title = models.CharField(max_length=20, default="선교 헌금")
    mission_subtitle = models.CharField(max_length=80, default="니카라과를 위한 선교 헌금")
    mission_button_text = models.CharField(max_length=40, default="선교 정보 더보기")
    mission_button_link = models.ForeignKey(
        "wagtailcore.Page",
        blank=False,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    education_title = models.CharField(max_length=20, default="교육 후원")
    education_subtitle = models.CharField(max_length=80, default="한국학교 및 틴데일 신학교 후원")
    education_button_text = models.CharField(max_length=40, default="교육 기관 더 보기")
    education_button_link = models.ForeignKey(
        "wagtailcore.Page",
        blank=False,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    donation_title = models.CharField(max_length=20, default="일반 후원")
    donation_subtitle = models.CharField(max_length=80, default="고아와 과부, 가정형편이 어려운분들을 위한 후원")

    give_main_title = models.CharField(max_length=30, default="후원 방법")

    check_subtitle = models.CharField(max_length=80, default="개인 체크(check)으로 후원")
    check_title = models.CharField(max_length=50, default="체크 보내기")
    check_description = RichTextField(default="description for check donation")

    onetime_subtitle = models.CharField(max_length=80, default="온라인 후원")
    onetime_title = models.CharField(max_length=50, default="일회성 후원")
    onetime_description = RichTextField(default="description for onetime donation")
    onetime_button_text = models.CharField(max_length=50, default="온라인 후원")
    onetime_button_link = models.CharField(max_length=50, default="www.epcla.com")

    recurring_subtitle = models.CharField(max_length=80, default="온라인 후원")
    recurring_title = models.CharField(max_length=50, default="주기적 후원")
    recurring_description = RichTextField(default="description for recurring donation")
    recurring_button_text = models.CharField(max_length=50, default="온라인 후원")
    recurring_button_link = models.CharField(max_length=50, default="www.epcla.com")

    content_panels = Page.content_panels + [
        FieldPanel('give_hero_title'),
        FieldPanel('give_verse'),

        FieldPanel('offering_title'),
        FieldPanel('offering_subtitle'),

        FieldPanel('mission_title'),
        FieldPanel('mission_subtitle'),
        FieldPanel('mission_button_text'),
        PageChooserPanel('mission_button_link'),

        FieldPanel('education_title'),
        FieldPanel('education_subtitle'),
        FieldPanel('education_button_text'),
        PageChooserPanel('education_button_link'),

        FieldPanel('donation_title'),
        FieldPanel('donation_subtitle'),

        FieldPanel('give_main_title'),

        FieldPanel('check_subtitle'),
        FieldPanel('check_title'),
        FieldPanel('check_description'),

        FieldPanel('onetime_subtitle'),
        FieldPanel('onetime_title'),
        FieldPanel('onetime_description'),
        FieldPanel('onetime_button_text'),
        FieldPanel('onetime_button_link'),

        FieldPanel('recurring_subtitle'),
        FieldPanel('recurring_title'),
        FieldPanel('recurring_description'),
        FieldPanel('recurring_button_text'),
        FieldPanel('recurring_button_link'),
    ]
