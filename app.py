import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go 
from plotly.subplots import make_subplots

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.float_format', lambda x: '%.2f' % x)




st.title('Análise COVID-19')

tab0, tab1, tab2, tab3 = st.tabs(["Introdução", "Vínculo Trabalhista vs Saúde", "Adoção do Trabalho Remoto", "Detalhamento Técnico"])

with tab0:
        '''
        # Introdução

        A pandemia de COVID-19, impactou drasticamente a sociedade em escala global. Este surto viral, originado em 2019, resultou em um impacto sem precedentes na saúde, na economia e na forma como as comunidades interagem e funcionam. Diversos setores foram afetados, contudo alguns com maior intesidade como saúde, economia, educação e bem-estar.

        Através da análise de dados é possível identificar indicadores fundamentais para o planejamento de ações e estratégias em futuros surtos. Insights derivados da análise podem ajudar a direcionar políticas de saúde pública, otimizar recursos e preparar medidas mais eficazes para mitigar o impacto em casos futuros, oferecendo uma base sólida para o planejamento e resposta a potenciais emergências. Para atingir este objetivo, foi utilizado a base PNAD-COVID-19 do IBGE (https://covid19.ibge.gov.br/pnad-covid/), sendo esta uma base confiável para compreender não apenas os aspectos de saúde, mas também dados sociais, econômicos e comportamentais. Além disso, também foi utilizada a base OpenDataSUS (https://opendatasus.saude.gov.br/) para um melhor entendimento da situação geral.

        O período selecionado para análise foram os meses de Maio, Junho e Julho de 2020, utilizando a quebra de semana para ter uma granularidade menor e possibilitar uma melhor visão.

        '''
