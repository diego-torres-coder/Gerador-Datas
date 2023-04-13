# Gerador de Datas

Esta aplicação permite que o usuário especifique um ano inicial e um ano final
para poder gerar todas as datas no intervalo de anos especificado.

Além de gerar as datas, a aplicação extrai as seguintes informações sobre elas:

- dia
- mês
- ano

O usuário tem ainda a possibilidade de baixar um CSV com os dados obtidos, o qual
ele pode importar, por exemplo, em um arquivo do Excel para poder fazer análises
temporais.

## Demo

Confira a aplicação já hospedada, clicando neste link: 

- https://diego-torres-coder-gerador-datas-main-t84qnx.streamlit.app/

## Como Reproduzir este Projeto

Primeiramente, navegue até a pasta em que deseja reproduzir este projeto. Em seguida,
digite este comando no terminal:

```bash
git clone https://github.com/diego-torres-coder/Gerador-Datas.git
```

Navegue para a pasta recém-criada com o passo anterior:

```bash
cd Gerador-Datas
```

Crie um ambiente conda para o projeto:

```bash
conda create -n stenv-gerador-datas python=3.10
```

Ative o ambiente virtual:

```bash
conda activate stenv-gerador-datas
```

Instale as dependências do projeto:

```bash
pip install numpy openpyxl panda streamlit
```

Alternativamente, instale as dependências a partir do arquivo `requirements.txt`:

```bash
pip install -r requirements.txt
```

Por fim, execute a aplicação:

```bash
streamlit run main.py
```
