import pymysql
from textblob import TextBlob


def trans(sentence):
    blob = TextBlob(sentence);
    return blob.translate(to="fr");


# Open database connection
db = pymysql.connect("localhost", "root", "password", "enc")
# prepare a cursor object using cursor() method
cursor = db.cursor()

# Prepare SQL query to INSERT a record into the database.
sql = "SELECT * FROM translation"

try:
    # Execute the SQL command
    cursor.execute(sql)
    # Fetch all the rows in a list of lists.
    results = cursor.fetchall()
    for row in results:
        user_input = row[0]
        # Now print fetched result
        print("User Input = %s" % (user_input))
        # try:
        # print("Translation : %d" % (int(user_input)))
        # except ValueError:
        try:
            transVal = trans(user_input)
            print("Translation : %s" % transVal)
            sql1 = "UPDATE translation SET  translation_value = %s WHERE translation_key =%s"
            strVal = str(transVal)
            data = (strVal, user_input)
            # print("SQL : " %sql1)
            cursor.execute(sql1, data)
            db.commit()
        except (pymysql.Error, pymysql.Warning) as e:
            # Rollback in case there is any error
            print("Error %s" % e)
            db.rollback()


except (pymysql.Error, pymysql.Warning) as e:
    print("Error: unable to fetch data %s" % e)
    # disconnect from server
    cursor.close()
    db.close()