with tab1: 
        '''
        # Vínculo Trabalhista vs Saúde
        Para entender um pouco mais do cenário da pandemia e a relação com vínculo trabalhista e também assuntos relacionados ao tratamento etc, seguem algumas análises.

        ## Análises e Ações Sugeridas
        
        Entre as pessoas que foram entrevistadas, qual a quantidade que trabalhou ou fez algum bico (por pelo menos uma hora) na semana passada?
        '''

        #Dados
        df_trabalhou_semana_passada = pd.read_csv('./dados/df_trabalhou_semana_passada.csv')
        df_sintomas = pd.read_csv('./dados/df_sintomas.csv')
        df_vinculo = pd.read_csv('./dados/df_vinculo.csv')
        df_sintomas_comuns = pd.read_csv('./dados/df_sintomas_comuns.csv')
        df_atitude_tomada = pd.read_csv('./dados/df_atitude_tomada.csv')
        df_remedio = pd.read_csv('./dados/df_remedio.csv')
        df_entubacao = pd.read_csv('./dados/df_entubacao.csv')
        df_plano_saude = pd.read_csv('./dados/df_plano_saude.csv')

        color_map = {'Sim': '#015fb7', 'Não': '#83c9ff'}

        #Trabalhou Semana Passada
        fig_trabalhou_semana_passada = go.Figure()
        fig_trabalhou_semana_passada = px.bar(df_trabalhou_semana_passada,
                x = 'Mes_Semana',
                y = 'Quantidade',
                color = 'Trabalhou_ou_fez_algum_bico_por_pelo_menos_uma_hora_na_semana_passada',
                color_discrete_map=color_map,
                barmode = 'group',  # Define o modo para 'group' para barras lado a lado
                labels = {'Trabalhou_ou_fez_algum_bico_por_pelo_menos_uma_hora_na_semana_passada': 'Trabalhou', 'Mes_Semana': 'Mês/Semana'},
                title = 'Quantidade de pessoas que trabalhou ou fez algum bico (por pelo menos uma hora) na semana passada'
                )
        st.plotly_chart(fig_trabalhou_semana_passada, use_container_width=True)

        '''
        Dentre esses que trabalharam ou fizeram algum bico (por pelo menos uma hora) na semana passada, quantos deles apresentaram sintomas?
        '''

        #Trabalhou Sintomas
        fig_sintomas = go.Figure()
        fig_sintomas = px.bar(df_sintomas,
                x = 'Mes_Semana',
                y = 'Quantidade',
                color = 'Teve_Sintomas',
                color_discrete_map=color_map,
                barmode = 'group',
                labels = {'Teve_Sintomas': 'Teve sintomas?', 'Mes_Semana': 'Mês/Semana'},
                title = 'Quantidade de pessoas que apresentaram algum sintoma entre as pessoas que trabalharam ou fizeram algum bico (por pelo menos uma hora) na semana passada'
                )
        st.plotly_chart(fig_sintomas, use_container_width=True)


        '''
        E desses, quais os tipos de vínculos trabalhistas mais comuns?
        '''

        #Vínculos
        fig_vinculo = go.Figure()
        fig_vinculo = px.bar(df_vinculo,
                x = 'Quantidade',
                y = 'Tipo_de_vinculo_trabalhista',
                title = 'Tipos de vínculo trabalhistas',
                )
        st.plotly_chart(fig_vinculo, use_container_width=True)


        '''
        Ainda entre esses que apresentaram sintomas, quais foram os sintomas mais comuns?
        '''
        #Sintomas Comuns
        fig_sintomas_comuns = go.Figure()
        fig_sintomas_comuns = px.bar(df_sintomas_comuns,
                x = 'Quantidade',
                y = 'Sintomas',
                title = 'Quantidade de pessoas que apresentaram cada sintoma'
                )
        st.plotly_chart(fig_sintomas_comuns, use_container_width=True)

        '''
        E qual a atitude que essas pessoas tomaram?
        '''

        #Atitude Tomada
        fig_atitude_tomada = go.Figure()
        fig_atitude_tomada = px.bar(df_atitude_tomada,
                x = 'Mes_Semana',
                y = 'Quantidade',
                color = 'Casa',
                color_discrete_map=color_map,
                barmode = 'relative',  # Define o modo para 'group' para barras lado a lado
                labels = {'Mes_Semana': 'Mês/Semana', 'Casa': 'Apenas ficou em casa?'},
                title = 'Essa pessoa que apresentou sintomas apenas ficou em casa?'
                )
        st.plotly_chart(fig_atitude_tomada, use_container_width=True)


        '''
        Caso a pessoa não tenha apenas ficado em casa, ou seja, tenha procurado ajuda médica, ela comprou e/ou tomou remédios por orientação médica?
        '''
        #Remédio
        fig_remedio = go.Figure()
        fig_remedio = px.bar(df_remedio,
                x = 'Mes_Semana',
                y = 'Quantidade',
                color = 'Remedio',
                color_discrete_map=color_map,
                barmode = 'relative',  # Define o modo para 'group' para barras lado a lado
                labels = {'Mes_Semana': 'Mês/Semana', 'Remedio': 'Comprou e/ou tomou remédios por orientação médica?'},
                title = 'Quantidade de pessoas que foi a alguma unidade de saúde e tomou ou não remédios por orientação médica'
                )
        st.plotly_chart(fig_remedio, use_container_width=True)

        '''
        E das pessoas que procuraram alguma unidade de saúde e foram internadas por um dia ou mais, quantas foram sedadas, entubadas ou colocadas em respiração artificial com ventilador?
        '''
        #Entubacao
        fig_entubacao = go.Figure()
        fig_entubacao = px.bar(df_entubacao,
                x = 'Mes_Semana',
                y = 'Quantidade',
                color = 'Tratamento',
                color_discrete_map=color_map,
                barmode = 'relative',  # Define o modo para 'group' para barras lado a lado
                labels = {'Mes_Semana': 'Mês/Semana', 'Tratamento': 'A pessoa foi sedada/entubada/respiração artificial'},
                title = 'Quantidade de pessoas que procuraram alguma unidade de saúde, foram internadas por um dia ou mais e foram sedadas, entubadas ou colocadas em respiração artificial com ventilador'
                )
        st.plotly_chart(fig_entubacao, use_container_width=True)

        '''
        E dessas pessoas que foram sedadas, entubadas ou colocadas em respiração artificial com ventilador, quantas possuem plano de saúde?
        '''
        #Plano de Saúde
        fig_plano_saude = go.Figure()
        fig_plano_saude = px.bar(df_plano_saude,
                x = 'Mes_Semana',
                y = 'Quantidade',
                color = 'Plano_de_saude',
                color_discrete_map=color_map,
                barmode = 'relative',  # Define o modo para 'group' para barras lado a lado
                labels = {'Mes_Semana': 'Mês/Semana', 'Plano_de_saude': 'Tem plano de saúde?'},
                title = 'Quantidade de pessoas que possuem plano de saúde dentre as que foram internadas por um dia ou mais e foram sedadas, entubadas ou colocadas em respiração artificial com ventilador'
                )
        st.plotly_chart(fig_plano_saude, use_container_width=True)


        '''
        De maneira resumida, podemos observar que, nos meses analisados (Maio/Junho/Julho 2020), a maior parte das pessoas entrevistadas (em torno dos 60%, na maioria dos períodos) não havia trabalhado ou feito algum bico (por pelo menos uma hora) na semana anterior. Entre esses que haviam trabalhado, uma pequena parte (de 5 a 10%) apresentou algum dos seguintes sintomas: febre (22492), tosse (35708), dor de garganta (30244), perda de cheiro ou sabor (15888), dificuldade para respirar (14172), dor de cabeça (65384) ou dor muscular (34928). Importante lembrar que a pessoa pode apresentar mais de um sintoma simultaneamente.
        Entre esses, podemos observar que o vínculo trabalhista mais comum foi a contratação via CLT, seguido dos que trabalham por contra própria, empregados do setor público e trabalhadores domésticos. Apenas 2,70% dessas pessoas estavam fora do mercado de trabalho (faziam apenas afazeres domésticos, cuidados de pessoas ou produção para próprio consumo).
        E dentre as pessoas que apresentaram pelo menos um sintoma, a maioria optou por apenas ficar em casa, não procurando ajuda médica.
        Dentre esses que optaram por procurar ajuda médica, a maioria acabou não comprando e/ou tomando remédios por orientação médica.
        Por outro lado, algumas pessoas procuraram unidades de saúde e acabaram sendo internadas por um dia ou mais, mas também uma minoria.
        Dentre essas que foram internadas, também uma pequena parte acabou sendo sedada, entubada ou colocada em respiração artificial com ventilador.
        Dessas, a maioria não possui plano de saúde, ou seja, precisou ser atendida pelo SUS (Sistema Único de Saúde).
        Com base nessas questões, caso aconteça um novo surto de COVID-19, algumas ações/medidas que o hospital pode adotar são:
        '''

        acoes = '''
        - Adotar um monitoramento constante dos sintomas da COVID na comunidade e na equipe que trabalha no hospital;
        - Seguir acompanhando a evolução do surto no passar do tempo;
        - Ter planos de contingência bem definidos para o caso de ocorrer um aumento rápido no número de casos;
        - Adotar campanhas que orientem a população em relação aos sintomas que podem ser apresentados (mais de um sintoma simultaneamente, inclusive), reforçando a importância da testagem e que a pessoa deve procurar ajuda médica ao apresentar sintomas mais severos;
        - Em parceria com o órgão governamental, dar suporte às pessoas em isolamento, garantindo que tenham as suas necessidades atendidas sem precisar sair de casa;
        - Facilitar o acesso a consultas médicas e exames, realizando testes em larga escala para conseguir identificar a maior quantidade de casos positivos, testando também as pessoas que eventualmente tiveram contato com aquelas em que o teste deu positivo;
        - Dar uma ajuda médica adequada às pessoas que procurarem atendimento;
        - Analisar os dados de maneira detalhada (ocupação laboral, condições de trabalho, etc) para compreender melhor possíveis padrões de disseminação da doença;
        - Identificar casos graves que necessitem de hospitalização com a maior rapidez possível;
        - Fortalecer a relação de colaboração com o SUS (Sistema Único de Saúde) para garantir que todas as pessoas tenham acesso à assistência médica necessária;
        - Preparar recursos adicionais (como leitos de UTI e equipamentos de respiração artificial, por exemplo), garantindo que não faltarão recursos para pacientes hospitalizados
        '''
        st.markdown(acoes)

