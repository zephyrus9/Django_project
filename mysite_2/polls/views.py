from django.shortcuts import render
from django.http import Http404

from django.http import HttpResponse
from django.template import RequestContext, loader
from .models import Question

# 每个视图函数只会负责处理两件事中的一件：返回包含请求页面内容的HTTPResponse对象
# 或者是抛出一个诸如Http404异常
# Django只会要求返回一个HttpResponse，或者是抛出异常


# Create your views here.
def index(request):
	lastest_question_list = Question.object.order_by('-pub_date'[:5])
	template = loader.get_template('polls/index.html')
	context = RequestContext(request, {'lastest_question_list': lastest_question_list, })
	# output = ', '.join([p.question_text for p in lastest_question_list])
	# return HttpResponse(template.render(context))
	return render(request, 'polls/indx.html', context)

def detail(request, question_id):
	try:
		question = Question.object.get(pk=question_id)
	except Question.DoesNotExist:
		raise Http404("Question does not exist")

	return render(request, 'polls/detail.html',  {'question': question})

def vote(request, question_id):
	return HttpResponse("You're voting on question %s." % question_id)

def results(request, question_id):
	response = "You're looking at the results of question %s."
	return HttpResponse(response % question_id)