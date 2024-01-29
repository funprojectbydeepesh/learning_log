from django.db import models

# Create your models here.
class Topic(models.Model):
    ''' The topic user is learning about'''
    title = models.CharField(max_length=200)
    added_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    

class Entry(models.Model):
    ''' Something specific  learned about the topic '''

    topic = models.ForeignKey(Topic,on_delete=models.CASCADE)
    about = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'
    
    def __str__(self):
        return self.about[:20] + '.....'
    
    