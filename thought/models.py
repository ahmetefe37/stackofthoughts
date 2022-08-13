from datetime import date, datetime
import email
from sre_constants import CATEGORY
from unicodedata import category
from django.db import models

#my classes

class Thought(models.Model):
    # categories
    CATEGORIES = (
        ("default","default"),
        ("engieneering","engieneering"),
        ("art","art"),
        ("health","health"),
        ("finance","finance"),
        ("logistic","logistic"),
        ("eductaion","eductaion"),
        ("socail","social"),
        ("science","science"),
        ("sale","sale"),
        ("administration","administration"),
        ("construction","construction"),
        ("internet","internet"),
        ("marketing","marketing"),
        ("sport","sport"),
        ("security","security"),
        ("environment","environment")
    )

    STATUS = (
        ("draft","draft"),
        ("published","published"),
        ("updated","updated")
    )

    # vars
    title = models.CharField(max_length=60, blank=False,null=False,default='Please enter a title..')
    summary = models.CharField(max_length=90, blank=False, null=False, default='Please enter a summary..')
    gist = models.TextField(max_length=250, blank=False, null=False, default='Please enter a gist..')
    problem = models.TextField(max_length=250, blank=False, null=False, default='Please enter a problem..')
    content = models.TextField(max_length=10000, blank=False, null=False, default='Please enter a content..')

    # dates
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    # image fields


    #file field

    
    # others
    category = models.CharField(max_length = 50,blank=False, null=False, default="default",choices=CATEGORIES)
    score = models.IntegerField(null=False, blank=False, default=0, editable=False)

    def __str__(self):
        return self.title



class User(models.Model):
    firstname = models.CharField(max_length=30, blank=False, null=False, default='Please enter your fullname..')
    lastname = models.CharField(max_length=30, blank=False, null=False, default='Please enter your fullname..')
    username = models.CharField(max_length=30, blank=False, null=False, default='Please enter your username..',unique=True)
    email = models.EmailField(max_length=60, blank=False, null=False, default='Please enter your email address..')
    age = models.IntegerField(null=False, blank=False,default=18)

    # long text
    introduction = models.TextField(max_length=1000, blank=False, null=False, default='Please enter your introduction..')
    academic_history = models.TextField(max_length=1000, blank=False, null=False, default='Please enter yourademic history..')
    qualifications = models.TextField(max_length=1000, blank=False, null=False, default='Please enter your qualifications..')
    job = models.TextField(max_length=250, blank=False, default='Please enter your job..')

    # images


    def __str__(self):
        return self.firstname

