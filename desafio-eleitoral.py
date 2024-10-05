# Importar a biblioteca pandas
import pandas as pd
import os 



url = 'https://raw.githubusercontent.com/jonathascamposmar/desafio-eleitoral/refs/heads/main/consulta_cand_2024_BRASIL_4.csv'
ranking = pd.read_csv(url, sep=';', encoding = 'utf-8')
#df = pd.read_csv(url)

ranking = ranking.drop(['SIGLA'], axis=1)

print(ranking)

#print(df.head(5))

ranking.sort_values(['SG_UF', 'NM_MUNICIPIO', 'indice'], ascending=[True, True, False], inplace=True)

print(ranking.columns)

ranking['QC_PARTIDARIO'] = [float(str(i).replace(",", ".")) for i in ranking['QC_PARTIDARIO']]
ranking['QC_PARTIDARIO'] = ranking['QC_PARTIDARIO'].astype('float')

ranking['PERCENTUAL_PREVISAO'] = [float(str(i).replace(",", ".")) for i in ranking['PERCENTUAL_PREVISAO']]
ranking['PERCENTUAL_PREVISAO'] = ranking['PERCENTUAL_PREVISAO'].astype('float')

ranking['maior_numero_percentual'] = [float(str(i).replace(",", ".")) for i in ranking['maior_numero_percentual']]
ranking['maior_numero_percentual'] = ranking['maior_numero_percentual'].astype('float')

ranking.loc[(ranking['QT_VAGA'] == 7) & (ranking['QC_PARTIDARIO'] > 2.50) & (ranking['QC_PARTIDARIO'] <= 4.4), "numero_efetivo"] = 3
ranking.loc[(ranking['QT_VAGA'] == 7) & (ranking['QC_PARTIDARIO'] > 1.70) & (ranking['QC_PARTIDARIO'] <= 2.5), "numero_efetivo"] = 2
ranking.loc[(ranking['QT_VAGA'] == 7) & (ranking['QC_PARTIDARIO'] > 1) & (ranking['QC_PARTIDARIO'] <= 1.70), "numero_efetivo"] = 1
ranking.loc[(ranking['QT_VAGA'] == 7) & (ranking['QC_PARTIDARIO'] <= 1), "numero_efetivo"] = 0

ranking.loc[(ranking['QT_VAGA'] == 9) & (ranking['QC_PARTIDARIO'] > 8) & (ranking['QT_DIFERENCA_PARTIDO_VAGA'] >= 2), "numero_efetivo"] = 8
ranking.loc[(ranking['QT_VAGA'] == 9) & (ranking['QC_PARTIDARIO'] > 7) & (ranking['QC_PARTIDARIO'] <= 8) & (ranking['QT_DIFERENCA_PARTIDO_VAGA'] >= 2), "numero_efetivo"] = 7
ranking.loc[(ranking['QT_VAGA'] == 9) & (ranking['QC_PARTIDARIO'] > 6) & (ranking['QC_PARTIDARIO'] <= 7) & (ranking['QT_DIFERENCA_PARTIDO_VAGA'] >= 2), "numero_efetivo"] = 6
ranking.loc[(ranking['QT_VAGA'] == 9) & (ranking['QC_PARTIDARIO'] > 4.9) & (ranking['QC_PARTIDARIO'] <= 6) & (ranking['QT_DIFERENCA_PARTIDO_VAGA'] >= 2), "numero_efetivo"] = 5
ranking.loc[(ranking['QT_VAGA'] == 9) & (ranking['QC_PARTIDARIO'] > 3.80) & (ranking['QC_PARTIDARIO'] <= 4.9) & (ranking['QT_DIFERENCA_PARTIDO_VAGA'] >= 2), "numero_efetivo"] = 4
ranking.loc[(ranking['QT_VAGA'] == 9) & (ranking['QC_PARTIDARIO'] > 3) & (ranking['QC_PARTIDARIO'] <= 3.80) & (ranking['QT_DIFERENCA_PARTIDO_VAGA'] >= 2), "numero_efetivo"] = 3
ranking.loc[(ranking['QT_VAGA'] == 9) & (ranking['QC_PARTIDARIO'] > 1.80) & (ranking['QC_PARTIDARIO'] <= 3) & (ranking['QT_DIFERENCA_PARTIDO_VAGA'] >= 2), "numero_efetivo"] = 2
ranking.loc[(ranking['QT_VAGA'] == 9) & (ranking['QC_PARTIDARIO'] > 0.9) & (ranking['QC_PARTIDARIO'] <= 1.80) & (ranking['QT_DIFERENCA_PARTIDO_VAGA'] >= 2), "numero_efetivo"] = 1
ranking.loc[(ranking['QT_VAGA'] == 9) & (ranking['QC_PARTIDARIO'] <= 0.9) & (ranking['QT_DIFERENCA_PARTIDO_VAGA'] >= 2), "numero_efetivo"] = 0

ranking.loc[(ranking['QT_VAGA'] == 9) & (ranking['QC_PARTIDARIO'] > 2.9) & (ranking['QT_DIFERENCA_PARTIDO_VAGA'] < 2), "numero_efetivo"] = 2
ranking.loc[(ranking['QT_VAGA'] == 9) & (ranking['QC_PARTIDARIO'] > 1.80) & (ranking['QC_PARTIDARIO'] <= 2.9) & (ranking['QT_DIFERENCA_PARTIDO_VAGA'] < 2), "numero_efetivo"] = 2
ranking.loc[(ranking['QT_VAGA'] == 9) & (ranking['QC_PARTIDARIO'] > 0.65) & (ranking['QC_PARTIDARIO'] <= 1.80) & (ranking['QT_DIFERENCA_PARTIDO_VAGA'] < 2), "numero_efetivo"] = 1
ranking.loc[(ranking['QT_VAGA'] == 9) & (ranking['QC_PARTIDARIO'] <= 0.65) & (ranking['QT_DIFERENCA_PARTIDO_VAGA'] < 2), "numero_efetivo"] = 0

ranking.loc[(ranking['QT_VAGA'] == 9) & (ranking['indice'] == 1) & (ranking['maior_numero_percentual'] < 0.21), "numero_efetivo"] = 1
ranking.loc[(ranking['QT_VAGA'] == 9) & (ranking['indice'] == 2) & (ranking['maior_numero_percentual'] < 0.21), "numero_efetivo"] = 1
ranking.loc[(ranking['QT_VAGA'] == 9) & (ranking['indice'] == 3) & (ranking['maior_numero_percentual'] < 0.21), "numero_efetivo"] = 1
ranking.loc[(ranking['QT_VAGA'] == 9) & (ranking['indice'] == 4) & (ranking['maior_numero_percentual'] < 0.21), "numero_efetivo"] = 1
ranking.loc[(ranking['QT_VAGA'] == 9) & (ranking['indice'] == 5) & (ranking['maior_numero_percentual'] < 0.21), "numero_efetivo"] = 1
ranking.loc[(ranking['QT_VAGA'] == 9) & (ranking['indice'] == 6) & (ranking['maior_numero_percentual'] < 0.21), "numero_efetivo"] = 1
ranking.loc[(ranking['QT_VAGA'] == 9) & (ranking['indice'] == 7) & (ranking['maior_numero_percentual'] < 0.21), "numero_efetivo"] = 1
ranking.loc[(ranking['QT_VAGA'] == 9) & (ranking['indice'] == 8) & (ranking['maior_numero_percentual'] < 0.21), "numero_efetivo"] = 1
ranking.loc[(ranking['QT_VAGA'] == 9) & (ranking['indice'] == 9) & (ranking['maior_numero_percentual'] < 0.21), "numero_efetivo"] = 1
ranking.loc[(ranking['QT_VAGA'] == 9) & (ranking['indice'] >= 10) & (ranking['maior_numero_percentual'] < 0.21), "numero_efetivo"] = 0


ranking.loc[(ranking['QT_VAGA'] == 10) & (ranking['QC_PARTIDARIO'] > 2.7) & (ranking['QT_DIFERENCA_PARTIDO_VAGA'] >= 2), "numero_efetivo"] = 3
ranking.loc[(ranking['QT_VAGA'] == 10) & (ranking['QC_PARTIDARIO'] > 1.80) & (ranking['QC_PARTIDARIO'] <= 2.7) & (ranking['QT_DIFERENCA_PARTIDO_VAGA'] >= 2), "numero_efetivo"] = 2
ranking.loc[(ranking['QT_VAGA'] == 10) & (ranking['QC_PARTIDARIO'] > 0.95) & (ranking['QC_PARTIDARIO'] <= 1.80) & (ranking['QT_DIFERENCA_PARTIDO_VAGA'] >= 2), "numero_efetivo"] = 1
ranking.loc[(ranking['QT_VAGA'] == 10) & (ranking['QC_PARTIDARIO'] <= 0.95) & (ranking['QT_DIFERENCA_PARTIDO_VAGA'] >= 2), "numero_efetivo"] = 0

ranking.loc[(ranking['QT_VAGA'] == 10) & (ranking['QC_PARTIDARIO'] > 2.72) & (ranking['QT_DIFERENCA_PARTIDO_VAGA'] < 2), "numero_efetivo"] = 2
ranking.loc[(ranking['QT_VAGA'] == 10) & (ranking['QC_PARTIDARIO'] > 1.75) & (ranking['QC_PARTIDARIO'] <= 2.72) & (ranking['QT_DIFERENCA_PARTIDO_VAGA'] < 2), "numero_efetivo"] = 2
ranking.loc[(ranking['QT_VAGA'] == 10) & (ranking['QC_PARTIDARIO'] > 0.63) & (ranking['QC_PARTIDARIO'] <= 1.75) & (ranking['QT_DIFERENCA_PARTIDO_VAGA'] < 2), "numero_efetivo"] = 1
ranking.loc[(ranking['QT_VAGA'] == 10) & (ranking['QC_PARTIDARIO'] <= 0.60) & (ranking['QT_DIFERENCA_PARTIDO_VAGA'] < 2), "numero_efetivo"] = 0

ranking.loc[(ranking['QT_VAGA'] == 10) & (ranking['indice'] == 1) & (ranking['maior_numero_percentual'] < 0.185), "numero_efetivo"] = 2
ranking.loc[(ranking['QT_VAGA'] == 10) & (ranking['indice'] == 2) & (ranking['maior_numero_percentual'] < 0.185), "numero_efetivo"] = 1
ranking.loc[(ranking['QT_VAGA'] == 10) & (ranking['indice'] == 3) & (ranking['maior_numero_percentual'] < 0.185), "numero_efetivo"] = 1
ranking.loc[(ranking['QT_VAGA'] == 10) & (ranking['indice'] == 4) & (ranking['maior_numero_percentual'] < 0.185), "numero_efetivo"] = 1
ranking.loc[(ranking['QT_VAGA'] == 10) & (ranking['indice'] == 5) & (ranking['maior_numero_percentual'] < 0.185), "numero_efetivo"] = 1
ranking.loc[(ranking['QT_VAGA'] == 10) & (ranking['indice'] == 6) & (ranking['maior_numero_percentual'] < 0.185), "numero_efetivo"] = 1
ranking.loc[(ranking['QT_VAGA'] == 10) & (ranking['indice'] == 7) & (ranking['maior_numero_percentual'] < 0.185), "numero_efetivo"] = 1
ranking.loc[(ranking['QT_VAGA'] == 10) & (ranking['indice'] == 8) & (ranking['maior_numero_percentual'] < 0.185), "numero_efetivo"] = 1
ranking.loc[(ranking['QT_VAGA'] == 10) & (ranking['indice'] == 9) & (ranking['maior_numero_percentual'] < 0.185), "numero_efetivo"] = 1
ranking.loc[(ranking['QT_VAGA'] == 10) & (ranking['indice'] >= 10) & (ranking['maior_numero_percentual'] < 0.185), "numero_efetivo"] = 0

