## 问题产生

rate(net_bytes_recv[2m])*8通过这种方式取速率速度比较慢，可以让prometheus在后台算好速率  

## recording rules可以解决

      - record: demo_recording_net_rate_bps
        expr: rate(net_bytes_recv[2m])*8

表达式计算完保存到demo_recording_net_rate_bps

docker restart prometheus

## 常见问题

不要忘记在prometheus.yml中增加rule_files，视频没有讲这个  