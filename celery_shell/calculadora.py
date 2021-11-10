from celery import Celery


app = Celery('calc', broker='redis://localhost:6379', backend='redis://localhost:6379')


@app.task
def suma(x, y):
    return float(x + y)

@app.task
def resta(x, y):
    return float(x - y)

@app.task
def mult(x, y):
    return float(x * y)

@app.task
def div(x, y):
    return float(x / y)

@app.task
def pot(x, y):
    return float(x ** y)