# Software Ciclo Térmico e Heat Input
Este projeto foi desenvolvido como parte do Trabalho de Graduação (TG) em Mecânica: Processos de Soldagem. Ele combina um software desktop escrito em Python e um aplicativo complementar  (disponível [neste repositório em formato APK](https://github.com/Matheus4ndrade/C_Termico)). Este repositório refere-se ao software que complementa o processo de análise térmica no contexto de soldagem.
O objetivo principal deste software é fornecer uma ferramenta prática e acessível para cálculos térmicos e de parâmetros essenciais no processo de soldagem, utilizando equações específicas da área.

## Objetivo
O software foi projetado para:

-   Realizar cálculos baseados em parâmetros como densidade, calor específico, velocidade de soldagem e outras variáveis.
-   Gerar gráficos de temperatura por distância e temperatura por tempo, essenciais para a análise do perfil térmico no material.
-   Auxiliar profissionais e estudantes da área de soldagem no planejamento e execução de processos mais eficientes.

## Importância para a Soldagem
Nos processos de soldagem, o controle térmico é crucial para garantir a qualidade e resistência das juntas soldadas. Este software utiliza equações específicas que permitem:   

- Determinar a distribuição de temperatura ao longo do material.
- Calcular o Heat Input (Ht), um parâmetro essencial para prever a microestrutura final da solda.
- Auxiliar na análise de viabilidade do processo com base nas propriedades do material e condições de operação.

 A ferramenta torna mais prática a análise de variáveis que tradicionalmente demandam cálculos complexos, proporcionando uma interface amigável e intuitiva.

## Funcionalidades
- Entrada de dados: Insira os parâmetros do processo de soldagem.
- Cálculo automático: Os valores necessários são calculados automaticamente após a inserção dos dados.
- Geração de gráficos:
    - Temperatura x Distância
    - Temperatura x Tempo
- Interface intuitiva para usuários de diversos níveis de experiência.

## Como Usar

### Pré-requisitos
- Python 3.6+: Certifique-se de que o Python está instalado no seu sistema.
- Bibliotecas necessárias: Instale as dependências com o seguinte comando:

``` 
pip install -r requirements.txt
```

### Executando o Software
#### Para executar o programa diretamente:
1) Navegue até a pasta dist onde está localizado o arquivo Ciclo_Termico.exe.

2) Execute o programa clicando duas vezes no arquivo Ciclo_Termico.exe.

#### Para executar o código no terminal:

**1º** Clone este repositório:
```
git clone https://github.com/Matheus4ndrade/cTermico.git
```

**2º** Navegue até a pasta do projeto:
```
cd cTermico
```

**3º** Execute o software com o seguinte comando:
```
python main.py
```

# Autor
Este projeto foi desenvolvido por Matheus Felipe Andrade Gomes como parte do Trabalho de Graduação em Mecânica: Processos de Soldagem.