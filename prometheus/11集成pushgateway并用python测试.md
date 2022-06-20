1、启动pushgateway  
2、localhost:9091/metrics有值  
3、http://localhost:9090/targets正常  
4、本地执行pushgateway.py  
5、localhost:9091/metrics上增加 
```text
# HELP pushgateway_job_last_success_unixtime Last time a batch job successfully finished
# TYPE pushgateway_job_last_success_unixtime gauge
pushgateway_job_last_success_unixtime{a="1",b="2",instance="",job="job+test"} 1.655729015174187e+09
```
pushgateway.py这个脚本的变动都要靠自己维护，否则只执行一次就是一个固定的值  
prometheus官网pushgateway部分有如何更新的建议  