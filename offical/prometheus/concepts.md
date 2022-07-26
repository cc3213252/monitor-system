## data model

label不能以双下划线开头，是内部用的  

notation，标记法，类似下面这种：  
<metric name>{<label name>=<label value>, ...}  
如： api_http_requests_total{method="POST", handler="/messages"}

value为空等同于没有这个label

## metric types

四种指标类型

counter累加，只加不减，这种就不适合用来比如当前运行的进程等  
[用python实现counter](https://github.com/prometheus/client_python#counter)  

gauge，计量器，可加可减，用来比如显示温度，当前内存占用率
[用python实现gauge](https://github.com/prometheus/client_python#gauge)

histogram，直方图，有累积效应的，比如应用程序性能分数，在基准数的基础上累加、个数统计等
[用python实现histogram](https://github.com/prometheus/client_python#histogram)

summary，摘要
[用python实现summary](https://github.com/prometheus/client_python#summary)

## jobs and instances

