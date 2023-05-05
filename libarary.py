import pymysql
# mysql database coonection
con = pymysql.connect(host="localhost",    
                     user="root",         
                     password="********",
                     database= "libarary"
                     )        


#feedback report of the customers
def feedback():
    sql = """SELECT * FROM books.feedback"""
    cur = con.cursor()
    cur.execute(sql)
    for row in cur:
        print(f'row = {row}')
    print()

feedback()
con.close()