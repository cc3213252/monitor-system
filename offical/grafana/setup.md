## install grafana

brew install grafana  

配置文件：  
/usr/local/Cellar/grafana/[version] (Homebrew v2)
/opt/homebrew/Cellar/grafana/[version] (Homebrew v3)  

## configure grafana

enable_gzip这个配置为true可以加快访问速度，但默认为了兼容性是false  
cdn_url，加快访问速度  
默认是sqlite3数据库  
remote_cache，权限类缓存加快速度，用redis  
send_user_header，设置为true可以把用户名字放在头中，默认false  
支持一些grafana使用bi统计  
enable_feedback_links，设置为false可以删除所有反馈的链接，默认true  
默认是开启防爆破功能  
x_xss_protection，防止xss攻击，默认关闭  
default_theme，有dark和light  
viewers_can_edit，设置为true，用户可以编辑但不能保存，默认false  
editors_can_admin，设置为true，用户可以动dashboard、文件夹和team  
disable_login_form，sso登陆时隐藏登陆框  
signout_redirect_url，退出登陆后可以跳到车联网安全中心  
支持sentry  
org_user，默认10个用户  
org_data_source，一个组织限制10个  
org_alert_rule，一个组织限制100条规则  
enable_alpha，启用panels、plugins中的试用功能  
allow_loading_unsigned_plugins，允许未签名插件  

default_timezone 
default_week_start  

调试grafana的性能问题时，可以使用tracing部分定位原因  
./grafana-server -profile -profile-addr=0.0.0.0 -profile-port=8080  

企业版可以换图标和应用名  
可以配置数据库加密，可以配置kms    
可以启用日志审计，到loki  
可以设置访问source或alert的频率、ip  

[分布式系统中端到端跟踪系统Jaeger](https://www.jaegertracing.io/)  
可以把grafana监控配置到prometheus，要借助[backend plugins](https://grafana.com/docs/grafana/latest/developers/plugins/backend/)  

把默认数据库改成mysql，多个grafana共享，就是高可用，session存在db中的，故不用在每个服务登陆    
alerting也可以高可用  

在告警中可以带上panel的图片，rendered后，图片保存到png文件夹，后台程序10分钟清理一次图片  
需要装一个[Image renderer plugin](https://grafana.com/grafana/plugins/grafana-image-renderer/#installation)  
可以对Image renderer plugin[增加监控](https://grafana.com/docs/grafana/latest/setup-grafana/image-rendering/monitoring/)  

ENABLE_METRICS=true，设置这个增加prometheus监控  
可以增加[nginx监控面板](https://github.com/gilbN/lsio-docker-mods/tree/master/letsencrypt/geoip2-nginx-stats)

设置日志等级debug来调试问题，特别是renderer类问题  
缺少lib类问题  

grafana live是一个实时消息引擎，可以发给自己的前端，也可以用订阅推送功能
比如dashboard发生变化了等消息  

【重要】[telegraf的数据可以直接在grafana展示](https://grafana.com/tutorials/stream-metrics-from-telegraf-to-grafana/)