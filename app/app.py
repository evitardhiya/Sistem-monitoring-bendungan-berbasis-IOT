import serial
import datetime
import time
import mysql.connector


if __name__ == '__main__':
    db = mysql.connector.connect(
        user= 'xxxx',
        password= 'xxxxx!',
        db= 'xxxxx',
        host= 'localhost',
        port= 3306
    )
    cursor = db.cursor()
    seri1=serial.Serial(port="COM4", timeout=1.5, baudrate=9600)
    seri2=serial.Serial(port="COM8", timeout=1.5, baudrate=9600)
    waktu1 = datetime.datetime.now()
    while True:
        a1=str(seri1.readline().strip())
        a2=str(seri2.readline().strip())
        data1 = a1.split("'")
        data2 = a2.split("'")
        print(data1,data2,a1,a2)
        command = """ INSERT INTO myapp_data_sensor
        (ketinggian_air, curah_hujan, tanggal_input)
        VALUES (%s,%s,%s) """
        value = tuple((str(data2[1]),str(data1[1]),str(waktu1)))
        cursor.execute(command,value)
#        time.sleep(1)
