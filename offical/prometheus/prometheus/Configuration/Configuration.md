## Configuration

可以用命令行或者文件来配置，命令行用于配置不可变的系统参数，如存储路径，本地存多少等  
看所有命令行： ./prometheus -h  

在--web.enable-lifecycle开启下，可以通过/-/reload命令，这个命令发送一个SIGHUP消息  

[一个较好的完整的配置](https://github.com/prometheus/prometheus/blob/release-2.37/config/testdata/conf.good.yml)  
relabel_configs，动态抓取前修改label  
honor_labels，如为true，则以抓取配置为准，冲突时忽略服务端配置，这个配置在pushgateway中可能有用    
honor_timestamps，如为true，采用抓取时间戳  


可以和consul的sd（服务发现）联合使用，还有各种服务发现    

alert_relabel_configs，发给alertmanager之前可以修改label  
tracing_config，还是实验特点  
remote_write，发送到远程端点前修改label  
remote_read，[可以集成服务写到alert webhook](https://prometheus.io/docs/operating/integrations/#remote-endpoints-and-storage)






