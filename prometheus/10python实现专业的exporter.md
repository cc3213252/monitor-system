localhost:9275/metrics

python_my_counter_total python会自动给我们加一个total的后缀

业务含义： 两个地址累加的方式，另外一个显示实时的值  

注意： docker-compose.yml里面的服务名必须与prometheus.yml里面的job_name一致  
      prometheus Web界面能查到python的指标了才成功