ranking.loc[(ranking['QT_VAGA'] == 11) & (ranking['QC_PARTIDARIO'] > 8) & (ranking['QT_DIFERENCA_PARTIDO_VAGA'] >= 0), "numero_efetivo"] = 8
ranking.loc[(ranking['QT_VAGA'] == 11) & (ranking['QC_PARTIDARIO'] > 7) & (ranking['QC_PARTIDARIO'] <= 8) & (ranking['QT_DIFERENCA_PARTIDO_VAGA'] >= 0), "numero_efetivo"] = 7
ranking.loc[(ranking['QT_VAGA'] == 11) & (ranking['QC_PARTIDARIO'] > 3.72) & (ranking['QC_PARTIDARIO'] <= 7) & (ranking['QT_DIFERENCA_PARTIDO_VAGA'] >= 0), "numero_efetivo"] = 6
ranking.loc[(ranking['QT_VAGA'] == 11) & (ranking['QC_PARTIDARIO'] > 5) & (ranking['QC_PARTIDARIO'] <= 6) & (ranking['QT_DIFERENCA_PARTIDO_VAGA'] >= 0), "numero_efetivo"] = 5
ranking.loc[(ranking['QT_VAGA'] == 11) & (ranking['QC_PARTIDARIO'] > 3.72) & (ranking['QC_PARTIDARIO'] <= 5) & (ranking['QT_DIFERENCA_PARTIDO_VAGA'] >= 0), "numero_efetivo"] = 4
ranking.loc[(ranking['QT_VAGA'] == 11) & (ranking['QC_PARTIDARIO'] > 3) & (ranking['QC_PARTIDARIO'] <= 3.72) & (ranking['QT_DIFERENCA_PARTIDO_VAGA'] >= 0), "numero_efetivo"] = 3
ranking.loc[(ranking['QT_VAGA'] == 11) & (ranking['QC_PARTIDARIO'] > 1.35) & (ranking['QC_PARTIDARIO'] <= 3) & (ranking['QT_DIFERENCA_PARTIDO_VAGA'] >= 0), "numero_efetivo"] = 2
ranking.loc[(ranking['QT_VAGA'] == 11) & (ranking['QC_PARTIDARIO'] > 0.8) & (ranking['QC_PARTIDARIO'] <= 1.35) & (ranking['QT_DIFERENCA_PARTIDO_VAGA'] >= 0), "numero_efetivo"] = 1
ranking.loc[(ranking['QT_VAGA'] == 11) & (ranking['QC_PARTIDARIO'] <= 0.8) & (ranking['QT_DIFERENCA_PARTIDO_VAGA'] >= 0), "numero_efetivo"] = 0

ranking.loc[(ranking['QT_VAGA'] == 11) & (ranking['QC_PARTIDARIO'] > 1.2) & (ranking['QT_DIFERENCA_PARTIDO_VAGA'] < 0), "numero_efetivo"] = 2
ranking.loc[(ranking['QT_VAGA'] == 11) & (ranking['QC_PARTIDARIO'] > 0.95) & (ranking['QC_PARTIDARIO'] <= 1.2) & (ranking['QT_DIFERENCA_PARTIDO_VAGA'] < 0), "numero_efetivo"] = 2
ranking.loc[(ranking['QT_VAGA'] == 11) & (ranking['QC_PARTIDARIO'] > 0.7) & (ranking['QC_PARTIDARIO'] <= 0.95) & (ranking['QT_DIFERENCA_PARTIDO_VAGA'] < 0), "numero_efetivo"] = 2
ranking.loc[(ranking['QT_VAGA'] == 11) & (ranking['QC_PARTIDARIO'] > 0.60) & (ranking['QC_PARTIDARIO'] <= 0.7) & (ranking['QT_DIFERENCA_PARTIDO_VAGA'] < 0), "numero_efetivo"] = 1
ranking.loc[(ranking['QT_VAGA'] == 11) & (ranking['QC_PARTIDARIO'] <= 0.60) & (ranking['QT_DIFERENCA_PARTIDO_VAGA'] < 0), "numero_efetivo"] = 0

ranking.loc[(ranking['QT_VAGA'] == 11) & (ranking['indice'] == 1) & (ranking['maior_numero_percentual'] < 0.23), "numero_efetivo"] = 2
ranking.loc[(ranking['QT_VAGA'] == 11) & (ranking['indice'] == 2) & (ranking['maior_numero_percentual'] < 0.23), "numero_efetivo"] = 2
ranking.loc[(ranking['QT_VAGA'] == 11) & (ranking['indice'] == 3) & (ranking['maior_numero_percentual'] < 0.23), "numero_efetivo"] = 2
ranking.loc[(ranking['QT_VAGA'] == 11) & (ranking['indice'] == 4) & (ranking['maior_numero_percentual'] < 0.23), "numero_efetivo"] = 2
ranking.loc[(ranking['QT_VAGA'] == 11) & (ranking['indice'] == 5) & (ranking['maior_numero_percentual'] < 0.23), "numero_efetivo"] = 2
ranking.loc[(ranking['QT_VAGA'] == 11) & (ranking['indice'] == 6) & (ranking['maior_numero_percentual'] < 0.23), "numero_efetivo"] = 1
ranking.loc[(ranking['QT_VAGA'] == 11) & (ranking['indice'] == 7) & (ranking['maior_numero_percentual'] < 0.23), "numero_efetivo"] = 0
ranking.loc[(ranking['QT_VAGA'] == 11) & (ranking['indice'] == 8) & (ranking['maior_numero_percentual'] < 0.23), "numero_efetivo"] = 0
ranking.loc[(ranking['QT_VAGA'] == 11) & (ranking['indice'] == 9) & (ranking['maior_numero_percentual'] < 0.23), "numero_efetivo"] = 0
ranking.loc[(ranking['QT_VAGA'] == 11) & (ranking['indice'] >= 10) & (ranking['maior_numero_percentual'] < 0.23), "numero_efetivo"] = 0

ranking.loc[(ranking['QT_VAGA'] == 12) & (ranking['QC_PARTIDARIO'] > 3.72) & (ranking['QT_DIFERENCA_PARTIDO_VAGA'] >= 2), "numero_efetivo"] = 4
ranking.loc[(ranking['QT_VAGA'] == 12) & (ranking['QC_PARTIDARIO'] > 2.72) & (ranking['QC_PARTIDARIO'] <= 3.72) & (ranking['QT_DIFERENCA_PARTIDO_VAGA'] >= 2), "numero_efetivo"] = 3
ranking.loc[(ranking['QT_VAGA'] == 12) & (ranking['QC_PARTIDARIO'] > 1.75) & (ranking['QC_PARTIDARIO'] <= 2.72) & (ranking['QT_DIFERENCA_PARTIDO_VAGA'] >= 2), "numero_efetivo"] = 2
ranking.loc[(ranking['QT_VAGA'] == 12) & (ranking['QC_PARTIDARIO'] > 0.95) & (ranking['QC_PARTIDARIO'] <= 1.75) & (ranking['QT_DIFERENCA_PARTIDO_VAGA'] >= 2), "numero_efetivo"] = 1
ranking.loc[(ranking['QT_VAGA'] == 12) & (ranking['QC_PARTIDARIO'] <= 0.95) & (ranking['QT_DIFERENCA_PARTIDO_VAGA'] >= 2), "numero_efetivo"] = 0

ranking.loc[(ranking['QT_VAGA'] == 12) & (ranking['QC_PARTIDARIO'] > 1.5) & (ranking['QT_DIFERENCA_PARTIDO_VAGA'] < 2), "numero_efetivo"] = 3
ranking.loc[(ranking['QT_VAGA'] == 12) & (ranking['QC_PARTIDARIO'] > 1.25) & (ranking['QC_PARTIDARIO'] <= 1.5) & (ranking['QT_DIFERENCA_PARTIDO_VAGA'] < 2), "numero_efetivo"] = 2
ranking.loc[(ranking['QT_VAGA'] == 12) & (ranking['QC_PARTIDARIO'] > 0.8) & (ranking['QC_PARTIDARIO'] <= 1.25) & (ranking['QT_DIFERENCA_PARTIDO_VAGA'] < 2), "numero_efetivo"] = 2
ranking.loc[(ranking['QT_VAGA'] == 12) & (ranking['QC_PARTIDARIO'] > 0.66) & (ranking['QC_PARTIDARIO'] <= 0.8) & (ranking['QT_DIFERENCA_PARTIDO_VAGA'] < 2), "numero_efetivo"] = 1
ranking.loc[(ranking['QT_VAGA'] == 12) & (ranking['QC_PARTIDARIO'] <= 0.66) & (ranking['QT_DIFERENCA_PARTIDO_VAGA'] < 2), "numero_efetivo"] = 0

ranking.loc[(ranking['QT_VAGA'] == 12) & (ranking['indice'] == 1) & (ranking['maior_numero_percentual'] < 0.21), "numero_efetivo"] = 3
ranking.loc[(ranking['QT_VAGA'] == 12) & (ranking['indice'] == 2) & (ranking['maior_numero_percentual'] < 0.21), "numero_efetivo"] = 2
ranking.loc[(ranking['QT_VAGA'] == 12) & (ranking['indice'] == 3) & (ranking['maior_numero_percentual'] < 0.21), "numero_efetivo"] = 2
ranking.loc[(ranking['QT_VAGA'] == 12) & (ranking['indice'] == 4) & (ranking['maior_numero_percentual'] < 0.21), "numero_efetivo"] = 2
ranking.loc[(ranking['QT_VAGA'] == 12) & (ranking['indice'] == 5) & (ranking['maior_numero_percentual'] < 0.21), "numero_efetivo"] = 1
ranking.loc[(ranking['QT_VAGA'] == 12) & (ranking['indice'] == 6) & (ranking['maior_numero_percentual'] < 0.21), "numero_efetivo"] = 1
ranking.loc[(ranking['QT_VAGA'] == 12) & (ranking['indice'] == 7) & (ranking['maior_numero_percentual'] < 0.21), "numero_efetivo"] = 1
ranking.loc[(ranking['QT_VAGA'] == 12) & (ranking['indice'] == 8) & (ranking['maior_numero_percentual'] < 0.21), "numero_efetivo"] = 0
ranking.loc[(ranking['QT_VAGA'] == 12) & (ranking['indice'] == 9) & (ranking['maior_numero_percentual'] < 0.21), "numero_efetivo"] = 0
ranking.loc[(ranking['QT_VAGA'] == 12) & (ranking['indice'] >= 10) & (ranking['maior_numero_percentual'] < 0.21), "numero_efetivo"] = 0

ranking.loc[(ranking['QT_VAGA'] == 13) & (ranking['QC_PARTIDARIO'] > 3.32) & (ranking['QT_DIFERENCA_PARTIDO_VAGA'] >= 0), "numero_efetivo"] = 4
ranking.loc[(ranking['QT_VAGA'] == 13) & (ranking['QC_PARTIDARIO'] > 2.32) & (ranking['QC_PARTIDARIO'] <= 3.32) & (ranking['QT_DIFERENCA_PARTIDO_VAGA'] >= 0), "numero_efetivo"] = 3
ranking.loc[(ranking['QT_VAGA'] == 13) & (ranking['QC_PARTIDARIO'] > 1.35) & (ranking['QC_PARTIDARIO'] <= 2.32) & (ranking['QT_DIFERENCA_PARTIDO_VAGA'] >= 0), "numero_efetivo"] = 2
ranking.loc[(ranking['QT_VAGA'] == 13) & (ranking['QC_PARTIDARIO'] > 0.98) & (ranking['QC_PARTIDARIO'] <= 1.35) & (ranking['QT_DIFERENCA_PARTIDO_VAGA'] >= 0), "numero_efetivo"] = 1
ranking.loc[(ranking['QT_VAGA'] == 13) & (ranking['QC_PARTIDARIO'] <= 0.98) & (ranking['QT_DIFERENCA_PARTIDO_VAGA'] >= 0), "numero_efetivo"] = 0

ranking.loc[(ranking['QT_VAGA'] == 13) & (ranking['QC_PARTIDARIO'] > 1.7) & (ranking['QT_DIFERENCA_PARTIDO_VAGA'] < 0), "numero_efetivo"] = 3
ranking.loc[(ranking['QT_VAGA'] == 13) & (ranking['QC_PARTIDARIO'] > 1.3) & (ranking['QC_PARTIDARIO'] <= 1.7) & (ranking['QT_DIFERENCA_PARTIDO_VAGA'] < 0), "numero_efetivo"] = 3
ranking.loc[(ranking['QT_VAGA'] == 13) & (ranking['QC_PARTIDARIO'] > 0.90) & (ranking['QC_PARTIDARIO'] <= 1.3) & (ranking['QT_DIFERENCA_PARTIDO_VAGA'] < 0), "numero_efetivo"] = 2
ranking.loc[(ranking['QT_VAGA'] == 13) & (ranking['QC_PARTIDARIO'] > 0.88) & (ranking['QC_PARTIDARIO'] <= 0.90) & (ranking['QT_DIFERENCA_PARTIDO_VAGA'] < 0), "numero_efetivo"] = 1
ranking.loc[(ranking['QT_VAGA'] == 13) & (ranking['QC_PARTIDARIO'] <= 0.88) & (ranking['QT_DIFERENCA_PARTIDO_VAGA'] < 2), "numero_efetivo"] = 0

