#Bruno Rabelo Torchio de Oliveira 	RA: 10239373
#Guilherme Dias Ferreira Pereira  	RA: 10417684

#Semana 1: Opções A e B sendo produzidas ao mesmo tempo da modelagem do grafo.
#Semana 2: Opções G, H e I  produzidas e criação do grafo.txt. para leitura.
#Semana 3: Opções C, D, E e F produzidas e criação da documentação e relatório.

#Talvez seja necessário usar o comando pip install para instalar algumas bibliotecas importados no projeto.
#Bibliotecas necessarias: networkx, matplotlib, chardet.

from grafoMatriz import Grafo
import chardet

def exibir_menu():
    print("\nMenu de Opções:")
    print("a) Ler dados do arquivo grafo.txt")
    print("b) Gravar dados no arquivo grafo.txt")
    print("c) Inserir vértice")
    print("d) Inserir aresta")
    print("e) Remover vértice")
    print("f) Remover aresta")
    print("g) Mostrar conteúdo do arquivo")
    print("h) Mostrar grafo")
    print("i) Apresentar a conexidade do grafo e o reduzido")
    print("j) Encerrar a aplicação")

def main():
    Grafito = None
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip().lower()
        
        match opcao:
            #Lê o arquivo salvando a variavel na memória RAM
            case 'a':
                print("\nOpção escolhida: Ler dados do arquivo grafo.txt")
                with open("grafo.txt", "r", encoding="utf-8", errors="replace") as file:
                    for line in file:
                        print(line, end='')
                with open("grafo.txt", "r", encoding="utf-8", errors="replace") as file:
                    tipo = file.readline().strip()
                    num_vertices = int(file.readline().strip())
                    
                    Grafito = Grafo(num_vertices)
                    
                    for _ in range(num_vertices):
                        line = file.readline().strip()
                        index, nome = line.split(" ", 1)
                        Grafito.add_vertex(int(index), nome.strip('"'))
                        
                    num_arestas = int(file.readline().strip())
                    for _ in range(num_arestas):
                        start, end = map(int, file.readline().split()[:2])
                        Grafito.insereA(start, end)
                        
            #Opção que atualiza o grafo.txt após mudanças
            #(NECESSARIO APOS TODA MUDANÇA AO GRAFO)
            case 'b':
                if Grafito is not None:
                    try:
                        print("\nOpção escolhida: Gravar dados no arquivo grafo.txt")
                        with open("grafo.txt", "w", encoding="utf-8") as file:
                            file.write(f"{tipo}\n")
                            file.write(f"{len(Grafito.vertices)}\n")
                            
                            for index in sorted(Grafito.vertices.keys()):
                                nome = Grafito.vertices[index]
                                file.write(f"{index} \"{nome}\"\n")

                            arestas = Grafito.get_arestas()
                            file.write(f"{len(arestas)}\n")
                            for origem, destino in arestas:
                                file.write(f"{origem} {destino}\n")
                    except Exception as e:
                        print(f"Erro ao salvar o grafo: {e}")
                else:
                    print("\nNenhum grafo foi carregado ou criado ainda.")
            case 'c':
                if Grafito is not None:
                    print("\nOpção escolhida: Inserir vértice")
                    try:
                        index = int(input("Digite o índice do novo vértice: "))
                        if index in Grafito.vertices:
                            print("Índice já existe.")
                            break
                        nome = input("Digite o nome do vértice: ")
                        Grafito.add_vertex(index, nome)
                        print(f"Vértice {index} - \"{nome}\" inserido com sucesso.")
                    except Exception as e:
                        print(f"Erro: {e}")
                else:
                    print("\nNenhum grafo foi carregado ou criado ainda.")
            case 'd':
                if Grafito is not None:
                    print("\nOpção escolhida: Inserir aresta")
                    try:
                        origem = int(input("Digite o índice de origem: "))
                        destino = int(input("Digite o índice de destino: "))
                        Grafito.insereA(origem, destino)
                        print(f"Aresta de {origem} para {destino} inserida com sucesso.")
                    except Exception as e:
                        print(f"Erro: {e}")
                else:
                    print("\nNenhum grafo foi carregado ou criado ainda.")
            case 'e':
                if Grafito is not None:
                    print("\nOpção escolhida: Remover vértice")
                    try:
                        index = int(input("Digite o índice do vértice a ser removido: "))
                        Grafito.remove_vertex(index)
                        print(f"Vértice {index} removido com sucesso.")
                    except Exception as e:
                        print(f"Erro: {e}")
                else:
                    print("\nNenhum grafo foi carregado ou criado ainda.")
            case 'f':
                if Grafito is not None:
                    print("\nOpção escolhida: Remover aresta")
                    try:
                        origem = int(input("Digite o índice de origem da aresta: "))
                        destino = int(input("Digite o índice de destino da aresta: "))
                        Grafito.removeA(origem, destino)
                        print(f"Aresta de {origem} para {destino} removida com sucesso.")
                    except Exception as e:
                        print(f"Erro: {e}")
                else:
                    print("\nNenhum grafo foi carregado ou criado ainda.")
            case 'g':
                print("\nOpção escolhida: Mostrar conteúdo do arquivo")
                with open("grafo.txt", "r", encoding="utf-8", errors="replace") as file:
                    lines = [line.strip() for line in file.readlines()]
                tipo = int(lines[0])
                if tipo == 0:
                    tipo_grafo = "grafo não orientado sem peso"
                elif tipo == 1:
                    tipo_grafo = "grafo não orientado com peso no vértice"
                elif tipo == 2:
                    tipo_grafo = "grafo não orientado com peso na aresta"
                elif tipo == 3:
                    tipo_grafo = "grafo não orientado com peso nos vértices e arestas"
                elif tipo == 4:
                    tipo_grafo = "grafo orientado sem peso"
                elif tipo == 5:
                    tipo_grafo = "grafo orientado com peso no vértice"
                elif tipo == 6:
                    tipo_grafo = "grafo orientado com peso na aresta"
                elif tipo == 7:
                    tipo_grafo = "– grafo orientado com peso nos vértices e arestas"
                num_vertices = int(lines[1])
                vertices = {}
                for i in range (2,2 + num_vertices):
                    index, nome = lines[i].split(" ", 1)
                    vertices[int(index)] = nome.strip('"')

                num_arestas = int(lines[2 + num_vertices])
                Arestas = []
                for i in range (3 + num_vertices, 3 + num_vertices + num_arestas):
                    arestinha = list(map(int, lines[i].split()))
                    Arestas.append((arestinha[0], arestinha[1]))
                    
                print("Graph Type: ", tipo_grafo)
                print("Vertices: ", vertices)
                print("Arestas (Começo, Fim):")
                for Aresta in Arestas:
                    print(Aresta)
            case 'h':
                print("\nOpção escolhida: Mostrar grafo")
                Grafito.show()
                Grafito.showMin()
                Grafito.visualize()
            case 'i':
                print("\nOpção escolhida: Apresentar a conexidade do grafo e o reduzido")
                if Grafito is not None:
                    if Grafito.eh_conexo():
                        print("O grafo é conexo.")
                    else:
                        print("O grafo NÃO é conexo.")
                else:
                    print("Nenhum grafo foi carregado ou criado.")
            case 'j':
                print("\nEncerrando a aplicação...")
                break
            case _:
                print("\nOpção inválida. Tente novamente.")

if __name__ == "__main__":
    main()

