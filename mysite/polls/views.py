from django.shortcuts import render_to_response
from django.template import Context, loader
from polls.models import Poll
from django.http import HttpResponse, Http404

def index(request):
	latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
	t = loader.get_template('polls/index.html')
	
	c = Context({
		'latest_poll_list': latest_poll_list,
	})
	return HttpResponse(t.render(c))
	
	

def detail(request, poll_id):
	try:
		p = Poll.objects.get(pk = poll_id)
	except Poll.DoesNotExist:
		raise Http404
	return render_to_response('polls/detail.html', {'poll':p})
	
def vote(request, poll_id):
	return HttpResponse("You're voting on poll %s."%poll_id)

def results(request, poll_id):
	return HttpResponse("Resultados %s"%poll_id)