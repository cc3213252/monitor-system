## tags和field的区别

看ping文档，可以看到tags是指url，fields是指packet_transmited等字段

telegraf主要是用来对接influxdb，
tags值有限，可以做index，fields是无限的，无法做index  