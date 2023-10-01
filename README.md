## Sobre o Relatório


O relatório deve ser feito no próprio README.md do repositório e deverar conter os seguintes pontos:


- *Título* do projeto e *membros* da equipe;
- A descrição da *arquitetura* do projeto, explicando como o *código foi organizado*;
- As *capturas de tela* do sistema funcionando para compor a galeria de projetos
- As *ferramentas, **bibliotecas, **frameworks* utilizados com as respectivas *justificativas* para o uso;
- A *divisão de trabalho* dentro do grupo (*quem fez o que*);
- Os *conceitos* que foram apresentados durante a disciplina e utilizados no projeto (indicando onde foram usados);
- Os *desafios* e *erros* enfrentados no decorrer do projeto e as *lições aprendidas*. Para tanto, respondam às seguintes perguntas:
    - Qual foi o maior erro cometido durante o projeto? Como vocês lidaram com ele?
    - Qual foi o maior desafio enfrentado durante o projeto? Como vocês lidaram com ele?
    - Quais as lições aprendidas durante o projeto?


# MangueBit - Jogo 2D em Python com Pygame
##Membros da Equipe:
-Artur Couto
-Juliana Talita
-Luana Queiroz
-Lucas Carvalho
- Walfrido Saturno






## Descrição do Jogo
MangueBit é um jogo 2D desenvolvido em Python com a biblioteca Pygame. O objetivo do jogo é controlar
um caranguejo e limpar o máximo de lixo possível do mangue, que está infestado com três tipos de lixo:
Pitú, Garrafa e Pneu. Cada vez que um pedaço de lixo passa direto pelo caranguejo sem ser coletado,
uma vida é descontada. O lixo só é coletado quando colide com o caranguejo.




## Estrutura do Projeto:

- main.py: Este é o arquivo principal responsável por iniciar a execução do jogo. Toda a lógica de inicialização e coordenação dos demais módulos é orquestrada a partir deste arquivo.
- objects.py: Este módulo engloba as classes que representam os diferentes objetos presentes no jogo. Notavelmente, ele incorpora a classe Player, representando o caranguejo, bem como as classes que modelam os lixos e seus respectivos comportamentos.
- functions.py: Este arquivo congrega funções auxiliares que são invocadas no arquivo principal, main.py. Funções como "spawn_lixo" (para criar instâncias de lixo) e "draw_counter" (para desenhar contadores) são exemplos das rotinas alojadas neste módulo.
- stopwatch.py: Esse módulo abriga funções essenciais para a operacionalização e exibição do contador de tempo na interface do jogo, permitindo ao usuário ter uma percepção temporal durante sua experiência.
- sprite_sheet.py: Aqui, são mantidos os sprites, que são representações gráficas bidimensionais, dos principais elementos do jogo, incluindo o personagem, os lixos e o cenário de fundo.
- button.py: Este módulo armazena a classe responsável pela modelagem dos botões que são apresentados na tela inicial do jogo, fornecendo interatividade ao usuário desde o início de sua jornada.
- music1.py: Dedicado à sonoridade, este módulo contém a classe que gerencia a música do jogo. Os métodos incluídos permitem executar e pausar as faixas sonoras conforme a interação do usuário e a progressão do jogo.
- graphics/: Trata-se de um diretório que serve como repositório para os recursos gráficos utilizados no jogo. Nele, são armazenados arquivos de imagem, animações, entre outros.
- musics/: Similarmente ao diretório de gráficos, este diretório é destinado ao armazenamento de recursos sonoros, incluindo trilhas sonoras, efeitos de som e demais arquivos de áudio necessários para a ambientação sonora do jogo.




## Ferramentas utilizadas:

Módulos:

Functions (from functions import ...):
Propósito: Um módulo personalizado que contém várias funções de utilidade para o jogo, como game_diff, init_game, draw_heart e assim por diante.
Justificativa: Separar funções utilitárias em um módulo distinto ajuda a manter o código principal limpo e organizado.


objects (from objects import Player):
Propósito: Um módulo personalizado que contém definições de objetos para o jogo. Aqui, a classe Player é importada.
Justificativa: Isolar a lógica relacionada ao jogador em sua própria classe ajuda a modularizar e organizar o código.


sprite_sheet (from sprite_sheet import sprites_player):
Propósito: Um módulo personalizado para lidar com spritesheets ou conjuntos de sprites.
Justificativa: Os spritesheets são uma maneira eficiente de gerenciar e usar várias imagens ou animações em jogos.


button (from button import Button_Start, Button_Exit):
Propósito: Módulo personalizado para lidar com botões na interface do jogo.
Justificativa: Isolar a lógica dos botões em classes distintas torna mais fácil de gerenciar sua funcionalidade e aparência.



counters (from counters import Stopwatch, Points_Counter):
Propósito: Módulo personalizado que lida com a contagem e exibição de pontos e tempo.
Justificativa: Manter contadores separados em suas próprias classes ajuda a organizar a lógica relacionada à pontuação e temporização.


music1 (from music1 import Music):
Propósito: Módulo personalizado que paree lida com a reprodução e controle de música e efeitos sonoros.
Justificativa: Ter uma classe dedicada à música permite controlar facilmente a reprodução dos sons no jogo.


Biblioteca:

