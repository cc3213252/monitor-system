自动服务发现，支持k8s，dns，openstack,consul等自动服务发现功能

应做到：  
k8s服务扩容、缩容主动发现node  
中间件和自己服务自动发现，给每个服务绑定一个exporter容器，给这类容器打标签，再用prometheus的relabel功能