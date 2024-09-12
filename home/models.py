from django.db import models

class Announcement(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    

class Plan(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    billing_period = models.CharField(max_length=50, default="Per Month")  # You can change this if needed
    features = models.TextField(help_text="Enter each feature on a new line.")

    def get_features_list(self):
        """Return the features as a list."""
        return self.features.split('\n')

    def __str__(self):
        return self.name
    
class Testimonial(models.Model):
    name = models.CharField(max_length=100)  # The person giving the testimony
    image = models.ImageField(upload_to='testimonials/', blank=True, null=True)
    testimony = models.TextField()

    def __str__(self):
        return f"{self.name}'s Testimonial"
    

from django.db import models

class Statistic(models.Model):
    title = models.CharField(max_length=100)
    value = models.CharField(max_length=20)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.title

from django.db import models

class AboutUs(models.Model):
    # Image field for the about us image
    image = models.ImageField(upload_to='about_us_images/', default='default.jpg')
    
    # Title for the section
    title = models.CharField(max_length=255, default='About Our Dojo')
    
    # Description of the dojo
    description = models.TextField(
        default='Our dojo is a place where karate enthusiasts of all levels come to train and improve. With a team of skilled instructors and a rich tradition of martial arts, we are committed to helping you achieve your karate goals.'
    )
    
    # Features of the dojo
    features = models.JSONField(
        default=list,
        help_text='A list of features, e.g., ["World-class training facilities", "Experienced and certified instructors", "Personalized training programs"]'
    )

    def __str__(self):
        return self.title
