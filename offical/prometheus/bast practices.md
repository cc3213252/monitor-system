## Histograms and summaries

都适用于样本观测值，如请求时长、响应大小，跟踪观测的数量或者观测值的和，允许你计算平均值

约定带_count后缀为counter，带_sum后缀也是counter

观测摄氏温度这个例子中，用sum会使数字下降，就不能用rate()了，故可以使用两个独立的summaries，一个正
一个负，用适合的PromQL表达式结合起来  

计算最近5分钟平均请求持续时间：  
rate(http_request_duration_seconds_sum[5m])
/ rate(http_request_duration_seconds_count[5m])