## <h1>Project_Rede_Hotel_Transylvania</h1>

> Estruturando 🤔

## <h2>O que o software propõe:</h2>

  <h3>Contexto do Software: </h3>

  <strong>Project_Rede_Hotel_Transylvania</strong> é um software de gerenciamento de hotéis projetado para automatizar e otimizar todas as operações associadas à administração de um hotel. Inspirado na temática do filme "Hotel Transilvânia," este software é especialmente voltado para hotéis que desejam oferecer uma experiência única e memorável aos seus hóspedes. Assim o software é essencial para facilitar as operações diárias do estabelecimento. Ele proporciona uma abordagem eficiente para lidar com o fluxo de reservas de uma rede de hoteís, garantindo uma administração mais organizada e melhor experiência para os clientes e funcionarios.
  
  
## <h2>Funcionalidades:</h2>
  
  + Reservas e Check-In
  + Gestão de quartos
  + Gestão de hoteis 
    
## <h2>Tecnologias Usadas:</h2>
 <h3>Linguagens:</h3>

  + Node 18.16.1               
  + Typescript 4.8
  + python 3.8
   
##  <h3>Banco de dados:</h3>

  + MySQL Ver 8.0.35-0ubuntu0.20.04.1 for Linux on x86_64 ((Ubuntu))

##  <h3>Frameworks :</h3>
  
  + Angular v 15.2.7.
  + Django 4.2.7.

## <h2>Regras de uso do github:</h2>

  + Commits:
  Os commits devem ser descritivos sendo a primeira palavra um verbo, ele também deve ocorrer sempre que algo e atualizado ou criado.
  + Pull Requests
  Os pull requests so serão feitos com a supervisão e juntamente com outro membro
  + Criação de branchs
  Deve se criar uma branch sempre que a alteração apresentar grau de complexidade alta e medio
  + Pastas
  As pastas são tendem a ser descritivas, ou seja, seus nomes são respectivos ao seu conteudo

## <h2>Regras para boa pratica de programação:</h2>

<h3>1.Nomenclatura Descritiva:</h3>
  
    Usa nomes de variáveis, funções e classes que descrevam claramente o propósito e a funcionalidade.
    Evite abreviações confusas. Prefira clareza e legibilidade sobre economia de caracteres.
    
<h3>2.Divisão Lógica e Modularização:</h3>
  
    Divida seu código em funções ou módulos pequenos e específicos. Cada função ou módulo deve realizar uma tarefa única.
    Evite funções muito longas que realizam muitas tarefas diferentes. Isso melhora a manutenibilidade e facilita a compreensão do código.

<h3>3.CLEAN CODE:</h3>

    Aplique os princípios do CLEAN CODE, como evitar duplicação de código, manter funções curtas e focadas, e garantir a clareza e simplicidade do código.

<h3>4.Consistência na Indentação Utilizando Tabs:</h3>
  
    Mantenha a consistência na indentação do código utilizando tabs.

## <h2>Explicação de pastas:</h2>


  Projeto Hotel Transilvania
          ->  Backend diretório que separa o back do front
              |-> hotelTransilvania : diretório com o projetodo do backend
                 |-> APP : diretório com a aplicação do back end
                    |-> funcionalidades : diretorio com as funcionalidades do projeto
                    |-> migrations : diretorio com as migrations do projeto
                 |-> hotelTransilvania : diretório de configurações do projeto
              | -> venv : diretório com o ambiente virtual



          -> Frontend
              |-> src : local onde pode se encontrar a estrutura principal do codigo 
              |  -> app: estrutura que se encontra a pasta de components, routina de paginas, services e modelos
              |     ->services : dentro de services possue as rotas de chamadas de dados ao backend, comunicação API
              |     -> models : são estruturas de dados que serão enviadas ou recebidas
              |     ->components: dentro de components estão cada elemento do codigo modularizado
              |     na pasta de componments tudo e muito descritivo por isso explicarei so a pasta de formularios e modal
              |        -> formularios: dentro desta pasta se encontrao todo tipo de formulario
              |        -> modal : modal são arquivos que vão listar algo para o usuario 
              |->arquivos.json : se encontrão as dependencias, versões de bibliotecas etc
