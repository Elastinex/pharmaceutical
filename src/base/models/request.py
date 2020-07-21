from django import forms
from django.shortcuts import render
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User, Group
from django.utils.translation import ugettext_lazy as _


class Request(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(default='')
    Phone = models.CharField(max_length=10, default='')
    message = models.TextField()

    class Meta:
        verbose_name = "Холбоо барих"
        ordering = ['name']

    def __str__(self):
        return self.name


class RequestForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = ["name", "Phone", 'email', 'message']
        labels = {'name': "Нэр",
                  "Phone": "Утас",
                  'email': 'Имайл',
                  'message': 'Холбоо барих',
                  }

    def __init__(self, *args, **kwargs):
        super(RequestForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(
            Submit('submit', 'Submit', css_class='btn-primary'))
        self.helper.form_method = 'POST'


def request(request):
    if request.method == "POST":
        form = RequestForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = RequestForm()
    return render(request, 'homecontact.html', {'form': form})


admin.site.register(Request)
