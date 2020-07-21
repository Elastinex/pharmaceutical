from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField
from django.shortcuts import render, redirect
from django.utils.translation import ugettext_lazy as _


class CourseCategory(models.Model):
    title = models.CharField(max_length=255, verbose_name=_('Title'))

    class Meta:
        verbose_name = "Course category"
        verbose_name_plural = "Courses category"
        ordering = ['title']

    def __str__(self):
        return self.title


class Course(models.Model):
    category = models.ForeignKey(
        CourseCategory, on_delete=models.CASCADE, related_name="Course_category", null=True)
    title = models.CharField(max_length=150, verbose_name=_('Title'))
    description = models.TextField(
        max_length=200, null=True, verbose_name=_('Description'))
    image = models.ImageField(
        upload_to='cat_images', default='cat_images/default.png', verbose_name=_('Picture'))
    students = models.ManyToManyField(
        User, swappable=True, verbose_name=_('Students'))
    price = models.CharField(
        max_length=150, verbose_name=_('Price'),  default="₮")

    class Meta:
        verbose_name = "Course"
        verbose_name_plural = "Courses"
        ordering = ['title']

    def __str__(self):
        return '{}'.format(self.title)


class Subject(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name=_('Created by '))
    title = models.CharField(max_length=30, verbose_name=_('Title'))
    slug = models.SlugField()
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, verbose_name=_('Course'))
    description = models.TextField(
        max_length=400, verbose_name=_('Description'))
    created_on = models.DateTimeField(
        auto_now=True, verbose_name=_('Created_on'))
    image_field = models.ImageField(
        upload_to='kurs_images', default='default', verbose_name=_('Upload picture'))

    class Meta:
        verbose_name = "Subject"
        verbose_name_plural = "Subjects"
        ordering = ['title']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("courses:course_detail", kwargs={"slug": self.slug})

    def get_courses_related_to_memberships(self):
        return self.courses.all()

    @property
    def lessons(self):
        return self.lesson_set.all().order_by('position')


class Lesson(models.Model):
    title = models.CharField(
        max_length=30, verbose_name=_(' Lesson title'))
    slug = models.SlugField()
    subject = models.ForeignKey(
        Subject, on_delete=models.CASCADE, verbose_name=_('Subject'))
    video_id = models.FileField(
        upload_to="course_video", blank=True, null=True, verbose_name=_('Upload video'))
    content = RichTextField(verbose_name=_('Content'))
    position = models.IntegerField(verbose_name=_('Lesson position'))
    pdf_file = models.FileField(upload_to="pdf_file", null=True, blank=True)
    photo = models.FileField(upload_to="course_image", null=True, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("courses:lesson_detail", kwargs={"course_slug": self.subject.slug, 'lesson_slug': self.slug})

    class Meta:
        verbose_name = "Lesson"
        verbose_name_plural = "Lessons"
        ordering = ['title']


class Post(models.Model):
    post = models.CharField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
