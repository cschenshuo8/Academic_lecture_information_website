from django.db import models

# Create your models here.
class Publisher(models.Model):
    name = models.CharField(max_length=30, verbose_name="名称")
    address = models.CharField("地址", max_length=50)
    city = models.CharField("城市", max_length=60)
    state_province = models.CharField("省份", max_length=30)
    country = models.CharField("国家", max_length=50)
    website = models.URLField("网址")

    class Meta:
        verbose_name = '出版商'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=30)

class AuthorDetail(models.Model):
    sex = models.BooleanField(max_length=1, choices=((0, '男'),(1, '女'),))
    email = models.EmailField()
    address = models.CharField(max_length=50)
    birthday = models.DateField()
    author = models.OneToOneField(Author, on_delete=models.CASCADE)

class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    publication_date = models.DateField()
    price = models.DecimalField(max_digits=5, decimal_places=2,default=10)

class TermInfo(models.Model):
     imsi = models.CharField(max_length=100)
     tmsi = models.CharField(max_length=100)
     tmei = models.CharField(max_length=100)
     rssi = models.IntegerField()
     time = models.CharField(max_length=100)
     band = models.CharField(max_length=100)
     mac = models.CharField(max_length=100)
     sn = models.CharField(max_length=100)
     longitude = models.DecimalField(max_digits=5, decimal_places=2,default=10)
     latitude = models.DecimalField(max_digits=5, decimal_places=2,default=10)

class Device(models.Model):
    #sn = models.CharField(max_length=100)
    #mac = models.CharField(max_length=100)
    #time = models.CharField(max_length=100)
    #fw = models.CharField(max_length=100)
    #band = models.CharField(max_length=100)
    #plmn = models.CharField(max_length=100)
    #cell = models.IntegerField()
    #rf = models.IntegerField()
    #gps = models.CharField(max_length=100)
    #cnm = models.IntegerField()
    #sync = models.CharField(max_length=100)
    #rip = models.IntegerField()
    #longitude = models.DecimalField(max_digits=5, decimal_places=2, default=10)
    #latitude = models.DecimalField(max_digits=5, decimal_places=2, default=10)
    #tmp =  models.DecimalField(max_digits=5, decimal_places=2, default=10)
    #frqc = models.CharField(max_length=100)
    #role = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    people = models.CharField(max_length=100)
    time = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    university = models.CharField(max_length=100)
    link = models.CharField(max_length=100)
    release_time = models.CharField(max_length=1000)
    content = models.CharField(max_length=5000, default=0)
    intro = models.CharField(max_length=2000, default=0)
    theme = models.CharField(max_length=100)
class School(models.Model):
    university = models.CharField(max_length=100)
    link = models.CharField(max_length=100)
    intro = models.CharField(max_length=2000, default=0)
class Team(models.Model):
    name = models.CharField(max_length=100)
    work = models.CharField(max_length=100)
    intro = models.CharField(max_length=2000, default=0)
class suggest(models.Model):
    score = models.CharField(max_length=100)
    advice = models.CharField(max_length=2000, default=0)