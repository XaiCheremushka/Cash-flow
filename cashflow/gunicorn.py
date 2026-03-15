import logging
import sys
from multiprocessing import cpu_count

from config import conf

def max_workers():
    return cpu_count()

bind = '0.0.0.0:' + conf.SITE_PORT
max_requests = 1000
worker_class = 'gevent'
timeout = 60 + 10  #(минута + буфер)

workers = max_workers()

reload = True
name = 'cashflow'