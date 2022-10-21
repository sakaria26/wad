import uuid
from django.db import models

def generateuserid():
    return 'UU{}{}'.format(str(uuid.uuid4())[:8], str(uuid.uuid4())[-4:])
# Create your models here.
class Title(models.Model):
    titleid = models.CharField(max_length=15, primary_key=True)
    title = models.CharField(max_length=15)

    def __str__(self):
        return self.title
class Category(models.Model):
    categoryid = models.CharField(max_length=15, primary_key=True)
    category = models.CharField(max_length=15)

    def __str__(self):
        return self.category

class Postal_Address(models.Model):
    postaladdressid = models.CharField(max_length=15, primary_key=True)
    postalcode = models.IntegerField()
    city = models.CharField(max_length=250)
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.postaladdressid

class Address(models.Model):
    addressid = models.CharField(max_length=15, primary_key=True)
    street = models.CharField(max_length=250)
    city = models.CharField(max_length=250)
    country = models.CharField(max_length=100)
    postaladdressid = models.ForeignKey(Postal_Address, on_delete=models.CASCADE)

    def __str__(self):
        return self.addressid

class Organisation(models.Model):
    organisationid = models.CharField(max_length=15, primary_key=True)
    name = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    phonenumber = models.CharField(max_length=15)
    organisationaddress = models.ForeignKey(Address, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class User(models.Model):
    userid = models.CharField(max_length=15, primary_key=True, default=generateuserid, editable=False)
    email = models.CharField(max_length=250)
    password = models.CharField(max_length=20)
    title = models.ForeignKey(Title, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    affiliateorganisation = models.ForeignKey(Organisation, on_delete=models.CASCADE)

    def __str__(self):
        return self.userid

class Author(models.Model):
    authorid = models.CharField(max_length=15, primary_key=True)
    name = models.CharField(max_length=250)
    surname = models.CharField(max_length=250)
    email = models.CharField(max_length=250)

    def __str__(self):
        return self.authorid

class Paper(models.Model):
    paperid = models.CharField(max_length=15, primary_key=True)
    papertitle = models.CharField(max_length=250)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    authorid = models.ForeignKey(Author, on_delete=models.CASCADE)
    paperurl = models.CharField(max_length=255)

    def __str__(self):
        return self.paperid

class Venue(models.Model):
    venueid = models.CharField(max_length=15, primary_key=True)
    name = models.CharField(max_length=250)
    capacity = models.IntegerField()
    available = models.BooleanField()
    addressid = models.ForeignKey(Address, on_delete=models.CASCADE)

    def __str__(self):
        return self.venueid

class Schedule(models.Model):
    scheduleid = models.CharField(max_length=15, primary_key=True)
    schedulename = models.CharField(max_length=250)
    dataandtime = models.DateTimeField()

    def __str__(self):
        return self.scheduleid

class Accomadation(models.Model):
    roomid = models.CharField(max_length=15, primary_key=True)
    roomphonenumber = models.CharField(max_length=20)
    tenant = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    available = models.BooleanField()

    def __str__(self):
        return self.roomid

class Speaker(models.Model):
    speakerid = models.CharField(max_length=15, primary_key=True)
    title = models.CharField(max_length=15)
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    profilepictureurl = models.CharField(max_length=255)
    speakerorganisation = models.ForeignKey(Organisation, on_delete=models.CASCADE)

    def __str__(self):
        return self.speakerid

class Reviews(models.Model):
    reviewid = models.CharField(max_length=15, primary_key=True)
    comment = models.CharField(max_length=255)
    rating = models.IntegerField()
    paperid = models.ForeignKey(Paper, on_delete=models.CASCADE)
    reviewer = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.reviewid