with tab2:
        '''
        # Adoção do Trabalho Remoto

        A adoção do trabalho remoto foi uma das estratégias em resposta à pandemia de COVID-19, buscando reduzir a disseminação do vírus e minimizar a sobrecarga nos sistemas de saúde. A transição para o trabalho remoto teve um impacto significativo na dinâmica da sociedade, alterando a forma como as pessoas interagem em ambientes profissionais e, consequentemente, afetando a propagação do vírus.

        A análise do impacto do trabalho remoto na redução dos casos e óbitos de COVID-19 é fundamental para compreender como medidas como essa, voltadas para a diminuição da interação presencial, podem contribuir para a contenção de novos surtos. Esta análise pode fornecer insights valiosos para estratégias futuras, não apenas em potenciais novas ondas da COVID-19, mas também para outras emergências de saúde pública, demonstrando a importância de medidas não farmacêuticas na contenção de doenças altamente transmissíveis.

        ## Análises e Ações Sugeridas

        Para entender melhor o impacto, vamos começar analisando a situação da pandemia no período selecionado (05-07/2020)
        '''

        #Dados
        df_cenario_pandemia = pd.read_csv('./dados/df_cenario_pandemia.csv')
        df_home_office = pd.read_csv('./dados/df_home_office.csv')
        df_covid = pd.read_csv('./dados/df_covid.csv')


        #Casos
        fig_cenario_pandemia_casos = go.Figure()

        fig_cenario_pandemia_casos = px.line(df_cenario_pandemia, x='mes_semana', y=['casos'], labels={'value': 'Pessoas', 'mes_semana': 'Mês/Semana'}, title='Casos por Mês/Semana')
        fig_cenario_pandemia_casos.update_traces(line=dict(color='orange'))
        st.plotly_chart(fig_cenario_pandemia_casos, use_container_width=True)


        #Óbitos
        fig_cenario_pandemia_obitos = go.Figure()

        fig_cenario_pandemia_obitos = px.line(df_cenario_pandemia, x='mes_semana', y=['obitos'], labels={'value': 'Pessoas', 'mes_semana': 'Mês/Semana'}, title='Óbitos por Mês/Semana')
        fig_cenario_pandemia_obitos.update_traces(line=dict(color='red'))
        st.plotly_chart(fig_cenario_pandemia_obitos, use_container_width=True)


        '''
        Como pode ser visto, tanto os casos quanto os óbitos subiram de maneira similar, mas com escalas diferentes.
        '''

        #Caso e Óbitos
        fig_cenario_pandemia = go.Figure()

        fig_cenario_pandemia = px.line(df_cenario_pandemia, x='mes_semana', y=['casos', 'obitos'], labels={'value': 'Pessoas', 'mes_semana': 'Mês/Semana'}, title='Casos e Óbitos por Mês/Semana')
        fig_cenario_pandemia.update_traces(line=dict(color='orange'), selector=dict(name='casos'))
        fig_cenario_pandemia.update_traces(line=dict(color='red'), selector=dict(name='obitos'))
        st.plotly_chart(fig_cenario_pandemia, use_container_width=True)


        '''
        Analisando a adoção do trabalho remoto no mesmo período, infelizmente acabamos por não ver uma crescente, mas sim um pico que depois voltou a reduzir
        '''


        #Home Office
        fig_home_office = go.Figure()
        fig_home_office = px.line(df_home_office, x='mes_semana', y='trabalho_remoto', labels={'value': 'Pessoas', 'mes_semana': 'Mês/Semana'}, title='Trabalho Remoto por Mês/Semana')
        fig_home_office.update_traces(line=dict(color='blue', dash='dash'))
        st.plotly_chart(fig_home_office, use_container_width=True)

        '''
        Ao cruzar estes datasets, percebemos que a redução do trabalho remoto coincidiu com o aumento tanto de casos quanto de óbitos - destaque para os gráficos individuais onde a escala pode ser mais facilmente comparada
        '''

        #Casos vs Home Office
        fig_casos_home_office = go.Figure()

        fig_casos_home_office.add_trace(go.Scatter(x=df_covid['mes_semana'], y=df_covid['casos'], mode='lines', name='Casos', line=dict(color='orange')))
        fig_casos_home_office.add_trace(go.Scatter(x=df_covid['mes_semana'], y=df_covid['trabalho_remoto'], mode='lines', name='Trabalho Remoto', line=dict(color='blue', dash='dash'), yaxis='y2'))

        fig_casos_home_office.update_layout(
        title='Casos vs Trabalho Remoto',
        xaxis=dict(title='Mês/Semana'),
        yaxis=dict(title='Casos'),
        yaxis2=dict(title='Trabalho Remoto', overlaying='y', side='right')
        )
        st.plotly_chart(fig_casos_home_office, use_container_width=True)



        #Óbitos vs Home Office
        fig_obitos_home_office = go.Figure()

        fig_obitos_home_office.add_trace(go.Scatter(x=df_covid['mes_semana'], y=df_covid['obitos'], mode='lines', name='Óbitos', line=dict(color='red')))
        fig_obitos_home_office.add_trace(go.Scatter(x=df_covid['mes_semana'], y=df_covid['trabalho_remoto'], mode='lines', name='Trabalho Remoto', line=dict(color='blue', dash='dash'), yaxis='y2'))

        fig_obitos_home_office.update_layout(
        title='Óbitos vs Trabalho Remoto',
        xaxis=dict(title='Mês/Semana'),
        yaxis=dict(title='Óbitos'),
        yaxis2=dict(title='Trabalho Remoto', overlaying='y', side='right')
        )
        st.plotly_chart(fig_obitos_home_office, use_container_width=True)



        #Casos, Óbitos vs Home Office
        fig_cenario_home_office = go.Figure()

        fig_cenario_home_office.add_trace(go.Scatter(x=df_covid['mes_semana'], y=df_covid['casos'], mode='lines', name='Casos', line=dict(color='orange')))
        fig_cenario_home_office.add_trace(go.Scatter(x=df_covid['mes_semana'], y=df_covid['obitos'], mode='lines', name='Óbitos', line=dict(color='red')))
        fig_cenario_home_office.add_trace(go.Scatter(x=df_covid['mes_semana'], y=df_covid['trabalho_remoto'], mode='lines', name='Trabalho Remoto', yaxis='y2', line=dict(color='blue', dash='dash')))

        fig_cenario_home_office.update_layout(
        title='Casos, Óbitos vs Trabalho Remoto',
        xaxis=dict(title='Mês/Semana'),
        yaxis=dict(title='Casos e Óbitos'),
        yaxis2=dict(title='Trabalho Remoto', overlaying='y', side='right')
        )
        st.plotly_chart(fig_cenario_home_office, use_container_width=True)


        '''
        Esta correlação não indica certeza de causalisade, contudo, devido ao que vimos nos últimos anos é fortemente um indício para tal. Sendo assim, uma das melhores ações que podem ser tomadas em caso de um cenário similar a esse, é a adoção do trabalho remoto o mais rápido possível e com o maior número de pessoas possíveis. Essa mudança na dinâmica do trabalho poderá, novamente, ajudar a conter a propagação do vírus ao reduzir significativamente a movimentação e o contato social, fatores que desempenham um papel crucial na transmissão da COVID-19.
        '''
        
