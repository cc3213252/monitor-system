PromQL: Prometheus Query Language

## 表达式可以评估的四种类型

Instant vector，同一个timestamp时的一组series，一个sample  
Range vector，很多instant vector  
Scalar，一个数字值  
String，目前还没使用  

返回即时向量的表达式是唯一可以用来画图的  

## Instant vector selectors

=～ 正则匹配  
!~ 正则不匹配  

env=~"foo" 等同于 env=~"^foo$"

http_requests_total{environment=~"staging|testing|development",method!="GET"}  
匹配三个环境方法不为GET  

匹配空就是匹配所有，故必须要指定一个名称，这个是非法的： {job=~".*"}  
这些是合法的： {job=~".+"}  {job=~".*",method="get"}  

metric name默认用__name__ label，故http_requests_total等同于{__name__="http_requests_total"}  
匹配多个job: {__name__=~"job:.*"}  

metric name不能用这些关键字：bool, on, ignoring, group_left and group_right  
不能写成on{}，应该写成{__name__="on"}  

## Range Vector Selectors

http_requests_total{job="prometheus"}[5m]  
5分钟内job名称为prometheus的时间序列  

## Offset modifier

http_requests_total offset 5m  
5分钟前的值  

必须要紧跟selector后面，下面是正确的： sum(http_requests_total{method="GET"} offset 5m)  
下面是不正确的： sum(http_requests_total{method="GET"}) offset 5m  

rate(http_requests_total[5m] offset 1w)   
一周前5分钟请求量  
rate(http_requests_total[5m] offset -1w)  
表示时间上向前移动  

## @ modifier

@ 对应一个浮点型unix timestamp  

http_requests_total @ 1609746000  
查询这个时间戳的值

sum(http_requests_total{method="GET"} @ 1609746000) // GOOD.  
sum(http_requests_total{method="GET"}) @ 1609746000 // INVALID.  

一些用法：  
rate(http_requests_total[5m] @ 1609746000) // GOOD  
http_requests_total @ 1609746000 offset 5m  // offset after @  
http_requests_total offset 5m @ 1609746000  // offset before @  
http_requests_total @ start()  
rate(http_requests_total[5m] @ end())  

## 陷阱

标记过时的样本会被删除  
数据很多时，应先在table中构建查询，然后切换到图形