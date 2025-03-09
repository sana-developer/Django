from django.db import models

# Create your models here.
# Our first Database Model

# this is the information of our database
class BlogPost(models.Model):
    # here model is the table like sql, now we need to find our columns, fields,
    #  or type of information story that it will store
    title = models.CharField(max_length=100)
    content = models.TextField()
    # auto_now_add=True means that the date and time will be added automatically when the object is created
    published_date = models.DateTimeField(auto_now_add=True)    
    
    # This creates a Blog table with title, content, and published_date fields.

    def __str__(self):
        return self.title
    
