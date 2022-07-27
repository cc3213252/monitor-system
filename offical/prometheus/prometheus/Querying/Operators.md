有四种运算： scalar/scalar, vector/scalar, and vector/vector

逻辑运算符仅适用于instant vectors：  
and 、or、unless  

vector1 unless vector2  表示vector1中有，vector2中没有，用的是精确匹配    

## ignoring例子

method_code:http_errors:rate5m{method="get", code="500"}  24
method_code:http_errors:rate5m{method="get", code="404"}  30
method_code:http_errors:rate5m{method="put", code="501"}  3
method_code:http_errors:rate5m{method="post", code="500"} 6
method_code:http_errors:rate5m{method="post", code="404"} 21

method:http_requests:rate5m{method="get"}  600
method:http_requests:rate5m{method="del"}  34
method:http_requests:rate5m{method="post"} 120

查询：  
method_code:http_errors:rate5m{code="500"} / ignoring(code) method:http_requests:rate5m  
返回：  
{method="get"}  0.04            //  24 / 600
{method="post"} 0.05            //   6 / 120  

ignoring表示结果中去掉该字段  
on是选取显示的字段  

## group_left例子

method_code:http_errors:rate5m / ignoring(code) group_left method:http_requests:rate5m  
结果：  
{method="get", code="500"}  0.04            //  24 / 600
{method="get", code="404"}  0.05            //  30 / 600
{method="post", code="500"} 0.05            //   6 / 120
{method="post", code="404"} 0.175           //  21 / 120  

group_left左对齐  

## 聚合操作

quantile 分位数，0-1之间的数  

例子：  
http_requests_total有三个label： application, instance, and group  
sum without (instance) (http_requests_total)   
等同于  
sum by (application, group) (http_requests_total)  

只关心总数，则sum(http_requests_total)  

统计各个build_version数： count_values("version", build_version)  
top5数量：  topk(5, http_requests_total)  