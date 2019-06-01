# coding=utf-8

frase_facil = "Mais __0__ um __1__ na __2__ do que dois __3__.";
frase_medio = "De __0__ e de __1__ todo __2__ tem um __3__.";
frase_dificil = "Agua __0__, __1__ dura, tanto __2__ ate que __3__.";
respostas_facil = ['vale', 'pássaro', 'mão', 'voando']
respostas_medio = ['médico', 'louco', 'mundo', 'pouco']
respostas_dificil = ['mole', 'pedra', 'bate', 'fura']
niveis = ['fácil', 'médio', 'difícil']
frase_facil_completa = "Mais vale um pássaro na mão do que dois voando.";
frase_medio_completa = "De médico e de louco todo mundo tem um pouco.";
frase_dificil_completa = "Água mole, pedra dura, tanto bate ate que fura.";


usuario_nivel = raw_input('Bem-vindo ao Quiz Python!!\nPara iniciar defina o nível de dificuldade do jogo, escolha entre uma das alternativas abaixo:\nFácil, Médio ou Difícil: ').lower()


def escolha_um_nivel(usuario_nivel, niveis):
#essa função serve para escolher o nível do jogador. Quando ele escolher, chama a função "selecionar frase"
    while usuario_nivel not in niveis:
        print 'Nivel incorreto! Tente novamente!\n\n'
        usuario_nivel = raw_input('Escolha uma das alternativas: Facil, Medio ou Dificil: ').lower()
    else:
        return selecionar_frase(usuario_nivel, niveis)

def selecionar_frase(usuario_nivel, niveis):
#essa função serve para mostrar que o jogo começou e mostrará a frase do nivel que ele escolheu".
#Com a frase mostrada, vai chamar a função do jogo: "play_game"
    if usuario_nivel == niveis[0]:
        print "\nLegal! vamos lá! Agora é só completar a frase abaixo! \n\n", frase_facil,'\n\n'
        return play_game(frase_facil, respostas_facil, frase_facil_completa)
    if usuario_nivel == niveis[1]:
        print "\nLegal! vamos lá! Agora é só completar a frase abaixo! \n\n", frase_medio,'\n\n'
        return play_game(frase_medio, respostas_medio, frase_medio_completa)
    if usuario_nivel == niveis[2]:
        print "\nLegal! vamos lá! Agora é só completar a frase abaixo! \n\n", frase_dificil,'\n\n'
        return play_game(frase_dificil, respostas_dificil, frase_dificil_completa)

def play_game(frase, respostas, frase_completa):
#É aqui que o jogo acontece, uma vez que irá analisar se o usuário está colocando as palavras corretas.
    lista_temp = []
    i = 0
    while len(lista_temp) < 4:
        resposta_do_usuario = raw_input('Digite o Valor da lacuna {} :'.format(i))
        if resposta_do_usuario not in respostas:
            print "Você errou tente novamente!"
        else:
            print "Você ACERTOU! Vamos para a próxima!"
            lista_temp.append(resposta_do_usuario)
            i = i + 1
    print "Você terminou! Parabéns!" ,frase_completa

escolha_um_nivel(usuario_nivel, niveis)
