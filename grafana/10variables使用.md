settings - variables

用来在界面提供一个筛选  

## 变量联动功能

先选的放前面，后选的把前面那个选择的当作Query:  
ping_average_response_ms{environment="$environment"}  

正则里面选出url： /.*url=\"([^\"]*).*/

在variable这个图里面ping_average_response_ms{url="$url"}

## 标题联动功能

panel title改成： variable $url

## 显示多个方法

settings-variables-url中multi-value打开  
ping_average_response_ms{url=~"$url"}