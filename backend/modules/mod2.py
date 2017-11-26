# Module test 1

class ModuleY:

	def init():
		print("Init2")

	def delete():
		print("Delete2")

	def payload(args):
		return {"status": 200, "data": [2 * args[0]]}



from . import doit
doit.cmds({
	"module": "Moding Name",
	"desc": "Module2 for Name-ing-ish",
	"constructor": ModuleY.init,
	"destructor":  ModuleY.delete,
	"cmds": [{
		"cmd": "sell",
		"desc": "sell the load",
		"function": ModuleY.payload,
		"in": [{
			"name": "qwe",
			"type": "int",
			"desc": "asd the int"
		}],
		"out": [{
			"name": "zxc",
			"display": "static"
		}],
		"status": [
			{"200": "Two times your number is $qwe"}
		]
	}]
})
