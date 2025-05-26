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
    print("j) Grau dos vértices")
    print("k) Verificar se é euleriano")
    print("l) Verificar se admite ciclo hamiltoniano usando o teorema de Dirac")
    print("m) Aeroporto com maior emissão total de carbono")
    print("n) Caminho de menor emissão entre dois aeroportos")
    print("o) Solução encontrada")
    print("p) Encerrar a aplicação")

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
                        parts = file.readline().split()
                        start, end = map(int, parts[:2])
                        peso = float(parts[2]) if len(parts) > 2 else None
                        Grafito.insereA(start, end, peso)
                        
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
                            for origem, destino, peso in Grafito.get_arestas():
                                if peso is not None:
                                    file.write(f"{origem} {destino} {peso}\n")
                                else:
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
                    parts = lines[i].split()
                    origem = int(parts[0])
                    destino = int(parts[1])
                    peso = float(parts[2]) if len(parts) > 2 else None
                    Arestas.append((origem, destino, peso))
                    
                print("Graph Type: ", tipo_grafo)
                print("Vertices: ", vertices)
                print("Arestas (Começo, Fim, Peso):")
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
                print("\nGrau dos vértices (aeroportos):")
                if Grafito is not None:
                    for v in Grafito.vertices:
                        grau = sum(1 for w in range(Grafito.n) if Grafito.adj[v][w] or Grafito.adj[w][v])
                        print(f"Aeroporto {v} ({Grafito.vertices[v]}): grau {grau}")
                else:
                    print("Nenhum grafo carregado.")

            case 'k':
                print("\nVerificando se o grafo é euleriano...")
                #Ciclo Euleriano: um caminho que passar por todas as arestas e retorna ao ponto de partida.()
                #Percurso Euleriano: um caminho que passarpor todas as arestas e não necessariamente volta ao ponto de partida.
                if Grafito is not None:
                    graus = [sum(1 for w in range(Grafito.n) if Grafito.adj[v][w] or Grafito.adj[w][v]) for v in Grafito.vertices]
                    graus_impares = sum(1 for g in graus if g % 2 == 1)
                    if graus_impares == 2:
                        print("O grafo possui um percurso euleriano (mas não é ciclo euleriano).")
                    elif graus_impares == 0:
                        print("O grafo é euleriano (possui ciclo euleriano).")
                    else:
                        print("O grafo NÃO possui percurso euleriano e nem ciclo euleriano.")
                else:
                    print("Nenhum grafo carregado.")

            case 'l':
                print("\nVerificando se admite ciclo hamiltoniano (heurística)...")
                if Grafito is not None:
                    # Heurística simples: se o grau de todos os vértices >= n/2, pode ser hamiltoniano (Dirac)
                    n = len(Grafito.vertices)
                    graus = [sum(1 for w in range(Grafito.n) if Grafito.adj[v][w] or Grafito.adj[w][v]) for v in Grafito.vertices]
                    if all(g >= n // 2 for g in graus):
                        print("Pode admitir ciclo hamiltoniano (Dirac).")
                    else:
                        print("Provavelmente NÃO admite ciclo hamiltoniano.")
                else:
                    print("Nenhum grafo carregado.")

            case 'm':
                print("\nAeroporto com maior emissão total de carbono(lembrando que os valores estão em kg):")
                if Grafito is not None:
                    max_emissao = -1
                    aeroporto = None
                    for v in Grafito.vertices:
                        total = sum(Grafito.pesos.get((v, w), 0) for w in range(Grafito.n)) + \
                                sum(Grafito.pesos.get((w, v), 0) for w in range(Grafito.n))
                        if total > max_emissao:
                            max_emissao = total
                            aeroporto = v
                    print(f"Aeroporto {aeroporto} ({Grafito.vertices[aeroporto]}) - Emissão total: {max_emissao}")
                else:
                    print("Nenhum grafo carregado.")

            case 'n':
                print("\nCaminho de menor emissão entre dois aeroportos (Dijkstra):")
                if Grafito is not None:
                    origem = int(input("Índice do aeroporto de origem: "))
                    destino = int(input("Índice do aeroporto de destino: "))
                    caminho, custo = Grafito.dijkstra(origem, destino)
                    if caminho is None or custo == float('inf'):
                        print("Não existe caminho entre os aeroportos informados.")
                    else:
                        nomes = [Grafito.vertices[v] for v in caminho]
                        print(f"Caminho: {' -> '.join(nomes)}")
                        print(f"Emissão total de carbono: {custo}")
                else:
                    print("Nenhum grafo carregado.")

            case 'o':
                print("\nObservaçôes: Para os calculos usamos a aeronave Boeing 737-800, que é uma das mais comuns no Brasil para viagens domesticas.")
                print("\nOs calculos foram feitos com base no método ICEC da  International Civil Aviation Organization(ICAO).")
                print("O método ICEC calcula as emissões de CO² com base no combustível consumido, na distância percorrida e no tipo de aeronave.")
                print()
                print("\nSoluções para Reduzir as Emissões de CO² em Rotas Aéreas Domésticas:")
                print("1. **Substituição por meios de transporte Menos Poluentes:**")
                print("   - Para rotas curtas, incentivar o uso de trens de alta velocidade, ônibus elétricos ou outros meios de transporte coletivo menos poluentes pode reduzir drasticamente as emissões.")
                print("   - Exemplo: A rota São Paulo-Guarulhos, que emite quase 10 toneladas de CO² por voo, poderia ser substituída por linhas de ônibus elétricos ou ferroviárias, reduzindo o impacto ambiental e o custo por passageiro.")
                print()
                print("2. **Otimização de Rotas e Operações:**")
                print("   - Com estudos mais aprofundados, podemos achar meios de diminuir escalas e fazer viagens diretas, poupando muitas horas de voo e, consequentemente, reduzindo as emissões de CO².")
                print("   - Implementar técnicas de gerenciamento de tráfego aéreo para minimizar esperas e trajetos circulares.")
                print("   - Exemplo: Otimizar a rota Florianópolis-Manaus(normalmente seria feito Florianópolis -> BH-Confins -> Recife -> Manaus que chega a quase 75 toneladas de CO²) para evitar escalas intermediárias e trajetos mais longos, reduzindo a emissão total de CO².")
                print()
                print("3. **Modernização da Frota Aérea:**")
                print("   - Investir em aeronaves mais modernas, com motores mais eficientes e aerodinâmica aprimorada, pode reduzir o consumo de combustível e, consequentemente, as emissões.")
                print("   - Exemplo: Substituir aviões antigos por modelos como o Airbus A320neo ou Boeing 737 MAX, que consomem menos combustível por quilômetro voado.")
                print()
                print("4. **Uso de Combustíveis Sustentáveis de Aviação (SAF):**")
                print("   - Incentivar o uso de biocombustíveis e combustíveis sintéticos, que emitem menos CO² ao longo do ciclo de vida.")
                print("   - Exemplo: Misturar SAF ao combustível convencional pode reduzir as emissões em até 80% em alguns casos.")
                print()
                print("5. **Compensação de Carbono:**")
                print("   - Implementar programas de compensação, como o plantio de árvores ou investimentos em projetos de energia renovável, para neutralizar as emissões dos voos.")
                print("   - Exemplo: Companhias aéreas podem oferecer aos passageiros a opção de compensar as emissões de suas viagens.")
                print()
                print()
                print("**Resumo:**")
                print("A redução das emissões de CO² no setor aéreo depende de uma combinação de tecnologia, políticas públicas, mudança de comportamento e inovação em infraestrutura. A escolha da solução ideal depende do perfil da rota, da infraestrutura disponível e do engajamento de todos os atores do setor.")
            case 'p':
                print("\nEncerrando a aplicação...")
                break
            case _:
                print("\nOpção inválida. Tente novamente.")

if __name__ == "__main__":
    main()

