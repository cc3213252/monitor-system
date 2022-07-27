## Recording rules

有两种rules： recording rules和alerting rules  

检查rule语法： promtool check rules /path/to/example.rules.yml  

recording rules是用规则来生成新的检测项的，用预先算好加快速度， dashboard中耗时项都应用recording rules代替  

```yaml
groups:
- name: cpu-node
  limit: 10
  rules:
  - record: job_instance_mode:node_cpu_seconds:avg_rate5m
    expr: avg by (job, instance, mode) (rate(node_cpu_seconds_total[5m]))
    labels:
      [ <labelname>: <labelvalue> ]
```
alerting rules:  
```yaml
groups:
  - name: example
    rules:
      - alert: PacketLoss > 0
        expr: ping_percent_packet_loss != 0
        for: 2m
        labels:
          severity: urgent
        annotations:
          summary: High request latency
```
设置了limit，数量满的时候，如果是alerting rules， 所有其他状态都会被改成error级别