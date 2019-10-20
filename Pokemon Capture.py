pokemons = ['pikachu', 'charmander', 'bulbasaur', 'squirtle']
capturados = []
opcao = 0
print("Pokémon Capture!")
while opcao != 3:
    countCapturados = aux = 0
    print("- - - - - - - Menu - - - - - - -"
          "\n1 - Capturar Pokémon\n"
          "2 - Mostrar Pokémons\n"
          "3 - Sair")
    opcao = int(input("Informe a opção escolhida: "))
    if opcao == 1:
        pokemon = str(input("Informe o nome do pokémon: "))
        pokemon = pokemon.lower()
        for pok in pokemons:
            if pok == pokemon:
                capturados.append(pokemon)
                print("Pokémon capturado com sucesso!")
                aux += 1
        if aux == 0:
            print("O pokémon informado não foi encontrado em Kanto.")
    elif opcao == 2:
        if len(capturados) > 0:
            print("Quantidade de pokémons capturados: ", len(capturados))
            countCapturados = len(capturados) - (len(capturados) - (len(sorted(set(capturados)))))
            print("Quantidade restante para concluir Pokédex: ", 142-countCapturados)
            print("Pokémons capturados: ")
            for pok in capturados:
                print(" - ", pok.capitalize())
        else:
            print("Você não capturou nenhum pokémon até o momento!")
else:
    print("Você saiu do Pokemon Capture!")