ranking.loc[(ranking['QT_VAGA'] == 13) & (ranking['indice'] == 1) & (ranking['maior_numero_percentual'] < 0.19), "numero_efetivo"] = 3
ranking.loc[(ranking['QT_VAGA'] == 13) & (ranking['indice'] == 2) & (ranking['maior_numero_percentual'] < 0.19), "numero_efetivo"] = 3
ranking.loc[(ranking['QT_VAGA'] == 13) & (ranking['indice'] == 3) & (ranking['maior_numero_percentual'] < 0.19), "numero_efetivo"] = 3
ranking.loc[(ranking['QT_VAGA'] == 13) & (ranking['indice'] == 4) & (ranking['maior_numero_percentual'] < 0.19), "numero_efetivo"] = 2
ranking.loc[(ranking['QT_VAGA'] == 13) & (ranking['indice'] == 5) & (ranking['maior_numero_percentual'] < 0.19), "numero_efetivo"] = 0
ranking.loc[(ranking['QT_VAGA'] == 13) & (ranking['indice'] == 6) & (ranking['maior_numero_percentual'] < 0.19), "numero_efetivo"] = 0
ranking.loc[(ranking['QT_VAGA'] == 13) & (ranking['indice'] == 7) & (ranking['maior_numero_percentual'] < 0.19), "numero_efetivo"] = 0
ranking.loc[(ranking['QT_VAGA'] == 13) & (ranking['indice'] == 8) & (ranking['maior_numero_percentual'] < 0.19), "numero_efetivo"] = 0
ranking.loc[(ranking['QT_VAGA'] == 13) & (ranking['indice'] == 9) & (ranking['maior_numero_percentual'] < 0.19), "numero_efetivo"] = 0
ranking.loc[(ranking['QT_VAGA'] == 13) & (ranking['indice'] >= 10) & (ranking['maior_numero_percentual'] < 0.19), "numero_efetivo"] = 0

ranking.loc[(ranking['QT_VAGA'] == 14) & (ranking['QC_PARTIDARIO'] > 3.72) & (ranking['QT_DIFERENCA_PARTIDO_VAGA'] >= 2), "numero_efetivo"] = 4
ranking.loc[(ranking['QT_VAGA'] == 14) & (ranking['QC_PARTIDARIO'] > 2.72) & (ranking['QC_PARTIDARIO'] <= 3.72) & (ranking['QT_DIFERENCA_PARTIDO_VAGA'] >= 2), "numero_efetivo"] = 3
ranking.loc[(ranking['QT_VAGA'] == 14) & (ranking['QC_PARTIDARIO'] > 1.75) & (ranking['QC_PARTIDARIO'] <= 2.72) & (ranking['QT_DIFERENCA_PARTIDO_VAGA'] >= 2), "numero_efetivo"] = 2
ranking.loc[(ranking['QT_VAGA'] == 14) & (ranking['QC_PARTIDARIO'] > 1.13) & (ranking['QC_PARTIDARIO'] <= 1.75) & (ranking['QT_DIFERENCA_PARTIDO_VAGA'] >= 2), "numero_efetivo"] = 1
ranking.loc[(ranking['QT_VAGA'] == 14) & (ranking['QC_PARTIDARIO'] <= 1.13) & (ranking['QT_DIFERENCA_PARTIDO_VAGA'] >= 2), "numero_efetivo"] = 0

ranking.loc[(ranking['QT_VAGA'] == 14) & (ranking['QC_PARTIDARIO'] > 3.72) & (ranking['QT_DIFERENCA_PARTIDO_VAGA'] < 2), "numero_efetivo"] = 3
ranking.loc[(ranking['QT_VAGA'] == 14) & (ranking['QC_PARTIDARIO'] > 2.72) & (ranking['QC_PARTIDARIO'] <= 3.72) & (ranking['QT_DIFERENCA_PARTIDO_VAGA'] < 2), "numero_efetivo"] = 2
ranking.loc[(ranking['QT_VAGA'] == 14) & (ranking['QC_PARTIDARIO'] > 1.55) & (ranking['QC_PARTIDARIO'] <= 2.72) & (ranking['QT_DIFERENCA_PARTIDO_VAGA'] < 2), "numero_efetivo"] = 2
ranking.loc[(ranking['QT_VAGA'] == 14) & (ranking['QC_PARTIDARIO'] > 1.13) & (ranking['QC_PARTIDARIO'] <= 1.55) & (ranking['QT_DIFERENCA_PARTIDO_VAGA'] < 2), "numero_efetivo"] = 1
ranking.loc[(ranking['QT_VAGA'] == 14) & (ranking['QC_PARTIDARIO'] <= 1.13) & (ranking['QT_DIFERENCA_PARTIDO_VAGA'] < 2), "numero_efetivo"] = 0

ranking.loc[(ranking['QT_VAGA'] == 14) & (ranking['indice'] == 1) & (ranking['maior_numero_percentual'] < 0.20), "numero_efetivo"] = 3
ranking.loc[(ranking['QT_VAGA'] == 14) & (ranking['indice'] == 2) & (ranking['maior_numero_percentual'] < 0.20), "numero_efetivo"] = 2
ranking.loc[(ranking['QT_VAGA'] == 14) & (ranking['indice'] == 3) & (ranking['maior_numero_percentual'] < 0.20), "numero_efetivo"] = 2
ranking.loc[(ranking['QT_VAGA'] == 14) & (ranking['indice'] == 4) & (ranking['maior_numero_percentual'] < 0.20), "numero_efetivo"] = 2
ranking.loc[(ranking['QT_VAGA'] == 14) & (ranking['indice'] == 5) & (ranking['maior_numero_percentual'] < 0.20), "numero_efetivo"] = 2
ranking.loc[(ranking['QT_VAGA'] == 14) & (ranking['indice'] == 6) & (ranking['maior_numero_percentual'] < 0.20), "numero_efetivo"] = 1
ranking.loc[(ranking['QT_VAGA'] == 14) & (ranking['indice'] == 7) & (ranking['maior_numero_percentual'] < 0.20), "numero_efetivo"] = 1
ranking.loc[(ranking['QT_VAGA'] == 14) & (ranking['indice'] == 8) & (ranking['maior_numero_percentual'] < 0.20), "numero_efetivo"] = 1
ranking.loc[(ranking['QT_VAGA'] == 14) & (ranking['indice'] == 9) & (ranking['maior_numero_percentual'] < 0.20), "numero_efetivo"] = 0
ranking.loc[(ranking['QT_VAGA'] == 14) & (ranking['indice'] >= 10) & (ranking['maior_numero_percentual'] < 0.20), "numero_efetivo"] = 0


ranking.loc[(ranking['QT_VAGA'] == 15) & (ranking['QC_PARTIDARIO'] > 4.72) & (ranking['QT_DIFERENCA_PARTIDO_VAGA'] >= 0), "numero_efetivo"] = 5
ranking.loc[(ranking['QT_VAGA'] == 15) & (ranking['QC_PARTIDARIO'] > 3.38) & (ranking['QC_PARTIDARIO'] <= 4.72) & (ranking['QT_DIFERENCA_PARTIDO_VAGA'] >= 0), "numero_efetivo"] = 4
ranking.loc[(ranking['QT_VAGA'] == 15) & (ranking['QC_PARTIDARIO'] > 2.42) & (ranking['QC_PARTIDARIO'] <= 3.38) & (ranking['QT_DIFERENCA_PARTIDO_VAGA'] >= 0), "numero_efetivo"] = 3
ranking.loc[(ranking['QT_VAGA'] == 15) & (ranking['QC_PARTIDARIO'] > 1.35) & (ranking['QC_PARTIDARIO'] <= 2.42) & (ranking['QT_DIFERENCA_PARTIDO_VAGA'] >= 0), "numero_efetivo"] = 2
ranking.loc[(ranking['QT_VAGA'] == 15) & (ranking['QC_PARTIDARIO'] > 1.13) & (ranking['QC_PARTIDARIO'] <= 1.35) & (ranking['QT_DIFERENCA_PARTIDO_VAGA'] >= 0), "numero_efetivo"] = 1
ranking.loc[(ranking['QT_VAGA'] == 15) & (ranking['QC_PARTIDARIO'] <= 1.13) & (ranking['QT_DIFERENCA_PARTIDO_VAGA'] >= 0), "numero_efetivo"] = 0

ranking.loc[(ranking['QT_VAGA'] == 15) & (ranking['QC_PARTIDARIO'] > 1.4) & (ranking['QT_DIFERENCA_PARTIDO_VAGA'] < 0), "numero_efetivo"] = 4
ranking.loc[(ranking['QT_VAGA'] == 15) & (ranking['QC_PARTIDARIO'] > 1.3) & (ranking['QC_PARTIDARIO'] <= 1.4) & (ranking['QT_DIFERENCA_PARTIDO_VAGA'] < 0), "numero_efetivo"] = 3
ranking.loc[(ranking['QT_VAGA'] == 15) & (ranking['QC_PARTIDARIO'] > 1) & (ranking['QC_PARTIDARIO'] <= 1.3) & (ranking['QT_DIFERENCA_PARTIDO_VAGA'] < 0), "numero_efetivo"] = 2
ranking.loc[(ranking['QT_VAGA'] == 15) & (ranking['QC_PARTIDARIO'] > 0.9) & (ranking['QC_PARTIDARIO'] <= 1) & (ranking['QT_DIFERENCA_PARTIDO_VAGA'] < 0), "numero_efetivo"] = 2
ranking.loc[(ranking['QT_VAGA'] == 15) & (ranking['QC_PARTIDARIO'] > 0.8) & (ranking['QC_PARTIDARIO'] <= 0.9) & (ranking['QT_DIFERENCA_PARTIDO_VAGA'] < 0), "numero_efetivo"] = 1
ranking.loc[(ranking['QT_VAGA'] == 15) & (ranking['QC_PARTIDARIO'] <= 0.8) & (ranking['QT_DIFERENCA_PARTIDO_VAGA'] < 0), "numero_efetivo"] = 0

ranking.loc[(ranking['QT_VAGA'] ==15) & (ranking['indice'] == 1) & (ranking['maior_numero_percentual'] < 0.20), "numero_efetivo"] = 3
ranking.loc[(ranking['QT_VAGA'] ==15) & (ranking['indice'] == 2) & (ranking['maior_numero_percentual'] < 0.20), "numero_efetivo"] = 2
ranking.loc[(ranking['QT_VAGA'] ==15) & (ranking['indice'] == 3) & (ranking['maior_numero_percentual'] < 0.20), "numero_efetivo"] = 2
ranking.loc[(ranking['QT_VAGA'] ==15) & (ranking['indice'] == 4) & (ranking['maior_numero_percentual'] < 0.20), "numero_efetivo"] = 2
ranking.loc[(ranking['QT_VAGA'] ==15) & (ranking['indice'] == 5) & (ranking['maior_numero_percentual'] < 0.20), "numero_efetivo"] = 2
ranking.loc[(ranking['QT_VAGA'] ==15) & (ranking['indice'] == 6) & (ranking['maior_numero_percentual'] < 0.20), "numero_efetivo"] = 1
ranking.loc[(ranking['QT_VAGA'] ==15) & (ranking['indice'] == 7) & (ranking['maior_numero_percentual'] < 0.20), "numero_efetivo"] = 1
ranking.loc[(ranking['QT_VAGA'] ==15) & (ranking['indice'] == 8) & (ranking['maior_numero_percentual'] < 0.20), "numero_efetivo"] = 1
ranking.loc[(ranking['QT_VAGA'] ==15) & (ranking['indice'] == 9) & (ranking['maior_numero_percentual'] < 0.20), "numero_efetivo"] = 1
ranking.loc[(ranking['QT_VAGA'] ==15) & (ranking['indice'] >= 10) & (ranking['maior_numero_percentual'] < 0.20), "numero_efetivo"] = 0

ranking.loc[(ranking['QT_VAGA'] == 16) & (ranking['QC_PARTIDARIO'] > 4.72) & (ranking['QT_DIFERENCA_PARTIDO_VAGA'] >= 0), "numero_efetivo"] = 5
ranking.loc[(ranking['QT_VAGA'] == 16) & (ranking['QC_PARTIDARIO'] > 3.38) & (ranking['QC_PARTIDARIO'] <= 4.72) & (ranking['QT_DIFERENCA_PARTIDO_VAGA'] >= 0), "numero_efetivo"] = 4
ranking.loc[(ranking['QT_VAGA'] == 16) & (ranking['QC_PARTIDARIO'] > 2.42) & (ranking['QC_PARTIDARIO'] <= 3.38) & (ranking['QT_DIFERENCA_PARTIDO_VAGA'] >= 0), "numero_efetivo"] = 3
ranking.loc[(ranking['QT_VAGA'] == 16) & (ranking['QC_PARTIDARIO'] > 1.35) & (ranking['QC_PARTIDARIO'] <= 2.42) & (ranking['QT_DIFERENCA_PARTIDO_VAGA'] >= 0), "numero_efetivo"] = 2
ranking.loc[(ranking['QT_VAGA'] == 16) & (ranking['QC_PARTIDARIO'] > 1.13) & (ranking['QC_PARTIDARIO'] <= 1.35) & (ranking['QT_DIFERENCA_PARTIDO_VAGA'] >= 0), "numero_efetivo"] = 1
ranking.loc[(ranking['QT_VAGA'] == 16) & (ranking['QC_PARTIDARIO'] <= 1.13) & (ranking['QT_DIFERENCA_PARTIDO_VAGA'] >= 0), "numero_efetivo"] = 0

