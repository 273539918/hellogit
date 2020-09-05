#!
job_engine="ea120prod"
awk '{print "blinkadmin bayes job stop "$0}' modify_job_engine  > stop_job
awk '{print "blinkadmin bayes job set_job_engine "$0 " '$job_engine'"}' modify_job_engine  > set_job_engine
awk '{print "blinkadmin bayes job start "$0}' modify_job_engine  > start_job