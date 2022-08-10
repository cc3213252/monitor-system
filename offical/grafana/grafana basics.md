## Exemplars 示例

示例是将高级基数元数据与特定事件与传统的时间表数据相关联的一种方式  
用来做数据对比，查找定位问题用的，作用理解不太好  

TSDB会存数据的偏移量，故会大幅度减少磁盘占用  

## Histograms and heatmaps

Heatmaps，热力图，类似直方图

## Best practices

两种方法： 
USE method聚焦于机器，如CPU使用率，节点负载，错误个数  
RED method聚焦于用户体验或者问题，告警应报告问题

常用观测策略：  
根据Google SRE handbook，四个最重要的指标是：Latency、Traffic、Errors、Saturation  
[这是一个例子](https://play.grafana.org/d/000000109/the-four-golden-signals?orgId=1)