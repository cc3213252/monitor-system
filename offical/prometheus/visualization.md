
grafana Legend format可以用格式：  
{{method}} - {{status}} 

rate(prometheus_http_request_duration_seconds_count{job="prometheus"}[5m])  
Legend填{{handler}}

grafana的rate和increase函数中推荐使用$__rate_interval这个变量  

## 示例console templates用法

/consoles/index.html.example这个文件，针对node_exporter的面板，job名字要命名成node  


[资料](https://yunlzheng.gitbook.io/prometheus-book/part-ii-prometheus-jin-jie/grafana/use-console-template)