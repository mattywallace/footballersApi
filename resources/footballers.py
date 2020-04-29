import models 

from flask import Blueprint, request

footballers = Blueprint('footballers', 'footballers')

@footballers.route('/')
def footballers_index():
		return 'footballers resource now working'

# @footballers.route('/', methods=['POST'])
# def creat_footballer():
# 	payload = request.get_json()
# 	print(payload)
# 	return 'you hit the create footballer route -- cheack terminal'