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



### 在线Kubernetes集群

https://www.katacoda.com/courses/kubernetes/playground

#### 本地搭建Kuberentes集群

minikube: https://github.com/kubernetes/minikube

### 搭建生产可用的Kubernetes集群

Kubeadm: https://kubernetes.io/docs/reference/setup-tools/kubeadm/



## 04 | 核心定义：Kubernetes 是如何搞定“不可变基础设施”的？

### 云原生的CNCF定义

云原生的代表技术包括容器技术、服务网格、微服务、不可变基础设施和声明式API。 借助这些典型的云原生技术，我们可以构建容错性好、易于管理、便于观察的松耦合系统。结合可靠的自动化手段，云原生技术使得工程师能够轻松对系统作出频繁和可预测的重大变更。

### 什么是不可变基础设施

不可变基础设施中的基础设施可以理解为服务器、虚拟机或者是容器。

与不可变基础设施对应的是可变基础设施，在传统的开发运维体系中，软件开发完成后，需要管理员登陆通过SSH登录到服务上来进行服务器的配置、软件包的安装等等操作，后续还可能会对服务器的配置做各种更改，这种可变基础设施带来的问题是：

1） 基础设施持续的变更给服务运行态引入了过多的中间态，增加了不可预知的风险
2） 不易标准化，交付运维过程异常痛苦，比如你可能经常遇到的，某个软件包几个月之前安装还能够正常运行，现在到一个新环境安装后，竟然无法正常工作了。
3）故障发生时，难以及时快速构建出新的服务副本；

不可变基础设施，则是部署完成以后，便成为一种只读状态，不可对其进行任何更改。如果需要更新或修改，就使用新的环境或服务器去替代旧的。可变和不可变最核心的区别在于：前者的组件旨在在部署后进行更改;后者的组成部分旨在保持不变并最终被替换

Kubernetes中的不可变基础设施就是Pod。

### Kubernetes为什么不直接使用容器，而抽象出Pod

因为使用一个新的逻辑对象 Pod 来管理容器，可以在不重载容器信息的基础上，添加更多的属性，而且也方便跟容器运行时进行解耦，兼容度高。比如：

（1）存活探针（Liveness Probe）可以从应用程序的角度去探测一个进程是否还存活着，在容器出现问题之前，就可以快速检测到问题；
（2）容器启动后和终止前可以进行的操作，比如，在容器停止前，可能需要做一些清理工作，或者不能马上结束进程；

（3）定义了容器终止后要采取的策略，比如始终重启、正常退出才重启等；



### 例子

一个pod的yaml

```
apiVersion: v1 #指定当前描述文件遵循v1版本的Kubernetes API

kind: Pod #我们在描述一个pod

metadata:

  name: twocontainers #指定pod的名称

  namespace: default #指定当前描述的pod所在的命名空间

  labels: #指定pod标签

    app: twocontainers

  annotations: #指定pod注释

    version: v0.5.0

    releasedBy: david

    purpose: demo

spec:

  containers:

  - name: sise #容器的名称

    image: quay.io/openshiftlabs/simpleservice:0.5.0 #创建容器所使用的镜像

    ports:

    - containerPort: 9876 #应用监听的端口

  - name: shell #容器的名称

    image: centos:7 #创建容器所使用的镜像

    command: #容器启动命令

      - "bin/bash"

      - "-c"

      - "sleep 10000"

```

 

```
#kubectl apply -f two_containers_pod.yaml
pod/twocontainers created
#kubectl exec twocontainers -c shell -i -i --bash
[root@twocontainers /]# curl -s localhost:9876/info
{"host": "localhost:9876", "version": "0.5.0", "from": "127.0.0.1"}
```



## 05 | K8s Pod：最小调度单元的使用进阶及实践



查看pod的状态

```
$kubectl get pod twocontainers -o=jsonpath='{.status.phase}'
Running
```

### Pod的健康检测

通过下例说明Pod的检查检查： startupProbe、livenessProbe、readinessProbe的工作流程

```
apiVersion: v1
kind: Pod
metadata:
  name: probe-demo
  namespace: demo
spec:
  containers:
  - name: sise
    image: quay.io/openshiftlabs/simpleservice:0.5.0
    ports:
    - containerPort: 9876
    readinessProbe:
      tcpSocket:
        port: 9876
      periodSeconds: 10
    livenessProbe:
      periodSeconds: 5
      httpGet:
        path: /health
        port: 9876
    startupProbe:
      httpGet:
        path: /health
        port: 9876
      failureThreshold: 3
      periodSeconds: 2
```

1、 kubelet创建好对应的容器后，会先运行 startupProbe 中的配置，这里我们用 HTTP handler 每隔 2 秒钟通过 http://localhost:9876/health 来判断服务是不是启动好了。这里我们会尝试 3 次检测，如果 6 秒以后还未成功，那么这个容器就会被干掉。而是否重启，这就要看 Pod 定义的重启策略。

2、一旦容器通过了 startupProbe 后，Kubelet 会每隔 5 秒钟进行一次探活检测 （livenessProbe），如果检查通过，表示容器正常存活

3、每隔 10 秒进行一次就绪检测（readinessProbe）。如果检查不通过，表示容器提供的服务不正常，如果有Service就会将其“隔离”，待服务正常后恢复



### init容器

Pod中允许定义init容器来完成一些初始化的工作，应用容器专注于业务处理，其他一些无关的初始化任务就可以放到 init 容器中。这种解耦有利于各自升级，也降低相互依赖。一个 Pod 中允许有一个或多个 init 容器。init 容器和其他一般的容器非常像，其与众不同的特点主要有：
1）总是运行到完成，可以理解为一次性的任务，不可以运行常驻型任务，因为会 block 应用容器的启动运行；
2）顺序启动执行，下一个的 init 容器都必须在上一个运行成功后才可以启动；
3）禁止使用 readiness/liveness 探针，可以使用 Pod 定义的activeDeadlineSeconds，这其中包含了 Init Container 的启动时间；
4）禁止使用 lifecycle hook。

如下是一个例子：

在 myapp-container 启动之前，它会依次启动 init-myservice、init-mydb，分别来检查依赖的服务是否可用。

```
apiVersion: v1
kind: Pod
metadata:
  name: myapp-pod
  namespace: demo
  labels:
    app: myapp
spec:
  containers:
  - name: myapp-container
    image: busybox:1.31
    command: [‘sh’, ‘-c’, ‘echo The app is running! && sleep 3600‘]
  initContainers:
  - name: init-myservice
    image: busybox:1.31
    command: ['sh', '-c', 'until nslookup myservice; do echo waiting for myservice; sleep 2; done;']
  - name: init-mydb
    image: busybox:1.31
    command: ['sh', '-c', 'until nslookup mydb; do echo waiting for mydb; sleep 2; done;']
```



































































