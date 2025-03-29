from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(max_length=255, blank=True, null=True)
    
    def __str__(self):
        return self.name

class Post(models.Model):
    STATUS_CHOICES = [
        ('draft','Draft'),
        ('published', 'Published')
    ]
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    slug = models.SlugField(unique=True, max_length=255)
    category = models.ManyToManyField(Category, related_name='posts')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class Tag(models.Model):
    name=models.CharField(max_length=100, unique=True)
    post = models.ManyToManyField(Post, related_name='tags')

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    # here foreign key means many Comments have one User
    # when the User (foriegn key) is deleted, the comment will be deleted too that where associated with the User
    # but if the comment is deleted, the User will not be deleted
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey(
        'self',  # Refers to the same model (Comment)
        on_delete=models.CASCADE,  # If the parent comment is deleted, its replies are also deleted
        null=True,  # A comment can exist without a parent (i.e., it is a top-level comment)
        blank=True,  # Allows this field to be optional in forms
        related_name='replies'  # Allows us to access replies using `parent_comment(comment.replies.all())`
    )


    def __str__(self):
        return f'{self.user.username} commented on {self.post.title}'

class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('post', 'user')
    # this means that a user can only like a post once

    def __str__(self):
        return f'{self.name} liked {self.post.title}'
    


# QuerySets:
post = Post.objects.all()   # Get all posts
post = Post.objects.filter(status='published')  # Get all published posts
post = Post.objects.filter(created_at__gte="2025-03-18")
topfivePosts = Post.objects.all()[:5]   # Get the first 5 posts
post = Post.objects.order_by('-title') # Order by title in descending order
firstPost = Post.objects.get(id=1)
firstPost.title = "new title"
firstPost.save() # Save the changes to the database
firstPost.delete()  # Delete the post from the database
post = Post.objects.filter(category__name='category_name')  # Get all posts in a specific category
post = Post.objects.filter(tags__name='tag_name')   # Get all posts with a specific tag


# Model Relationships:
# OneToOne: One User can have one profile (e.g., Employer) OnetoOne is make when you want to extend a model
# and its foreign key is added in the extended model

# OneToMany: One User can have many posts. OneToMany is used when A model "Belongs to" B model. A will have a foreign key to B model
# and its foreign key is stored in the A model which belongs to B model. and foriegn key will be in the Many model

# ManyToMany: One Post can have many categories and one category can have many posts. ManyToMany is used when A model has many B models and B model has many A models.
# and its foreign key is added in either model you want.

class User:
    name=models.CharField(max_length=100)

class Profile:
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')


# 1️⃣ One-to-Many (ForeignKey)
# Example: Post and User (One User → Many Posts)

user = User.objects.get(username="sana")
posts = user.posts.all() # Get all posts by the user

post = Post.objects.first()
author = post.author  # Get the author of the post

# 2️⃣ Many-to-Many (ManyToManyField)
# Example: Post and Category

# when making this foreign key, we add related_name='posts' to it, to access the posts from the category(other) model
# and we can access the category from the post model using post.category.all()

# Definition	                Query to Get Posts from Category
# related_name='posts'      	    category.posts.all()
# No related_name	               category.post_set.all()

category = Category.objects.get(name="category_name")
posts_in_category = category.posts.all()  # Get all posts in the category

post = Post.objects.first()
categories_of_post = post.category.all()    # Get all categories of the post

# 3️⃣ Self-Referencing (Recursive) One-to-Many
# Example: Comments and Replies

comment = Comment.objects.get(id=1)
replies = comment.replies.all() # Get all replies to the comment

reply = Comment.objects.get(id=2)
parent_comment = reply.parent  # Get the parent comment of the reply

# 4️⃣ One-to-One (OneToOneField)
# Example: User and Profile

user = User.objects.get(username="sana")
profile = user.profile  # Get the profile of the user

profile = Profile.objects.get(id=1)
user = profile.user  # Get the user of the profile

# Reverse Queries
# If a ForeignKey or OneToOneField doesn't have a related_name, Django creates a default reverse name:

# modelname_set.all()                 ->   for One-to-Many

# modelname                           ->   for One-to-One

user = User.objects.get(username="sana")
posts = user.post_set.all() # Get all posts by the user (reverse query)

user = User.objects.get(username="sana")
profile = user.profile  # Get the profile of the user (reverse query)