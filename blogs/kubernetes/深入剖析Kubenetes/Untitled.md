有一个疑问 ，Calico IPIP模式下。IPIP封包前后，IP Header里面的目的IP都是“192.168.2.2”。那为什么封包前不能从Node1发送到Node2 ？

6.20 

Node 2 跟 Node 1 却根本不在一个子网里，没办法通过二层网络把 IP 包发送到下一跳地址。