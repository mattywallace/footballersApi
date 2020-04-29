import models 
from flask import Blueprint, request


footballers = Blueprint('footballers', 'footballers')





@footballers.route('/', methods=['GET'])
def footballers_index():
		return 'footballers resource now working'




@footballers.route('/', methods=['POST'])
def create_footballer():
	
	payload = request.get_json()
	
	print(payload,'here is the payload')
	
	new_footballer = models.Footballer.create(firstname=payload['first_name'])
	
	print(new_footballer, 'here is the new footballer')
	
	return 'you hit the create route'
	
	

	# 	last_name=payload['last_name'], 
	# 	nationality=payload['nationality'], 
	# 	position=payload['position'], 
	# 	age=payload['age'], 
	# 	club_team=payload['club_team'], 
	# 	number=payload['number'])

	# print(new_footballer)
	# print(dir(new_footballer))
	# footballer_dict = model_to_dict(new_footballer)
	# return jsonify (
	# 	data=footballer_dict,
	# 	message='succussefully created footballer!',
	# 	status=201
	# 	),201
