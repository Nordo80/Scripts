import os

def git_push():
    os.system("mysqldump -u newuser -ppassword flask > /home/aleksandr/flaskpower/flask.sql")
    os.system("mysql -u b12f26d01aa967 -pb85dc090 heroku_b40d4a2594424bc -h eu-cdbr-west-01.cleardb.com < /home/aleksandr/flaskpower/flask.sql")
    os.system("git add .")
    commit = input("Enter the name of commit: \n")
    os.system(f"git commit -m \"{commit}\"")
    os.system("git push origin master")

git_push()
