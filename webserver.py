from time import sleep
import os
import sys
import requests

from tarefas import *
from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)
dicionario = globaldict()
redirecionador = redirector(os.environ["REDIRECTIP"])

@app.route('/Tarefa', methods=['GET', 'POST'])
def Tarefa():
    if request.method == 'GET':
        return redirecionador.redirect_request("listar")
        # return dicionario.dict
    if request.method == 'POST':
        return redirecionador.redirect_request("adicionar", request.form)
        # dicionario.add_coisa(request.form)
        # resp = jsonify(success=True)
        # return resp

@app.route('/Tarefa/<id>', methods=['GET', 'PUT', 'DELETE'])
def Tarefa_id(id):
    if request.method == 'GET':
        return redirecionador.redirect_request("buscar", params=[id])
        # resp = dicionario.get_coisa(id)
        # if (resp != False):
        #     return resp
        # resp = jsonify(success = False)
        # return resp
    if request.method == 'PUT':
        return redirecionador.redirect_request("atualizar", params=[id, request.form])
        # resp = dicionario.update_coisa(id, request.form)
        # resp = jsonify(success=(resp != False))
        # return resp
    if request.method == 'DELETE':
        return redirecionador.redirect_request("apagar", params=[id])
        # resp = dicionario.deleta_coisa(id)
        # resp = jsonify(success=(resp != False))
        # return resp

@app.route('/healthcheck')
def healthcheck():
    resp = jsonify(success = True)
    return resp

if __name__ == '__main__':
    app.run(host='0.0.0.0')
