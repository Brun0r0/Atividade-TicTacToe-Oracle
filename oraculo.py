
#estado inicial do tabuleiro(vazio)
tabuleiroVazio = [0, 0, 0, 0, 0, 0, 0, 0, 0]

def tabuleiroCheio(estado):
        for i in range(9):
                if(estado[i] == 0):
                        return False             
        return True

#função para verificar estado objetivo
def estadoObjetivo(tabu):
        for i in range(3):
                if tabu[i*3] == tabu[(i*3)+1] == tabu[(i*3)+2] != 0:
                        return tabu[i*3]
                
        for i in range(3):
                if tabu[i] == tabu[i+3] == tabu[i+6] != 0:
                        return tabu[i]
                
        if tabu[0] == tabu[4] == tabu[8] != 0:
                return tabu[0]
        
        elif tabu[2] == tabu[4] == tabu[6] != 0:
                return tabu[2]
        
        if tabuleiroCheio(tabu):
                return 0

        return None

#função para saber quem joga naquele instante
def playerVez(estado):
        playerX = 0
        playerO = 0
        for i in range(9):
                if estado[i] == 1:
                        playerX += 1
                elif estado[i] == -1:
                        playerO += 1

        if playerX > playerO:
                return -1
        else:
                return 1

#func para mudar de um estado para o outro
def proxEstado(est, info):
        (player, pos) = info
        copiaEstado = est.copy()
        copiaEstado[pos] = player

        return copiaEstado

def acaoSucessora(estado):
        player = playerVez(estado)
        lista = []
        for i in range(len(estado)):
                if estado[i] == 0:
                        lista.append((player, i))
        return lista


def geradorEstados(estado, prof):

        objetivo = estadoObjetivo(estado)

        if objetivo is not None:
                return (objetivo, prof)

        listaAcoes = acaoSucessora(estado)
        jogadas = []

        for acao in listaAcoes:
                novo = proxEstado(estado, acao)
                jogadas.append(geradorEstados(novo, prof+1))
        
        pontuacao = jogadas[0][0]
        _prof = jogadas[0][1]
        player = playerVez(estado)

        if player == 1:
                for i in range(len(jogadas)):
                        if jogadas[i][0] > pontuacao:
                                pontuacao = jogadas[i][0]
                                _prof = jogadas[i][1]
        else:
                for i in range(len(jogadas)):
                        if jogadas[i][0] < pontuacao:
                                pontuacao = jogadas[i][0]
                                _prof = jogadas[i][1]

        return pontuacao, _prof

def minimax(estado):

        listaAcoes = acaoSucessora(estado)
        jogadas = []

        for acao in listaAcoes:
                novo = proxEstado(estado, acao)
                jogadas.append((acao, geradorEstados(novo, 1)))
        
        if(len(jogadas)) == 0:
                return ((0,0),(0,0))
        

        #Para variar as possibilidades de vitória
        listaJogadasSorteada = sorted(jogadas, key=lambda l : l[0][1])
        
        mov = min(listaJogadasSorteada, key = lambda l : l[1])
        return mov

def qualPlayer(player):
        if(player == 0):
                return ' '
        elif(player == 1):
                return 'X'
        elif(player == -1):
                return 'O'

def imprimirTabu(estado):
        for i in range(9):
                jogador = qualPlayer(estado[i])
                print('|', jogador, end='')
                if (i+1)%3 == 0:
                        print('|')

def matrizPArray(estado):
        array = []
        for i in estado:
                for j in i:
                        if(j == 2):
                                j = -1
                        array.append(int(j))

        return array