ranking.loc[(ranking['QT_VAGA'] == 16) & (ranking['QC_PARTIDARIO'] > 1.4) & (ranking['QT_DIFERENCA_PARTIDO_VAGA'] < 0), "numero_efetivo"] = 4
ranking.loc[(ranking['QT_VAGA'] == 16) & (ranking['QC_PARTIDARIO'] > 1.3) & (ranking['QC_PARTIDARIO'] <= 1.4) & (ranking['QT_DIFERENCA_PARTIDO_VAGA'] < 0), "numero_efetivo"] = 3
ranking.loc[(ranking['QT_VAGA'] == 16) & (ranking['QC_PARTIDARIO'] > 1) & (ranking['QC_PARTIDARIO'] <= 1.3) & (ranking['QT_DIFERENCA_PARTIDO_VAGA'] < 0), "numero_efetivo"] = 2
ranking.loc[(ranking['QT_VAGA'] == 16) & (ranking['QC_PARTIDARIO'] > 0.9) & (ranking['QC_PARTIDARIO'] <= 1) & (ranking['QT_DIFERENCA_PARTIDO_VAGA'] < 0), "numero_efetivo"] = 2
ranking.loc[(ranking['QT_VAGA'] == 16) & (ranking['QC_PARTIDARIO'] > 0.8) & (ranking['QC_PARTIDARIO'] <= 0.9) & (ranking['QT_DIFERENCA_PARTIDO_VAGA'] < 0), "numero_efetivo"] = 1
ranking.loc[(ranking['QT_VAGA'] == 16) & (ranking['QC_PARTIDARIO'] <= 0.8) & (ranking['QT_DIFERENCA_PARTIDO_VAGA'] < 0), "numero_efetivo"] = 0

ranking.loc[(ranking['QT_VAGA'] ==16) & (ranking['indice'] == 1) & (ranking['maior_numero_percentual'] < 0.20), "numero_efetivo"] = 3
ranking.loc[(ranking['QT_VAGA'] ==16) & (ranking['indice'] == 2) & (ranking['maior_numero_percentual'] < 0.20), "numero_efetivo"] = 2
ranking.loc[(ranking['QT_VAGA'] ==16) & (ranking['indice'] == 3) & (ranking['maior_numero_percentual'] < 0.20), "numero_efetivo"] = 3
ranking.loc[(ranking['QT_VAGA'] ==16) & (ranking['indice'] == 4) & (ranking['maior_numero_percentual'] < 0.20), "numero_efetivo"] = 2
ranking.loc[(ranking['QT_VAGA'] ==16) & (ranking['indice'] == 5) & (ranking['maior_numero_percentual'] < 0.20), "numero_efetivo"] = 2
ranking.loc[(ranking['QT_VAGA'] ==16) & (ranking['indice'] == 6) & (ranking['maior_numero_percentual'] < 0.20), "numero_efetivo"] = 1
ranking.loc[(ranking['QT_VAGA'] ==16) & (ranking['indice'] == 7) & (ranking['maior_numero_percentual'] < 0.20), "numero_efetivo"] = 1
ranking.loc[(ranking['QT_VAGA'] ==16) & (ranking['indice'] == 8) & (ranking['maior_numero_percentual'] < 0.20), "numero_efetivo"] = 1
ranking.loc[(ranking['QT_VAGA'] ==16) & (ranking['indice'] == 9) & (ranking['maior_numero_percentual'] < 0.20), "numero_efetivo"] = 1
ranking.loc[(ranking['QT_VAGA'] ==16) & (ranking['indice'] >= 10) & (ranking['maior_numero_percentual'] < 0.20), "numero_efetivo"] = 0



ranking.loc[(ranking['QT_VAGA'] == 17) & (ranking['QC_PARTIDARIO'] > 9.7) & (ranking['QT_DIFERENCA_PARTIDO_VAGA'] >= 2), "numero_efetivo"] = 10
ranking.loc[(ranking['QT_VAGA'] == 17) & (ranking['QC_PARTIDARIO'] > 8.72) & (ranking['QC_PARTIDARIO'] <= 9.72) & (ranking['QT_DIFERENCA_PARTIDO_VAGA'] >= 2), "numero_efetivo"] = 9
ranking.loc[(ranking['QT_VAGA'] == 17) & (ranking['QC_PARTIDARIO'] > 7.72) & (ranking['QC_PARTIDARIO'] <= 8.72) & (ranking['QT_DIFERENCA_PARTIDO_VAGA'] >= 2), "numero_efetivo"] = 8
ranking.loc[(ranking['QT_VAGA'] == 17) & (ranking['QC_PARTIDARIO'] > 7) & (ranking['QC_PARTIDARIO'] <= 7.72) & (ranking['QT_DIFERENCA_PARTIDO_VAGA'] >= 2), "numero_efetivo"] = 7
ranking.loc[(ranking['QT_VAGA'] == 17) & (ranking['QC_PARTIDARIO'] > 6) & (ranking['QC_PARTIDARIO'] <= 6.72) & (ranking['QT_DIFERENCA_PARTIDO_VAGA'] >= 2), "numero_efetivo"] = 6
ranking.loc[(ranking['QT_VAGA'] == 17) & (ranking['QC_PARTIDARIO'] > 4.72) & (ranking['QC_PARTIDARIO'] <= 5.72) & (ranking['QT_DIFERENCA_PARTIDO_VAGA'] >= 2), "numero_efetivo"] = 5
ranking.loc[(ranking['QT_VAGA'] == 17) & (ranking['QC_PARTIDARIO'] > 3.72) & (ranking['QC_PARTIDARIO'] <= 4.72) & (ranking['QT_DIFERENCA_PARTIDO_VAGA'] >= 2), "numero_efetivo"] = 4
ranking.loc[(ranking['QT_VAGA'] == 17) & (ranking['QC_PARTIDARIO'] > 2.52) & (ranking['QC_PARTIDARIO'] <= 3.72) & (ranking['QT_DIFERENCA_PARTIDO_VAGA'] >= 2), "numero_efetivo"] = 3
ranking.loc[(ranking['QT_VAGA'] == 17) & (ranking['QC_PARTIDARIO'] > 1.55) & (ranking['QC_PARTIDARIO'] <= 2.52) & (ranking['QT_DIFERENCA_PARTIDO_VAGA'] >= 2), "numero_efetivo"] = 2
ranking.loc[(ranking['QT_VAGA'] == 17) & (ranking['QC_PARTIDARIO'] > 1.03) & (ranking['QC_PARTIDARIO'] <= 1.55) & (ranking['QT_DIFERENCA_PARTIDO_VAGA'] >= 2), "numero_efetivo"] = 1
ranking.loc[(ranking['QT_VAGA'] == 17) & (ranking['QC_PARTIDARIO'] <= 1.13) & (ranking['QT_DIFERENCA_PARTIDO_VAGA'] >= 2), "numero_efetivo"] = 0

ranking.loc[(ranking['QT_VAGA'] == 17) & (ranking['QC_PARTIDARIO'] > 2.4) & (ranking['QT_DIFERENCA_PARTIDO_VAGA'] < 2), "numero_efetivo"] = 5
ranking.loc[(ranking['QT_VAGA'] == 17) & (ranking['QC_PARTIDARIO'] > 1.5) & (ranking['QC_PARTIDARIO'] <= 2.4) & (ranking['QT_DIFERENCA_PARTIDO_VAGA'] < 2), "numero_efetivo"] = 4
ranking.loc[(ranking['QT_VAGA'] == 17) & (ranking['QC_PARTIDARIO'] > 1) & (ranking['QC_PARTIDARIO'] <= 1.5) & (ranking['QT_DIFERENCA_PARTIDO_VAGA'] < 2), "numero_efetivo"] = 3
ranking.loc[(ranking['QT_VAGA'] == 17) & (ranking['QC_PARTIDARIO'] > 0.9) & (ranking['QC_PARTIDARIO'] <= 1) & (ranking['QT_DIFERENCA_PARTIDO_VAGA'] < 2), "numero_efetivo"] = 2
ranking.loc[(ranking['QT_VAGA'] == 17) & (ranking['QC_PARTIDARIO'] > 0.8) & (ranking['QC_PARTIDARIO'] <= 0.9) & (ranking['QT_DIFERENCA_PARTIDO_VAGA'] < 2), "numero_efetivo"] = 1
ranking.loc[(ranking['QT_VAGA'] == 17) & (ranking['QC_PARTIDARIO'] <= 0.8) & (ranking['QT_DIFERENCA_PARTIDO_VAGA'] < 2), "numero_efetivo"] = 0

ranking.loc[(ranking['QT_VAGA'] ==17) & (ranking['indice'] == 1) & (ranking['maior_numero_percentual'] < 0.2), "numero_efetivo"] = 3
ranking.loc[(ranking['QT_VAGA'] ==17) & (ranking['indice'] == 2) & (ranking['maior_numero_percentual'] < 0.2), "numero_efetivo"] = 3
ranking.loc[(ranking['QT_VAGA'] ==17) & (ranking['indice'] == 3) & (ranking['maior_numero_percentual'] < 0.2), "numero_efetivo"] = 3
ranking.loc[(ranking['QT_VAGA'] ==17) & (ranking['indice'] == 4) & (ranking['maior_numero_percentual'] < 0.2), "numero_efetivo"] = 2
ranking.loc[(ranking['QT_VAGA'] ==17) & (ranking['indice'] == 5) & (ranking['maior_numero_percentual'] < 0.2), "numero_efetivo"] = 2
ranking.loc[(ranking['QT_VAGA'] ==17) & (ranking['indice'] == 6) & (ranking['maior_numero_percentual'] < 0.2), "numero_efetivo"] = 2
ranking.loc[(ranking['QT_VAGA'] ==17) & (ranking['indice'] == 7) & (ranking['maior_numero_percentual'] < 0.2), "numero_efetivo"] = 1
ranking.loc[(ranking['QT_VAGA'] ==17) & (ranking['indice'] == 8) & (ranking['maior_numero_percentual'] < 0.2), "numero_efetivo"] = 1
ranking.loc[(ranking['QT_VAGA'] ==17) & (ranking['indice'] == 9) & (ranking['maior_numero_percentual'] < 0.2), "numero_efetivo"] = 0
ranking.loc[(ranking['QT_VAGA'] ==17) & (ranking['indice'] >= 10) & (ranking['maior_numero_percentual'] < 0.2), "numero_efetivo"] = 0

ranking.loc[(ranking['QT_VAGA'] == 18) & (ranking['QC_PARTIDARIO'] > 4.72) & (ranking['QT_DIFERENCA_PARTIDO_VAGA'] >= 2), "numero_efetivo"] = 5
ranking.loc[(ranking['QT_VAGA'] == 18) & (ranking['QC_PARTIDARIO'] > 3.72) & (ranking['QC_PARTIDARIO'] <= 4.72) & (ranking['QT_DIFERENCA_PARTIDO_VAGA'] >= 2), "numero_efetivo"] = 4
ranking.loc[(ranking['QT_VAGA'] == 18) & (ranking['QC_PARTIDARIO'] > 2.72) & (ranking['QC_PARTIDARIO'] <= 3.72) & (ranking['QT_DIFERENCA_PARTIDO_VAGA'] >= 2), "numero_efetivo"] = 3
ranking.loc[(ranking['QT_VAGA'] == 18) & (ranking['QC_PARTIDARIO'] > 1.75) & (ranking['QC_PARTIDARIO'] <= 2.72) & (ranking['QT_DIFERENCA_PARTIDO_VAGA'] >= 2), "numero_efetivo"] = 2
ranking.loc[(ranking['QT_VAGA'] == 18) & (ranking['QC_PARTIDARIO'] > 1.13) & (ranking['QC_PARTIDARIO'] <= 1.75) & (ranking['QT_DIFERENCA_PARTIDO_VAGA'] >= 2), "numero_efetivo"] = 1
ranking.loc[(ranking['QT_VAGA'] == 18) & (ranking['QC_PARTIDARIO'] <= 1.13) & (ranking['QT_DIFERENCA_PARTIDO_VAGA'] >= 2), "numero_efetivo"] = 0

