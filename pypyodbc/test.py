# -*- coding: utf-8 -*-
import sys, os, os.path
import pypyodbc
import ctypes


def cur_file_dir():
    return os.path.dirname(os.path.realpath(sys.argv[0]))

c_Path = ctypes.create_string_buffer(u"CREATE_DB=.\\人.mdb General\0".encode('mbcs'))
ODBC_ADD_SYS_DSN = 1
#ctypes.windll.ODBCCP32.SQLConfigDataSource(None,ODBC_ADD_SYS_DSN,"Microsoft Access Driver (*.mdb)", c_Path)


def u8_enc(v, force_str = False):
    if v == None:
        return ('')
    elif isinstance(v,unicode):
        return (v.encode('utf_8','replace'))
    elif isinstance(v, buffer):
        return ('')
    else:
        if force_str:
            return (str(v))
        else:
            return (v)




if __name__ == "__main__":
    
    DSN_list = pypyodbc.dataSources()
    print (DSN_list)
    
    if sys.platform == "win32":
        dsn_test =  'mdb'
    else:
        dsn_test =  'pg'
    user = 'tutti'


    



    
    conn = pypyodbc.connect(u'Driver={Microsoft Access Driver (*.mdb)};DBQ='+cur_file_dir()+u'\\人.mdb')
    #conn = connect('DSN=PostgreSQL35W')
    #Dsn list
    #print conn.info
    #Get tables list
    #cur = conn.cursor()
    #tables = cur.tables()
    #if sys.platform == "win32": t = tables[0][0]
    #else: t = "ttt"
    
    #cur.close()
    cur = conn.cursor()
    #Get fields on the table
    #cols = cur.columns(t)
    #print cols
    #Make a query
    
    cur.close()
    cur = conn.cursor()
    try:
        cur.execute(u""" DROP TABLE data; """)
    except:
        pass
    cur.execute(u"""CREATE TABLE  pp(pp varchar(100));""")
    cur.execute(u"""select * from data""".encode('mbcs'))
    print [(x[0], x[1]) for x in cur.description]
    #Get results
    import time
    
    for row in cur.fetchmany(15):
        for field in row:
            print type(field),
            
            if isinstance(field, unicode):
                print (field.encode('mbcs'))
            else:
                print (field)
            time.sleep(0.2)
            

    
    
    print (len(cur.fetchall()))
    
    cur.close()
    cur = conn.cursor()
    #cur.execute(u"delete from data ".encode('mbcs'))
    
    cur.execute(u"""select * from data""".encode('mbcs'))

    #Get results
    
    for row in cur.fetchmany(8):
            print (u' '.join([field for field in row]).encode('mbcs'))
    
    cur.close
    conn.rollback()
    cur = conn.cursor()

    cur.execute('update data set Num = '+str(time.time()))
    conn.commit()
    for row in cur.execute(u"""select * from data""".encode('mbcs')).fetchone():
        for field in row:
            if isinstance(field, unicode):
                print (field.encode('mbcs'))
            else:
                print (field)
        print ('')
        print (cur.description)
    
    i = 1
    row = cur.fetchone()
    while row != []:
        row = cur.fetchone()
        for field in row:
            x = field
        i += 1
        if i % 2500 == 0:
            print (i)
    #print conn.FetchAll()
    #Close before exit
    cur.close()
    conn.close()
