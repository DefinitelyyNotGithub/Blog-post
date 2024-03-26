from django.db import models
from Account.models import User


class ContactUsModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='messages', null=True, blank=True)
    name = models.CharField(max_length=50, null=True, blank=True)
    subject = models.CharField(max_length=150)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    email = models.EmailField()
    seen = models.BooleanField(default=False)

    def __str__(self):
        return self.subject[:40]

    class Meta:
        verbose_name = "user feedback"
        verbose_name_plural = "user feedbacks"


class site_general_info(models.Model):
    website_name = models.CharField(max_length=50, verbose_name="website name")
    email_address = models.EmailField(verbose_name="Email address")
    alternative_email_address = models.EmailField(verbose_name="second Email address (optional)", null=True, blank=True)
    phone_number = models.CharField(max_length=20, verbose_name="phone number")
    alternative_phone_number = models.CharField(max_length=20, verbose_name="second phone number (optional)", null=True, blank=True)
    company_address = models.TextField(verbose_name="company address")

    insa_url = models.CharField(max_length=255, null=True, blank=True, verbose_name="instagram")
    fb_url = models.CharField(max_length=255, null=True, blank=True, verbose_name="facebook")
    pin_url = models.CharField(max_length=255, null=True, blank=True, verbose_name="pinterest")
    in_url = models.CharField(max_length=255, null=True, blank=True, verbose_name="linkedin")
    twitter_url = models.CharField(max_length=255, null=True, blank=True, verbose_name="twitter")


    def __str__(self):
        return f'{self.website_name} | {self.phone_number}'

    class Meta:
        verbose_name = "website general information"

class AboutUs_Model(models.Model):
    pottage = models.ImageField(upload_to='images/aboutus_title', null=True, blank=True)
    general_description = models.TextField(verbose_name="General description")


    A_1_title = models.CharField(max_length=30, null=True, blank=True, verbose_name="first Paragraph title")
    A_1_body = models.TextField(null=True, blank=True,  verbose_name="first Paragraph")

    A_2_title = models.CharField(max_length=30, null=True, blank=True, verbose_name="second paragraph title")
    A_2_body = models.TextField(null=True, blank=True, verbose_name="second paragraph")

    B_1_title = models.CharField(max_length=25, null=True, blank=True, verbose_name="small paragraph title 1" )
    B_1_body = models.TextField(null=True, blank=True, verbose_name="small paragraph 1")

    B_2_title = models.CharField(max_length=25, null=True, blank=True, verbose_name="small paragraph title 2" )
    B_2_body = models.TextField(null=True, blank=True, verbose_name="small paragraph 2")

    B_3_title = models.CharField(max_length=25, null=True, blank=True, verbose_name="small paragraph title 3" )
    B_3_body = models.TextField(null=True, blank=True, verbose_name="small paragraph 3")


    def __str__(self):
        return self.general_description[:10]

    class Meta:
        verbose_name = "about us page"






