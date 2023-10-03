# pieces

pieces =  {
		0: {'cost':2,'steps':2,'yield':0,'shape':
	[
		[0,1,0,],
		[1,1,1,]
	]
	},
		1: {'cost':1,'steps':5,'yield':1,'shape':
	[
		[1,1,1,1],
		[1,0,0,1]
	]
	},

		2: {'cost':5,'steps':5,'yield':2,'shape':
	[
		[1,1,1],
		[0,1,0],
		[0,1,0]
	]
	},
		3: {'cost':2,'steps':1,'yield':0,'shape':
	[
		[0,1,0],
		[1,1,0],
		[0,1,1],
		[0,1,0]
	]
	},
		4: {'cost':1,'steps':2,'yield':0,'shape':
	[
		[1,0,1],
		[1,1,1]

	]
	},
		5: {'cost':1,'steps':2,'yield':0,'shape':
	[
		[0,0,0,1],
		[1,1,1,1],
		[1,0,0,0]
	]
	},
		6: {'cost':3,'steps':3,'yield':1,'shape':
	[
		[1,1,1,1]

	]
	},
		7: {'cost':7,'steps':1,'yield':1,'shape':
	[
		[1,1,1,1,1]
	]
	},
		8: {'cost':0,'steps':3,'yield':1,'shape':
	[
		[0,1,0],
		[1,1,1],
		[0,1,0],
		[0,1,0]
	]
	},
		9: {'cost':1,'steps':3,'yield':0,'shape':
	[
		[0,1],
		[1,1]
	]
	},
		10: {'cost':3,'steps':2,'yield':1,'shape':
	[
		[0,1],
		[0,1],
		[1,0],
		[1,0]
	]
	},
		11: {'cost':7,'steps':2,'yield':2,'shape':
	[
		[1,1,1],
		[0,1,0],
		[0,1,0],
		[0,1,0]
	]
	},
		12: {'cost':5,'steps':4,'yield':2,'shape':
	[
		[0,1,0],
		[1,1,1],
		[0,1,0]
		
	]
	},
		13: {'cost':6,'steps':5,'yield':2,'shape':
	[
		[1,1],
		[1,1]

	]
	},
		14: {'cost':8,'steps':6,'yield':3,'shape':
	[
		[0,1,1],
		[1,1,0],
		[1,1,0]

	]
	},
		15: {'cost':10,'steps':3,'yield':2,'shape':
	[
		[0,1],
		[0,1],
		[0,1],
		[1,1]
	]
	},
		16: {'cost':10,'steps':4,'yield':3,'shape':
	[
		[1,0,0],
		[1,1,0],
		[0,1,1]

	]
	},
		17: {'cost':10,'steps':5,'yield':3,'shape':
	[
		[1,1],
		[1,1],
		[0,1],
		[0,1]
	]
	},
		18: {'cost':7,'steps':6,'yield':3,'shape':
	[
		[0,1,1],
		[1,1,0]

	]
	},
		19: {'cost':4,'steps':6,'yield':2,'shape':
	[
		[1,1],
		[1,0],
		[1,0]

	]
	},
		20: {'cost':7,'steps':4,'yield':2,'shape':
	[
		[0,1,1,0],
		[1,1,1,1]

	]
	},
		21: {'cost':4,'steps':2,'yield':1,'shape':
	[
		[1,1,1],
		[1,0,0]

	]
	},
		22: {'cost':2,'steps':2,'yield':0,'shape':
	[
		[1,1,1]

	]
	},
		23: {'cost':2,'steps':3,'yield':0,'shape':
	[
		[1,1,1],
		[0,1,0],
		[1,1,1]
	]
	},
		24: {'cost':3,'steps':4,'yield':1,'shape':
	[
		[1,0],
		[1,0],
		[1,1],
		[1,0]
	]
	},
		25: {'cost':2,'steps':3,'yield':1,'shape':
	[
		[1,0],
		[1,0],
		[1,1],
		[0,1]
	]
	},
		26: {'cost':2,'steps':1,'yield':0,'shape':
	[
		[1,1]

	]
	},
		27: {'cost':3,'steps':1,'yield':0,'shape':
	[
		[1,0],
		[1,1]

	]
	},
		28: {'cost':1,'steps':4,'yield':1,'shape':
	[
		[0,1,0],
		[0,1,0],
		[1,1,1],
		[0,1,0],
		[0,1,0]
	]
	},
		29: {'cost':4,'steps':2,'yield':0,'shape':
	[
		[0,1],
		[0,1],
		[1,1],
		[1,0]
	]
	},
		30: {'cost':3,'steps':6,'yield':2,'shape':
	[
		[0,1,1],
		[1,1,0],
		[0,1,1]

	]
	},
		31: {'cost':2,'steps':2,'yield':0,'shape':
	[
		[0,1,1],
		[1,1,1]

	]
	},
		32: {'cost':5,'steps':3,'yield':1,'shape':
	[
		[0,1,0],
		[1,1,1],
		[1,1,1],
		[0,1,0]
	]
	},
		33: {'cost':0,'steps':0,'yield':0,'shape':
	[
		[1]

	]
	},
}

for piece,data in pieces.items():
	print('\n',piece)

	fullString = ''
	for x in data['shape']:
		for y in x:
			if y:
				fullString += '[]'
			else:
				fullString += '  '
		fullString += '\n'
	print (fullString)