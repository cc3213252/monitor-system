## 创建一个显示内存cpu使用量的图形

cpu_usage_system{cpu="cpu-total"}  
mem_used  

Unit:  
mem: bytes(IEC)  
cpu: Percent(0-100)

数据对应在Series overrides里做：  
Alias or regex: cpu  
Y-axis: 2  
Color: red  

dashboard的导出和引入等操作

## 08 stat gauge等操作