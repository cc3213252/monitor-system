## 默认数据源

--Grafana--： 随机数据，测试可视化组件用  
--Mixed--: 多个数据源在一个panel显示  
--Dashbboard--: 使用同一个dashboard中的另一个panel  

## expressions

expressions主要用于告警  
Operation有四种：  
Math  公式  
Reduce 分别作用于每个数据最后得到一个数据，有mode，可以丢弃空值    
Resample 重新采样，统一调整时间戳为相同间隔  
Classic condition 另一个查询中的条数是否符合要求，或者最大最小值等  

## Query inspect

检查查询  
右侧data栏可以download csv  
Stats可以检查所花费时间  
Query可以查看请求和返回的数据  

## Data links

用于点击panel时显示链接信息  
可以用$、ctrl + Space出现提示，生成特定地址链接  

## Transform data

作用：字段重命名  
一个视图可以作为另一个视图的起点  

Mode--Reduce row  把Calculation函数按行作用于Field name指定的字段  
Mode--Binary option  一行中的两个字段做算术运算成一个字段  

Convert field type可以把字符串转成数字，日期格式转换等   
Filter data by name可以删除部分结果  
Filter data by value可以过滤一些特定数据的记录    

可以集成的插件：  
echarts、OnCall、MapTrack3D、Gantt、Radar Graph、Website Navigation Panel、Colored svg panel  

换主题： Boom Theme
[Redis dashboard](https://demo.volkovlabs.io/d/TgibHBv7z/redis-overview?orgId=1&refresh=1h)