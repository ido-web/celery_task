from celery.task import Task
import time
from celery import platforms

platforms.C_FORCE_ROOT = True  #root用户启动需要加上这一行

class mytask1(Task):
	```
		异步任务
	```
	# 异步任务队列
	name = 'task1'
	def run(self,*args,**kwargs):
		print('start mytask1 task--------------------------------1')
		time.sleep(4)
		print ('args={},kwargs={}'.format(args,kwargs))
		print('end mytask1 task----------------------------------1')


class mytask2(Task):
	```
		定时任务
	```
	# 为任务起名字
	name = 'task2'
	def run(self,*args,**kwargs):
		print('start mytask2 task----------------------------------2')
		time.sleep(4)
		print ('args={},kwargs={}'.format(args,kwargs))
		print('end mytask2 task-----------------------------------2')