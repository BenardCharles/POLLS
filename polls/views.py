from django.shortcuts import get_object_or_404, render
# get_object_or_404 is a short cut for Http404
from django.http import HttpResponse, Http404, HttpResponseRedirect
# Http404 raises and exception if requested ID doesn't exist
from django.template import loader
from django.views import generic
from django.urls import reverse

from .models import Choice, Question
# Create your views here.

class IndexView(generic.ListView):

	# display the latest 5 poll questions
	# latest_question_list = Question.objects.order_by('-pub_date')[:5]

	# loads the template and passes it to the context
	# template = loader.get_template('polls/index.html') required for OPTION 1
	# context = {
	# 	'latest_question_list': latest_question_list,
	# }

	# to return the HttpResponse
	# OPTION 1 - using HttpResponse
	# return HttpResponse(template.render(context, request))

	# OPTION 2 - we don't need the loader. we use render
	# return render(request, 'polls/index.html', context)

	# NOTE: the render takes 3 arguments
	# render(request, template, optional third argument(Dictionary))

	template_name = 'polls/index.html'
	context_object_name = 'latest_question_list'

	def get_queryset(self):
		""" Return the last five published questions."""
		return Question.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
	model = Question
	template_name = 'polls/detail.html'

	# WHEN USING Http404
	# try:
	# 	question = Question.objects.get(pk=question_id)
	# except Question.DoesNotExist:
	# 	raise Http404("Question does not exist.")

	# WHEN USING get_object_or_404
	#  get_object_or_404() function takes a model as its first argument and an arbitrary number of keyword arguments
	# question = get_object_or_404(Question, pk=question_id)

	# return render(request, 'polls/detail.html', {'question': question})

class ResultsView(generic.DetailView):
	model = Question
	template_name = 'polls/detail.html'

	# question = get_object_or_404(Question, pk=question_id)
	# return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	try:
		selected_choice = question.choice_set.get(pk=request.POST['choice'])

	except (KeyError, Choice.DoesNotExist ):
		# Redisplay the question voting form.
		return render(request, 'polls/detail.html', 
			{
			'question': question,
			'error_message': "You didn't select a choice.",
			})

	else:
		selected_choice.votes += 1
		selected_choice.save()
		# Always return an HttpResponseRedirect after successfully dealing with POST data.
		# This prevents data from being posted twice if a user hits the back button.
		return HttpResponseRedirect(reverse('polls:results', args=(question.id)))