# AnimadorAFD
O objetivo deste trabalho é aplicar os conhecimentos obtidos sobre AFDs para construir uma ferramenta que produza uma animação de um AFD sob uma dada entrada. A ideia para a realização deste trabalho consiste em produzir um quadro de imagem para cada passo da configuração instantânea da máquina, realçando-se o estado corrente e as próximas transições possíveis. O trabalho de juntar todos os quadros e formar uma animação deve ser gerenciado por uma ferramenta externa e está fora do escopo deste trabalho.

## Requisitos
Para executar o código, e necessário ter isntalado na maquina o Python 3.8+, e o GraphViz. Em seguida, instalar os pacotes presentes no "requirements.txt" (pip install -r requirements.txt). A execução estável deste programa é realizada no Ubuntu 20.04, ou usando o WSL com o mesmo sistema.

## Execução do código
Após instalados os requisitos, o arquivo de entrada ("entrada.txt") deve ser editado para inserir algum automato. Devido a problemas que tive no desenvolvimento, esse programa anima apenas AFD's, ficando para uma proxima oportunidade a animação dos AFN's.
Para iniciar o programa, você deve executar o arquivo "app.py", encontrado na pasta "src". Se executado de forma correta, os arquivos salvos pelo programa, estarão na pasta "assets". Na subpasta "dot", estarão salvos os passos em formato .dot; Na subpasta "steps" ficam armazenados temporariamente (assim que criado o gif elas são excluídas), as imagens equivalentes aos arquivos .dot gerados anteriormente; Na subpasta "gif" fica armazenado o .gif gerado pela animação do automato.
Para casos onde as palavras não são válidas a animação execurará até o ponto de erro. 