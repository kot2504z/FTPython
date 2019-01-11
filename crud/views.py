from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect,HttpResponse
from django.template import loader
from django.utils import timezone
from django.urls import reverse

from .models import Posts
# Create your views here.

def posts_page(request):
	Posts.delete_old_posts(Posts, 5) #delete posts (object, leave_posts)
	return render(request, 'crud/index.html', {'list_of_posts': Posts.objects.order_by('-pub_date')})
	
def add_post(request):
	if request.method == 'POST':
		Posts.add_post(Posts, request.POST.get('text_field'), timezone.now())

	return HttpResponseRedirect(reverse('posts_page'))