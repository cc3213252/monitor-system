# encoding: utf-8
# Date: 2022/6/20 19:53

__author__ = 'yudan.chen'

from prometheus_client import CollectorRegistry, Gauge, push_to_gateway

registry = CollectorRegistry()
g = Gauge(
    'pushgateway_job_last_success_unixtime',    # 指标名称
    'Last time a batch job successfully finished',  # help部分
    ['a', 'b'],  # 属性名
    registry=registry)
g.labels(a='1', b='2').set_to_current_time()
push_to_gateway('localhost:9091', job='job test', registry=registry)