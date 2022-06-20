```text
alert: PacketLoss > 0
expr: ping_percent_packet_loss != 0
for: 2m
labels:
  severity: urgent
```
这个rule的含义是持续2分钟都有丢包则报警  
每隔10秒ping一次host1


步骤：  
1、ping_percent_packet_loss查看丢包状态  
2、http://localhost:9090/alerts查看告警状态  