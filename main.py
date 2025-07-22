import streamlit as st
import pandas as pd
import pydeck as pdk
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from PIL import Image
import cv2
import numpy as np
import os


with open("style.css") as f:
    css = f.read()

st.markdown(f'<style>{css}</style> <h1>INFOVENOM</h1>' , unsafe_allow_html=True)


@st.cache_data
def load_data():
    data = pd.read_csv('arquivos csv/mes_todos.csv')
    return data
df = load_data()

def load_data2():
    data = pd.read_csv('arquivos csv/regiao_todos.csv')
    return data
df2 = load_data2()

def load_data3():
    data = pd.read_csv('arquivos csv/idade_todos.csv')
    return data
df3 = load_data3()

def load_data4():
    data = pd.read_csv('arquivos csv/atendimento_todos.csv')
    return data
df4 = load_data4()

def load_data5():
    data = pd.read_csv('arquivos csv/tipo_serpente.csv')
    return data
df5 = load_data5()

def load_data6 ():
    data = pd.read_csv('arquivos csv/tipo_aranha.csv')
    return data
df6 = load_data6()

def load_data7 ():
    data = pd.read_csv('arquivos csv/local_picada.csv')
    return data
df7 = load_data7()

def load_data8 ():
    data = pd.read_csv('arquivos csv/tipo_acidente.csv')
    return data

df8 = load_data8()

def load_data9():
    data = pd.read_csv('arquivos csv/evolucao_caso_todos.csv')
    return data

df9 = load_data9()

st.subheader("Situação Epidemiológica")  

