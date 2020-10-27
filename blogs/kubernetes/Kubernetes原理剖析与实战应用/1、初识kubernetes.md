# 开篇

## 00. 如何深入掌握Kuberentes

 

kuberentes非常重要，国内外各大产对k8s的人家需求旺盛，k8s的学习曲线陡峭，这个课程让k8s学习者更快更稳地掌握k8s。



# 云原生基石

## 01. 前世今生：Kubernetes是如何火起来的？



云计算 -> 成本/适配/迁移 逐渐成为痛点-> 容器化 

容器化的规模越来越大 - > 不得不考虑容器调度、部署、跨多节点访问、自动伸缩等问题 -> 出现了容器编排需求  kubernetes。

容器编排引擎解决的问题包括： 调度、亲和/反亲和、健康检查、容错、可扩展、网络、服务发现、滚动升级



## 02 | 高屋建瓴：Kubernetes 的架构为什么是这样的？

Google先后创建了3套容器调度管理系统：Borg、Omega 和 Kubernetes。Kubernetes的架构设计参考了Borg的架构设计。

### 02.01 k8s与borg的设计相反的点

Borg 在这里面有个特殊的设计，BorgMaster 和 Borglet 之间的交互方式是 BorgMaster 主动请求 Borglet 。即使出现诸如整个 Cell 突然意外断电恢复，也不会存在大量的 Borglet 主动连 BorgMaster，所以就避免了大规模的流量将 BorgMaster 打挂的情况出现。这种方式由 BorgMaster 自己做流控，还可以避免每次 BorgMaster 自己重启后，自己被打挂的情形发生。

在这一点上，Kubernetes 和 Borg 完全相反。Kubernetes 中所有的状态都是采用上报的方式实现的。APIServer 不会主动跟 Kubelet 建立请求链接，所有的容器状态汇报都是由 Kubelet 主动向APIServer 发起的。到这里你也许有疑惑，这种方式会不会对 APIServer 产生很大的流量影响？这个问题，我们同样会在后续课程里，给你一一解答。

### 02.02 k8s核心组件

 kubernetes组件：
（1）kube-apiserve： 所有信息汇聚中枢，请入的入口
（2）Kube-Controller-Manager：控制中枢
（3）Kube-scheduler：负责调度

节点上的组件：
（1）CRI：容器运行时
（2） kubelet: 负责Pod的生命周期
（3）Kube-Proxy：负责k8s内部通信

Add-on 组件：

（1）CoreDNS 负责为整个集群提供 DNS 服务
（2）Ingress Controller 为服务提供外网接入能力
（3）Dashboard 提供 GUI 可视化界面
（4）Fluentd + Elasticsearch 为集群提供日志采集、存储与查询等能力。



## 03 | 集群搭建：手把手教你玩转 Kubernetes 集群搭建















































































