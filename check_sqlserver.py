#!/usr/bin/env python
import os
import sys
import string
import time
import datetime
import MySQLdb
import pymssql
import logging
import logging.config
logging.config.fileConfig("etc/logger.ini")
logger = logging.getLogger("lepus")
path='./include'
sys.path.insert(0,path)
import functions as func
import lepus_sqlserver as sqlserver
from multiprocessing import Process;

     

def check_sqlserver(host,port,username,passwd,server_id,tags):
    try:
        conn = pymssql.connect(host=host,port=int(port),user=username,password=passwd,charset="utf8")

        connect = 1
        role = -1
        uptime = sqlserver.get_uptime(conn)
        version = sqlserver.get_version(conn)
        
        lock_timeout = sqlserver.get_variables(conn,'LOCK_TIMEOUT')
        trancount = sqlserver.get_variables(conn,'TRANCOUNT')
        max_connections = sqlserver.get_variables(conn,'MAX_CONNECTIONS')
        processes = sqlserver.ger_processes(conn)
        processes_running = sqlserver.ger_processes_running(conn)
        processes_waits = sqlserver.ger_processes_waits(conn)

        connections = sqlserver.get_variables(conn,'CONNECTIONS')
        pack_received = sqlserver.get_variables(conn,'PACK_RECEIVED')
        pack_sent = sqlserver.get_variables(conn,'PACK_SENT')
        packet_errors = sqlserver.get_variables(conn,'PACKET_ERRORS')

        time.sleep(1)

        connections_2 = sqlserver.get_variables(conn,'CONNECTIONS')
        pack_received_2 = sqlserver.get_variables(conn,'PACK_RECEIVED')
        pack_sent_2 = sqlserver.get_variables(conn,'PACK_SENT')
        packet_errors_2 = sqlserver.get_variables(conn,'PACKET_ERRORS')

        connections_persecond = int(connections_2) - int(connections)
        pack_received_persecond = int(pack_received_2) - int(pack_received)
        pack_sent_persecond = int(pack_sent_2) - int(pack_sent)
        packet_errors_persecond = int(packet_errors_2) - int(packet_errors)

        sql = "insert into sqlserver_status(server_id,tags,host,port,connect,role,uptime,version,lock_timeout,trancount,max_connections,processes,processes_running,processes_waits,connections_persecond,pack_received_persecond,pack_sent_persecond,packet_errors_persecond) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
        param = (server_id,tags,host,port,connect,role,uptime,version,lock_timeout,trancount,max_connections,processes,processes_running,processes_waits,connections_persecond,pack_received_persecond,pack_sent_persecond,packet_errors_persecond)
        func.mysql_exec(sql,param)
        func.update_db_status_init(role,version,host,port,tags)

    except Exception, e:
        logger_msg="check sqlserver %s:%s : %s" %(host,port,e)
        logger.warning(logger_msg)
   
        try:
            connect=0
            sql="insert into sqlserver_status(server_id,host,port,tags,connect) values(%s,%s,%s,%s,%s)"
            param=(server_id,host,port,tags,connect)
            func.mysql_exec(sql,param)

        except Exception, e:
            logger.error(e)
            sys.exit(1)
        finally:
            sys.exit(1)

    finally:
        func.check_db_status(server_id,host,port,tags,'sqlserver')   
        sys.exit(1)


def main():

    func.mysql_exec("insert into sqlserver_status_history SELECT *,LEFT(REPLACE(REPLACE(REPLACE(create_time,'-',''),' ',''),':',''),12) from sqlserver_status;",'')
    func.mysql_exec('delete from sqlserver_status;','')

    servers = func.mysql_query('select id,host,port,username,password,tags from db_servers_sqlserver where is_delete=0 and monitor=1;')

    logger.info("check sqlserver controller started.")

    if servers:
         plist = []

         for row in servers:
             server_id=row[0]
             host=row[1]
             port=row[2]
             username=row[3]
             passwd=row[4]
             tags=row[5]
             p = Process(target = check_sqlserver, args = (host,port,username,passwd,server_id,tags))
             plist.append(p)
             p.start()

         for p in plist:
             p.join()

    else:
         logger.warning("check sqlserver: not found any servers")

    logger.info("check sqlserver controller finished.")

if __name__=='__main__':
    main()
