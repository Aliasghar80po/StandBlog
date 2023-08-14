from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from django.utils.text import slugify


# User => DELETE
# models.CASCADE
# author = models.ForeignKey(User, on_delete=odels.SET_NULL , null=True, blank= True)
# models.SET_NULL اگر نال رو ترو قرار دادیم مقدارش جاش خالی میشه و اگر بیلنک را هم ترو قرار بدیم تو پنل مدیریت جای کاربر میشه خالی گذاشت
# models.SET_DEFAULT  یک مقدار دیفالت قرار دهیم که اگر کاربر حذف شد یکی دیگر بصورت دیفالت جای اون بیاد
# models.PROTECT محافظت میکند که کاربری که اطلاعات داره حذف نشه مگر اینکه زیر مجموعه هاش حذف بشه
# models.DO_NOTHING کم استفاده
class Category(models.Model):
    title = models.CharField(max_length=100, verbose_name="دسته بندی")
    created = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ انتشار")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "دسته بندی"
        verbose_name_plural = "دسته بندی ها"


class ArticleManager(models.Manager):
    def counter(self):
        return len(self.all())


class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="نویسنده مقاله")
    category = models.ManyToManyField(Category, verbose_name="دسته بندی")
    title = models.CharField(max_length=50, help_text="عنوان خود را انتخاب کنید", db_column='mytitle',verbose_name="عنوان")
    body = models.TextField(help_text="توضیخات خود را وارد کنید",verbose_name="توضیحات")
    image = models.ImageField(upload_to="images/articles",verbose_name="عکس")
    created = models.DateTimeField(auto_now_add=True,verbose_name="تاریخ انتشار")
    updated = models.DateTimeField(auto_now=True,verbose_name="تاریخ بروزرسانی")
    pub_date = models.DateField(default=timezone.now,verbose_name="تاریخ")
    status = models.BooleanField(default=True,verbose_name="وضعیت")
    objects = ArticleManager()
    slug = models.SlugField(null=True, unique=True, blank=True)

    class Meta:
        ordering = ('-created',)
        verbose_name = 'مقاله'
        verbose_name_plural = 'مقاله ها'

    def save(
            self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        self.slug = slugify(self.title)
        super(Article, self).save()

    def get_absolute_url(self):
        return reverse('blog:article_detail', kwargs={"slug": self.slug})

    # or return reverse('blog:article_detail',kwargs={'pk':self.id} )

    def __str__(self):
        return f'{self.title} - {self.body[:40]}'


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments',  verbose_name=" مقاله")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments', verbose_name="نویسنده")
    body = models.TextField(max_length=100,  verbose_name="توضیحات")
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies', verbose_name="پاسح برای")
    created_at = models.DateTimeField(auto_now_add=True, null=True, verbose_name="تاریخ ایجاد")

    # image_user = models.ImageField(upload_to='comment_image', blank=True,null=True)

    def __str__(self):
        return self.body[:30]

    class Meta:
        verbose_name = "اظهار نظر"
        verbose_name_plural = "نظرات"
class Message(models.Model):
    title = models.CharField(max_length=10, verbose_name="عنوان")
    text = models.TextField(verbose_name="توضیحات")
    email = models.EmailField(verbose_name="ایمیل")
    created_at = models.DateTimeField(auto_now_add=True, null=True, verbose_name="تاریخ ایجاد")
    age = models.IntegerField(db_column='age', null=True, verbose_name="سن")
    date = models.DateField(auto_now=True, verbose_name="تاریخ")
    # image = models.ImageField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "پیام"
        verbose_name_plural = "پیام ها"

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes',verbose_name='کاربر')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='likes', verbose_name='مقاله')
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.user.username} - {self.article.title}"

    class Meta:
        unique_together = ('user', 'article')
        verbose_name = "لابک"
        verbose_name_plural = "لایک ها"
        ordering = ('created_at',)