opcao2 = st.selectbox("Selecione o ano:", ["2023", "2022", "2021", "2020"])
opcao3 = st.selectbox("Selecione a visualização:", ["Número de Acidentes por Mês", "Região de Notificação", "Taxa de cura por Faixa Etária", "Tempo Picada/Atendimento", "Tipo da Serpente", "Tipo da Aranha", "Local da picada", "Tipo de Acidente", "Evolução do caso"])
if opcao2 == "2023":
        if opcao3 == "Número de Acidentes por Mês":
                    ano = 2023
                    linha_ano = df[df['Ano'] == str(ano)] 
                    meses = linha_ano.columns[1:-1] 
                    acidentes_por_mes = [str(value) for value in linha_ano.iloc[0, 1:-1].values]
            
                    plt.figure(figsize=(10, 5))
                    plt.plot(meses, [int(value) for value in acidentes_por_mes], marker='o', color='#325c74') 
                    plt.title(f'Número de Acidentes por Mês em {ano}')
                    plt.xlabel('Meses')
                    plt.ylabel('Número de Acidentes')
                    plt.xticks(rotation=45)
                    plt.grid(axis='y')
                    st.pyplot(plt)
                    st.dataframe(linha_ano)

                    if st.checkbox('Mostrar detalhes adicionais'):
                        st.write('Comparação do número de acidentes por mês entre os anos 2020 a 2023.')

                       
                        ano1 = 2020
                        ano2 = 2021
                        ano3 = 2022
                        ano4 = 2023

                       
                        linha_ano1 = df[df['Ano'] == str(ano1)]
                        linha_ano2 = df[df['Ano'] == str(ano2)]
                        linha_ano3 = df[df['Ano'] == str(ano3)]
                        linha_ano4 = df[df['Ano'] == str(ano4)]

                      
                        meses = linha_ano1.columns[1:-1]

                 
                        acidentes_ano1 = linha_ano1.iloc[0, 1:-1].values
                        acidentes_ano2 = linha_ano2.iloc[0, 1:-1].values
                        acidentes_ano3 = linha_ano3.iloc[0, 1:-1].values
                        acidentes_ano4 = linha_ano4.iloc[0, 1:-1].values

                      
                        import numpy as np
                        x = np.arange(len(meses)) 
                        largura = 0.2

                    
                        cor_ano1 = '#325c74'  
                        cor_ano2 = '#b8a99a'  
                        cor_ano3 = '#70866f'  
                        cor_ano4 = '#e4d9c4'  

                      
                        plt.figure(figsize=(12, 6))
                        plt.bar(x - 1.5*largura, acidentes_ano1, width=largura, label=f'{ano1}', color=cor_ano1)
                        plt.bar(x - 0.5*largura, acidentes_ano2, width=largura, label=f'{ano2}', color=cor_ano2)
                        plt.bar(x + 0.5*largura, acidentes_ano3, width=largura, label=f'{ano3}', color=cor_ano3)
                        plt.bar(x + 1.5*largura, acidentes_ano4, width=largura, label=f'{ano4}', color=cor_ano4)

                        plt.xlabel('Meses')
                        plt.ylabel('Número de Acidentes')
                        plt.title('Número de Acidentes por Mês (2020–2023)')
                        plt.xticks(x, meses, rotation=45)
                        plt.legend()
                        plt.grid(axis='y')

                        st.pyplot(plt)

                    
                        dados_comparacao = pd.DataFrame({
                            'Meses': meses,
                            f'Acidentes {ano1}': [int(value) for value in acidentes_ano1],
                            f'Acidentes {ano2}': [int(value) for value in acidentes_ano2],
                            f'Acidentes {ano3}': [int(value) for value in acidentes_ano3],
                            f'Acidentes {ano4}': [int(value) for value in acidentes_ano4]
                        })

                        st.dataframe(dados_comparacao)
        if opcao3 == "Região de Notificação":
                    ano = 2023
                    linha_ano = df2[df2['Ano'] == str(ano)]  # Filtra a linha correspondente ao ano (convertendo ano para string)
                    regioes = linha_ano.columns[1:-1] 
                    acidentes_por_regiao = [str(value) for value in linha_ano.iloc[0, 1:-1].values]
                    plt.figure(figsize=(10, 5))
                    plt.bar(regioes, [int(value) for value in acidentes_por_regiao], color='#325c74')  # Converte de volta para int para o gráfico
                    plt.title(f'Número de Acidentes por Região de Notificação em {ano}')
                    plt.xlabel('Regiões')
                    plt.ylabel('Número de Acidentes')
                    plt.xticks(rotation=45)
                    plt.grid(axis='y')
                    st.pyplot(plt)
                    st.dataframe(linha_ano)

                    if st.checkbox('Mostrar detalhes adicionais'):
                        st.write('Comparação do número de acidentes por região de notificação entre os anos 2020 a 2023.')

                        # Definindo os anos
                        ano1 = 2020
                        ano2 = 2021
                        ano3 = 2022
                        ano4 = 2023

                        # Filtrando os dados por ano
                        linha_ano1 = df2[df2['Ano'] == str(ano1)]
                        linha_ano2 = df2[df2['Ano'] == str(ano2)]
                        linha_ano3 = df2[df2['Ano'] == str(ano3)]
                        linha_ano4 = df2[df2['Ano'] == str(ano4)]

                        # Regiões
                        regioes = linha_ano1.columns[1:-1]

                        # Coletar os valores
                        acidentes_ano1 = [int(value) for value in linha_ano1.iloc[0, 1:-1].values]
                        acidentes_ano2 = [int(value) for value in linha_ano2.iloc[0, 1:-1].values]
                        acidentes_ano3 = [int(value) for value in linha_ano3.iloc[0, 1:-1].values]
                        acidentes_ano4 = [int(value) for value in linha_ano4.iloc[0, 1:-1].values]

                        # Configurar posições das barras
                        import numpy as np
                        x = np.arange(len(regioes))  # posições das categorias
                        largura = 0.2  # largura de cada barra

                        # Cores definidas para cada ano
                        cor_ano1 = '#325c74'  # azul
                        cor_ano2 = '#b8a99a'  # laranja
                        cor_ano3 = '#70866f'  # verde
                        cor_ano4 = '#e4d9c4'  # vermelho

                        # Criar figura
                        plt.figure(figsize=(12, 6))
                        plt.bar(x - 1.5*largura, acidentes_ano1, width=largura, label=f'{ano1}', color=cor_ano1)
                        plt.bar(x - 0.5*largura, acidentes_ano2, width=largura, label=f'{ano2}', color=cor_ano2)
                        plt.bar(x + 0.5*largura, acidentes_ano3, width=largura, label=f'{ano3}', color=cor_ano3)
                        plt.bar(x + 1.5*largura, acidentes_ano4, width=largura, label=f'{ano4}', color=cor_ano4)

                        plt.xlabel('Regiões')
                        plt.ylabel('Número de Acidentes')
                        plt.title('Número de Acidentes por Região de Notificação (2020–2023)')
                        plt.xticks(x, regioes, rotation=45)
                        plt.legend()
                        plt.grid(axis='y')

                        st.pyplot(plt)

                        # Mostrar os dados em tabela
                        dados_comparacao_regioes = pd.DataFrame({
                            'Região': regioes,
                            f'Acidentes {ano1}': acidentes_ano1,
                            f'Acidentes {ano2}': acidentes_ano2,
                            f'Acidentes {ano3}': acidentes_ano3,
                            f'Acidentes {ano4}': acidentes_ano4
                        })
                        st.dataframe(dados_comparacao_regioes)
        if opcao3 == "Taxa de cura por Faixa Etária":
                    ano = 2023
                    linha_ano = df3[df3['Ano'] == str(ano)]  # Filtra a linha correspondente ao ano (convertendo ano para string)
                    idades = linha_ano.columns[1:-1] 
                    acidentes_por_idade = [str(value) for value in linha_ano.iloc[0, 1:-1].values]
                    plt.figure(figsize=(10, 5))
                    plt.fill_between(idades, [int(value) for value in acidentes_por_idade], color='#325c74', alpha=0.5)
                    plt.plot(idades, [int(value) for value in acidentes_por_idade], marker='o', color='#325c74')  # Adiciona a linha acima da área preenchida
                    plt.title(f'Número de Acidentes por Faixa Etária em {ano}')
                    plt.xlabel('Faixa Etária')
                    plt.ylabel('Número de Acidentes')
                    plt.xticks(rotation=45)
                    plt.grid(axis='y')
                    st.pyplot(plt)
                    st.dataframe(linha_ano)

                    if st.checkbox('Mostrar detalhes adicionais'):
                        st.write('Comparação do número de acidentes por faixa etária entre os anos 2020 a 2023.')

                        # Anos
                        ano1 = 2020
                        ano2 = 2021
                        ano3 = 2022
                        ano4 = 2023

                        # Filtrar os dados por ano
                        linha_ano1 = df3[df3['Ano'] == str(ano1)]
                        linha_ano2 = df3[df3['Ano'] == str(ano2)]
                        linha_ano3 = df3[df3['Ano'] == str(ano3)]
                        linha_ano4 = df3[df3['Ano'] == str(ano4)]

                        # Faixas etárias
                        idades = linha_ano1.columns[1:-1]

                        # Coletar os valores
                        acidentes_ano1 = [int(value) for value in linha_ano1.iloc[0, 1:-1].values]
                        acidentes_ano2 = [int(value) for value in linha_ano2.iloc[0, 1:-1].values]
                        acidentes_ano3 = [int(value) for value in linha_ano3.iloc[0, 1:-1].values]
                        acidentes_ano4 = [int(value) for value in linha_ano4.iloc[0, 1:-1].values]

                        # Posições das barras
                        import numpy as np
                        x = np.arange(len(idades))
                        largura = 0.2

                        # Cores definidas para cada ano
                        cor_ano1 = '#325c74'  # azul
                        cor_ano2 = '#b8a99a'  # laranja
                        cor_ano3 = '#70866f'  # verde
                        cor_ano4 = '#e4d9c4'  # vermelho

                        # Criar figura
                        plt.figure(figsize=(12, 6))
                        plt.bar(x - 1.5*largura, acidentes_ano1, width=largura, label=f'{ano1}', color=cor_ano1)
                        plt.bar(x - 0.5*largura, acidentes_ano2, width=largura, label=f'{ano2}', color=cor_ano2)
                        plt.bar(x + 0.5*largura, acidentes_ano3, width=largura, label=f'{ano3}', color=cor_ano3)
                        plt.bar(x + 1.5*largura, acidentes_ano4, width=largura, label=f'{ano4}', color=cor_ano4)

                        plt.xlabel('Faixa Etária')
                        plt.ylabel('Número de Acidentes')
                        plt.title('Número de Acidentes por Faixa Etária (2020–2023)')
                        plt.xticks(x, idades, rotation=45)
                        plt.legend()
                        plt.grid(axis='y')

                        st.pyplot(plt)

                        # Exibir os dados em tabela
                        dados_comparacao_idades = pd.DataFrame({
                            'Faixa Etária': idades,
                            f'Acidentes {ano1}': acidentes_ano1,
                            f'Acidentes {ano2}': acidentes_ano2,
                            f'Acidentes {ano3}': acidentes_ano3,
                            f'Acidentes {ano4}': acidentes_ano4
                        })
                        st.dataframe(dados_comparacao_idades)
        if opcao3 == "Tempo Picada/Atendimento":
                    ano = 2023
                    linha_ano = df4[df4['Ano'] == str(ano)]
                    tempos = linha_ano.columns[1:-1]
                    acidentes_por_tempo =  [str(value) for value in linha_ano.iloc[0, 1:-1].values]
                    plt.figure(figsize=(10,5))
                    plt.plot(tempos, [int(value) for value in acidentes_por_tempo], marker='o', color='#325c74')
                    plt.title('Número de acidentes por Tempo de Atendimento')
                    plt.xlabel('Tempo de Atendimento')
                    plt.ylabel('Número de Acidentes')
                    plt.xticks(rotation=50)
                    plt.grid(axis='y')
                    st.pyplot(plt)
                    st.dataframe(linha_ano)

                    if st.checkbox('Mostrar detalhes adicionais'):
                        st.write('Aqui estão mais informações sobre o assunto...')
                        ano1 = 2020
                        ano2 = 2021
                        ano3 = 2022
                        ano4 = 2023

                    # Coletar dados para o primeiro ano
                        linha_ano1 = df4[df4['Ano'] == str(ano1)]
                        tempos = linha_ano1.columns[1:-1]  # Ignora a coluna 'Ano' e a coluna 'Total'
                        acidentes_por_tempo_ano1 = linha_ano1.iloc[0, 1:-1].values  # Pega os dados da primeira linha após filtrar pelo ano

                        # Coletar dados para o segundo ano
                        linha_ano2 = df4[df4['Ano'] == str(ano2)]
                        acidentes_por_tempo_ano2 = linha_ano2.iloc[0, 1:-1].values  # Pega os dados da primeira linha após filtrar pelo ano

                            # Coletar dados para o terceiro ano
                        linha_ano3 = df4[df4['Ano'] == str(ano3)]
                        acidentes_por_tempo_ano3 = linha_ano3.iloc[0, 1:-1].values  # Pega os dados da primeira linha após filtrar pelo ano

                        # Coletar dados para o quarto ano
                        linha_ano4 = df4[df4['Ano'] == str(ano4)]
                        acidentes_por_tempo_ano4 = linha_ano4.iloc[0, 1:-1].values  # Pega os dados da primeira linha após filtrar pelo ano


                        # Definir a ordem correta dos meses
                        ordem_tempos = ['0 a 1 horas', '1 a 3 horas', '3 a 6 horas', '6 a 12 horas', '12 a 24 horas', '24 e + horas']

                        # Criar um DataFrame para comparação
                        dados_comparacao = pd.DataFrame({
                            'Tempos': tempos,
                            f'Acidentes {ano1}': [int(value) for value in acidentes_por_tempo_ano1],
                            f'Acidentes {ano2}': [int(value) for value in acidentes_por_tempo_ano2],
                            f'Acidentes {ano3}': [int(value) for value in acidentes_por_tempo_ano3],
                            f'Acidentes {ano4}': [int(value) for value in acidentes_por_tempo_ano4]
                        })
                        # Reorganizar o DataFrame com base na ordem dos meses
                        dados_comparacao["Tempos"] = pd.Categorical(dados_comparacao["Tempos"], categories=ordem_tempos, ordered=True)

                        # Definir o índice do DataFrame como meses
                        dados_comparacao.set_index('Tempos', inplace=True)

                        # Usar st.line_chart para comparar os dois anos
                        st.line_chart(dados_comparacao)

                        # Exibir os dados em tabela (opcional)
                        st.dataframe(dados_comparacao.reset_index())
        if opcao3 == "Tipo da Serpente":
                    ano = 2023
                    linha_ano = df5[df5['Ano'] == str(ano)]  # Filtra a linha correspondente ao ano (convertendo ano para string)
                    serpente = linha_ano.columns[1:-1] 
                    acidentes_por_ts = [str(value) for value in linha_ano.iloc[0, 1:-1].values]
                    plt.figure(figsize=(10, 5))
                    plt.bar(serpente, [int(value) for value in acidentes_por_ts], color='#325c74')  # Converte de volta para int para o gráfico
                    plt.title(f'Número de Acidentes por Tipo da Serpente em {ano}')
                    plt.xlabel('Regiões')
                    plt.ylabel('Número de Acidentes')
                    plt.xticks(rotation=45)
                    plt.grid(axis='y')
                    st.pyplot(plt)
                    st.dataframe(linha_ano)
                        

                    if st.checkbox('Mostrar detalhes adicionais'):
                        st.write('Comparação do número de acidentes por tipo de serpente entre os anos 2020 a 2023.')

                        # Anos
                        ano1 = 2020
                        ano2 = 2021
                        ano3 = 2022
                        ano4 = 2023

                        # Filtrando os dados por ano
                        linha_ano1 = df5[df5['Ano'] == str(ano1)]
                        linha_ano2 = df5[df5['Ano'] == str(ano2)]
                        linha_ano3 = df5[df5['Ano'] == str(ano3)]
                        linha_ano4 = df5[df5['Ano'] == str(ano4)]

                        # Nomes dos tipos de serpente
                        serpentes = linha_ano1.columns[1:-1]

                        # Coleta dos valores por tipo
                        acidentes_ano1 = [int(value) for value in linha_ano1.iloc[0, 1:-1].values]
                        acidentes_ano2 = [int(value) for value in linha_ano2.iloc[0, 1:-1].values]
                        acidentes_ano3 = [int(value) for value in linha_ano3.iloc[0, 1:-1].values]
                        acidentes_ano4 = [int(value) for value in linha_ano4.iloc[0, 1:-1].values]

                        # Configurar posições das barras
                        import numpy as np
                        x = np.arange(len(serpentes))  # posições das categorias
                        largura = 0.2  # largura de cada barra

                        # Cores definidas para cada ano
                        cor_ano1 = '#325c74'  # azul
                        cor_ano2 = '#b8a99a'  # laranja
                        cor_ano3 = '#70866f'  # verde
                        cor_ano4 = '#e4d9c4'  # vermelho

                        # Criar figura
                        plt.figure(figsize=(12, 6))
                        plt.bar(x - 1.5*largura, acidentes_ano1, width=largura, label=f'{ano1}', color=cor_ano1)
                        plt.bar(x - 0.5*largura, acidentes_ano2, width=largura, label=f'{ano2}', color=cor_ano2)
                        plt.bar(x + 0.5*largura, acidentes_ano3, width=largura, label=f'{ano3}', color=cor_ano3)
                        plt.bar(x + 1.5*largura, acidentes_ano4, width=largura, label=f'{ano4}', color=cor_ano4)

                        plt.xlabel('Tipo de Serpente')
                        plt.ylabel('Número de Acidentes')
                        plt.title('Número de Acidentes por Tipo de Serpente (2020–2023)')
                        plt.xticks(x, serpentes, rotation=45)
                        plt.legend()
                        plt.grid(axis='y')

                        st.pyplot(plt)

                        # Mostrar os dados em tabela
                        dados_comparacao_serpentes = pd.DataFrame({
                            'Tipo de Serpente': serpentes,
                            f'Acidentes {ano1}': acidentes_ano1,
                            f'Acidentes {ano2}': acidentes_ano2,
                            f'Acidentes {ano3}': acidentes_ano3,
                            f'Acidentes {ano4}': acidentes_ano4
                        })
                        st.dataframe(dados_comparacao_serpentes)
        if opcao3 == "Tipo da Aranha":
                    ano = 2023
                    linha_ano = df6[df6['Ano'] == str(ano)]  # Filtra a linha correspondente ao ano (convertendo ano para string)
                    aranha = linha_ano.columns[1:-1] 
                    acidentes_por_ta = [str(value) for value in linha_ano.iloc[0, 1:-1].values]
                    plt.figure(figsize=(10, 5))
                    plt.fill_between(aranha, [int(value) for value in acidentes_por_ta], color='#325c74', alpha=0.5)
                    plt.plot(aranha, [int(value) for value in acidentes_por_ta], marker='o', color='#325c74')  # Adiciona a linha acima da área preenchida
                    plt.title(f'Número de Acidentes por Tipo da Aranha em {ano}')
                    plt.xlabel('Faixa Etária')
                    plt.ylabel('Número de Acidentes')
                    plt.xticks(rotation=45)
                    plt.grid(axis='y')
                    st.pyplot(plt)
                    st.dataframe(linha_ano)

                    if st.checkbox('Mostrar detalhes adicionais'):
                        st.write('Comparação do número de acidentes por tipo de aranha entre os anos 2020 a 2023.')

                        # Definindo os anos
                        ano1 = 2020
                        ano2 = 2021
                        ano3 = 2022
                        ano4 = 2023

                        # Filtrando os dados por ano
                        linha_ano1 = df6[df6['Ano'] == str(ano1)]
                        linha_ano2 = df6[df6['Ano'] == str(ano2)]
                        linha_ano3 = df6[df6['Ano'] == str(ano3)]
                        linha_ano4 = df6[df6['Ano'] == str(ano4)]

                        # Tipos de aranha
                        aranha = linha_ano1.columns[1:-1]

                        # Coletando os dados por tipo de aranha
                        acidentes_ano1 = [int(value) for value in linha_ano1.iloc[0, 1:-1].values]
                        acidentes_ano2 = [int(value) for value in linha_ano2.iloc[0, 1:-1].values]
                        acidentes_ano3 = [int(value) for value in linha_ano3.iloc[0, 1:-1].values]
                        acidentes_ano4 = [int(value) for value in linha_ano4.iloc[0, 1:-1].values]

                        # Posições das barras
                        import numpy as np
                        x = np.arange(len(aranha))  # posições dos tipos de aranha
                        largura = 0.2  # largura de cada barra

                        # Cores definidas para cada ano
                        cor_ano1 = '#325c74'  # azul
                        cor_ano2 = '#b8a99a'  # laranja
                        cor_ano3 = '#70866f'  # verde
                        cor_ano4 = '#e4d9c4'  # vermelho

                        # Criar figura
                        plt.figure(figsize=(12, 6))
                        plt.bar(x - 1.5*largura, acidentes_ano1, width=largura, label=f'{ano1}', color=cor_ano1)
                        plt.bar(x - 0.5*largura, acidentes_ano2, width=largura, label=f'{ano2}', color=cor_ano2)
                        plt.bar(x + 0.5*largura, acidentes_ano3, width=largura, label=f'{ano3}', color=cor_ano3)
                        plt.bar(x + 1.5*largura, acidentes_ano4, width=largura, label=f'{ano4}', color=cor_ano4)

                        plt.xlabel('Tipo de Aranha')
                        plt.ylabel('Número de Acidentes')
                        plt.title('Número de Acidentes por Tipo de Aranha (2020–2023)')
                        plt.xticks(x, aranha, rotation=45)
                        plt.legend()
                        plt.grid(axis='y')

                        st.pyplot(plt)

                        # Criar DataFrame para comparação
                        dados_comparacao = pd.DataFrame({
                            'Tipo de Aranha': aranha,
                            f'Acidentes {ano1}': acidentes_ano1,
                            f'Acidentes {ano2}': acidentes_ano2,
                            f'Acidentes {ano3}': acidentes_ano3,
                            f'Acidentes {ano4}': acidentes_ano4
                        })

                        st.dataframe(dados_comparacao)
        if opcao3 == "Local da picada":
                    ano = 2023
                    linha_ano = df7[df7['Ano'] == str(ano)]
                    local_picada = linha_ano.columns[1:-1]
                    acidentes_por_lp = [str(value) for value in linha_ano.iloc[0, 1:-1].values]
                    plt.figure()
                    plt.plot(local_picada, [int(value) for value in acidentes_por_lp], marker='o', color='#325c74')
                    plt.xlabel('Local da picada')
                    plt.ylabel('Número de Acidentes')
                    plt.xticks(rotation=45)
                    plt.grid(axis='y')
                    st.pyplot(plt)
                    st.dataframe(linha_ano)

                    if st.checkbox('Mostrar detalhes adicionais'):
                        st.write('Comparação do número de acidentes por local da picada entre os anos 2020 a 2023.')

                        # Definindo os anos
                        ano1 = 2020
                        ano2 = 2021
                        ano3 = 2022
                        ano4 = 2023

                        # Filtrando os dados por ano
                        linha_ano1 = df7[df7['Ano'] == str(ano1)]
                        linha_ano2 = df7[df7['Ano'] == str(ano2)]
                        linha_ano3 = df7[df7['Ano'] == str(ano3)]
                        linha_ano4 = df7[df7['Ano'] == str(ano4)]

                        # Locais da picada
                        local_picada = linha_ano1.columns[1:-1]

                        # Coletando os dados por local de picada
                        acidentes_ano1 = [int(value) for value in linha_ano1.iloc[0, 1:-1].values]
                        acidentes_ano2 = [int(value) for value in linha_ano2.iloc[0, 1:-1].values]
                        acidentes_ano3 = [int(value) for value in linha_ano3.iloc[0, 1:-1].values]
                        acidentes_ano4 = [int(value) for value in linha_ano4.iloc[0, 1:-1].values]

                        # Posições das barras
                        import numpy as np
                        x = np.arange(len(local_picada))  # posições dos locais de picada
                        largura = 0.2  # largura de cada barra

                        # Cores definidas para cada ano
                        cor_ano1 = '#325c74'  # azul
                        cor_ano2 = '#b8a99a'  # laranja
                        cor_ano3 = '#70866f'  # verde
                        cor_ano4 = '#e4d9c4'  # vermelho

                        # Criar figura
                        plt.figure(figsize=(12, 6))
                        plt.bar(x - 1.5*largura, acidentes_ano1, width=largura, label=f'{ano1}', color=cor_ano1)
                        plt.bar(x - 0.5*largura, acidentes_ano2, width=largura, label=f'{ano2}', color=cor_ano2)
                        plt.bar(x + 0.5*largura, acidentes_ano3, width=largura, label=f'{ano3}', color=cor_ano3)
                        plt.bar(x + 1.5*largura, acidentes_ano4, width=largura, label=f'{ano4}', color=cor_ano4)

                        plt.xlabel('Local da Picada')
                        plt.ylabel('Número de Acidentes')
                        plt.title('Número de Acidentes por Local da Picada (2020–2023)')
                        plt.xticks(x, local_picada, rotation=45)
                        plt.legend()
                        plt.grid(axis='y')

                        st.pyplot(plt)

                        # Criar DataFrame para comparação
                        dados_comparacao = pd.DataFrame({
                            'Local da Picada': local_picada,
                            f'Acidentes {ano1}': acidentes_ano1,
                            f'Acidentes {ano2}': acidentes_ano2,
                            f'Acidentes {ano3}': acidentes_ano3,
                            f'Acidentes {ano4}': acidentes_ano4
                        })

                        st.dataframe(dados_comparacao)
        if opcao3 == "Tipo de Acidente":
                    ano = 2023
                    linha_ano = df8[df8['Ano'] == str(ano)]  # Filtra a linha correspondente ao ano (convertendo ano para string)
                    tipo_acidente = linha_ano.columns[1:-1] 
                    acidentes_por_ta = [str(value) for value in linha_ano.iloc[0, 1:-1].values]
                    plt.figure(figsize=(10, 5))
                    plt.bar(tipo_acidente, [int(value) for value in acidentes_por_ta], color='#325c74')  # Converte de volta para int para o gráfico
                    plt.title(f'Número de Acidentes por Tipo de Acidente em {ano}')
                    plt.xlabel('Tipo de acidente')
                    plt.ylabel('Número de Acidentes')
                    plt.xticks(rotation=45)
                    plt.grid(axis='y')
                    st.pyplot(plt)
                    st.dataframe(linha_ano)

                    if st.checkbox('Mostrar detalhes adicionais'):
                        st.write('Comparação do número de acidentes por tipo de acidente entre os anos 2020 a 2023.')

                        # Definindo os anos
                        ano1 = 2020
                        ano2 = 2021
                        ano3 = 2022
                        ano4 = 2023

                        # Filtrando os dados por ano
                        linha_ano1 = df8[df8['Ano'] == str(ano1)]
                        linha_ano2 = df8[df8['Ano'] == str(ano2)]
                        linha_ano3 = df8[df8['Ano'] == str(ano3)]
                        linha_ano4 = df8[df8['Ano'] == str(ano4)]

                        # Tipos de acidente
                        tipo_acidente = linha_ano1.columns[1:-1]

                        # Coletando os dados por tipo de acidente
                        acidentes_ano1 = [int(value) for value in linha_ano1.iloc[0, 1:-1].values]
                        acidentes_ano2 = [int(value) for value in linha_ano2.iloc[0, 1:-1].values]
                        acidentes_ano3 = [int(value) for value in linha_ano3.iloc[0, 1:-1].values]
                        acidentes_ano4 = [int(value) for value in linha_ano4.iloc[0, 1:-1].values]

                        # Posições das barras
                        import numpy as np
                        x = np.arange(len(tipo_acidente))  # posições dos tipos de acidente
                        largura = 0.2  # largura de cada barra

                        # Cores definidas para cada ano
                        cor_ano1 = '#325c74'  # azul
                        cor_ano2 = '#b8a99a'  # laranja
                        cor_ano3 = '#70866f'  # verde
                        cor_ano4 = '#e4d9c4'  # vermelho

                        # Criar figura
                        plt.figure(figsize=(12, 6))
                        plt.bar(x - 1.5*largura, acidentes_ano1, width=largura, label=f'{ano1}', color=cor_ano1)
                        plt.bar(x - 0.5*largura, acidentes_ano2, width=largura, label=f'{ano2}', color=cor_ano2)
                        plt.bar(x + 0.5*largura, acidentes_ano3, width=largura, label=f'{ano3}', color=cor_ano3)
                        plt.bar(x + 1.5*largura, acidentes_ano4, width=largura, label=f'{ano4}', color=cor_ano4)

                        plt.xlabel('Tipo de Acidente')
                        plt.ylabel('Número de Acidentes')
                        plt.title('Número de Acidentes por Tipo de Acidente (2020–2023)')
                        plt.xticks(x, tipo_acidente, rotation=45)
                        plt.legend()
                        plt.grid(axis='y')

                        st.pyplot(plt)

                        # Criar DataFrame para comparação
                        dados_comparacao = pd.DataFrame({
                            'Tipo de Acidente': tipo_acidente,
                            f'Acidentes {ano1}': acidentes_ano1,
                            f'Acidentes {ano2}': acidentes_ano2,
                            f'Acidentes {ano3}': acidentes_ano3,
                            f'Acidentes {ano4}': acidentes_ano4
                        })

                        st.dataframe(dados_comparacao)
        if opcao3 == "Evolução do caso":
                    ano = 2023
                    linha_ano = df9[df9['Ano'] == str(ano)]  # Filtra a linha correspondente ao ano (convertendo ano para string)
                    evolucao = linha_ano.columns[1:-1] 
                    acidentes_por_evolucao = [str(value) for value in linha_ano.iloc[0, 1:-1].values]
                    plt.figure(figsize=(10, 5))
                    plt.fill_between(evolucao, [int(value) for value in acidentes_por_evolucao], color='#325c74', alpha=0.5)
                    plt.plot(evolucao, [int(value) for value in acidentes_por_evolucao], marker='o', color='#325c74')  # Adiciona a linha acima da área preenchida
                    plt.title(f'Número de Acidentes por Evolução do caso em {ano}')
                    plt.xlabel('Faixa Etária')
                    plt.ylabel('Número de Acidentes')
                    plt.xticks(rotation=45)
                    plt.grid(axis='y')
                    st.pyplot(plt)
                    st.dataframe(linha_ano)

                    if st.checkbox('Mostrar detalhes adicionais'):
                        st.write('Comparação do número de acidentes por evolução do caso entre os anos 2020 a 2023.')

                        # Definindo os anos
                        ano1 = 2020
                        ano2 = 2021
                        ano3 = 2022
                        ano4 = 2023

                        # Filtrando os dados por ano
                        linha_ano1 = df9[df9['Ano'] == str(ano1)]
                        linha_ano2 = df9[df9['Ano'] == str(ano2)]
                        linha_ano3 = df9[df9['Ano'] == str(ano3)]
                        linha_ano4 = df9[df9['Ano'] == str(ano4)]

                        # Evoluções do caso
                        evolucao = linha_ano1.columns[1:-1]

                        # Coletando os dados por evolução do caso
                        acidentes_ano1 = [int(value) for value in linha_ano1.iloc[0, 1:-1].values]
                        acidentes_ano2 = [int(value) for value in linha_ano2.iloc[0, 1:-1].values]
                        acidentes_ano3 = [int(value) for value in linha_ano3.iloc[0, 1:-1].values]
                        acidentes_ano4 = [int(value) for value in linha_ano4.iloc[0, 1:-1].values]

                        # Posições das barras
                        import numpy as np
                        x = np.arange(len(evolucao))  # posições das evoluções do caso
                        largura = 0.2  # largura de cada barra

                        # Cores definidas para cada ano
                        cor_ano1 = '#325c74'  # azul
                        cor_ano2 = '#b8a99a'  # laranja
                        cor_ano3 = '#70866f'  # verde
                        cor_ano4 = '#e4d9c4'  # vermelho

                        # Criar figura
                        plt.figure(figsize=(12, 6))
                        plt.bar(x - 1.5*largura, acidentes_ano1, width=largura, label=f'{ano1}', color=cor_ano1)
                        plt.bar(x - 0.5*largura, acidentes_ano2, width=largura, label=f'{ano2}', color=cor_ano2)
                        plt.bar(x + 0.5*largura, acidentes_ano3, width=largura, label=f'{ano3}', color=cor_ano3)
                        plt.bar(x + 1.5*largura, acidentes_ano4, width=largura, label=f'{ano4}', color=cor_ano4)

                        plt.xlabel('Evolução do Caso')
                        plt.ylabel('Número de Acidentes')
                        plt.title('Número de Acidentes por Evolução do Caso (2020–2023)')
                        plt.xticks(x, evolucao, rotation=45)
                        plt.legend()
                        plt.grid(axis='y')

                        st.pyplot(plt)

                        # Criar DataFrame para comparação
                        dados_comparacao = pd.DataFrame({
                            'Evolução do Caso': evolucao,
                            f'Acidentes {ano1}': acidentes_ano1,
                            f'Acidentes {ano2}': acidentes_ano2,
                            f'Acidentes {ano3}': acidentes_ano3,
                            f'Acidentes {ano4}': acidentes_ano4
                        })

                        st.dataframe(dados_comparacao)
