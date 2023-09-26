# MangueBit - Jogo 2D em Python com Pygame

## Descrição do Jogo
MangueBit é um jogo 2D desenvolvido em Python com a biblioteca Pygame. O objetivo do jogo é controlar
um caranguejo e limpar o máximo de lixo possível do mangue, que está infestado com três tipos de lixo:
Pitú, Garrafa e Pneu. Cada vez que um pedaço de lixo passa direto pelo caranguejo sem ser coletado, 
uma vida é descontada. O lixo só é coletado quando colide com o caranguejo.

## Controles
Pressione A para mover o caranguejo para a esquerda.
Pressione D para mover o caranguejo para a direita.

## Regras do Jogo:
- O jogador começa com um número limitado de vidas;
- O jogo continua até que todas as vidas sejam perdidas;
- Ganhe pontos coletando o lixo antes que ele passe pelo caranguejo;
- Cada tipo de lixo coletado concede uma quantidade diferente de pontos;
- Cada vez que o lixo passa direto pelo caranguejo (sem colisão), uma vida é descontada;
- O objetivo é conseguir a maior pontuação possível antes de perder todas as vidas.

## Como Jogar:
- Execute o arquivo main.py.
- Use as teclas A e D para movimentação.
- Colete o máximo de lixo possível para ganhar pontos e evitar a perda de vidas.

## Requisitos:
- Python 3.x
- Pygame (você pode instalá-lo com 'pip install pygame')

## Estrutura do Projeto:
- main.py: arquivo principal que inicia a execução do jogo;
- objects.py: contém as classes que repesentam o caranguejo (Player), os lixos e seus comportamentos;
- functions.py: arquivo que reune funções acessórias usadas em main.py, como o spawn_lixo e draw_counter;
- stopwatch.py: contém as funções necessárias para exibir o contador de tempo em tela;
- sprite_sheet.py: contém os sprites principais do personagem, lixos e background;
- button.py: armazena a classe de botões que são usados na tela inicial;
- music1.py: contém a classe de música com os métodos de play e pause;
- graphics/: diretório com recursos gráficos;
- musics/: diretório com recursos sonoros;

Este projeto foi realizado para disciplina de Introdução à Programação no CIn UFPE
### Divirta-se jogando MangueBit e ajudando a limpar o mangue!


