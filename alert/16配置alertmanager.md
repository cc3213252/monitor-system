## 要配三个地方

1、prometheus.yml  
2、alertmanager.yml  
3、docker-compose.yml  

## 访问

http://localhost:9093/#/alerts  

## 触发告警

docker stop host1  
大概过3分钟，可以看到prometheus中有fire记录  
再到alerts界面，有详细告警内容了  