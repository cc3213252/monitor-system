ping_average_response_ms{service_name="amazon"}

~开头表示后面是正则表达式  
ping_average_response_ms{url=~"^amazon.*"}

多个label取交集  
ping_average_response_ms{url=~"^amazon.*", url!="amazon.cn"}

过滤value  
ping_average_response_ms{url=~"^amazon.*", url!="amazon.cn"}<200

运算符可以用 =、!=

## range vector

之前的都是同一个时间点上的数据，这里是一段时间  
语法： http_requests_total{job="prometheus"}[5m] 最近5分钟内  

查看net_bytes_recv这个指标，可以看到graph中是一直往上涨，从metrics中也看到# TYPE net_bytes_recv counter，
说明这个指标是counter类型

算速率：  rate(net_bytes_recv[1m])  
单位换成bytes：  rate(net_bytes_recv[1m])*8