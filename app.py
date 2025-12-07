from flask import Flask
import redis
import pymysql  

app = Flask(__name__)

# Redis connection
r = redis.Redis(host="redis", port=6379)

# MySQL connection details
DB_HOST = "mysql"
DB_USER = "root"
DB_PASSWORD = "dipesh@123"
DB_NAME = "dipeshDB"


def check_redis():
    try:
        r.ping()
        return "Redis is UP!"
    except Exception as e:
        return f"Redis is DOWN! ({e})"


def check_mysql(db_host, db_name, db_user, db_password):
    try:
        connection = pymysql.connect(
            host=db_host,
            user=db_user,
            password=db_password,
            database=db_name,
            connect_timeout=5
        )
        connection.close()
        return "MySQL Database is UP!"
    except Exception as e:
        return f"MySQL Database is DOWN! ({e})"

@app.route("/")
def check_health_of_both():
    redis_status = check_redis()
    mysql_status = check_mysql(DB_HOST, DB_NAME, DB_USER, DB_PASSWORD)
    return f'''
    <html>
    <body>
        <p>Redis status: {redis_status}</p>
        <p>MySQL DB status: {mysql_status}</p>
    </body>
    </html>
    '''



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