A biblioteca pygame foi empregada como a principal ferramenta para o desenvolvimento da interface gráfica e da dinâmica de um jogo. Através dela, a interface de exibição foi inicializada, permitindo a renderização de elementos gráficos como imagens de fundo, sprites e botões. Além disso, ela é usada para detectar e gerenciar eventos de interação do usuário, como pressionamentos de teclas e operações de fechamento de janelas do jogo. A biblioteca também monitora o tempo do jogo e usa um relógio que ajuda a determinar a taxa de atualização para garantir que o jogo seja executado em uma velocidade consistente.
A utilização do pygame se justifica por fornecer uma ampla gama de funcionalidades básicas para o desenvolvimento de jogos de forma simples e eficaz. Dada a natureza gráfica e interativa do projeto, era crucial ter uma biblioteca que pudesse lidar de forma integrada com gráficos, som e interação do usuário. Pygame, uma das bibliotecas de desenvolvimento de jogos mais populares em Python, fornece esses recursos e se considera uma escolha lógica para sanar as necessidades de codificação relacionadas. É, pois, a espinha dorsal desse projeto.


time (from time import time):
Propósito: 'time' é uma biblioteca padrão em Python que fornece funções relacionadas ao tempo. Aqui, a função time é usada para a utilização de um crônometro.
Justificativa: No jogo, usamos o crônometro para medir o tempo de sobrevivência do jogador.



Aplicativos e Sites:
Entre as ferramentas utilizadas para o desenvolvimento do projeto, se encontram : Vscode, Discord, Notion, Figma, Aseprite, Canva, Pixabay e Github. O Vscode, em conjunto com o Github, foi utilizado para todo o desenvolvimento do código do jogo, através da criação de um repositório em que todos os membros da equipe possuíam acesso para atualizar o código.
Para o planejamento e acompanhamento do progresso do projeto, foi utilizado um canal no Discord para realizar as reuniões remotas, e o Notion para o planejamento inicial da base do jogo.
A arte do Manguebit foi criada por meio do Figma e Aseprite, plataformas que permitem a utilização de pixel art no desenvolvimento de sprites. No âmbito sonoro, foi através do Pixabay que se obteve o efeito sonoro que aparece assim que o jogador clica em “start”.




## Divisão de Trabalhos:
A tomada de decisão no que se diz em relação à dinâmica do jogo, bem como a escolha do tema, da interface, da lógica do jogo, das regras,ideias, features, personagens e etc foi feita conjuntamente com participação ativa de todos os membros da equipe. Todos opinaram, votaram, tiveram suas escolhas levadas em consideração durante o processo idealizatorio e criativo.

Questões técnicas:


- Artur Couto:
    Design do caranguejo;
    Implementação do stopwatch; 
    Criação do Notion;
    Criação do grupo do WhatsApp;
    Responsável pelo relatório;
    Design do background;
    Otimização do código sobre as colisões;
    Revisão e otimização de algumas functions.


- Juliana Talita:
    Criação da logica dos contadores, bem como sua respectiva implementação na tela;
    Criação das lógicas das vidas e suas funções correlacionadas;
    Implementação da musica;
    Download da musica;
    Animação do carangueijo;
    Implementação do spawn de diferentes tipos de lixos;
    Implementação dos assets;
    Design e implementação das vidas;
    Artes do botões;
    Criação dos slides pelo Canva.


- Luana Queiroz:
    Implementação da tela inicial, juntamente com a criação do módulo button.py, contendo a classe dos botões da tela de início;
    Criação do servidor do Discord;
    Responsável pelo relatório;
    Auxílio no desenvolvimento das artes do jogo
    Desenho dos objetos
    Optimização dos objetos.


- Lucas Carvalho
    Criação do contador de lixos coletados, bem como sua implementação na tela;
    Criação das classes jogador, botão de início, botão QUIT e contador de lixo,
    Criação das vidas do jogo
    Preparo da tela final
    Correção de código e revisão de classes. 


- Walfrido Saturno
    Criação da engine do jogo;
    Criação das classes do lixo e do player;
    Criação das funções basicas do jogo (queda dos objetos, movimentação do caranguejo, spawn dos sobjetos, etc);
    Adição de funcionalidades de animação de sprites para o player e de rotação para os lixos;
    Criação do nivel de dificuldade em função do tempo;
    Optimização da main;
    Correção de buggs no display;
    Ajuste dos recursos.




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




## Desafios:
O maior erro que o grupo teve que lidar foi a questão de garantir que a resolução da tela funcionasse de maneira adequada em diferentes dispositivos. Resolvemos tal problema com a utilização da função “get_window_size”, que possibilitou obter as dimensões da tela, e então definir a proporção da tela que o jogo iria ocupar.  
Entre os desafios encontrados, destaca-se, também, a utilização de programação orientada a objetos, pois, ocasionalmente, ocorreu de que, sem que o grupo percebesse, partes do código não estarem seguindo tal modelo. Entretanto, conseguimos resolver tal problema sem muita dificuldade, apenas com foco e empenho.
Além disso, também vale ressaltar que a multiplicidade das demandas acadêmicas acabaram por atrapalhar um pouco o foco no projeto devido à sobreposição de horários, provas, aulas, reuniões e etc. Necessitamos de muita organização para sanar tal problemática.
     Aprendemos, assim, que os verdadeiros projetos e os mais frutíferos dos jogos são os amigos que fazemos pelo caminho, pois sem o apoio, engajamento e compreensão do grupo como um todo, não teria sido possível passar por tantas problemáticas 






## Requisitos:
- Python 3.x
- Pygame (você pode instalá-lo com 'pip install pygame')


Este projeto foi realizado para disciplina de Introdução à Programação no CIn UFPE
### Divirta-se jogando MangueBit e ajudando a limpar o mangue!
#################################################################


