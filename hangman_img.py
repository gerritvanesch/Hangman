def printTop():
		print("""\
			   -------
			   |     |\
		""")

def printBottom():
		print("""\
			         |
			         |
			-----------\
		""")

def printImg(wrong):
	printTop()
	if wrong == 0:
		print("""\
			   O     |
			         |
			         |
			         |
			         |
			         |
			         |\
		""")
	elif wrong == 1:
		print("""\
			   O     |
			   |     |
			         |
			         |
			         |
			         |
			         |\
		""")
	elif wrong == 2:
		print("""\
			   O     |
			  -|-    |
			         |
			         |
			         |
			         |
			         |\
		""")
	elif wrong == 3:
		print("""\
			   O     |
			  -|-    |
			 /   \   |
			         |
			         |
			         |
			         |\
		""")
	elif wrong == 4:
		print("""\
			   O     |
			  -|-    |
			 / | \   |
			         |
			         |
			         |
			         |\
		""")
	elif wrong == 5:
		print("""\
			   O     |
			  -|-    |
			 / | \   |
			  -|-    |
			         |
			         |
			         |\
		""")
	elif wrong == 6:
		print("""\
			   O     |
			  -|-    |
			 / | \   |
			  -|-    |
			 /   \   |
			         |
			         |\
		""")
	printBottom()