with tab3:
        '''
        # Detalhamento Técnico
        
        ## Perguntas vs Análises
        Para a realização das análises, foram utilizadas as perguntas disponibilizadas no dataset do PNAD. Mais detalhes de quais perguntas foram utilizadas em cada análise podem ser conferidos logo abaixo.

        #### Análise 1 - Entre as pessoas que foram entrevistadas, qual a quantidade que trabalhou ou fez algum bico (por pelo menos uma hora) na semana passada?
        - V1012 - Semana no mês
        - V1013 - Mês da pesquisa
        - C001 - Na semana passada, por pelo menos uma hora, trabalhou ou fez algum bico?

        #### Análise 2 - Dentre esses que trabalharam ou fizeram algum bico (por pelo menos uma hora) na semana passada, quantos deles apresentaram sintomas?
        - V1012 - Semana no mês
        - V1013 - Mês da pesquisa
        - C001 - Na semana passada, por pelo menos uma hora, trabalhou ou fez algum bico?
        - B0011 - Na semana passada teve febre?
        - B0012 - Na semana passada teve tosse?
        - B0013 - Na semana passada teve dor de garganta?
        - B0014 - Na semana passada teve dificuldade para respirar?
        - B0015 - Na semana passada teve dor de cabeça?
        - B00111 - Na semana passada teve perda de cheiro ou sabor?
        - B00112 - Na semana passada teve dor muscular?

        #### Análise 3 - E desses, quais os tipos de vínculos trabalhistas mais comuns?
        - C001 - Na semana passada, por pelo menos uma hora, trabalhou ou fez algum bico?
        - B0011 - Na semana passada teve febre?
        - B0012 - Na semana passada teve tosse?
        - B0013 - Na semana passada teve dor de garganta?
        - B0014 - Na semana passada teve dificuldade para respirar?
        - B0015 - Na semana passada teve dor de cabeça?
        - B00111 - Na semana passada teve perda de cheiro ou sabor?
        - B00112 - Na semana passada teve dor muscular?
        - C007 - No trabalho (único ou principal) que tinha nessa semana, era:

        #### Análise 4 - Ainda entre esses que apresentaram sintomas, quais foram os sintomas mais comuns?
        - C001: Na semana passada, por pelo menos uma hora, trabalhou ou fez algum bico?
        - B0011: Na semana passada teve febre?
        - B0012: Na semana passada teve tosse?
        - B0013: Na semana passada teve dor de garganta?
        - B0014: Na semana passada teve dificuldade para respirar?
        - B0015: Na semana passada teve dor de cabeça?
        - B00111: Na semana passada teve perda de cheiro ou sabor?
        - B00112: Na semana passada teve dor muscular?

        #### Análise 5 - E qual a atitude que essas pessoas tomaram?
        - V1012: Semana no mês
        - V1013: Mês da pesquisa
        - B0011: Na semana passada teve febre?
        - B0012: Na semana passada teve tosse?
        - B0013: Na semana passada teve dor de garganta?
        - B0014: Na semana passada teve dificuldade para respirar?
        - B0015: Na semana passada teve dor de cabeça?
        - B00111: Na semana passada teve perda de cheiro ou sabor?
        - B00112: Na semana passada teve dor muscular?
        - B0031: Providência tomada para recuperar dos sintomas foi ficar em casa

        #### Análise 6 - Caso a pessoa não tenha apenas ficado em casa, ou seja, tenha procurado ajuda médica, ela comprou e/ou tomou remédios por orientação médica?
        - V1012: Semana no mês
        - V1013: Mês da pesquisa
        - B0011: Na semana passada teve febre?
        - B0012: Na semana passada teve tosse?
        - B0013: Na semana passada teve dor de garganta?
        - B0014: Na semana passada teve dificuldade para respirar?
        - B0015: Na semana passada teve dor de cabeça?
        - B00111: Na semana passada teve perda de cheiro ou sabor?
        - B00112: Na semana passada teve dor muscular?
        - B0034: Providência tomada para recuperar dos sintomas foi comprar e/ou tomar remédio por orientação médica

        #### Análise 7 - E das pessoas que procuraram alguma unidade de saúde e foram internadas por um dia ou mais, quantas foram sedadas, entubadas ou colocadas em respiração artificial com ventilador?
        - V1012: Semana no mês
        - V1013: Mês da pesquisa
        - B002: Por causa disso, foi a algum estabelecimento de saúde?
        - B0041: Local que buscou atendimento foi posto de saúde/Unidade básica de saúde /Equipe de Saúde da Família (médico, enfermeiro, técnico de enfermagem ou agente comunitário de saúde)
        - B0042: Local que buscou atendimento foi pronto socorro do SUS/UPA
        - B0043: Local que buscou atendimento foi hospital do SUS
        - B005: Ao procurar o hospital, teve que ficar internado por um dia ou mais
        - B006: Durante a internação, foi sedado, entubado e colocado em respiração artificial com ventilador


        #### Análise 8 - E dessas pessoas que foram sedadas, entubadas ou colocadas em respiração artificial com ventilador, quantas possuem plano de saúde?
        - V1012 - Semana no mês
        - V1013 - Mês da pesquisa
        - B002 - Por causa disso, foi a algum estabelecimento de saúde?
        - B0041 - Local que buscou atendimento foi posto de saúde/Unidade básica de saúde /Equipe de Saúde da Família (médico, enfermeiro, técnico de enfermagem ou agente comunitário de saúde)
        - B0042 -	Local que buscou atendimento foi pronto socorro do SUS/UPA
        - B0043 - Local que buscou atendimento foi hospital do SUS
        - B005 - Ao procurar o hospital, teve que ficar internado por um dia ou mais
        - B006 - Durante a internação, foi sedado, entubado e colocado em respiração artificial com ventilador
        - B007 - Tem algum plano de saúde médico, seja particular, de empresa ou de órgão público

        #### Trabalho Remoto

        Além disso, para a análise do trabalho remoto e a sua possível relação com o número de casos e óbitos, além das perguntas abaixo que estão disponíveis no dataset do PNAD, também foram utilizados dados de datasets disponibilizados pelo DataSUS:
        - V1012 - Semana no mês
        - V1013 - Mês da pesquisa
        - C013 - Na semana passada, o(a) Sr(a) estava em trabalho remoto (home office ou teletrabalho)?
        '''

        
        '''
        ## Arquitetura e Implementação
        Com o intuito de identificar os principais indicadores para o planejamento de ações e estratégias em futuros surtos, este projeto buscou estar preparado para uma arquitetura de Big Data. Embora neste momento foram analisados apenas 3 meses e utilizado apenas 2 bases de dados (PNAD e DataSUS), o projeto suporta a leitura, tratamento e análise de uma imensa quantidade de dados.

        Para isso ser possível, utilizamos principalmente a Google Cloud Platform (GCP) e Python. O seguinte diagrama simplificado demonstra a atual arquitetura do projeto.
        '''

        st.image('./imagens/diagrama_arquitetura_simplificado.png', caption='Diagrama de Arquitetura Simplificado')

        '''
        Em suma, foi realizado o upload manual para o Google Cloud Storage - algo que no futuro poderia ser automatizado - dos arquivos CSVs exportados das bases de dados e então foram criados dois notebooks para a ingestão dos dados. Cada notebook realiza a leitura e tratamento de cada uma das bases de dados e então grava os dados em tabelas do Google Big Query - uma para cada fonte de dado. Um terceiro notebook foi desenvolvido especificamente para análise, assim, caso novos dados precisam ser ingeridos, a camada de ingestão está totalmente separada da camada analítica. Esse notebook de análise conecta-se ao Big Query, extraindo os datasets necessários através de queries SQL para cada análise.
        
        Com o intuito de apresentar os resultados, foi desenvolvido este App Streamlit que basicamente detalha o storytelling do projeto e exibe as análises desenvolvidas. Os notebooks de ingestão e de análise estão disponíveis no mesmo GitHub deste app. Além disso, as seguintes imagens ilustram alguns dos passos acima comentados.
        '''
        
        st.image('./imagens/cloud_storage.png', caption='Cloud Storage')
        st.image('./imagens/notebook_ingestao_pnad.png', caption='Notebook Ingestão PNAD')
        st.image('./imagens/notebook_ingestao_datasus.png', caption='Notebook Ingestão DataSUS')
        st.image('./imagens/big_query_pnad_covid.png', caption='Big Query - PNAD')
        st.image('./imagens/big_query_datasus_covid.png', caption='Big Query - DataSus')
        st.image('./imagens/notebook_analises_sql.png', caption='Análises SQL')
        st.image('./imagens/notebook_analises.png', caption='Análises')