http_requests_total{status!~"4.."}  
返回状态码不为4开头的三位数  

rate(http_requests_total[5m])[30m:1m]  
返回过去30分钟，5分钟速率线，分辨率为1分钟  

rate(http_requests_total[5m])  
求过去5分钟http总请求每秒速率

sum by (job) (
  rate(http_requests_total[5m])
)
过去5分钟每秒速率，以job为维度求和

(instance_memory_limit_bytes - instance_memory_usage_bytes) / 1024 / 1024  
算未使用内存以M为单位，维度相同的metrics可以合并  

sum by (app, proc) (
  instance_memory_limit_bytes - instance_memory_usage_bytes
) / 1024 / 1024  
未使用内存按app、proc分组求和  

## 例子

nstance_cpu_time_ns{app="lion", proc="web", rev="34d0f99", env="prod", job="cluster-manager"}
instance_cpu_time_ns{app="elephant", proc="worker", rev="34d0f99", env="prod", job="cluster-manager"}
instance_cpu_time_ns{app="turtle", proc="api", rev="4d3a513", env="prod", job="cluster-manager"}
instance_cpu_time_ns{app="fox", proc="widget", rev="4d3a513", env="prod", job="cluster-manager"}

按app、proc求top 3的cpu使用：  
topk(3, sum by (app, proc) (rate(instance_cpu_time_ns[5m])))  

按app统计跑的instance数量：  
count by (app) (instance_cpu_time_ns)  