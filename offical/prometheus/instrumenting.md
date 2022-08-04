[python client library](https://github.com/prometheus/client_python)

## client libraries

用client libraries主要用来实现prometheus的metric types  

有lua版client libraries，用来集成在kong上  

没有合适的客户端库，也可以自己实现，只要符合[exposition formats](https://prometheus.io/docs/instrumenting/exposition_formats/)

## writing client libraries

讲作为客户端库应该提供的函数和api

ENCOURAGED，最好有，也可以没有  
MUST，基于内部回调，线程安全    
SHOULD，需要遵守这里的结构  

histograms允许聚合

同一个指标不应该用不同的label

看到Exposition