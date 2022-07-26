## Overview

2012年开始，2016年加入云原生

架构图

## First steps

global:
  scrape_interval:     15s
  evaluation_interval: 15s

evaluation_interval多久评估一次规则  
启动时要等待30秒取自己数据  

promhttp_metric_handler_requests_total，请求prometheus的总数  
promhttp_metric_handler_requests_total{code="200"}，筛选返回200的  
count(promhttp_metric_handler_requests_total)，统计总数  
rate(promhttp_metric_handler_requests_total{code="200"}[1h])，每小时http请求返回200比率  

## Comparison to alternatives

prometheus与Graphite、influxDB、OpenTSDB、Nagios、Sensu对比

## FAQ

把应用日志变成metrics，用google的[mtail](https://github.com/google/mtail) 

alertmanager支持微信告警  

输出到控制台可以用[控制台模版](https://prometheus.io/docs/visualization/consoles/)

监控网络设备，用官方提供的[snmp exporter](https://github.com/prometheus/snmp_exporter)

监控批量job，很短暂的，一次执行一批的那种，用pushgateway

java程序的监控可以统一用[JMX Exporter](https://github.com/prometheus/jmx_exporter)

## Roadmap

讲将来prometheus的发展方向

1、服务端metric元数据支持  
2、metric新标准支持  
3、可追溯的告警  
4、TLS更易于使用  
5、更多语音和生态支持  

## Design Documents

设计文档，一些个人提的TODO

## Media

关于prometheus的各种资源  
社区维护的[Awesome prometheus](https://github.com/roaldnefs/awesome-prometheus#tutorials)  

官网偏学习的[blog](https://prometheus.io/blog/)

[python开发metrics](https://github.com/juliusv/prometheus_workshop)