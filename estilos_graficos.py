# Grafico de area

plt.figure(figsize=(10, 5))
plt.fill_between(meses, [int(value) for value in acidentes_por_mes], color='green', alpha=0.5)
plt.plot(meses, [int(value) for value in acidentes_por_mes], marker='o', color='green')  # Adiciona a linha acima da área preenchida
plt.title(f'Número de Acidentes por Mês em {ano}')
plt.xlabel('Meses')
plt.ylabel('Número de Acidentes')
plt.xticks(rotation=45)
plt.grid(axis='y')

    st.pyplot(plt)

# Grafico de Pizza

plt.figure(figsize=(8, 8))
plt.pie([int(value) for value in acidentes_por_mes], labels=meses, autopct='%1.1f%%', startangle=90)
plt.title(f'Proporção de Acidentes por Mês em {ano}')
plt.axis('equal')  # Para garantir que o gráfico seja um círculo

st.pyplot(plt)

# Grafico de Linhas

plt.figure(figsize=(10, 5))
plt.plot(meses, [int(value) for value in acidentes_por_mes], marker='o', color='green')  # Gráfico de linhas com marcadores
plt.title(f'Número de Acidentes por Mês em {ano}')
plt.xlabel('Meses')
plt.ylabel('Número de Acidentes')
plt.xticks(rotation=45)
plt.grid(axis='y')
st.pyplot(plt)

# Grafico de Barras

            plt.figure(figsize=(10, 5))
            plt.bar(meses, [int(value) for value in acidentes_por_mes], color='green')  # Converte de volta para int para o gráfico
            plt.title(f'Número de Acidentes por Mês em {ano}')
            plt.xlabel('Meses')
            plt.ylabel('Número de Acidentes')
            plt.xticks(rotation=45)
            plt.grid(axis='y')
            st.pyplot(plt)