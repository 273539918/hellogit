#!/usr/bin/python
# -*- coding: UTF-8 -*-
##

machine_cpu = 96
machine_mem = 512
yarn_cpu = 92
yarn_mem = 512
cpu_ratio = 1.21
mem_ratio = 1.21
cpu_high_water = 0.9
cpu_low_water = 0.5
mem_high_water = 0.9
mem_low_water = 0.7
rm_host = "bd011014044002.ea120.tbsite.net"

print """ ---- update key  for yarn.site  ---- """
print "yarn.nodemanager.resource.cpu.report-ratio=%.2f" % (cpu_ratio)
print "yarn.nodemanager.resource.memory.report-ratio=%.2f" % (mem_ratio)
print "yarn.nodemanager.overallocation.cpu-utilization-threshold=%.2f" % (
    machine_cpu * cpu_high_water / (yarn_cpu * cpu_ratio) - 0.1)
print "yarn.nodemanager.overallocation.memory-utilization-threshold=%.2f" % (
    machine_mem * mem_high_water / (yarn_mem * mem_ratio) - 0.1)
print "yarn.nodemanager.overallocation.general-utilization-threshold=%.2f" % (
    min(machine_cpu * cpu_high_water / (yarn_cpu * cpu_ratio) - 0.1,
        machine_mem * mem_high_water / (yarn_mem * mem_ratio) - 0.1)
)
print """yarn.nodemanager.resource.memory.enforced=false
yarn.nodemanager.resource.percentage-physical-cpu-limit=95
yarn.scheduler.maximum-allocation-vcores=3000
yarn.am.liveness-monitor.expiry-interval-ms=300000
"""
print """ ---- end ---- """

cpu_high_water_mark = round(machine_cpu * cpu_high_water / (yarn_cpu * cpu_ratio), 2)
cpu_low_water_mark = round(machine_cpu * cpu_low_water / (yarn_cpu * cpu_ratio), 2)
mem_high_water_mark = round(machine_mem * mem_high_water / (yarn_mem * mem_ratio), 2)
mem_low_water_mark = round(
    machine_mem * mem_low_water / (yarn_mem * mem_ratio), 2)
print """ ---- update key  for  sheduler  ---- """
print "yarn.resourcemanager.monitor.capacity.hotspot-rebalance.cpu.high-water-mark=%s" % (
    cpu_high_water_mark)
print "yarn.resourcemanager.monitor.capacity.hotspot-rebalance.cpu.low-water-mark=%s" % (
    cpu_low_water_mark)
print "yarn.resourcemanager.monitor.capacity.hotspot-rebalance.memory.high-water-mark=%s" % (
    mem_high_water_mark)
print "yarn.resourcemanager.monitor.capacity.hotspot-rebalance.memory.low-water-mark=%s" % (mem_low_water_mark)
print "yarn.resourcemanager.monitor.capacity.hotspot-rebalance.non-overlimit-guaranteed-containers.preemption-disabled=false"

print """ ---- end ---- """

print """
curl -X PUT -H "Content-type: application/json" 'http://{rm_host}:8088/ws/v1/cluster/sched-conf'  -d '
""".format(rm_host=rm_host)

print "{"
print """
"global-updates": [
   { 
     "entry": [{
       "key":"yarn.resourcemanager.monitor.capacity.hotspot-rebalance.cpu.high-water-mark",
       "value":"%s"
     },
     {
       "key":"yarn.resourcemanager.monitor.capacity.hotspot-rebalance.cpu.low-water-mark",
       "value":"%s"
     },
     {
       "key":"yarn.resourcemanager.monitor.capacity.hotspot-rebalance.memory.high-water-mark",
       "value":"%s"
     },
     {
       "key":"yarn.resourcemanager.monitor.capacity.hotspot-rebalance.memory.low-water-mark",
       "value":"%s"
     }
     ]
   }
 ]
""" % (cpu_high_water_mark, cpu_low_water_mark, mem_high_water_mark, mem_low_water_mark)
print "}'"
