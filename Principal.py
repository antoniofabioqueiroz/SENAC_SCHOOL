from Menu import menu


Op = ""
Aluno = [
			["", "", ""],
			["", "", ""],
			["", "", ""],
			["", "", ""],
			["", "", ""],
			["", "", ""],
			["", "", ""],
			["", "", ""],
			["", "", ""],
			["", "", ""],
			["", "", ""],
			["", "", ""],
			["", "", ""],
			["", "", ""],
			["", "", ""]
]
Vet = [
			[0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0]
]
while Op != "7":
    data = menu(Op, Vet, Aluno)
    Op = data[0]
    Vet = data[2]
    Aluno = data[1]
print(" Agradecemos sua presença.")