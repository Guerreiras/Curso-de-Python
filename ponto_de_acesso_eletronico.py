identidade=input("Qual é o nº do seu BI?")    
resultado=identidade.strip()
base_de_dados={
    "874553848HA076":
    {
        "nome":"Jandira Manuel",
        "cursos":["Python","Desenvolvimento Web"],
        "computador":"Mediateca"
        }
    }
aluna=base_de_dados.get(resultado)
if aluna:
    print("Aluna foi encontrada com sucesso")
else:
    print("O BI não corresponde a nenhuma aluna")
