import re
import pymysql

conn = pymysql.connect(host = 'localhost', user = 'root', password = '1234', db = 'firewall', charset = 'utf8')

curs = conn.cursor(pymysql.cursors.DictCursor)

log = re.compile('\d+-\d+-.+dst_port=\d+')

f = open('readtest.txt', 'rb')


while(1):

    data = f.read(0x140)
    
    if data:
        try:
            a_len = len(data)

            n_len = len(log.findall((str(data)))[0])

            l_len = a_len - n_len

            f.seek(-l_len, 1)
            
            data2 = log.findall((str(data)))

            a_data = re.split('[=]', data2[0])

            r_data1 = str(a_data).replace(':', '', 2)
            r_data2 = str(r_data1).replace('-', '')
            r_data3 = r_data2.replace('\'', '')
            r_data4 = r_data3.replace('[', '')
            r_data5 = r_data4.replace(']', '')
            r_data6 = r_data5.replace(',', '.')
            r_data7 = r_data6.replace('.', '')
            r_data8 = r_data7.split(' ')

            
            date = r_data8[0] + r_data8[1]
            src_mac = r_data8[19]
            dst_mac = r_data8[21]
            src_ip = r_data8[23]
            dst_ip = r_data8[25]
            length = r_data8[27]
            src_port = r_data8[29]
            dst_port = r_data8[31]

            sql = "insert into test5(date, src_mac, dst_mac, src_ip, dst_ip, length, src_port, dst_port) values('"+date+"', '"+src_mac+"', '"+dst_mac+"', '"+src_ip+"', '"+dst_ip+"', '"+length+"', '"+src_port+"', '"+dst_port+"')"

            q_data = (date, src_mac, dst_mac, src_ip, dst_ip, length, src_port, dst_port)

            #print(q_data)
            
            curs.execute(sql)
            conn.commit()

            
        except:
            pass
        
    else:
         break
readtest.py 
