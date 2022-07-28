## 本地存储

会分组为两个小时一个块  

这个块是一个目录，包括一个chunk子目录，这个子目录包含一个元数据文件和一个索引文件。块目录中的示例由多个段文件组成，
每个段文件512M。

通过api删除时，删除的文件会单独存储在tombstone文件中，而不会直接删除数据（两小时内由后台程序删除）  

当前数据块是保存在内存中的，wal保存在wal目录中，128M一个段，这些数据是未经压缩的，prometheus会保留3个段。  
高并发的服务可能需要保存多于3个wal文件以保证保留2小时数据  

WAL（write-ahead log）,防止prometheus崩溃用的，当prometheus重启时会重放一遍

也可以用api接口存储到远程，但是要仔细评估性能耗时等因素

## 压缩

数据会压缩保留31天，或者保留时间的10%，哪个小为准  

保留时间不太明白  

## 可选项

--storage.tsdb.path 默认data/  
--storage.tsdb.retention.time  数据默认保留15天，  

一个系统需要多少磁盘空间，可以用下面这个公式粗略计算：  
needed_disk_space = retention_time_seconds * ingested_samples_per_second * bytes_per_sample

若本地存储发生错误，最好办法是删除整个存储文件  
NFS不支持，推荐使用本地文件系统  

## 远程存储集成

目前用的协议是snappy-compressed，以后会用gRPC over HTTP/2  
支持完全分布式PromQL目前不可行，因为数据会要先加载到本地  

使用TSDB进行远程存储水过  

federation联邦功能是多个prometheus服务连用的，过