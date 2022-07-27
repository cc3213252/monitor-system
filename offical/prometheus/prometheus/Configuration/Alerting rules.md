## alerting rules

状态： pending、alert、firing  
annotations可以用来显示告警详情，或者外部链接，值可以用模版  
label和annotations的value都可以用console templates  

### template

{{ $labels.<labelname> }} $labels使用label  

```yaml
- alert: InstanceDown
    expr: up == 0
    for: 5m
    labels:
      severity: page
    annotations:
      summary: "Instance {{ $labels.instance }} down"
      description: "{{ $labels.instance }} of job {{ $labels.job }} has been down for more than 5 minutes."

  # Alert for any instance that has a median request latency >1s.
  - alert: APIHighRequestLatency
    expr: api_http_request_latencies_second{quantile="0.5"} > 1
    for: 10m
    annotations:
      summary: "High request latency on {{ $labels.instance }}"
      description: "{{ $labels.instance }} has a median request latency above 1s (current value: {{ $value }}s)"

```

对于pending和firing告警，prometheus会保存一份数据：  
ALERTS{alertname="<alert name>", alertstate="<pending or firing>", <additional alert labels>}  
发生时把值设置为1，同时其他值设置为过期  
可以配置定期服务发现alertmanager  