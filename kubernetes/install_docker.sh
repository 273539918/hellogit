#!/bin/sh

if [ `whoami` != "root" ];then
    echo "please use root to execute this script.."
    exit 1
fi

if [ `which docker >/dev/null 2>/dev/null;echo $?` -eq 0 ];then
    echo "docker already exist in this machine, skip install.."
    exit 2
fi

logfile=/tmp/install_docker.log

function log(){
    level=$1
    shift
    content=$@
    echo "[`date \"+%Y-%m-%d %H:%M:%S\"`][$level] $content" | tee -a $logfile
    if [ "$level" == "ERROR" ];then
        exit 3
    fi
}

function main(){
    log "INFO" "start to install basic system tools.."
    yum install -y device-mapper-persistent-data lvm2 && log "INFO" "install basic system tools success" || log "ERROR" "install basic system tools failed"
    log "INFO" "start to add docker repo source.."
    yum-config-manager --add-repo http://mirrors.aliyun.com/docker-ce/linux/centos/docker-ce.repo && log "INFO" "add docker repo source success"|| log "ERROR" "add docker repo source failed.."
    log "INFO" "start to update & install Docker-CE"
    yum makecache fast

    log "INFO" "check if container-selinux installed or not.."
    if [ `rpm -qa | grep -v grep | grep -c "container-selinux"` -gt 0 ];then
        log "INFO" "container-selinux already installed, skip this.."
    else
        log "INFO" "start to install container-selinux.."
        wget -O /etc/yum.repos.d/CentOS-Base.repo http://mirrors.aliyun.com/repo/Centos-7.repo
        yum install -y epel-release || log "ERROR" "install epel-release failed.."
        yum install -y container-selinux && log "INFO" "install container-selinux success.." || log "ERROR" "install container-selinux failed.."
    fi

    yum -y install docker-ce && log "INFO" "install docker success.." || log "ERROR" "install docker failed.."
    log "INFO" "start docker service"
    systemctl start docker && log "INFO" "start docker success.." || log "ERROR" "start docker service failed.."

    log "INFO" "set docker service auto start.."
    systemctl enable docker.service && log "INFO" "enable docker service auto start success.." || log "ERROR" "enable docker service auto start failed.."
}

main $*
exit $?