if opcao2 == "2022":
        if opcao3 == "Número de Acidentes por Mês":      
                    ano = 2022
                    linha_ano = df[df['Ano'] == str(ano)]  # Filtra a linha correspondente ao ano (convertendo ano para string)
                    meses = linha_ano.columns[1:-1] 
                    acidentes_por_mes = [str(value) for value in linha_ano.iloc[0, 1:-1].values]
                    # Criando gráfico interativo com Plotly
                    plt.figure(figsize=(10, 5))
                    plt.plot(meses, [int(value) for value in acidentes_por_mes], marker='o', color='#325c74')  # Gráfico de linhas com marcadores
                    plt.title(f'Número de Acidentes por Mês em {ano}')
                    plt.xlabel('Meses')
                    plt.ylabel('Número de Acidentes')
                    plt.xticks(rotation=45)
                    plt.grid(axis='y')
                    st.pyplot(plt)
                    st.dataframe(linha_ano)
        if opcao3 == "Região de Notificação":
                    ano = 2022
                    linha_ano = df2[df2['Ano'] == str(ano)]  # Filtra a linha correspondente ao ano (convertendo ano para string)
                    regioes = linha_ano.columns[1:-1] 
                    acidentes_por_regiao = [str(value) for value in linha_ano.iloc[0, 1:-1].values]
                    plt.figure(figsize=(10, 5))
                    plt.bar(regioes, [int(value) for value in acidentes_por_regiao], color='#325c74')  # Converte de volta para int para o gráfico
                    plt.title(f'Número de Acidentes por Região de Notificação em {ano}')
                    plt.xlabel('Regiões')
                    plt.ylabel('Número de Acidentes')
                    plt.xticks(rotation=45)
                    plt.grid(axis='y')
                    st.pyplot(plt)
                    st.dataframe(linha_ano)
        if opcao3 == "Taxa de cura por Faixa Etária":
                    ano = 2022
                    linha_ano = df3[df3['Ano'] == str(ano)]  # Filtra a linha correspondente ao ano (convertendo ano para string)
                    idades = linha_ano.columns[1:-1] 
                    acidentes_por_idade = [str(value) for value in linha_ano.iloc[0, 1:-1].values]
                    plt.figure(figsize=(10, 5))
                    plt.fill_between(idades, [int(value) for value in acidentes_por_idade], color='#325c74', alpha=0.5)
                    plt.plot(idades, [int(value) for value in acidentes_por_idade], marker='o', color='#325c74')  # Adiciona a linha acima da área preenchida
                    plt.title(f'Número de Acidentes por Faixa Etária em {ano}')
                    plt.xlabel('Faixa Etária')
                    plt.ylabel('Número de Acidentes')
                    plt.xticks(rotation=45)
                    plt.grid(axis='y')
                    st.pyplot(plt)
                    st.dataframe(linha_ano)
        if opcao3 == "Tempo Picada/Atendimento":
                    ano = 2022
                    linha_ano = df4[df4['Ano'] == str(ano)]
                    tempos = linha_ano.columns[1:-1]
                    acidentes_por_tempo =  [str(value) for value in linha_ano.iloc[0, 1:-1].values]
                    plt.figure(figsize=(10,5))
                    plt.plot(tempos, [int(value) for value in acidentes_por_tempo], marker='o', color='#325c74')
                    plt.title('Número de acidentes por Tempo de Atendimento')
                    plt.xlabel('Tempo de Atendimento')
                    plt.ylabel('Número de Acidentes')
                    plt.xticks(rotation=50)
                    plt.grid(axis='y')
                    st.pyplot(plt)
                    st.dataframe(linha_ano)
        if opcao3 == "Tipo da Serpente":
                    ano = 2022
                    linha_ano = df5[df5['Ano'] == str(ano)]  # Filtra a linha correspondente ao ano (convertendo ano para string)
                    serpente = linha_ano.columns[1:-1] 
                    acidentes_por_ts = [str(value) for value in linha_ano.iloc[0, 1:-1].values]
                    plt.figure(figsize=(10, 5))
                    plt.bar(serpente, [int(value) for value in acidentes_por_ts], color='#325c74')  # Converte de volta para int para o gráfico
                    plt.title(f'Número de Acidentes por Tipo da Serpente em {ano}')
                    plt.xlabel('Regiões')
                    plt.ylabel('Número de Acidentes')
                    plt.xticks(rotation=45)
                    plt.grid(axis='y')
                    st.pyplot(plt)
                    st.dataframe(linha_ano)
        if opcao3 == "Tipo da Aranha":
                    ano = 2022
                    linha_ano = df6[df6['Ano'] == str(ano)]  # Filtra a linha correspondente ao ano (convertendo ano para string)
                    aranha = linha_ano.columns[1:-1] 
                    acidentes_por_ta = [str(value) for value in linha_ano.iloc[0, 1:-1].values]
                    plt.figure(figsize=(10, 5))
                    plt.fill_between(aranha, [int(value) for value in acidentes_por_ta], color='#325c74', alpha=0.5)
                    plt.plot(aranha, [int(value) for value in acidentes_por_ta], marker='o', color='#325c74')  # Adiciona a linha acima da área preenchida
                    plt.title(f'Número de Acidentes por Tipo da Aranha em {ano}')
                    plt.xlabel('Faixa Etária')
                    plt.ylabel('Número de Acidentes')
                    plt.xticks(rotation=45)
                    plt.grid(axis='y')
                    st.pyplot(plt)
                    st.dataframe(linha_ano)

                    imagem1 = Image.open('imagens/phoneutria.jpg').resize((250, 150))
                    imagem2 = Image.open('imagens/loxosceles.jpg').resize((250, 150))
                    imagem3 = Image.open('imagens/latrodexus.jpg').resize((250, 150))

                        # Cria duas colunas
                    col1, col2, col3 = st.columns(3)

                        # Mostra cada imagem em sua coluna
                    with col1:
                        st.image(imagem1, caption='Phoneutria')

                    with col2:
                        st.image(imagem2, caption='Loxosceles')
                        
                    with col3:
                            st.image(imagem3, caption='Latrodectus')
        if opcao3 == "Local da picada":
                    ano = 2022
                    linha_ano = df7[df7['Ano'] == str(ano)]
                    local_picada = linha_ano.columns[1:-1]
                    acidentes_por_lp = [str(value) for value in linha_ano.iloc[0, 1:-1].values]
                    plt.figure()
                    plt.plot(local_picada, [int(value) for value in acidentes_por_lp], marker='o', color='#325c74')
                    plt.xlabel('Local da picada')
                    plt.ylabel('Número de Acidentes')
                    plt.xticks(rotation=45)
                    plt.grid(axis='y')
                    st.pyplot(plt)
                    st.dataframe(linha_ano)
        if opcao3 == "Tipo de Acidente":
                    ano = 2022
                    linha_ano = df8[df8['Ano'] == str(ano)]  # Filtra a linha correspondente ao ano (convertendo ano para string)
                    tipo_acidente = linha_ano.columns[1:-1] 
                    acidentes_por_ta = [str(value) for value in linha_ano.iloc[0, 1:-1].values]
                    plt.figure(figsize=(10, 5))
                    plt.bar(tipo_acidente, [int(value) for value in acidentes_por_ta], color='#325c74')  # Converte de volta para int para o gráfico
                    plt.title(f'Número de Acidentes por Tipo de Acidente em {ano}')
                    plt.xlabel('Tipo de acidente')
                    plt.ylabel('Número de Acidentes')
                    plt.xticks(rotation=45)
                    plt.grid(axis='y')
                    st.pyplot(plt)
                    st.dataframe(linha_ano)
        if opcao3 == "Evolução do caso":
                    ano = 2022
                    linha_ano = df9[df9['Ano'] == str(ano)]  # Filtra a linha correspondente ao ano (convertendo ano para string)
                    evolucao = linha_ano.columns[1:-1] 
                    acidentes_por_evolucao = [str(value) for value in linha_ano.iloc[0, 1:-1].values]
                    plt.figure(figsize=(10, 5))
                    plt.fill_between(evolucao, [int(value) for value in acidentes_por_evolucao], color='#325c74', alpha=0.5)
                    plt.plot(evolucao, [int(value) for value in acidentes_por_evolucao], marker='o', color='#325c74')  # Adiciona a linha acima da área preenchida
                    plt.title(f'Número de Acidentes por Evolução do caso em {ano}')
                    plt.xlabel('Faixa Etária')
                    plt.ylabel('Número de Acidentes')
                    plt.xticks(rotation=45)
                    plt.grid(axis='y')
                    st.pyplot(plt)
                    st.dataframe(linha_ano)
