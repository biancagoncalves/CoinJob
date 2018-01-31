# CryptoMarketAnalysis  ![](https://www.allcoin.com/Content/image/allcoin_logo02.png)
## Trabalho do curso de Verão 2018 

  - Autor: Bianca Gonçalves
  - Professor: Renato Rocha e Flavio Coelho
  - Exchange escolhida: Allcoin
  - Local da exchange: Canada
  - Mercados: ![](https://o56yv98bm.qnssl.com/coin_BTG.png?imageView2/2/w/19) Gold Bitcoin (BTG/BTC), ![](https://o56yv98bm.qnssl.com/coin_BCD.png?imageView2/2/w/19) Bitcoin Diamond (BCD/BTC) e ![](https://o56yv98bm.qnssl.com/coin_ETH.png?imageView2/2/w/19) Ether (ETH/BTC)


### Estrutura do trabalho
 

#### 1 -  Obtendo os dados 
       
Escolhida a exchange **`Allcoin`**, os dados são obtidos através da biblioteca **`ccxt`**

  - **`src/capturador.py`**: possui uma classe chamada **`capturador`** que exectua a extração baseada nos seguintes argumentos: 
   
    - **`max_dias`**: Quanditade de dias até a data atual
    - **`symbol`**: Tipo de moeda que se deseja obter os valores
    - **`time_frame`**: intervalo de tempo dos dados (ex.: 5 minutos)


#### 2 -  Banco de dados (MySQL) 

Com o banco de dados online, uma tabela foi criada para os dados da exchange escolhida. Com uma chave primária composta (date e mercado). É possível armazenar em um unico lugar, dados de diferentes moedas e time frames sem duplicatas. 

Estando o banco online, não há necessidade de recriar o storage toda vez que o script for rodado em um ambiente novo. 

  - **`src/capturador.py`**: possui uma função chamada **`salva_banquinho`** que armazena os dados extraídos do capturador. Argumentos:
  
    - **`data1`**: objeto com os dados da moeda
    - **`symbol`**: Tipo de moeda que se deseja obter os valores


#### 3 - Visualização dos dados apartir do banco. 



##### Dependências para rodar os códigos

  - bokeh
  - numpy
  - ccxt
  - pandas
  - requests
  - mysql.connector

