from invoke import task


@task
def setup(c):
    c.run("python manage.py migrate")


@task
def run(c):
    print("running server on http://localhost:8000")
    c.run("python manage.py runserver")


@task
def test(c):
    c.run("python manage.py test")


@task
def lint(c):
    c.run("black --check .")


@task
def fix(c):
    c.run("black .")