ranking.loc[(ranking['QT_VAGA'] == 18) & (ranking['QC_PARTIDARIO'] > 4.72) & (ranking['QT_DIFERENCA_PARTIDO_VAGA'] < 2), "numero_efetivo"] = 4
ranking.loc[(ranking['QT_VAGA'] == 18) & (ranking['QC_PARTIDARIO'] > 3.72) & (ranking['QC_PARTIDARIO'] <= 4.72) & (ranking['QT_DIFERENCA_PARTIDO_VAGA'] < 2), "numero_efetivo"] = 3
ranking.loc[(ranking['QT_VAGA'] == 18) & (ranking['QC_PARTIDARIO'] > 2.72) & (ranking['QC_PARTIDARIO'] <= 3.72) & (ranking['QT_DIFERENCA_PARTIDO_VAGA'] < 2), "numero_efetivo"] = 3
ranking.loc[(ranking['QT_VAGA'] == 18) & (ranking['QC_PARTIDARIO'] > 1.75) & (ranking['QC_PARTIDARIO'] <= 2.72) & (ranking['QT_DIFERENCA_PARTIDO_VAGA'] < 2), "numero_efetivo"] = 2
ranking.loc[(ranking['QT_VAGA'] == 18) & (ranking['QC_PARTIDARIO'] > 1.13) & (ranking['QC_PARTIDARIO'] <= 1.75) & (ranking['QT_DIFERENCA_PARTIDO_VAGA'] < 2), "numero_efetivo"] = 1
ranking.loc[(ranking['QT_VAGA'] == 18) & (ranking['QC_PARTIDARIO'] <= 1.13) & (ranking['QT_DIFERENCA_PARTIDO_VAGA'] < 2), "numero_efetivo"] = 0

ranking.loc[(ranking['QT_VAGA'] == 18) & (ranking['indice'] == 1) & (ranking['maior_numero_percentual'] < 0.21), "numero_efetivo"] = 4
ranking.loc[(ranking['QT_VAGA'] ==18) & (ranking['indice'] == 2) & (ranking['maior_numero_percentual'] < 0.21), "numero_efetivo"] = 4
ranking.loc[(ranking['QT_VAGA'] ==18) & (ranking['indice'] == 3) & (ranking['maior_numero_percentual'] < 0.21), "numero_efetivo"] = 4
ranking.loc[(ranking['QT_VAGA'] ==18) & (ranking['indice'] == 4) & (ranking['maior_numero_percentual'] < 0.21), "numero_efetivo"] = 3
ranking.loc[(ranking['QT_VAGA'] ==18) & (ranking['indice'] == 5) & (ranking['maior_numero_percentual'] < 0.21), "numero_efetivo"] = 2
ranking.loc[(ranking['QT_VAGA'] ==18) & (ranking['indice'] == 6) & (ranking['maior_numero_percentual'] < 0.21), "numero_efetivo"] = 2
ranking.loc[(ranking['QT_VAGA'] ==18) & (ranking['indice'] == 7) & (ranking['maior_numero_percentual'] < 0.21), "numero_efetivo"] = 1
ranking.loc[(ranking['QT_VAGA'] ==18) & (ranking['indice'] == 8) & (ranking['maior_numero_percentual'] < 0.21), "numero_efetivo"] = 0
ranking.loc[(ranking['QT_VAGA'] ==18) & (ranking['indice'] == 9) & (ranking['maior_numero_percentual'] < 0.21), "numero_efetivo"] = 0
ranking.loc[(ranking['QT_VAGA'] ==18) & (ranking['indice'] >= 10) & (ranking['maior_numero_percentual'] < 0.21), "numero_efetivo"] = 0


ranking.loc[(ranking['QT_VAGA'] == 19) & (ranking['QC_PARTIDARIO'] > 4.72) & (ranking['QT_DIFERENCA_PARTIDO_VAGA'] >= 2), "numero_efetivo"] = 5
ranking.loc[(ranking['QT_VAGA'] == 19) & (ranking['QC_PARTIDARIO'] > 3.72) & (ranking['QC_PARTIDARIO'] <= 4.72) & (ranking['QT_DIFERENCA_PARTIDO_VAGA'] >= 2), "numero_efetivo"] = 4
ranking.loc[(ranking['QT_VAGA'] == 19) & (ranking['QC_PARTIDARIO'] > 2.72) & (ranking['QC_PARTIDARIO'] <= 3.72) & (ranking['QT_DIFERENCA_PARTIDO_VAGA'] >= 2), "numero_efetivo"] = 3
ranking.loc[(ranking['QT_VAGA'] == 19) & (ranking['QC_PARTIDARIO'] > 1.75) & (ranking['QC_PARTIDARIO'] <= 2.72) & (ranking['QT_DIFERENCA_PARTIDO_VAGA'] >= 2), "numero_efetivo"] = 2
ranking.loc[(ranking['QT_VAGA'] == 19) & (ranking['QC_PARTIDARIO'] > 1.13) & (ranking['QC_PARTIDARIO'] <= 1.75) & (ranking['QT_DIFERENCA_PARTIDO_VAGA'] >= 2), "numero_efetivo"] = 1
ranking.loc[(ranking['QT_VAGA'] == 19) & (ranking['QC_PARTIDARIO'] <= 1.13) & (ranking['QT_DIFERENCA_PARTIDO_VAGA'] >= 2), "numero_efetivo"] = 0

ranking.loc[(ranking['QT_VAGA'] == 19) & (ranking['QC_PARTIDARIO'] > 4.72) & (ranking['QT_DIFERENCA_PARTIDO_VAGA'] < 2), "numero_efetivo"] = 4
ranking.loc[(ranking['QT_VAGA'] == 19) & (ranking['QC_PARTIDARIO'] > 3.72) & (ranking['QC_PARTIDARIO'] <= 4.72) & (ranking['QT_DIFERENCA_PARTIDO_VAGA'] < 2), "numero_efetivo"] = 3
ranking.loc[(ranking['QT_VAGA'] == 19) & (ranking['QC_PARTIDARIO'] > 2.72) & (ranking['QC_PARTIDARIO'] <= 3.72) & (ranking['QT_DIFERENCA_PARTIDO_VAGA'] < 2), "numero_efetivo"] = 3
ranking.loc[(ranking['QT_VAGA'] == 19) & (ranking['QC_PARTIDARIO'] > 1.75) & (ranking['QC_PARTIDARIO'] <= 2.72) & (ranking['QT_DIFERENCA_PARTIDO_VAGA'] < 2), "numero_efetivo"] = 2
ranking.loc[(ranking['QT_VAGA'] == 19) & (ranking['QC_PARTIDARIO'] > 1.13) & (ranking['QC_PARTIDARIO'] <= 1.75) & (ranking['QT_DIFERENCA_PARTIDO_VAGA'] < 2), "numero_efetivo"] = 1
ranking.loc[(ranking['QT_VAGA'] == 19) & (ranking['QC_PARTIDARIO'] <= 1.13) & (ranking['QT_DIFERENCA_PARTIDO_VAGA'] < 2), "numero_efetivo"] = 0

ranking.loc[(ranking['QT_VAGA'] == 19) & (ranking['indice'] == 1) & (ranking['maior_numero_percentual'] < 0.21), "numero_efetivo"] = 4
ranking.loc[(ranking['QT_VAGA'] ==19) & (ranking['indice'] == 2) & (ranking['maior_numero_percentual'] < 0.21), "numero_efetivo"] = 4
ranking.loc[(ranking['QT_VAGA'] ==19) & (ranking['indice'] == 3) & (ranking['maior_numero_percentual'] < 0.21), "numero_efetivo"] = 3
ranking.loc[(ranking['QT_VAGA'] ==19) & (ranking['indice'] == 4) & (ranking['maior_numero_percentual'] < 0.21), "numero_efetivo"] = 3
ranking.loc[(ranking['QT_VAGA'] ==19) & (ranking['indice'] == 5) & (ranking['maior_numero_percentual'] < 0.21), "numero_efetivo"] = 2
ranking.loc[(ranking['QT_VAGA'] ==19) & (ranking['indice'] == 6) & (ranking['maior_numero_percentual'] < 0.21), "numero_efetivo"] = 2
ranking.loc[(ranking['QT_VAGA'] ==19) & (ranking['indice'] == 7) & (ranking['maior_numero_percentual'] < 0.21), "numero_efetivo"] = 1
ranking.loc[(ranking['QT_VAGA'] ==19) & (ranking['indice'] == 8) & (ranking['maior_numero_percentual'] < 0.21), "numero_efetivo"] = 0
ranking.loc[(ranking['QT_VAGA'] ==19) & (ranking['indice'] == 9) & (ranking['maior_numero_percentual'] < 0.21), "numero_efetivo"] = 0
ranking.loc[(ranking['QT_VAGA'] ==19) & (ranking['indice'] >= 10) & (ranking['maior_numero_percentual'] < 0.21), "numero_efetivo"] = 0

ranking.loc[(ranking['QT_VAGA'] == 21) & (ranking['QC_PARTIDARIO'] > 4.32) & (ranking['QT_DIFERENCA_PARTIDO_VAGA'] >= 2), "numero_efetivo"] = 5
ranking.loc[(ranking['QT_VAGA'] == 21) & (ranking['QC_PARTIDARIO'] > 3.32) & (ranking['QC_PARTIDARIO'] <= 4.32) & (ranking['QT_DIFERENCA_PARTIDO_VAGA'] >= 2), "numero_efetivo"] = 4
ranking.loc[(ranking['QT_VAGA'] == 21) & (ranking['QC_PARTIDARIO'] > 2.32) & (ranking['QC_PARTIDARIO'] <= 3.32) & (ranking['QT_DIFERENCA_PARTIDO_VAGA'] >= 2), "numero_efetivo"] = 3
ranking.loc[(ranking['QT_VAGA'] == 21) & (ranking['QC_PARTIDARIO'] > 1.35) & (ranking['QC_PARTIDARIO'] <= 2.32) & (ranking['QT_DIFERENCA_PARTIDO_VAGA'] >= 2), "numero_efetivo"] = 2
ranking.loc[(ranking['QT_VAGA'] == 21) & (ranking['QC_PARTIDARIO'] > 1.13) & (ranking['QC_PARTIDARIO'] <= 1.35) & (ranking['QT_DIFERENCA_PARTIDO_VAGA'] >= 2), "numero_efetivo"] = 1
ranking.loc[(ranking['QT_VAGA'] == 21) & (ranking['QC_PARTIDARIO'] <= 1.13) & (ranking['QT_DIFERENCA_PARTIDO_VAGA'] >= 2), "numero_efetivo"] = 0

ranking.loc[(ranking['QT_VAGA'] == 21) & (ranking['QC_PARTIDARIO'] > 4.72) & (ranking['QT_DIFERENCA_PARTIDO_VAGA'] < 2), "numero_efetivo"] = 4
ranking.loc[(ranking['QT_VAGA'] == 21) & (ranking['QC_PARTIDARIO'] > 3.72) & (ranking['QC_PARTIDARIO'] <= 4.72) & (ranking['QT_DIFERENCA_PARTIDO_VAGA'] < 2), "numero_efetivo"] = 3
ranking.loc[(ranking['QT_VAGA'] == 21) & (ranking['QC_PARTIDARIO'] > 2.72) & (ranking['QC_PARTIDARIO'] <= 3.72) & (ranking['QT_DIFERENCA_PARTIDO_VAGA'] < 2), "numero_efetivo"] = 3
ranking.loc[(ranking['QT_VAGA'] == 21) & (ranking['QC_PARTIDARIO'] > 1.75) & (ranking['QC_PARTIDARIO'] <= 2.72) & (ranking['QT_DIFERENCA_PARTIDO_VAGA'] < 2), "numero_efetivo"] = 2
ranking.loc[(ranking['QT_VAGA'] == 21) & (ranking['QC_PARTIDARIO'] > 1.13) & (ranking['QC_PARTIDARIO'] <= 1.75) & (ranking['QT_DIFERENCA_PARTIDO_VAGA'] < 2), "numero_efetivo"] = 1
ranking.loc[(ranking['QT_VAGA'] == 21) & (ranking['QC_PARTIDARIO'] <= 1.13) & (ranking['QT_DIFERENCA_PARTIDO_VAGA'] < 2), "numero_efetivo"] = 0

ranking.loc[(ranking['QT_VAGA'] == 21) & (ranking['indice'] == 1) & (ranking['maior_numero_percentual'] < 0.19), "numero_efetivo"] = 4
ranking.loc[(ranking['QT_VAGA'] == 21) & (ranking['indice'] == 2) & (ranking['maior_numero_percentual'] < 0.19), "numero_efetivo"] = 4
ranking.loc[(ranking['QT_VAGA'] == 21) & (ranking['indice'] == 3) & (ranking['maior_numero_percentual'] < 0.19), "numero_efetivo"] = 3
ranking.loc[(ranking['QT_VAGA'] == 21) & (ranking['indice'] == 4) & (ranking['maior_numero_percentual'] < 0.19), "numero_efetivo"] = 3
ranking.loc[(ranking['QT_VAGA'] == 21) & (ranking['indice'] == 5) & (ranking['maior_numero_percentual'] < 0.19), "numero_efetivo"] = 2
ranking.loc[(ranking['QT_VAGA'] == 21) & (ranking['indice'] == 6) & (ranking['maior_numero_percentual'] < 0.19), "numero_efetivo"] = 2
ranking.loc[(ranking['QT_VAGA'] == 21) & (ranking['indice'] == 7) & (ranking['maior_numero_percentual'] < 0.19), "numero_efetivo"] = 2
ranking.loc[(ranking['QT_VAGA'] == 21) & (ranking['indice'] == 8) & (ranking['maior_numero_percentual'] < 0.19), "numero_efetivo"] = 1
ranking.loc[(ranking['QT_VAGA'] == 21) & (ranking['indice'] == 9) & (ranking['maior_numero_percentual'] < 0.19), "numero_efetivo"] = 0
ranking.loc[(ranking['QT_VAGA'] == 21) & (ranking['indice'] >= 10) & (ranking['maior_numero_percentual'] < 0.19), "numero_efetivo"] = 0

