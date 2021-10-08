import mysql.connector


User_name = input("Enter Username :")
Pw = input("Enter Password :")

def login():
    global Username
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="",
            database="Publication"
        )
    except:
        print("Not Connected to the Server(localhost)")
    else:
        print("Successfully Connected")
        #usern = User.get()
        #passw = Pass.get()
        cur = conn.cursor()
        query = "SELECT Username,Password FROM login_details"
        cur.execute(query)
        for (usern,pas) in cur:
            if User_name == usern and Pw == pas:
                login = True
                break
            else:
                login = False
        if login ==True:
            print ("Login Successful",User_name)
        elif login == False:
            print ("Email or Password is wrong")
        cur.close()
        conn.close ()