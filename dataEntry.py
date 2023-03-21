import psycopg2
import psycopg2.extras

class database():
    def __init__(self) -> None:
        """
        Initiate the database class by creating a cursor that connects to a (in this case) local database
        """        
        self.cursor = self.getCursor()
        
    def getCursor(self) -> object:
        """Creates a connection curse to perform operations in the database

        Returns:
            cursor (object): connection cursor
        """        

        conn = psycopg2.connect(database="student details",user="postgres",password="12345",host="localhost",port="5432")
        conn.autocommit = True
        cur = conn.cursor()
        self.conn = conn

        return cur

    def executeQuery(self, query, tup : tuple = None) -> None:
        """Executes a query/Performs an operation in postgresql 

        Args:
            query (str): the query to be executed
            tup (tuple, optional): A tuple that can be mapped to format values in the query. Defaults to None.
        """        

        if tup != None:
            self.cursor.execute(query, tup)
        else:
            self.cursor.execute(query)

    
    def selectUID(self, uid: str) -> tuple:
        """Gives the row for the provided UID

        Args:
            uid (str): the user ID to identify a row

        Returns:
            tuple: resulted row that is found
        """        

        """tuple- (id, name, addr, cgpa, 10th%, 12th%, remarks, phone)"""
        query = "SELECT * FROM student_info WHERE uid = %s"
        self.executeQuery(query, tup = (uid,)) 

        res = self.cursor.fetchall()[0]
        return res
    
    def insertValues(self, uid: str, name: str, address: str,
                    curCGPA: float, percent10th: float, 
                    percent12th: float, remarks: str, phone: str) -> None:
        """
            A function to insert values in a row
        Args:
            uid (str): User ID (primary key)
            name (str): Name of the user
            address (str): Address of the user
            curCGPA (float): current CGPA of the user
            percent10th (float): 10th percentage of the user
            percent12th (float): 12th percentage of the user
            remarks (str): remarks by the mentor
            phone (str): Phone no. of the user
        """   

        query = "INSERT INTO student_info VALUES(%s, %s, %s, %s, %s, %s, %s, %s)"
        self.executeQuery(query, tup = (uid, name, address, curCGPA, percent10th, percent12th, remarks, phone))


db = database()
if __name__ == "__main__":
    db.insertValues('6687', 'Aaryan', 'Somewhere', 8.6, 98.5, 99.9, 'Big', '9891558594')
    print(db.selectUID('6668'))