from fabric.api import cd, run

app_name = "flask-api"

def deploy():
    run("rm -fr %s" % app_name)
    run("mkdir %s" % app_name)
    with cd("%s" % app_name):
        run("virtualenv %s-env" % app_name)
        run("source %s-env/bin/activate" % app_name)
        run("sudo pip install supervisor gunicorn")
        checkoutGitRepo("https://github.com/tomaszguzialek/flask-api.git")
        run("sudo pip install -r requirements.txt")
        run("echo \"[supervisord]\n# Empty\n\n[program:flask-api]\ncommand=gunicorn -b 0.0.0.0:8000 src.runner:app\" > supervisord.conf")
        # Supervisord searches for supervisord.conf in current working directory
        run("supervisord")

def checkoutGitRepo(url):
    run("git init")
    run("git remote add origin %s" % url)
    run("git fetch")
    run("git checkout -t origin/master")
