<h1>Desafio PokéAPI</h1>

<h2>Descrição:</h2>
<p>Realiza a conexão e o consumo da api PokéApi, para gerar uma lista dos 20 primeiros Pokémons da Pokédex e depois permite que o usuário selecione um Pokémon dessa lista e retorna mais informações do Pokémon selecionado.</p>

<h2>Esse projeto realiza: </h2>
<ul>
    <li>O consumo da api PokéApi, utilizando a biblioteca Requests do Python, retornando um objeto json com bruto com a informações dos 20 primeiros Pokémons da Pokédex.</li> 
    <li>Manipula o objeto json para que seja possível gerar uma lista dos 20 primeiros Pokémons, exibindo a lista no console com o 'id' e o 'nome do Pokémon'.</li>
    <li>Permite que o usuário digite o 'id' de um dos Pokémons, assim o usuário terá acesso a uma série de informações do Pokémon selecionado como tipos, habilidades, peso e a url para obter a informação completa sobre o Pokémon selecionado.</li>
    <li>Permite que o usuário realize uma nova busca em sequência, exibindo novamente a lista e questionando novamente o 'id' do Pokémon que será o alvo da busca.</li>
    <li>Exibe uma mensagem de alerta ao usuário caso seja informado um 'id' que não corresponda a lista mostrada no console.</li>
</ul>

<h2>Pré-requisitos:</h2>
<ul>
    <li>Ter o Python 3 instalado em qualquer versão igual ou superior a 3.8.</li>
    <li>Ter um editor para trabalhar com o código como o VSCode.</li>
</ul>
<p>Passo a passo para executar a rotina no Windows</p>
<ol>
    <li>Faça o download da pasta compactada com os arquivos deste repositório e defina um diretório em seu computador onde os arquivos ficaram armazenados.</li>
    <li>Abra o CMD e com o comando cd + o caminho do diretório onde estão os arquivos posicione na pasta onde os arquivos estão armazenados.</li>
    <li>Uma vez que esteja posicionado no diretório, utilize o comando python pokemon.py para executar o arquivo.</li>
</ol>

<h2>Como Testar</h2>
<ol>
    <li>Ao executar o arquivo pokemon.py, no console aparecerá a lista com os 20 primeiros Pokémons da PokéDex.</li>
    <li>A rotina exibirá uma pergunta questionando qual o id do Pokémon que você deseja consultar.</li>
    <li>Informando um dos id's que aparecem na tela, será apresentado umma lista de itens que correspondek ao Pokémon que pertence a aquele id, como nome, peso, tipos, habilidades e uma url para visualizar os dados completos do Pokémon.</li>
    <li>Depois de carregar todas as informações do Pokémon a rotina questionará se deseja realizar uma nova consulta, pressionando 'y' de yes, a rotina recarregará a lista de Pokémons, pressionando 'n' de no, a execução da rotina será finalizada.</li>
</ol>
<p>*Caso seja informado um id que não corresponda aos id's da lista, a rotina exibirirá a mensagem 'O id digitado não corresponde a lista de pokemons apresentada acima' e será solicitado que o id seja digitado novamente.</p>
<p>**Atualmente a consulta dos Pokémons só é possível ser feita através do id, não sendo possível consultar pelo nome.</p>

<h2>Tecnologia</h2>
<p>Python 3 versão 3.9.7</p>

<h2>Autor</h2>
<p>Rafael Antunes dos Santos</p>
