## prometheus结构

Retrieval: pull metrics  
Storage: Store metrics，是时序数据库    
Http server: Accept Query  

prometheus体系需要提供metrics的服务，叫metrics exporter，就是telegraf

prometheus官网有第三方exporter，有es等  
https://prometheus.io/docs/instrumenting/exporters/

## prometheus为啥设计成pull的方式

1、可以部署多个prometheus同时pull，exporter不关心有几个  
2、pull更容易检测exporter是否挂了，如push则需要定时器了  

