不想在本地挂载配置文件，可以这么做：  
```ini
FROM prom/prometheus
ADD prometheus.yml /etc/prometheus/
```
```bash
docker build -t my-prometheus .
docker run -p 9090:9090 my-prometheus
```

有用ansible管理prometheus，还有chef、puppet、saltstack等