if opcao2 == "2021":
        if opcao3 == "Número de Acidentes por Mês":      
                    ano = 2021
                    linha_ano = df[df['Ano'] == str(ano)]  # Filtra a linha correspondente ao ano (convertendo ano para string)
                    meses = linha_ano.columns[1:-1] 
                    acidentes_por_mes = [str(value) for value in linha_ano.iloc[0, 1:-1].values]
                    # Criando gráfico interativo com Plotly
                    plt.figure(figsize=(10, 5))
                    plt.plot(meses, [int(value) for value in acidentes_por_mes], marker='o', color='#325c74')  # Gráfico de linhas com marcadores
                    plt.title(f'Número de Acidentes por Mês em {ano}')
                    plt.xlabel('Meses')
                    plt.ylabel('Número de Acidentes')
                    plt.xticks(rotation=45)
                    plt.grid(axis='y')
                    st.pyplot(plt)
                    st.dataframe(linha_ano)
        if opcao3 == "Região de Notificação":
                    ano = 2021
                    linha_ano = df2[df2['Ano'] == str(ano)]  # Filtra a linha correspondente ao ano (convertendo ano para string)
                    regioes = linha_ano.columns[1:-1] 
                    acidentes_por_regiao = [str(value) for value in linha_ano.iloc[0, 1:-1].values]
                    plt.figure(figsize=(10, 5))
                    plt.bar(regioes, [int(value) for value in acidentes_por_regiao], color='#325c74')  # Converte de volta para int para o gráfico
                    plt.title(f'Número de Acidentes por Região de Notificação em {ano}')
                    plt.xlabel('Regiões')
                    plt.ylabel('Número de Acidentes')
                    plt.xticks(rotation=45)
                    plt.grid(axis='y')
                    st.pyplot(plt)
                    st.dataframe(linha_ano)
        if opcao3 == "Taxa de cura por Faixa Etária":
                    ano = 2021
                    linha_ano = df3[df3['Ano'] == str(ano)]  # Filtra a linha correspondente ao ano (convertendo ano para string)
                    idades = linha_ano.columns[1:-1] 
                    acidentes_por_idade = [str(value) for value in linha_ano.iloc[0, 1:-1].values]
                    plt.figure(figsize=(10, 5))
                    plt.fill_between(idades, [int(value) for value in acidentes_por_idade], color='#325c74', alpha=0.5)
                    plt.plot(idades, [int(value) for value in acidentes_por_idade], marker='o', color='#325c74')  # Adiciona a linha acima da área preenchida
                    plt.title(f'Número de Acidentes por Faixa Etária em {ano}')
                    plt.xlabel('Faixa Etária')
                    plt.ylabel('Número de Acidentes')
                    plt.xticks(rotation=45)
                    plt.grid(axis='y')
                    st.pyplot(plt)
                    st.dataframe(linha_ano)
        if opcao3 == "Tempo Picada/Atendimento":
                    ano = 2021
                    linha_ano = df4[df4['Ano'] == str(ano)]
                    tempos = linha_ano.columns[1:-1]
                    acidentes_por_tempo =  [str(value) for value in linha_ano.iloc[0, 1:-1].values]
                    plt.figure(figsize=(10,5))
                    plt.plot(tempos, [int(value) for value in acidentes_por_tempo], marker='o', color='#325c74')
                    plt.title('Número de acidentes por Tempo de Atendimento')
                    plt.xlabel('Tempo de Atendimento')
                    plt.ylabel('Número de Acidentes')
                    plt.xticks(rotation=50)
                    plt.grid(axis='y')
                    st.pyplot(plt)
                    st.dataframe(linha_ano)
        if opcao3 == "Tipo da Serpente":
                    ano = 2021
                    linha_ano = df5[df5['Ano'] == str(ano)]  # Filtra a linha correspondente ao ano (convertendo ano para string)
                    serpente = linha_ano.columns[1:-1] 
                    acidentes_por_ts = [str(value) for value in linha_ano.iloc[0, 1:-1].values]
                    plt.figure(figsize=(10, 5))
                    plt.bar(serpente, [int(value) for value in acidentes_por_ts], color='#325c74')  # Converte de volta para int para o gráfico
                    plt.title(f'Número de Acidentes por Tipo da Serpente em {ano}')
                    plt.xlabel('Regiões')
                    plt.ylabel('Número de Acidentes')
                    plt.xticks(rotation=45)
                    plt.grid(axis='y')
                    st.pyplot(plt)
                    st.dataframe(linha_ano)
        if opcao3 == "Tipo da Aranha":
                    ano = 2021
                    linha_ano = df6[df6['Ano'] == str(ano)]  # Filtra a linha correspondente ao ano (convertendo ano para string)
                    aranha = linha_ano.columns[1:-1] 
                    acidentes_por_ta = [str(value) for value in linha_ano.iloc[0, 1:-1].values]
                    plt.figure(figsize=(10, 5))
                    plt.fill_between(aranha, [int(value) for value in acidentes_por_ta], color='#325c74', alpha=0.5)
                    plt.plot(aranha, [int(value) for value in acidentes_por_ta], marker='o', color='#325c74')  # Adiciona a linha acima da área preenchida
                    plt.title(f'Número de Acidentes por Tipo da Aranha em {ano}')
                    plt.xlabel('Faixa Etária')
                    plt.ylabel('Número de Acidentes')
                    plt.xticks(rotation=45)
                    plt.grid(axis='y')
                    st.pyplot(plt)
                    st.dataframe(linha_ano)

                    imagem1 = Image.open('imagens/phoneutria.jpg').resize((250, 150))
                    imagem2 = Image.open('imagens/loxosceles.jpg').resize((250, 150))
                    imagem3 = Image.open('imagens/latrodexus.jpg').resize((250, 150))

                        # Cria duas colunas
                    col1, col2, col3 = st.columns(3)

                        # Mostra cada imagem em sua coluna
                    with col1:
                        st.image(imagem1, caption='Phoneutria')

                    with col2:
                        st.image(imagem2, caption='Loxosceles')
                        
                    with col3:
                            st.image(imagem3, caption='Latrodectus')
        if opcao3 == "Local da picada":
                    ano = 2021
                    linha_ano = df7[df7['Ano'] == str(ano)]
                    local_picada = linha_ano.columns[1:-1]
                    acidentes_por_lp = [str(value) for value in linha_ano.iloc[0, 1:-1].values]
                    plt.figure()
                    plt.plot(local_picada, [int(value) for value in acidentes_por_lp], marker='o', color='#325c74')
                    plt.xlabel('Local da picada')
                    plt.ylabel('Número de Acidentes')
                    plt.xticks(rotation=45)
                    plt.grid(axis='y')
                    st.pyplot(plt)
                    st.dataframe(linha_ano)
        if opcao3 == "Tipo de Acidente":
                    ano = 2021
                    linha_ano = df8[df8['Ano'] == str(ano)]  # Filtra a linha correspondente ao ano (convertendo ano para string)
                    tipo_acidente = linha_ano.columns[1:-1] 
                    acidentes_por_ta = [str(value) for value in linha_ano.iloc[0, 1:-1].values]
                    plt.figure(figsize=(10, 5))
                    plt.bar(tipo_acidente, [int(value) for value in acidentes_por_ta], color='#325c74')  # Converte de volta para int para o gráfico
                    plt.title(f'Número de Acidentes por Tipo de Acidente em {ano}')
                    plt.xlabel('Tipo de acidente')
                    plt.ylabel('Número de Acidentes')
                    plt.xticks(rotation=45)
                    plt.grid(axis='y')
                    st.pyplot(plt)
                    st.dataframe(linha_ano)
        if opcao3 == "Evolução do caso":
                    ano = 2021
                    linha_ano = df9[df9['Ano'] == str(ano)]  # Filtra a linha correspondente ao ano (convertendo ano para string)
                    evolucao = linha_ano.columns[1:-1] 
                    acidentes_por_evolucao = [str(value) for value in linha_ano.iloc[0, 1:-1].values]
                    plt.figure(figsize=(10, 5))
                    plt.fill_between(evolucao, [int(value) for value in acidentes_por_evolucao], color='#325c74', alpha=0.5)
                    plt.plot(evolucao, [int(value) for value in acidentes_por_evolucao], marker='o', color='#325c74')  # Adiciona a linha acima da área preenchida
                    plt.title(f'Número de Acidentes por Evolução do caso em {ano}')
                    plt.xlabel('Faixa Etária')
                    plt.ylabel('Número de Acidentes')
                    plt.xticks(rotation=45)
                    plt.grid(axis='y')
                    st.pyplot(plt)
                    st.dataframe(linha_ano)