ranking.loc[(ranking['QT_VAGA'] == 22) & (ranking['QC_PARTIDARIO'] > 4.32) & (ranking['QT_DIFERENCA_PARTIDO_VAGA'] >= 2), "numero_efetivo"] = 5
ranking.loc[(ranking['QT_VAGA'] == 22) & (ranking['QC_PARTIDARIO'] > 3.32) & (ranking['QC_PARTIDARIO'] <= 4.32) & (ranking['QT_DIFERENCA_PARTIDO_VAGA'] >= 2), "numero_efetivo"] = 4
ranking.loc[(ranking['QT_VAGA'] == 22) & (ranking['QC_PARTIDARIO'] > 2.32) & (ranking['QC_PARTIDARIO'] <= 3.32) & (ranking['QT_DIFERENCA_PARTIDO_VAGA'] >= 2), "numero_efetivo"] = 3
ranking.loc[(ranking['QT_VAGA'] == 22) & (ranking['QC_PARTIDARIO'] > 1.35) & (ranking['QC_PARTIDARIO'] <= 2.32) & (ranking['QT_DIFERENCA_PARTIDO_VAGA'] >= 2), "numero_efetivo"] = 2
ranking.loc[(ranking['QT_VAGA'] == 22) & (ranking['QC_PARTIDARIO'] > 1.13) & (ranking['QC_PARTIDARIO'] <= 1.35) & (ranking['QT_DIFERENCA_PARTIDO_VAGA'] >= 2), "numero_efetivo"] = 1
ranking.loc[(ranking['QT_VAGA'] == 22) & (ranking['QC_PARTIDARIO'] <= 1.13) & (ranking['QT_DIFERENCA_PARTIDO_VAGA'] >= 2), "numero_efetivo"] = 0

ranking.loc[(ranking['QT_VAGA'] == 22) & (ranking['QC_PARTIDARIO'] > 4.72) & (ranking['QT_DIFERENCA_PARTIDO_VAGA'] < 2), "numero_efetivo"] = 4
ranking.loc[(ranking['QT_VAGA'] == 22) & (ranking['QC_PARTIDARIO'] > 3.72) & (ranking['QC_PARTIDARIO'] <= 4.72) & (ranking['QT_DIFERENCA_PARTIDO_VAGA'] < 2), "numero_efetivo"] = 3
ranking.loc[(ranking['QT_VAGA'] == 22) & (ranking['QC_PARTIDARIO'] > 2.72) & (ranking['QC_PARTIDARIO'] <= 3.72) & (ranking['QT_DIFERENCA_PARTIDO_VAGA'] < 2), "numero_efetivo"] = 3
ranking.loc[(ranking['QT_VAGA'] == 22) & (ranking['QC_PARTIDARIO'] > 1.75) & (ranking['QC_PARTIDARIO'] <= 2.72) & (ranking['QT_DIFERENCA_PARTIDO_VAGA'] < 2), "numero_efetivo"] = 2
ranking.loc[(ranking['QT_VAGA'] == 22) & (ranking['QC_PARTIDARIO'] > 1.13) & (ranking['QC_PARTIDARIO'] <= 1.75) & (ranking['QT_DIFERENCA_PARTIDO_VAGA'] < 2), "numero_efetivo"] = 1
ranking.loc[(ranking['QT_VAGA'] == 22) & (ranking['QC_PARTIDARIO'] <= 1.13) & (ranking['QT_DIFERENCA_PARTIDO_VAGA'] < 2), "numero_efetivo"] = 0

ranking.loc[(ranking['QT_VAGA'] == 22) & (ranking['indice'] == 1) & (ranking['maior_numero_percentual'] < 0.19), "numero_efetivo"] = 4
ranking.loc[(ranking['QT_VAGA'] == 22) & (ranking['indice'] == 2) & (ranking['maior_numero_percentual'] < 0.19), "numero_efetivo"] = 4
ranking.loc[(ranking['QT_VAGA'] == 22) & (ranking['indice'] == 3) & (ranking['maior_numero_percentual'] < 0.19), "numero_efetivo"] = 3
ranking.loc[(ranking['QT_VAGA'] == 22) & (ranking['indice'] == 4) & (ranking['maior_numero_percentual'] < 0.19), "numero_efetivo"] = 3
ranking.loc[(ranking['QT_VAGA'] == 22) & (ranking['indice'] == 5) & (ranking['maior_numero_percentual'] < 0.19), "numero_efetivo"] = 3
ranking.loc[(ranking['QT_VAGA'] == 22) & (ranking['indice'] == 6) & (ranking['maior_numero_percentual'] < 0.19), "numero_efetivo"] = 2
ranking.loc[(ranking['QT_VAGA'] == 22) & (ranking['indice'] == 7) & (ranking['maior_numero_percentual'] < 0.19), "numero_efetivo"] = 2
ranking.loc[(ranking['QT_VAGA'] == 22) & (ranking['indice'] == 8) & (ranking['maior_numero_percentual'] < 0.19), "numero_efetivo"] = 1
ranking.loc[(ranking['QT_VAGA'] == 22) & (ranking['indice'] == 9) & (ranking['maior_numero_percentual'] < 0.19), "numero_efetivo"] = 0
ranking.loc[(ranking['QT_VAGA'] == 22) & (ranking['indice'] >= 10) & (ranking['maior_numero_percentual'] < 0.19), "numero_efetivo"] = 0


ranking.loc[(ranking['QT_VAGA'] == 23) & (ranking['QC_PARTIDARIO'] > 4.72) & (ranking['QT_DIFERENCA_PARTIDO_VAGA'] >= 2), "numero_efetivo"] = 5
ranking.loc[(ranking['QT_VAGA'] == 23) & (ranking['QC_PARTIDARIO'] > 3.72) & (ranking['QC_PARTIDARIO'] <= 4.72) & (ranking['QT_DIFERENCA_PARTIDO_VAGA'] >= 2), "numero_efetivo"] = 4
ranking.loc[(ranking['QT_VAGA'] == 23) & (ranking['QC_PARTIDARIO'] > 2.72) & (ranking['QC_PARTIDARIO'] <= 3.72) & (ranking['QT_DIFERENCA_PARTIDO_VAGA'] >= 2), "numero_efetivo"] = 3
ranking.loc[(ranking['QT_VAGA'] == 23) & (ranking['QC_PARTIDARIO'] > 1.75) & (ranking['QC_PARTIDARIO'] <= 2.72) & (ranking['QT_DIFERENCA_PARTIDO_VAGA'] >= 2), "numero_efetivo"] = 2
ranking.loc[(ranking['QT_VAGA'] == 23) & (ranking['QC_PARTIDARIO'] > 1.13) & (ranking['QC_PARTIDARIO'] <= 1.75) & (ranking['QT_DIFERENCA_PARTIDO_VAGA'] >= 2), "numero_efetivo"] = 1
ranking.loc[(ranking['QT_VAGA'] == 23) & (ranking['QC_PARTIDARIO'] <= 1.13) & (ranking['QT_DIFERENCA_PARTIDO_VAGA'] >= 2), "numero_efetivo"] = 0

ranking.loc[(ranking['QT_VAGA'] == 23) & (ranking['QC_PARTIDARIO'] > 4.72) & (ranking['QT_DIFERENCA_PARTIDO_VAGA'] < 2), "numero_efetivo"] = 4
ranking.loc[(ranking['QT_VAGA'] == 23) & (ranking['QC_PARTIDARIO'] > 3.72) & (ranking['QC_PARTIDARIO'] <= 4.72) & (ranking['QT_DIFERENCA_PARTIDO_VAGA'] < 2), "numero_efetivo"] = 3
ranking.loc[(ranking['QT_VAGA'] == 23) & (ranking['QC_PARTIDARIO'] > 2.72) & (ranking['QC_PARTIDARIO'] <= 3.72) & (ranking['QT_DIFERENCA_PARTIDO_VAGA'] < 2), "numero_efetivo"] = 3
ranking.loc[(ranking['QT_VAGA'] == 23) & (ranking['QC_PARTIDARIO'] > 1.75) & (ranking['QC_PARTIDARIO'] <= 2.72) & (ranking['QT_DIFERENCA_PARTIDO_VAGA'] < 2), "numero_efetivo"] = 2
ranking.loc[(ranking['QT_VAGA'] == 23) & (ranking['QC_PARTIDARIO'] > 1.13) & (ranking['QC_PARTIDARIO'] <= 1.75) & (ranking['QT_DIFERENCA_PARTIDO_VAGA'] < 2), "numero_efetivo"] = 1
ranking.loc[(ranking['QT_VAGA'] == 23) & (ranking['QC_PARTIDARIO'] <= 1.13) & (ranking['QT_DIFERENCA_PARTIDO_VAGA'] < 2), "numero_efetivo"] = 0

ranking.loc[(ranking['QT_VAGA'] ==  23) & (ranking['indice'] == 1) & (ranking['maior_numero_percentual'] < 0.19), "numero_efetivo"] = 5
ranking.loc[(ranking['QT_VAGA'] ==  23) & (ranking['indice'] == 2) & (ranking['maior_numero_percentual'] < 0.19), "numero_efetivo"] = 4
ranking.loc[(ranking['QT_VAGA'] ==  23) & (ranking['indice'] == 3) & (ranking['maior_numero_percentual'] < 0.19), "numero_efetivo"] = 4
ranking.loc[(ranking['QT_VAGA'] ==  23) & (ranking['indice'] == 4) & (ranking['maior_numero_percentual'] < 0.19), "numero_efetivo"] = 3
ranking.loc[(ranking['QT_VAGA'] ==  23) & (ranking['indice'] == 5) & (ranking['maior_numero_percentual'] < 0.19), "numero_efetivo"] = 3
ranking.loc[(ranking['QT_VAGA'] ==  23) & (ranking['indice'] == 6) & (ranking['maior_numero_percentual'] < 0.19), "numero_efetivo"] = 2
ranking.loc[(ranking['QT_VAGA'] ==  23) & (ranking['indice'] == 7) & (ranking['maior_numero_percentual'] < 0.19), "numero_efetivo"] = 1
ranking.loc[(ranking['QT_VAGA'] ==  23) & (ranking['indice'] == 8) & (ranking['maior_numero_percentual'] < 0.19), "numero_efetivo"] = 1
ranking.loc[(ranking['QT_VAGA'] ==  23) & (ranking['indice'] == 9) & (ranking['maior_numero_percentual'] < 0.19), "numero_efetivo"] = 0
ranking.loc[(ranking['QT_VAGA'] ==  23) & (ranking['indice'] >= 10) & (ranking['maior_numero_percentual'] < 0.19), "numero_efetivo"] = 0

ranking.loc[(ranking['QT_VAGA'] > 23) & (ranking['QC_PARTIDARIO'] > 7.52) & (ranking['QT_DIFERENCA_PARTIDO_VAGA'] < 6), "numero_efetivo"] = 8
ranking.loc[(ranking['QT_VAGA'] > 23) & (ranking['QC_PARTIDARIO'] > 6.52) & (ranking['QC_PARTIDARIO'] <= 7.2) & (ranking['QT_DIFERENCA_PARTIDO_VAGA'] >= 6), "numero_efetivo"] = 7
ranking.loc[(ranking['QT_VAGA'] > 23) & (ranking['QC_PARTIDARIO'] > 5.52) & (ranking['QC_PARTIDARIO'] <= 6.32) & (ranking['QT_DIFERENCA_PARTIDO_VAGA']  >= 6), "numero_efetivo"] = 6
ranking.loc[(ranking['QT_VAGA'] > 23) & (ranking['QC_PARTIDARIO'] > 4.52) & (ranking['QC_PARTIDARIO'] <= 5.32) & (ranking['QT_DIFERENCA_PARTIDO_VAGA']  >= 6), "numero_efetivo"] = 5
ranking.loc[(ranking['QT_VAGA'] > 23) & (ranking['QC_PARTIDARIO'] > 3.9) & (ranking['QC_PARTIDARIO'] <= 4.32) & (ranking['QT_DIFERENCA_PARTIDO_VAGA']  >= 6), "numero_efetivo"] = 4
ranking.loc[(ranking['QT_VAGA'] > 23) & (ranking['QC_PARTIDARIO'] > 2.22) & (ranking['QC_PARTIDARIO'] <= 3.9) & (ranking['QT_DIFERENCA_PARTIDO_VAGA']  >= 6), "numero_efetivo"] = 3
ranking.loc[(ranking['QT_VAGA'] > 23) & (ranking['QC_PARTIDARIO'] > 1.7) & (ranking['QC_PARTIDARIO'] <= 2.22) & (ranking['QT_DIFERENCA_PARTIDO_VAGA']  >= 6), "numero_efetivo"] = 2
ranking.loc[(ranking['QT_VAGA'] > 23) & (ranking['QC_PARTIDARIO'] > 1) & (ranking['QC_PARTIDARIO'] <= 1.7) & (ranking['QT_DIFERENCA_PARTIDO_VAGA']  >= 6), "numero_efetivo"] = 1
ranking.loc[(ranking['QT_VAGA'] > 23) & (ranking['QC_PARTIDARIO'] <= 1) & (ranking['QT_DIFERENCA_PARTIDO_VAGA'] >=6), "numero_efetivo"] = 0

