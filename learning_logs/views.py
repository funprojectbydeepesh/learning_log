from django.shortcuts import render
from .models import Topic

# Create your views here.

def home(request):
    return render(request, 'index.html')


''' The topic detail views '''

def topics(request):
    topics = Topic.objects.order_by('added_date')
    context = {
        'topics':topics,
    }
    return render(request, 'topics.html', context)

def detailview(request,topic_id):
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-created')

    context = {
      'topic' : topic,
      'entries' : entries,
    }

    return render(request, 'detail.html', context)


