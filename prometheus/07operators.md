ping_packets_received只是这个查询会列出每个网站返回的数据包  

sum(ping_packets_received)算总数据包  
sum(ping_packets_received) by (service_name) 按service_name分类统计  
sum(ping_packets_received) by (service_name, host) 按service_name、host排列组合展示  

ping_maximum_response_ms只是这个查询返回响应最大时间

topk(3, ping_maximum_response_ms) top3最大响应时间

