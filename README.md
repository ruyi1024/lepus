##Lepus简介

欢迎使用开源Lepus数据库企业监控系统

Lepus(天兔)数据库企业监控系统是一套由专业DBA针对互联网企业开发的一款专业、强大的企业数据库监控管理系统，企业通过Lepus可以对数据库的实时健康和各种性能指标进行全方位的监控。目前已经支持MySQL、Oracle、MongoDB、Redis数据库的全面监控. Lepus可以在数据库出现故障或者潜在性能问题时,根据用户设置及时将数据库的异常进行报警通知到数据库管理员进行处理和优化,帮助企业解决数据库性能监控问题，及时发现性能和瓶颈,避免由数据库潜在问题造成的直接经济损失。Lepus能够查看各种实时性能状态指标，并且对监控、性能数据进行统计分析，从运维者到决策者多个层面的视角，查看相关报表。帮助决策者对未来数据库容量进行更好的规划，从而降低了硬件成本。

Lepus是一个真正的能够帮助企业解决数据库监控和运维的问题，可以帮助企业解决如下问题：

1.帮助企业解决数据库性能监控问题，及时发现性能和瓶颈,避免由数据库潜在问题造成的直接经济损失
 "Lepus数据库企业监控系统"是针对互联网企业开发的一款专业、强大的企业数据库监控管理系统，企业通过Lepus可以对数据库的实时健康和各种性能指标进行全方位的监控。目前已经支持MySQL、Oracle、MongoDB、Redis数据库的全面监控. Lepus可以在数据库出现数据库无法连通、会话数、进程数、等待事件、同步、延时等故障或者潜在性能问题时,根据用户设置阀值及时将数据库的异常进行报警通知到数据库管理员进行处理和优化,避免因数据库故障或性能瓶颈造成直接的经济损失。

2.帮助企业运维领导决策者更好的统筹数据库容量资源，降低企业硬件成本
Lepus采用列式方式呈现监控指标，适合中大型互联网公司大规模数据库的监控管理。通过WEB界面，企业运维人员和决策者可以进行任意几台主机或所有主机监控的数据库性能、系统资源使用情况对比,并提供数据库性能资源按不同维度排序功能，以及系统资源Top信息图表，帮助决策者更好的发现哪些数据库性能开销大,哪些比较空闲,从运维者到决策者多个层面的视角，查看相关报表。帮助决策者对未来数据库容量进行更好的规划，从而降低了硬件成本。

3.帮助企业DBA运维人员解决重复和枯燥的工作，提高运维人员工作效率
面对几时台甚至上百台数据库服务器，如果没有统一的数据库的基础信息，将会使数据库运维管理变的无序，如果想了解数据库的基本健康状态信息，则需要登录数据库或登录服务器。重复的工作容易使人疲惫和厌倦。Lepus提供数据库的基础数据指标采集，比如数据库版本，运行时间，基本健康状态,核心配置参数等基础数据，有了这些基础数据，无需登录机器即可通过系统集中查询，减少了DBA运维人员的重复性工作和枯燥的敲命令工作。

4.慢查询推送和AWR性能报告，降低数据库运维人员和开发人员的沟通成本
Lepus拥有创新的MySQL慢查询分析，TopSQL自动推送，基于时间范围的MySQL AWR性能报告功能。打破了数据库管理人员被动的联系开发人员解决SQL问题的常规低效率现象。Lepus会定时收集影响数据库稳定性的慢SQL,并根据计划任务定时推送查询次数最多,查询时间最长的TopSQL给相关开发人员，开发人员也可以通过有限的权限自主查询任意时间内的慢SQL语句。也可以通过在线AWR性能报告功能查询数据库历史任意时间的数据库性能问题和瓶颈。降低数据库运维人员和开发人员的沟通成本。


- 开发团队:茹作军
- 官方网站:www.lepus.cc
- 文档中心:www.lepus.cc/manual/index
- 交流社区:www.dba-china.com/node/lepus (新社区)
- 捐赠我们:www.lepus.cc/page/crowdfunding
- 联系我们:ruzuojun@139.com (服务/合作/定制/赞助)


##部分客户
`以下是在2014-2015年的时候了解到的一些知名企业在使用Lepus，截止目前，Lepus在官网下载量超过30000+，相信有更多的企业也在默默使用Lepus，当然下列案例都是由企业的DBA提供，也可能目前已经不在使用，具体情况我目前也没有再进行过了解。除此之外目前我还维护着一个商业客户，是由Lepus进行深度定制开发的,如果大家有兴趣或有需求进行定制开发，可以联系我，我会在考虑时间允许的情况下进行开发，包括风格界面，功能增强，服务支持等，但是拒绝廉价劳动力哦，毕竟时间宝贵。`

![](http://www.lepus.cc/themes/default/styles/images/cases_logo/letv.jpg)
![](http://www.lepus.cc/themes/default/styles/images/cases_logo/pinganfang.jpg)
![](http://www.lepus.cc/themes/default/styles/images/cases_logo/feiniu.jpg)
![](http://www.lepus.cc/themes/default/styles/images/cases_logo/ly.jpg)
![](http://www.lepus.cc/themes/default/styles/images/cases_logo/mtime.jpg)
![](http://www.lepus.cc/themes/default/styles/images/cases_logo/mazhan.jpg)
![](http://www.lepus.cc/themes/default/styles/images/cases_logo/365fanyi.jpg)
![](http://www.lepus.cc/themes/default/styles/images/cases_logo/phpok.jpg)

##产品快照

github上面图片被裁剪了，更多产品图片介绍可以查看 http://www.lepus.cc/page/product

###1.监控面板

![](http://www.lepus.cc/themes/default/styles/images/product/lepus_dashboard.jpg)

###2.主机配置

![](http://www.lepus.cc/themes/default/styles/images/product/lepus_mysql_config.jpg)

###3.监控指标

![](http://www.lepus.cc/themes/default/styles/images/product/lepus_mysql_index.jpg)

![](http://www.lepus.cc/themes/default/styles/images/product/lepus_mysql_repl.jpg)

![](http://www.lepus.cc/themes/default/styles/images/product/lepus_mysql_innodb.jpg)

![](http://www.lepus.cc/themes/default/styles/images/product/lepus_mongo_index.jpg)

![](http://www.lepus.cc/themes/default/styles/images/product/lepus_mongo_index.jpg)

![](http://www.lepus.cc/themes/default/styles/images/product/lepus_mongo_indexes.jpg)

###4.性能图表

![](http://www.lepus.cc/themes/default/styles/images/product/lepus_mysql_chart.jpg)

![](http://www.lepus.cc/themes/default/styles/images/product/lepus_mysql_chart2.jpg)

![](http://www.lepus.cc/themes/default/styles/images/product/lepus_mysql_chart3.jpg)

![](http://www.lepus.cc/themes/default/styles/images/product/lepus_oracle_chart1.jpg)

![](http://www.lepus.cc/themes/default/styles/images/product/lepus_oracle_chart2.jpg)

###5.慢查询分析平台

![](http://www.lepus.cc/themes/default/styles/images/product/lepus_mysql_slowquery.jpg)

###6.告警系统

![](http://www.lepus.cc/themes/default/styles/images/product/lepus_alarm.jpg)

###7.AWR性能报告分析

![](http://www.lepus.cc/themes/default/styles/images/product/lepus_mysql_awr.jpg)

![](http://www.lepus.cc/themes/default/styles/images/product/lepus_mysql_awr2.jpg)


