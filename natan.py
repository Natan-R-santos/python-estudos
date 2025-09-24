def calcular_notas(listas_de_notas):
    return sum(listas_de_notas) / len (listas_de_notas)

def verificar_situacao(media):
    if media >= 7:
        return("aprovado🎉")
    else:
        return("reprovado❌")

nome = input("digite seu nome")
notas = input("digite sua notas por espaços") 
notas = [float (n) for n in notas.split()]

media = calcular_notas(notas)
situacao = verificar_situacao(media)
print(f"nome:{nome}")  
print(f"media:{media:.2f}")
print(f"situacao:{situacao}")

