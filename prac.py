import pymysql

def write_file(data, filename):
    with open(filename, 'wb') as f:
        f.write(data)

def read_blob(category, filename):
    query= "SELECT image FROM images where category= %s  "
    
    db_config=pymysql.connect(user='root',password='mypass',database='spor')
    
    try:
        cursor=db_config.cursor()
        cursor.execute(query, (category))
        photo=cursor.fetchone()[0]
        
        write_file(photo,filename)
    except:
        
        print("oopsie")
    finally:
        cursor.close()
        db_config.close()
def main():
    
    
    read_blob('plant', 'hfresh\test15.jpg' )
if __name__ == '__main__':
    main()
            