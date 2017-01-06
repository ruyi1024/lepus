#!/bin/env python
#-*-coding:utf-8-*-

import pymssql
import string
import sys 
import datetime
import time
reload(sys) 
sys.setdefaultencoding('utf8')
import ConfigParser

def get_item(data_dict,item):
    try:
       item_value = data_dict[item]
       return item_value
    except:
       pass


def get_variables(conn,var_name):
    try:
        curs=conn.cursor()
        data=curs.execute('select @@'+var_name);
        data=curs.fetchone()
        parameters=data[0]

    except Exception,e:
        print e

    finally:
        curs.close()

    return parameters

def get_version(conn):
    try:
        curs=conn.cursor()
        data=curs.execute("SELECT @@VERSION");
        data=curs.fetchone()
        result  = data[0].split(' ')[3]
    except Exception,e:
        print e

    finally:
        curs.close()

    return result

def get_uptime(conn):
    try:
        curs=conn.cursor()
        data=curs.execute("SELECT crdate time_restart,GETDATE() AS time_now,DATEDIFF(mi,crdate,GETDATE()) AS minutes_since_restart,@@cpu_busy/15000.0 AS minutes_cpu_busy,@@io_busy/15000.0 AS minutes_io_busy,@@idle/15000.0 AS minutes_idle,(@@cpu_busy+@@io_busy+@@idle)/15000.0 AS minutes_since_restart2,@@connections AS connections FROM master..sysdatabases WHERE name = 'tempdb'");
        data=curs.fetchone()
        result  = int(data[2]*3600)
    except Exception,e:
        print e

    finally:
        curs.close()

    return result


def get_database(conn,field):
    try:
        curs=conn.cursor()
        curs.execute("select %s from v$database" %(field) );
        result = curs.fetchone()[0]

    except Exception,e:
        result = ''
        print e

    finally:
        curs.close()

    return result


def ger_processes(conn):
    try:
        curs=conn.cursor()
        curs.execute("SELECT COUNT(*) FROM [Master].[dbo].[SYSPROCESSES] WHERE [DBID] IN ( SELECT  [dbid] FROM [Master].[dbo].[SYSDATABASES])");
        result = curs.fetchone()[0]
        return result

    except Exception,e:
        return null    
        print e

    finally:
        curs.close()


def ger_processes_running(conn):
    try:
        curs=conn.cursor()
        curs.execute("SELECT COUNT(*) FROM [Master].[dbo].[SYSPROCESSES] WHERE [DBID] IN ( SELECT  [dbid] FROM [Master].[dbo].[SYSDATABASES])  AND  status !='SLEEPING' AND status !='BACKGROUND'");
        result = curs.fetchone()[0]
        return result

    except Exception,e:
        return null
        print e

    finally:
        curs.close()

def ger_processes_waits(conn):
    try:
        curs=conn.cursor()
        curs.execute("SELECT COUNT(*) FROM [Master].[dbo].[SYSPROCESSES] WHERE [DBID] IN ( SELECT  [dbid] FROM [Master].[dbo].[SYSDATABASES])  AND  status ='SUSPENDED' AND waittime >2 ");
        result = curs.fetchone()[0]
        return result

    except Exception,e:
        return null
        print e

    finally:
        curs.close()


