import psycopg2

class database():
    def __init__(self) -> None:
        self.cursor = self.getCursor()
        
    def getCursor(self) -> object:

        conn = psycopg2.connect(database="student details",user="postgres",password="12345",host="localhost",port="5432")
        conn.autocommit = True
        cur = conn.cursor()

        return cur

    def executeQuery(self, query, tup : tuple = None) -> None:
        if tup != None:
            self.cursor.execute(query, tup)
        else:
            self.cursor.execute(query)

    
    def selectUID(self, uid: str) -> None:
        query = "SELECT * FROM student_info WHERE uid = %s"
        self.executeQuery(query, tup = (uid,)) 
        
        return self.cursor.fetchall()[0]

    def insertValues(self, uid: str, name: str, address: str,
                    curCGPA: float, percent10th: float, 
                    percent12th: float, remarks: str, phone: str) -> None:
        query = "INSERT INTO student_info VALUES(%s, %s, %s, %s, %s, %s, %s, %s)"
        self.executeQuery(query, tup = (uid, name, address, curCGPA, percent10th, percent12th, remarks, phone))


db = database()
db.insertValues('6687', 'Aaryan', 'Somewhere', 8.6, 98.5, 99.9, 'Big', '9891558594')
print(db.selectUID('6687'))