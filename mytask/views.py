from django.http import JsonResponse

# Create your views here.
from . import task

def task_run(request):
	# 执行异步任务
	task.mytask1.delay()
	return JsonResponse({'result':'ok'})

