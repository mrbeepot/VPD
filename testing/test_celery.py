import sys
sys.path.append("../")


from celery import Celery
app = Celery("test_celery", backend="amqp", broker="amqp://")
@app.task
def add(x,y):
    print("HELLO THERE")
    return x+y