if opcao2 == "2020":
        if opcao3 == "Número de Acidentes por Mês":      
                    ano = 2020
                    linha_ano = df[df['Ano'] == str(ano)]  # Filtra a linha correspondente ao ano (convertendo ano para string)
                    meses = linha_ano.columns[1:-1] 
                    acidentes_por_mes = [str(value) for value in linha_ano.iloc[0, 1:-1].values]
                    # Criando gráfico interativo com Plotly
                    plt.figure(figsize=(10, 5))
                    plt.plot(meses, [int(value) for value in acidentes_por_mes], marker='o', color='#325c74')  # Gráfico de linhas com marcadores
                    plt.title(f'Número de Acidentes por Mês em {ano}')
                    plt.xlabel('Meses')
                    plt.ylabel('Número de Acidentes')
                    plt.xticks(rotation=45)
                    plt.grid(axis='y')
                    st.pyplot(plt)
                    st.dataframe(linha_ano)
        if opcao3 == "Região de Notificação":
                    ano = 2020
                    linha_ano = df2[df2['Ano'] == str(ano)]  # Filtra a linha correspondente ao ano (convertendo ano para string)
                    regioes = linha_ano.columns[1:-1] 
                    acidentes_por_regiao = [str(value) for value in linha_ano.iloc[0, 1:-1].values]
                    plt.figure(figsize=(10, 5))
                    plt.bar(regioes, [int(value) for value in acidentes_por_regiao], color='#325c74')  # Converte de volta para int para o gráfico
                    plt.title(f'Número de Acidentes por Região de Notificação em {ano}')
                    plt.xlabel('Regiões')
                    plt.ylabel('Número de Acidentes')
                    plt.xticks(rotation=45)
                    plt.grid(axis='y')
                    st.pyplot(plt)
                    st.dataframe(linha_ano)
        if opcao3 == "Taxa de cura por Faixa Etária":
                    ano = 2020
                    linha_ano = df3[df3['Ano'] == str(ano)]
                    idades = linha_ano.columns[1:-1] 
                    acidentes_por_idade = [str(value) for value in linha_ano.iloc[0, 1:-1].values]
                    plt.figure(figsize=(10, 5))
                    plt.fill_between(idades, [int(value) for value in acidentes_por_idade], color='#325c74', alpha=0.5)
                    plt.plot(idades, [int(value) for value in acidentes_por_idade], marker='o', color='#325c74') 
                    plt.title(f'Número de Acidentes por Faixa Etária em {ano}')
                    plt.xlabel('Faixa Etária')
                    plt.ylabel('Número de Acidentes')
                    plt.xticks(rotation=45)
                    plt.grid(axis='y')
                    st.pyplot(plt)
                    st.dataframe(linha_ano)
        if opcao3 == "Tempo Picada/Atendimento":
                    ano = 2020
                    linha_ano = df4[df4['Ano'] == str(ano)]
                    tempos = linha_ano.columns[1:-1]
                    acidentes_por_tempo =  [str(value) for value in linha_ano.iloc[0, 1:-1].values]
                    plt.figure(figsize=(10,5))
                    plt.plot(tempos, [int(value) for value in acidentes_por_tempo], marker='o', color='#325c74')
                    plt.title('Número de acidentes por Tempo de Atendimento')
                    plt.xlabel('Tempo de Atendimento')
                    plt.ylabel('Número de Acidentes')
                    plt.xticks(rotation=50)
                    plt.grid(axis='y')
                    st.pyplot(plt)
                    st.dataframe(linha_ano)
        if opcao3 == "Tipo da Serpente":
                    ano = 2020
                    linha_ano = df5[df5['Ano'] == str(ano)]  # Filtra a linha correspondente ao ano (convertendo ano para string)
                    serpente = linha_ano.columns[1:-1] 
                    acidentes_por_ts = [str(value) for value in linha_ano.iloc[0, 1:-1].values]
                    plt.figure(figsize=(10, 5))
                    plt.bar(serpente, [int(value) for value in acidentes_por_ts], color='#325c74')  # Converte de volta para int para o gráfico
                    plt.title(f'Número de Acidentes por Tipo da Serpente em {ano}')
                    plt.xlabel('Regiões')
                    plt.ylabel('Número de Acidentes')
                    plt.xticks(rotation=45)
                    plt.grid(axis='y')
                    st.pyplot(plt)
                    st.dataframe(linha_ano)
        if opcao3 == "Tipo da Aranha":
                    ano = 2020
                    linha_ano = df6[df6['Ano'] == str(ano)]  # Filtra a linha correspondente ao ano (convertendo ano para string)
                    aranha = linha_ano.columns[1:-1] 
                    acidentes_por_ta = [str(value) for value in linha_ano.iloc[0, 1:-1].values]
                    plt.figure(figsize=(10, 5))
                    plt.fill_between(aranha, [int(value) for value in acidentes_por_ta], color='#325c74', alpha=0.5)
                    plt.plot(aranha, [int(value) for value in acidentes_por_ta], marker='o', color='#325c74')  # Adiciona a linha acima da área preenchida
                    plt.title(f'Número de Acidentes por Tipo da Aranha em {ano}')
                    plt.xlabel('Faixa Etária')
                    plt.ylabel('Número de Acidentes')
                    plt.xticks(rotation=45)
                    plt.grid(axis='y')
                    st.pyplot(plt)
                    st.dataframe(linha_ano)

                    imagem1 = Image.open('imagens/phoneutria.jpg').resize((250, 150))
                    imagem2 = Image.open('imagens/loxosceles.jpg').resize((250, 150))
                    imagem3 = Image.open('imagens/latrodexus.jpg').resize((250, 150))

                        # Cria duas colunas
                    col1, col2, col3 = st.columns(3)

                        # Mostra cada imagem em sua coluna
                    with col1:
                        st.image(imagem1, caption='Phoneutria')

                    with col2:
                        st.image(imagem2, caption='Loxosceles')
                        
                    with col3:
                            st.image(imagem3, caption='Latrodectus')
        if opcao3 == "Local da picada":
                    ano = 2020
                    linha_ano = df7[df7['Ano'] == str(ano)]
                    local_picada = linha_ano.columns[1:-1]
                    acidentes_por_lp = [str(value) for value in linha_ano.iloc[0, 1:-1].values]
                    plt.figure()
                    plt.plot(local_picada, [int(value) for value in acidentes_por_lp], marker='o', color='#325c74')
                    plt.xlabel('Local da picada')
                    plt.ylabel('Número de Acidentes')
                    plt.xticks(rotation=45)
                    plt.grid(axis='y')
                    st.pyplot(plt)
                    st.dataframe(linha_ano)
        if opcao3 == "Tipo de Acidente":
                ano = 2020
                linha_ano = df8[df8['Ano'] == str(ano)]  # Filtra a linha correspondente ao ano (convertendo ano para string)
                tipo_acidente = linha_ano.columns[1:-1] 
                acidentes_por_ta = [str(value) for value in linha_ano.iloc[0, 1:-1].values]
                plt.figure(figsize=(10, 5))
                plt.bar(tipo_acidente, [int(value) for value in acidentes_por_ta], color='#325c74')  # Converte de volta para int para o gráfico
                plt.title(f'Número de Acidentes por Tipo de Acidente em {ano}')
                plt.xlabel('Tipo de acidente')
                plt.ylabel('Número de Acidentes')
                plt.xticks(rotation=45)
                plt.grid(axis='y')
                st.pyplot(plt)
                st.dataframe(linha_ano)
        if opcao3 == "Evolução do caso":
                    ano = 2020
                    linha_ano = df9[df9['Ano'] == str(ano)]  # Filtra a linha correspondente ao ano (convertendo ano para string)
                    evolucao = linha_ano.columns[1:-1] 
                    acidentes_por_evolucao = [str(value) for value in linha_ano.iloc[0, 1:-1].values]
                    plt.figure(figsize=(10, 5))
                    plt.fill_between(evolucao, [int(value) for value in acidentes_por_evolucao], color='#325c74', alpha=0.5)
                    plt.plot(evolucao, [int(value) for value in acidentes_por_evolucao], marker='o', color='#325c74')  # Adiciona a linha acima da área preenchida
                    plt.title(f'Número de Acidentes por Evolução do caso em {ano}')
                    plt.xlabel('Faixa Etária')
                    plt.ylabel('Número de Acidentes')
                    plt.xticks(rotation=45)
                    plt.grid(axis='y')
                    st.pyplot(plt)
                    st.dataframe(linha_ano)

st.markdown("---")
st.markdown("© 2025 - Desenvolvido por Fábio Matheus Spindola da Cunha")
st.markdown("Departamento de Engenharia Biomédica")
