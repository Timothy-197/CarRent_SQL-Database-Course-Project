import csv
import pymysql

conn = pymysql.connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='123456',
    db='CarRental')


with open('test_import.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    headers = next(csv_reader)

    try:
        for row in csv_reader:
            with conn.cursor() as cursor:
                cursor.execute("insert into `car_rental_demand` values (%s, %s, %s)", row)
            conn.commit()
    except Exception as e:
        print(e)
        conn.rollback()
    

#close the connection to the database.
conn.close()
print("Done")
