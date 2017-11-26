# Module test 1

class ModuleX:

	def init():
		print("Init")

	def delete():
		print("Delete")

	def payload(args):
		print(args[0])
		return {"status": 200, "data": [3 * args[0]]}



from . import doit
doit.cmds({
	"module": "Mod Name",
	"desc": "Module for Name-ing-ish",
	"constructor": ModuleX.init,
	"destructor":  ModuleX.delete,
	"cmds": [{
		"cmd": "pay",
		"desc": "paying the load",
		"function": ModuleX.payload,
		"in": [{
			"name": "asd",
			"type": "int",
			"desc": "asd the int"
		}],
		"out": [{
			"name": "qwe",
			"display": "static"
		}],
		"status": [
			{"200": "Three times your number is $qwe"}
		]
	}]
})
