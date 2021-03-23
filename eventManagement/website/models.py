from django.db import models

class service(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    image = models.FileField(upload_to='service/')

    def __str__(self):
        return self.title

class serviceItem(models.Model):
    service = models.ForeignKey(service,on_delete=models.CASCADE,null=True)
    title = models.CharField(max_length=150)
    description = models.TextField()
    image1 = models.FileField(upload_to='service/')
    image2 = models.FileField(upload_to='service/')

    def __str__(self):
        return self.title

class galleryItem(models.Model):
    title = models.CharField(max_length=120,null=True,blank=True)
    description = models.CharField(max_length=120,null=True,blank=True)
    image = models.FileField(upload_to='service/')
    isVideo = models.BooleanField(default=False)
    videoLink = models.CharField(max_length=120,null=True,blank=True)

    def __str__(self):
        return self.image.url