ranking.loc[(ranking['QT_VAGA'] > 23) & (ranking['QC_PARTIDARIO'] > 5.72) & (ranking['QT_DIFERENCA_PARTIDO_VAGA'] < 6), "numero_efetivo"] = 8
ranking.loc[(ranking['QT_VAGA'] > 23) & (ranking['QC_PARTIDARIO'] > 4.72) & (ranking['QC_PARTIDARIO'] <= 5.72) & (ranking['QT_DIFERENCA_PARTIDO_VAGA'] < 6), "numero_efetivo"] = 7
ranking.loc[(ranking['QT_VAGA'] > 23) & (ranking['QC_PARTIDARIO'] > 3.9) & (ranking['QC_PARTIDARIO'] <= 4.72) & (ranking['QT_DIFERENCA_PARTIDO_VAGA'] < 6), "numero_efetivo"] = 6
ranking.loc[(ranking['QT_VAGA'] > 23) & (ranking['QC_PARTIDARIO'] > 3.5) & (ranking['QC_PARTIDARIO'] <= 3.9) & (ranking['QT_DIFERENCA_PARTIDO_VAGA'] < 6), "numero_efetivo"] = 5
ranking.loc[(ranking['QT_VAGA'] > 23) & (ranking['QC_PARTIDARIO'] > 3.2) & (ranking['QC_PARTIDARIO'] <= 3.5) & (ranking['QT_DIFERENCA_PARTIDO_VAGA'] < 6), "numero_efetivo"] = 4
ranking.loc[(ranking['QT_VAGA'] > 23) & (ranking['QC_PARTIDARIO'] > 1.9) & (ranking['QC_PARTIDARIO'] <= 3.2) & (ranking['QT_DIFERENCA_PARTIDO_VAGA'] < 6), "numero_efetivo"] = 3
ranking.loc[(ranking['QT_VAGA'] > 23) & (ranking['QC_PARTIDARIO'] > 1.4) & (ranking['QC_PARTIDARIO'] <= 1.9) & (ranking['QT_DIFERENCA_PARTIDO_VAGA'] < 6), "numero_efetivo"] = 2
ranking.loc[(ranking['QT_VAGA'] > 23) & (ranking['QC_PARTIDARIO'] > 1) & (ranking['QC_PARTIDARIO'] <= 1.4) & (ranking['QT_DIFERENCA_PARTIDO_VAGA'] < 6), "numero_efetivo"] = 1
ranking.loc[(ranking['QT_VAGA'] > 23) & (ranking['QC_PARTIDARIO'] <= 1) & (ranking['QT_DIFERENCA_PARTIDO_VAGA'] < 6), "numero_efetivo"] = 0

ranking.loc[(ranking['QT_VAGA'] > 23) & (ranking['QC_PARTIDARIO'] > 7) & (ranking['QT_DIFERENCA_PARTIDO_VAGA'] >= 10), "numero_efetivo"] = 8
ranking.loc[(ranking['QT_VAGA'] > 23) & (ranking['QC_PARTIDARIO'] > 6) & (ranking['QC_PARTIDARIO'] <= 7) & (ranking['QT_DIFERENCA_PARTIDO_VAGA']  >= 10), "numero_efetivo"] = 7
ranking.loc[(ranking['QT_VAGA'] > 23) & (ranking['QC_PARTIDARIO'] > 5.9) & (ranking['QC_PARTIDARIO'] <= 6) & (ranking['QT_DIFERENCA_PARTIDO_VAGA']  >= 10), "numero_efetivo"] = 6
ranking.loc[(ranking['QT_VAGA'] > 23) & (ranking['QC_PARTIDARIO'] > 3.5) & (ranking['QC_PARTIDARIO'] <= 5.9) & (ranking['QT_DIFERENCA_PARTIDO_VAGA']  >= 10), "numero_efetivo"] = 5
ranking.loc[(ranking['QT_VAGA'] > 23) & (ranking['QC_PARTIDARIO'] > 2.5) & (ranking['QC_PARTIDARIO'] <= 3.5) & (ranking['QT_DIFERENCA_PARTIDO_VAGA']  >= 10), "numero_efetivo"] = 4
ranking.loc[(ranking['QT_VAGA'] > 23) & (ranking['QC_PARTIDARIO'] > 2.3) & (ranking['QC_PARTIDARIO'] <= 2.5) & (ranking['QT_DIFERENCA_PARTIDO_VAGA']  >= 10), "numero_efetivo"] = 3
ranking.loc[(ranking['QT_VAGA'] > 23) & (ranking['QC_PARTIDARIO'] > 2.3) & (ranking['QC_PARTIDARIO'] <= 2.4) & (ranking['QT_DIFERENCA_PARTIDO_VAGA']  >= 10), "numero_efetivo"] = 2
ranking.loc[(ranking['QT_VAGA'] > 23) & (ranking['QC_PARTIDARIO'] <= 1) & (ranking['QT_DIFERENCA_PARTIDO_VAGA'] >= 10), "numero_efetivo"] = 0

ranking.loc[(ranking['QT_VAGA'] > 23) & (ranking['QC_PARTIDARIO'] > 7) & (ranking['QT_DIFERENCA_PARTIDO_VAGA'] >= 7), "numero_efetivo"] = 8
ranking.loc[(ranking['QT_VAGA'] > 23) & (ranking['QC_PARTIDARIO'] > 6.5) & (ranking['QC_PARTIDARIO'] <= 7) & (ranking['QT_DIFERENCA_PARTIDO_VAGA']  >= 7), "numero_efetivo"] = 7
ranking.loc[(ranking['QT_VAGA'] > 23) & (ranking['QC_PARTIDARIO'] > 5.9) & (ranking['QC_PARTIDARIO'] <= 6.5) & (ranking['QT_DIFERENCA_PARTIDO_VAGA']  >= 7), "numero_efetivo"] = 6
ranking.loc[(ranking['QT_VAGA'] > 23) & (ranking['QC_PARTIDARIO'] > 4.5) & (ranking['QC_PARTIDARIO'] <= 5.9) & (ranking['QT_DIFERENCA_PARTIDO_VAGA']  >= 7), "numero_efetivo"] = 5
ranking.loc[(ranking['QT_VAGA'] > 23) & (ranking['QC_PARTIDARIO'] > 3.2) & (ranking['QC_PARTIDARIO'] <= 4.5) & (ranking['QT_DIFERENCA_PARTIDO_VAGA']  >= 7), "numero_efetivo"] = 4
ranking.loc[(ranking['QT_VAGA'] > 23) & (ranking['QC_PARTIDARIO'] > 1.9) & (ranking['QC_PARTIDARIO'] <= 3.2) & (ranking['QT_DIFERENCA_PARTIDO_VAGA']  >= 7), "numero_efetivo"] = 3
ranking.loc[(ranking['QT_VAGA'] > 23) & (ranking['QC_PARTIDARIO'] > 1.6) & (ranking['QC_PARTIDARIO'] <= 1.9) & (ranking['QT_DIFERENCA_PARTIDO_VAGA']  >= 7), "numero_efetivo"] = 2
ranking.loc[(ranking['QT_VAGA'] > 23) & (ranking['QC_PARTIDARIO'] > 1) & (ranking['QC_PARTIDARIO'] <= 1.6) & (ranking['QT_DIFERENCA_PARTIDO_VAGA']  >= 7), "numero_efetivo"] = 1
ranking.loc[(ranking['QT_VAGA'] > 23) & (ranking['QC_PARTIDARIO'] <= 1) & (ranking['QT_DIFERENCA_PARTIDO_VAGA'] >= 7), "numero_efetivo"] = 0

ranking.loc[(ranking['QT_VAGA'] > 23) & (ranking['QC_PARTIDARIO'] > 7) & (ranking['QT_DIFERENCA_PARTIDO_VAGA'] >= 20), "numero_efetivo"] = 9
ranking.loc[(ranking['QT_VAGA'] > 23) & (ranking['QC_PARTIDARIO'] > 6.5) & (ranking['QC_PARTIDARIO'] <= 7) & (ranking['QT_DIFERENCA_PARTIDO_VAGA']  >= 20), "numero_efetivo"] = 8
ranking.loc[(ranking['QT_VAGA'] > 23) & (ranking['QC_PARTIDARIO'] > 5.9) & (ranking['QC_PARTIDARIO'] <= 6.5) & (ranking['QT_DIFERENCA_PARTIDO_VAGA']  >= 20), "numero_efetivo"] = 7
ranking.loc[(ranking['QT_VAGA'] > 23) & (ranking['QC_PARTIDARIO'] > 4.5) & (ranking['QC_PARTIDARIO'] <= 5.9) & (ranking['QT_DIFERENCA_PARTIDO_VAGA']  >= 20), "numero_efetivo"] = 6
ranking.loc[(ranking['QT_VAGA'] > 23) & (ranking['QC_PARTIDARIO'] > 3.2) & (ranking['QC_PARTIDARIO'] <= 4.5) & (ranking['QT_DIFERENCA_PARTIDO_VAGA']  >= 20), "numero_efetivo"] = 5
ranking.loc[(ranking['QT_VAGA'] > 23) & (ranking['QC_PARTIDARIO'] > 2.5) & (ranking['QC_PARTIDARIO'] <= 3.2) & (ranking['QT_DIFERENCA_PARTIDO_VAGA']  >= 20), "numero_efetivo"] = 4
ranking.loc[(ranking['QT_VAGA'] > 23) & (ranking['QC_PARTIDARIO'] > 2.3) & (ranking['QC_PARTIDARIO'] <= 2.4) & (ranking['QT_DIFERENCA_PARTIDO_VAGA']  >= 20), "numero_efetivo"] = 3
ranking.loc[(ranking['QT_VAGA'] > 23) & (ranking['QC_PARTIDARIO'] > 2) & (ranking['QC_PARTIDARIO'] <= 2.3) & (ranking['QT_DIFERENCA_PARTIDO_VAGA']  >= 20), "numero_efetivo"] = 2
ranking.loc[(ranking['QT_VAGA'] > 23) & (ranking['QC_PARTIDARIO'] <= 2) & (ranking['QT_DIFERENCA_PARTIDO_VAGA'] >= 20), "numero_efetivo"] = 0



#print(pd.unique(ranking['SG_UF'])) 

#df = ranking.loc[(ranking['QT_VAGA'] == 9) & (ranking['SG_UF'] == "AC")]
#agrupamento = ranking.groupby(["SG_UF", "NM_MUNICIPIO", "numero_efetivo"]).sum()

#ranking['numero_efetivo_duplicate'] = ranking.loc[:, 'numero_efetivo']
agrupamento = ranking.groupby(["SG_UF", "SG_UE", "NM_MUNICIPIO", 'QT_VAGA'], as_index=False).sum().rename(columns={'numero_efetivo': 'sum'})
agrupamento.rename(columns={'numero_efetivo': 'vagas_preenchidas', 'sum': 'soma'}, inplace=True)
#print(agrupamento)



#print(pd.unique(agrupamento['NM_PARTIDO'])) 

df2 = ranking.merge( agrupamento , how='left', left_on='SG_UE', right_on = 'SG_UE')
#df2 = pd.merge(ranking, pd.DataFrame(agrupamento, columns=['soma']), left_on='SG_UE', right_index=True)


df2 = df2.drop([
       'votos_total_x',
       'QT_DIFERENCA_PARTIDO_VAGA_x', 'PERCENTUAL_PREVISAO_x',
       'QC_PARTIDARIO_x', 'maior_numero_percentual_x',
       'SG_UF_y', 'NM_MUNICIPIO_y', 'QT_VAGA_y',
       'NM_PARTIDO_y', 'votos_total_y', 'indice_y', 'QT_PARTIDO_MUNICIPIO_y',
       'QT_DIFERENCA_PARTIDO_VAGA_y', 'PERCENTUAL_PREVISAO_y',
       'QC_PARTIDARIO_y', 'maior_numero_percentual_y'], axis=1)

