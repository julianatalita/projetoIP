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
- main.py: Este é o arquivo principal responsável por iniciar a execução do jogo. Toda a lógica de inicialização e coordenação dos demais módulos é orquestrada a partir deste arquivo.
- objects.py: Este módulo engloba as classes que representam os diferentes objetos presentes no jogo. Notavelmente, ele incorpora a classe Player, representando o caranguejo, bem como as classes que modelam os lixos e seus respectivos comportamentos.
- functions.py: Este arquivo congrega funções auxiliares que são invocadas no arquivo principal, main.py. Funções como "spawn_lixo" (para criar instâncias de lixo) e "draw_counter" (para desenhar contadores) são exemplos das rotinas alojadas neste módulo.
- stopwatch.py: Esse módulo abriga funções essenciais para a operacionalização e exibição do contador de tempo na interface do jogo, permitindo ao usuário ter uma percepção temporal durante sua experiência.
- sprite_sheet.py: Aqui, são mantidos os sprites, que são representações gráficas bidimensionais, dos principais elementos do jogo, incluindo o personagem, os lixos e o cenário de fundo.
- button.py: Este módulo armazena a classe responsável pela modelagem dos botões que são apresentados na tela inicial do jogo, fornecendo interatividade ao usuário desde o início de sua jornada.
- music1.py: Dedicado à sonoridade, este módulo contém a classe que gerencia a música do jogo. Os métodos inclusos permitem executar e pausar as faixas sonoras conforme a interação do usuário e a progressão do jogo.
- graphics/: Trata-se de um diretório que serve como repositório para os recursos gráficos utilizados no jogo. Nele, são armazenados arquivos de imagem, animações, entre outros.
- musics/: Similarmente ao diretório de gráficos, este diretório é destinado ao armazenamento de recursos sonoros, incluindo trilhas sonoras, efeitos de som e demais arquivos de áudio necessários para a ambientação sonora do jogo.

Este projeto foi realizado para disciplina de Introdução à Programação no CIn UFPE
### Divirta-se jogando MangueBit e ajudando a limpar o mangue!


