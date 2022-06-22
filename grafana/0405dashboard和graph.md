dashboard要多保存

只显示amazon.cn的：  
ping_average_response_ms{url="amazon.cn"}

Legend可以填成模版的方式： {{url}}  
也可以加前缀： average_{{url}}   
{{environment}}_{{url}}   

## 如何设置min step

Min step 最小点间隔  
先看prometheus中多少时间一个点： http://localhost:9090/graph?g0.expr=ping_average_response_ms%7Burl%3D%22host1%22%7D%5B2m%5D&g0.tab=1&g0.stacked=0&g0.show_exemplars=0&g0.range_input=1h  
从ping_average_response_ms{url="host1"}[2m]这个表达式看出，  
2分钟4个点，故30秒一个点，源头30秒一个点，那grafana设置小于30秒就没有意义  

Resolution分辨率  
instant是结合table用的  