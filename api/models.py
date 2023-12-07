from django.db import models

# Create your models here.

class TodoItem(models.Model):
    STATUS_CHOICES = [
        ('OPEN', 'Open'),
        ('WORKING', 'Working'),
        ('DONE', 'Done'),
        ('OVERDUE', 'Overdue'),
    ]

    timestamp = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    due_date = models.DateField(null=True, blank=True)
    # tags = models.ManyToManyField('Tag', blank=True)
    tags = models.CharField(null=True, blank=True, max_length=500)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, 
                              default='OPEN')
    
    def save(self, *args, **kwargs):
        #To save unique tags
        if self.tags:
            tag = self.tags.replace(" ", "")
            tag = tag.split(",")
            tag = set(tag)
            self.tags = ", ".join(tag)
        super().save(*args, **kwargs)  #Call the "real" save() method.

    def __str__(self):
        return str(self.id)


# class Tag(models.Model):
#     value = models.CharField(max_length=50, unique=True)

#     def __str__(self):
#         return self.value
