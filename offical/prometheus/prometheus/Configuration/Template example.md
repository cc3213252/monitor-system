prometheus用的模版语音是基于[Go templating](https://golang.org/pkg/text/template/)  

性能考虑，写在annotations中的模版应轻量化，复杂的模版应放到consule里面去  

## Simple iteration

{{ range query "up" }}
  {{ .Labels.instance }} {{ .Value }}
{{ end }}

.包含当前sample

## Display one value

go的template是强类型的  

{{ with query "some_metric{instance='someinstance'}" }}
  {{ . | first | value | humanize }}
{{ end }}

以上模版不太理解  
有错误发生时，prom_query_drilldown这个sample会处理

## Using console URL parameters

这块也不太理解，还有借助range来循环的高级用法，用到时查官网  

## 定义重复使用的模版

{{define "myTemplate"}}
  do something
{{end}}

{{template "myTemplate"}}