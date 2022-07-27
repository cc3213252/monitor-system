global:
  scrape_interval:     15s # By default, scrape targets every 15 seconds.

  # 这个label是给外部系统标识本系统用的
  external_labels:
    monitor: 'codelab-monitor'
  

prometheus_target_interval_length_seconds  
延迟百分比和目标组间隔，quantile是延迟指标  
统计数量： count(prometheus_target_interval_length_seconds)  

rate(prometheus_tsdb_head_chunks_created_total[1d])  
每天创建chunks的比率  

node_cpu_seconds_total每秒cpu用量  

## 配置rules来聚合数据

下面这个语句能实现统计5分钟内平均每秒cpu使用情况：  
avg by (job, instance, mode) (rate(node_cpu_seconds_total[5m]))

但是有个问题，效率会比较低，为了更高效，可以使用record rule  

```ini
# prometheus.rules.yml
groups:
- name: cpu-node
  rules:
  - record: job_instance_mode:node_cpu_seconds:avg_rate5m
    expr: avg by (job, instance, mode) (rate(node_cpu_seconds_total[5m]))
```

```ini
# prometheus.yml
rule_files:
  - 'prometheus.rules.yml'
```



