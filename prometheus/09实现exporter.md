只要返回类似localhost:9273/metrics格式的数据就行

查看自定义的python服务：  
localhost:9275/metrics  

或者：  
curl localhost:9275/metrics


进入python服务：  docker exec -it 172676255cb2 sh  
当本地修改metrics时，会发现容器里面也发生变化，下次prometheus  
说明只需动态维护一个文件，就实现了监控  