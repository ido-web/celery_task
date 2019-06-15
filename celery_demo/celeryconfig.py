import djcelery
from datetime import timedelta

djcelery.setup_loader()

# 设置任务队列
CELERY_QUEUES = {
	'beat_tasks':{
		'exchange':'beat_tasks',
		'exchange_type':'direct',
		'binging_key':'beat_tasks'
	},
	'work_queue':{
		'exchange':'work_queue',
		'exchange_type':'direct',
		'binging_key':'work_queue'
	}
}

# 默认使用的队列
CELERY_DEFAULT_QUEUE = 'work_queue'


CELERY_IMPORTS = (

	'mytask.task',
)


# 有些情况可以防止死锁
CELERYD_FORCE_EXECV = True

# 设置并发worker数量
CELERYD_CONCURRENCY = 4

# 失败后允许重试
CELERY_ACKS_LATE = True

# 每个worker最多可以执行100个任务被销毁，可以防止内存泄漏
CELERYD_MAX_TASKS_PER_CHILD = 100

# 单个任务的最大运行时间
CELERYD_TASK_TIME_LIMIT = 12 * 30


# 定义一个定时任务
CELERYBEAT_SCHEDULE = {
	'task1':{
		'task':'task2',
		'schedule':timedelta(seconds=5),   # 设置任务每5秒执行一次
		'options':{
			'queue':'beat_tasks'          # 指定一个任务队列
		}
	}
}