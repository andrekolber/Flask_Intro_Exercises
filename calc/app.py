from flask import Flask, request
from  operations import add, sub, mult, div

app = Flask(__name__)

@app.route('/add')
def add_nums():
    '''add a and b paramaters'''
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = add(a,b)

    return str(result)
    

@app.route('/sub')
def subtract_nums():
    '''Subtract a and b paramaters'''
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = sub(a,b)

    return str(result)
    
@app.route('/mult')
def multiply_nums():
    '''Multiply a and b paramaters'''
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = mult(a,b)

    return str(result)
    

@app.route('/div')
def divide_nums():
    '''Divide a and b paramaters'''
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = div(a,b)

    return str(result)
    
### Part Two

operators = {
    'add': add,
    'sub': sub,
    'mult': mult,
    'div': div
}

@app.route('/math/<operation>')
def do_math(operation):
    '''Do math on a and b paramaters'''
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = operators[operation](a,b)

    return str(result)