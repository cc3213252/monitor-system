## Grouping

把多个同类型告警归类为一个告警  

比如可以把同一台服务器的相关告警归类为一个grouping  
在配置文件中配置

## Inhibition

抑制警报，比如一个集群不可达了，已经有告警了，其他的告警就被抑制，以免报和实际情况无关的警告  
在配置文件中配置  

## Silences

符合一定规则在一段时间内不报  
在web界面配置  

配置--cluster-*可以达到高可用目的