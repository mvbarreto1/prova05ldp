def calcular_media(notas):
    return sum(notas) / len(notas)

def main():
    
    num_alunos = int(input("Digite o número de alunos: "))
    
    soma_medias = 0
    
    for i in range(num_alunos):
        
        nome = input(f"\nDigite o nome do aluno {i + 1}: ")
        
        
        notas = []
        for j in range(3):
            nota = float(input(f"Digite a nota {j + 1} de {nome}: "))
            notas.append(nota)
        
        
        media = calcular_media(notas)
        
        
        if media >= 7.0:
            status = "Aprovado"
        else:
            status = "Reprovado"
     
        print(f"\nAluno: {nome}")
        print(f"Notas: {notas}")
        print(f"Média: {media:.2f}")
        print(f"Status: {status}")
        
       
        soma_medias += media
    
   
    media_geral = soma_medias / num_alunos
    print(f"\nMédia geral da turma: {media_geral:.2f}")

if __name__ == "__main__":
    main()
