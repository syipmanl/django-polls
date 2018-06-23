from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.utils import timezone

from .models import Question, Choice

# change dataset, acess dataset,
# handle errors
# shows whats up with django.shortcuts' render



"""
# ----- OLD INDEX --- #
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
    'latest_question_list': latest_question_list
    }
    return HttpResponse(template.render(context, request))
   return render(request, 'polls/index.html', context)
# ------------------- #
"""



# --- OLD DETAIL --- #
"""
def detail(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	return render(request, 'polls/detail.html', {'question': question})

	#	try: 
	#		a_question = Question.objects.get(pk=question_id)
	#	except Question.DoesNotExist:
	#		raise Http404("Question does not exist")
"""
# ------------------- #


# --- OLD RESULT --- #
"""
def results(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	return render(request, 'polls/results.html', {'question':question})

 	#   response = "You're looking at the results of question %s."
 	#   return HttpResponse(response % question_id)
 """
# ------------------- #


class IndexView(generic.ListView):
	template_name = 'polls/index.html'
	context_object_name = 'latest_question_list'

	def get_queryset(self):
		"""RETURN the last five published questions. (not including those set to be
		published in the future)."""
		#return Question.objects.order_by('-pub_date')[:5]
		return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]


# Leave the rest of the views (detail, results, vote) unchanged


# Now, let’s tackle the question detail view – the
# page that displays the question text for a given poll. Here’s the view:

class DetailView(generic.DetailView):
	model = Question
	template_name = 'polls/detail.html'

	def get_queryset(self):
		"""
		Excludes any questions that aren't published yet.
		"""
		return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
	model = Question
	template_name = 'polls/results.html'





def vote(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	try:
		selected_choice = question.choice_set.get(pk=request.POST['choice'])

	except (KeyError, Choice.DoesNotExist):
		# Redisplay the question voting form.
		return render(request, 'polls/detail.html', {
			'question': question,
			'error_message': "You didn't select a choice."
			})

	else:
		selected_choice.votes += 1
		selected_choice.save()

		# Always return an HttpResponseRedirect after sucessfully dealing
		# with POST data. This prevents data from being posted twice if a 
		# user hits the Back Button
		return HttpResponseRedirect(reverse('polls:results', args=[question.id]))






 #   return HttpResponse("You're voting on question %s." % question_id)

