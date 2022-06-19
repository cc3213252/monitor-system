## 时间戳问题

prometheus每隔5秒查询，telegraf每隔10秒取数据，output每隔2秒flush，时间戳就会有延迟  

最好是output时使用取数据的时间  
配置export_timestamp = true即可  

显示的时间去掉后三个0，可以在下面这个网站上查询：  
https://unixtimestamp.com/index.php  

具体配置资料要查询outputs.prometheus_client：  
https://github.com/influxdata/telegraf/blob/master/plugins/outputs/prometheus_client/README.md