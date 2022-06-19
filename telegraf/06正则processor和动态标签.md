## Regex Processor plugin

processor用来生成动态tag，这个可以通过正则方式来改变tag值，生成新的tag

## 例子

ping希望有一个新的标签，点前面的字符  

```ini
[[processors.regex]]
namepass = ["ping"]

[[processors.regex.tags]]
key = "url"
pattern = "^([^.]+).*$"
replacement = "${1}"
result_key = "service_name"
```

可以通过https://regex101.com/这个网站尝试正则  

