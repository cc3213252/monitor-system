筛选字段，用Transform功能

Filter by name筛选字段

## 合并两个数据源

ping_average_response_ms format:table  
ping_maximum_response_ms format:table   
transform里面用outer join, field name: url  

修改表头： transform中用organize fields  
修改单位： 右侧field-Standard options-Unit
         milliseconds(ms)


## overrides用法

对某个字段可以特殊定制化，阈值，单位，颜色等