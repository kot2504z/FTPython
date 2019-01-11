from django.db import models

class Posts(models.Model):
	post_text = models.CharField(max_length=500)
	pub_date = models.DateTimeField('date published')

	def add_post(self, post_value, post_date):
		if post_value and post_date:
			self(post_text = post_value, pub_date = post_date).save()
		
		return 0

	def delete_old_posts(self, delete_more_than):
		if self.objects.count() > delete_more_than and delete_more_than > 0:
			x = 0
			for object in self.objects.order_by('-pub_date'):
				x = x + 1
				if x > delete_more_than:
					object.delete()
		return 0

	def __str__(self): 
		return self.post_text