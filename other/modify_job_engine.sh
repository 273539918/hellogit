#!
job_engine="ea120prod_ea119blinkcptssd1_root__GCJ__alimama_ecpm_odl_tesla_mi"
awk '{print "blinkadmin bayes job stop "$0}' job_list  > stop_job
awk '{print "blinkadmin bayes job set_job_engine "$0 " '$job_engine'"}' job_list  > set_job_engine
awk '{print "blinkadmin bayes job start "$0}' job_list  > start_job