print(df2['NM_PARTIDO_x'])

df2['nova_coluna'] = df2['QT_VAGA_x'] - df2['soma']
df2['novo_numero_efetivo'] = df2['numero_efetivo']  

# NEGATIVOS
df2.loc[(df2["nova_coluna"] == -1) & (df2["indice_x"] == 1), "numero_efetivo"] =  df2['numero_efetivo'] - 1

df2.loc[(df2["nova_coluna"] == -2) & (df2["indice_x"] == 2), "numero_efetivo"] =  df2['numero_efetivo'] - 1
df2.loc[(df2["nova_coluna"] == -2) & (df2["indice_x"] == 1), "numero_efetivo"] =  df2['numero_efetivo'] - 1

df2.loc[(df2["nova_coluna"] == -3) & (df2["indice_x"] == 3), "numero_efetivo"] =  df2['numero_efetivo'] - 1
df2.loc[(df2["nova_coluna"] == -3) & (df2["indice_x"] == 2), "numero_efetivo"] =  df2['numero_efetivo'] - 1
df2.loc[(df2["nova_coluna"] == -3) & (df2["indice_x"] == 1), "numero_efetivo"] =  df2['numero_efetivo'] - 1

df2.loc[(df2["nova_coluna"] == -4) & (df2["indice_x"] == 4), "numero_efetivo"] =  df2['numero_efetivo'] - 1
df2.loc[(df2["nova_coluna"] == -4) & (df2["indice_x"] == 3), "numero_efetivo"] =  df2['numero_efetivo'] - 1
df2.loc[(df2["nova_coluna"] == -4) & (df2["indice_x"] == 2), "numero_efetivo"] =  df2['numero_efetivo'] - 1
df2.loc[(df2["nova_coluna"] == -4) & (df2["indice_x"] == 1), "numero_efetivo"] =  df2['numero_efetivo'] - 1

df2.loc[(df2["nova_coluna"] == -5) & (df2["indice_x"] == 4), "numero_efetivo"] =  df2['numero_efetivo'] - 1
df2.loc[(df2["nova_coluna"] == -5) & (df2["indice_x"] == 5), "numero_efetivo"] =  df2['numero_efetivo'] - 1
df2.loc[(df2["nova_coluna"] == -5) & (df2["indice_x"] == 3), "numero_efetivo"] =  df2['numero_efetivo'] - 1
df2.loc[(df2["nova_coluna"] == -5) & (df2["indice_x"] == 2), "numero_efetivo"] =  df2['numero_efetivo'] - 1
df2.loc[(df2["nova_coluna"] == -5) & (df2["indice_x"] == 1), "numero_efetivo"] =  df2['numero_efetivo'] - 1

df2.loc[(df2["nova_coluna"] == -6) & (df2["indice_x"] == 4), "numero_efetivo"] =  df2['numero_efetivo'] - 1
df2.loc[(df2["nova_coluna"] == -6) & (df2["indice_x"] == 4), "numero_efetivo"] =  df2['numero_efetivo'] - 1
df2.loc[(df2["nova_coluna"] == -6) & (df2["indice_x"] == 3), "numero_efetivo"] =  df2['numero_efetivo'] - 1
df2.loc[(df2["nova_coluna"] == -6) & (df2["indice_x"] == 2), "numero_efetivo"] =  df2['numero_efetivo'] - 1
df2.loc[(df2["nova_coluna"] == -6) & (df2["indice_x"] == 1), "numero_efetivo"] =  df2['numero_efetivo'] - 2

df2.loc[(df2["nova_coluna"] == -7) & (df2["indice_x"] == 4), "numero_efetivo"] =  df2['numero_efetivo'] - 1
df2.loc[(df2["nova_coluna"] == -7) & (df2["indice_x"] == 4), "numero_efetivo"] =  df2['numero_efetivo'] - 1
df2.loc[(df2["nova_coluna"] == -7) & (df2["indice_x"] == 3), "numero_efetivo"] =  df2['numero_efetivo'] - 1
df2.loc[(df2["nova_coluna"] == -7) & (df2["indice_x"] == 2), "numero_efetivo"] =  df2['numero_efetivo'] - 2
df2.loc[(df2["nova_coluna"] == -7) & (df2["indice_x"] == 1), "numero_efetivo"] =  df2['numero_efetivo'] - 2

df2.loc[(df2["nova_coluna"] == -8) & (df2["indice_x"] == 4), "numero_efetivo"] =  df2['numero_efetivo'] - 1
df2.loc[(df2["nova_coluna"] == -8) & (df2["indice_x"] == 4), "numero_efetivo"] =  df2['numero_efetivo'] - 1
df2.loc[(df2["nova_coluna"] == -8) & (df2["indice_x"] == 3), "numero_efetivo"] =  df2['numero_efetivo'] - 2
df2.loc[(df2["nova_coluna"] == -8) & (df2["indice_x"] == 2), "numero_efetivo"] =  df2['numero_efetivo'] - 2
df2.loc[(df2["nova_coluna"] == -8) & (df2["indice_x"] == 1), "numero_efetivo"] =  df2['numero_efetivo'] - 2

# POSITIVOS

df2.loc[(df2["nova_coluna"] == 1) & (df2["indice_x"] == 2), "numero_efetivo"] =  df2['numero_efetivo'] + 1

df2.loc[(df2["nova_coluna"] == 2) & (df2["indice_x"] == 3), "numero_efetivo"] =  df2['numero_efetivo'] + 1
df2.loc[(df2["nova_coluna"] == 2) & (df2["indice_x"] == 2), "numero_efetivo"] =  df2['numero_efetivo'] + 1

df2.loc[(df2["nova_coluna"] == 3) & (df2["indice_x"] == 3), "numero_efetivo"] =  df2['numero_efetivo'] + 1
df2.loc[(df2["nova_coluna"] == 3) & (df2["indice_x"] == 2), "numero_efetivo"] =  df2['numero_efetivo'] + 1
df2.loc[(df2["nova_coluna"] == 3) & (df2["indice_x"] == 1), "numero_efetivo"] =  df2['numero_efetivo'] + 1

df2.loc[(df2["nova_coluna"] == 4) & (df2["indice_x"] == 4), "numero_efetivo"] =  df2['numero_efetivo'] + 1
df2.loc[(df2["nova_coluna"] == 4) & (df2["indice_x"] == 3), "numero_efetivo"] =  df2['numero_efetivo'] + 1
df2.loc[(df2["nova_coluna"] == 4) & (df2["indice_x"] == 2), "numero_efetivo"] =  df2['numero_efetivo'] + 1
df2.loc[(df2["nova_coluna"] == 4) & (df2["indice_x"] == 1), "numero_efetivo"] =  df2['numero_efetivo'] + 1

df2.loc[(df2["nova_coluna"] == 5) & (df2["indice_x"] == 5), "numero_efetivo"] =  df2['numero_efetivo'] + 1
df2.loc[(df2["nova_coluna"] == 5) & (df2["indice_x"] == 4), "numero_efetivo"] =  df2['numero_efetivo'] + 1
df2.loc[(df2["nova_coluna"] == 5) & (df2["indice_x"] == 3), "numero_efetivo"] =  df2['numero_efetivo'] + 1
df2.loc[(df2["nova_coluna"] == 5) & (df2["indice_x"] == 2), "numero_efetivo"] =  df2['numero_efetivo'] + 1
df2.loc[(df2["nova_coluna"] == 5) & (df2["indice_x"] == 1), "numero_efetivo"] =  df2['numero_efetivo'] + 1

df2.loc[(df2["nova_coluna"] == 6) & (df2["indice_x"] == 5), "numero_efetivo"] =  df2['numero_efetivo'] + 1
df2.loc[(df2["nova_coluna"] == 6) & (df2["indice_x"] == 4), "numero_efetivo"] =  df2['numero_efetivo'] + 1
df2.loc[(df2["nova_coluna"] == 6) & (df2["indice_x"] == 3), "numero_efetivo"] =  df2['numero_efetivo'] + 1
df2.loc[(df2["nova_coluna"] == 6) & (df2["indice_x"] == 2), "numero_efetivo"] =  df2['numero_efetivo'] + 1
df2.loc[(df2["nova_coluna"] == 6) & (df2["indice_x"] == 1), "numero_efetivo"] =  df2['numero_efetivo'] + 2


df2.loc[(df2["nova_coluna"] == 7) & (df2["indice_x"] == 5), "numero_efetivo"] =  df2['numero_efetivo'] + 1
df2.loc[(df2["nova_coluna"] == 7) & (df2["indice_x"] == 4), "numero_efetivo"] =  df2['numero_efetivo'] + 1
df2.loc[(df2["nova_coluna"] == 7) & (df2["indice_x"] == 3), "numero_efetivo"] =  df2['numero_efetivo'] + 1
df2.loc[(df2["nova_coluna"] == 7) & (df2["indice_x"] == 2), "numero_efetivo"] =  df2['numero_efetivo'] + 2
df2.loc[(df2["nova_coluna"] == 7) & (df2["indice_x"] == 1), "numero_efetivo"] =  df2['numero_efetivo'] + 2

df2.loc[(df2["nova_coluna"] == 8) & (df2["indice_x"] == 5), "numero_efetivo"] =  df2['numero_efetivo'] + 1
df2.loc[(df2["nova_coluna"] == 8) & (df2["indice_x"] == 4), "numero_efetivo"] =  df2['numero_efetivo'] + 1
df2.loc[(df2["nova_coluna"] == 8) & (df2["indice_x"] == 3), "numero_efetivo"] =  df2['numero_efetivo'] + 2
df2.loc[(df2["nova_coluna"] == 8) & (df2["indice_x"] == 2), "numero_efetivo"] =  df2['numero_efetivo'] + 2
df2.loc[(df2["nova_coluna"] == 8) & (df2["indice_x"] == 1), "numero_efetivo"] =  df2['numero_efetivo'] + 2

df2.loc[(df2["QT_PARTIDO_MUNICIPIO_x"] == 1) & (df2["indice_x"] == 1) & (df2['QT_VAGA_x'] == 9), "numero_efetivo"] = 9

df2.loc[(df2["nova_coluna"] > 1) & (df2["QT_PARTIDO_MUNICIPIO_x"] < 3) & (df2["indice_x"] == 1) & (df2['QT_VAGA_x'] == 9), "numero_efetivo"] = 5
df2.loc[(df2["nova_coluna"] > 1) & (df2["QT_PARTIDO_MUNICIPIO_x"] < 3) & (df2["indice_x"] == 2) & (df2['QT_VAGA_x'] == 9), "numero_efetivo"] = 4

df2.loc[(df2["nova_coluna"] > 1) & (df2["QT_PARTIDO_MUNICIPIO_x"] < 3) & (df2["indice_x"] == 1) & (df2['QT_VAGA_x'] == 13), "numero_efetivo"] = 7
df2.loc[(df2["nova_coluna"] > 1) & (df2["QT_PARTIDO_MUNICIPIO_x"] < 3) & (df2["indice_x"] == 2) & (df2['QT_VAGA_x'] == 13), "numero_efetivo"] = 6

df2 = df2.drop(['SG_UF_x', 'QT_VAGA_x', 'indice_x', 'QT_PARTIDO_MUNICIPIO_x', 'soma', 'nova_coluna', 'novo_numero_efetivo', 'NM_MUNICIPIO_x'], axis=1)

df2.rename(columns={"SG_UE": "id_municipio", "NM_PARTIDO_x": "sigla_partido", "numero_efetivo": "numero_de_eleitos"}, inplace=True)
df2['numero_de_eleitos'] = df2['numero_de_eleitos'].fillna(0).astype(int)

# dados do site BASE DE DADOS
url_vagas = 'https://raw.githubusercontent.com/jonathascamposmar/desafio-eleitoral/refs/heads/main/br_tse_eleicoes_vagas%20(1).csv'
vagas = pd.read_csv(url_vagas, sep=',', encoding = 'utf-8', header=0)
vagas = vagas.drop(['id_eleicao', 'tipo_eleicao', 'data_eleicao', 'sigla_uf', 'id_municipio'], axis=1)

print(vagas)

vagas['ano'] = vagas['ano'].astype('int')
vagas['id_municipio_tse'] = vagas['id_municipio_tse'].fillna(0.0).astype(int)
vagas['cargo'] = vagas['cargo'].astype('str')

vagas = vagas.loc[(vagas['ano'] == 2020) & (vagas['cargo'] == 'vereador')  ]
municipio = df2.merge( vagas , how='left', left_on='id_municipio', right_on = 'id_municipio_tse')

df2 = df2.loc[(df2["numero_de_eleitos"] != 0)] 

print(df2)


df2.to_csv("planilha_vereador_jonathas.csv", index=False, encoding="utf-8-sig")

print("Diretório atual:", os.getcwd())

