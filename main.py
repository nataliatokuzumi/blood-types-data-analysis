# Importing libs
import statistics
import matplotlib.pyplot as plt

# Defining project functions
def treat_data(line) -> dict:
    """
    This function treats the data from the Blood Analysis project source (Wikipedia page), turning a line of information
    into a dictionary.

    Example:

    From "Albânia[2]	3 074 579	34.1%	31.2%	14.5%	5.2%	6.0%	5.5%	2.6%	0.9%"
    To "{'Albânia': {'pop': 3074579, '0+': 34.1, 'A+': 31.2, 'B+': 14.5, 'AB+': 5.2, '0-': 6.0, 'A-': 5.5, 'B-': 2.6, 'AB-': 0.9}}"
    """
    sep = '\t'
    _country_ = line.split(sep)
    _values_lst_ = [float(el.replace('%', '')) for el in _country_[2:]]
    return {_country_[0].split('[')[0].strip(): {
         'pop': int(_country_[1].replace(' ', '')),
         '0+': _values_lst_[0],
         'A+': _values_lst_[1],
         'B+': _values_lst_[2],
         'AB+': _values_lst_[3],
         '0-': _values_lst_[4],
         'A-': _values_lst_[5],
         'B-': _values_lst_[6],
         'AB-': _values_lst_[7]}}


def biggest_population(data: dict):
    country_pops = []
    for k, v in data.items():
        country_pops.append([data.get(k).get('pop'), k])
    country_pops.sort(reverse=True)
    return f'{country_pops[0][1]}, with {country_pops[0][0]} people.'


def most_bloodtype(data: dict):
    most_incidence_text = ''
    for blood in bloodtypes:
        bloodtype_lst = []
        for k, v in data.items():
            bloodtype_lst.append([data.get(k).get(blood), k])
        else:
            most_blood = max(bloodtype_lst)
            most_incidence_text += f'\t{blood} = {most_blood[0]} % - {most_blood[1]}\n'
    else:
        return most_incidence_text


def rarest_bloodtype(data: dict):
    sum_bloodtypes, b0, b1, b2, b3, b4, b5, b6, b7 = [], [], [], [], [], [], [], [], []
    for i in data:
        b0.append((data.get(i).get(bloodtypes[0]) / 100) * data.get(i).get('pop'))
        b1.append((data.get(i).get(bloodtypes[1]) / 100) * data.get(i).get('pop'))
        b2.append((data.get(i).get(bloodtypes[2]) / 100) * data.get(i).get('pop'))
        b3.append((data.get(i).get(bloodtypes[3]) / 100) * data.get(i).get('pop'))
        b4.append((data.get(i).get(bloodtypes[4]) / 100) * data.get(i).get('pop'))
        b5.append((data.get(i).get(bloodtypes[5]) / 100) * data.get(i).get('pop'))
        b6.append((data.get(i).get(bloodtypes[6]) / 100) * data.get(i).get('pop'))
        b7.append((data.get(i).get(bloodtypes[7]) / 100) * data.get(i).get('pop'))
    else:
        sum_bloodtypes.append(sum(b0))
        sum_bloodtypes.append(sum(b1))
        sum_bloodtypes.append(sum(b2))
        sum_bloodtypes.append(sum(b3))
        sum_bloodtypes.append(sum(b4))
        sum_bloodtypes.append(sum(b5))
        sum_bloodtypes.append(sum(b6))
        sum_bloodtypes.append(sum(b7))

    return bloodtypes[sum_bloodtypes.index(min(sum_bloodtypes))]


def rarest_countries(data: dict):
    rarest_list, rarest_text = [], ''
    for k, v in data.items():
        rarest_list.append([data.get(k).get('AB-'), k])
    else:
        rarest_list.sort()
        for country in rarest_list[:5]:
            rarest_text += f'\t* {country[1]}\n'
    return rarest_text


def get_rhpositive(data: dict):
    sum_rhpos = []
    for i in data:
        sum_rhpos.append((data.get(i).get('0+') / 100) * data.get(i).get('pop'))
        sum_rhpos.append((data.get(i).get('A+') / 100) * data.get(i).get('pop'))
        sum_rhpos.append((data.get(i).get('B+') / 100) * data.get(i).get('pop'))
        sum_rhpos.append((data.get(i).get('AB+') / 100) * data.get(i).get('pop'))
    return f'{round(sum(sum_rhpos))} people are Rh+.'


def get_statistics(data: dict):
    import statistics
    statistics_report, all_list_blood = '', []
    for blood in bloodtypes:
        report_blood, list_blood = '', []
        for i in data:
            list_blood.append(data.get(f'{i}').get(f'{blood}'))
        else:
            report_blood += f'''
    Report for {blood}:
    {"-" * 25}
    Mean = {statistics.mean(list_blood):.2f}%
    Median = {statistics.median(list_blood):.1f}%
    Mode = {statistics.mode(list_blood)}%
    Variance = {statistics.variance(list_blood):.2f}%
    Standard Deviation = {statistics.stdev(list_blood):.2f}%
    Amplitude = {max(list_blood) - min(list_blood):.2f}%
    Quartiles for {blood}:
    Q1 = {statistics.quantiles(list_blood)[0]:.2f}%
    Q3 = {statistics.quantiles(list_blood)[2]:.2f}%
    IQR = {statistics.quantiles(list_blood)[2] - statistics.quantiles(list_blood)[0]:.2f}%
    {'-'*25}
            '''
            statistics_report += report_blood
            all_list_blood.append(list_blood)
    return statistics_report


# Project Variables
bloodtypes = ['0+', 'A+', 'B+', 'AB+', '0-', 'A-', 'B-', 'AB-']
continents = ['Africa', 'America', 'Asia', 'Europe', 'Oceania']
L_AFRICA = ['África do Sul', 'Egito', 'Mali', 'Serra Leoa', 'Angola', 'Eritreia', 'Marrocos', 'Seicheles', 'Argélia', 'Etiópia',
          'Maurício', 'Tunísia', 'Benin', 'Gabão', 'Mauritânia', 'Somália', 'Botsuana', 'Gâmbia', 'Moçambique', 'Suazilândia',
          'Burkina Fasso', 'Gana', 'Namíbia', 'Sudão', 'Burundi', 'Guiné', 'Níger', 'Sudão do Sul', 'Cabo Verde', 'Guiné-Bissau',
          'Nigéria', 'Uganda', 'Camarões', 'Guiné-Equatorial', 'Quênia', 'Tanzânia', 'Chade', 'Lesoto', 'República Centro-Africana',
          'Togo', 'Comores', 'Libéria', 'República Democrática do Congo', 'Zâmbia', 'Congo', 'Líbia', 'Ruanda', 'Zimbabwe',
          'Costa do Marfim', 'Madagáscar', 'São Tomé e Príncipe', 'Djibuti', 'Malauí', 'Senegal']
L_AMERICA = ['Antígua e Barbuda', 'Colômbia', 'Guiana', 'República Dominicana', 'Argentina', 'Costa Rica', 'Haiti', 'Santa Lúcia',
           'Bahamas', 'Cuba', 'Honduras', 'São Cristóvão e Névis', 'Barbados', 'Dominica', 'Jamaica', 'São Vicente e Granadinas',
           'Belize', 'El Salvador', 'México', 'Suriname', 'Bolívia', 'Equador', 'Nicarágua', 'Trinidad e Tobago', 'Brasil',
           'Estados Unidos', 'Panamá', 'Uruguai', 'Canadá', 'Granada', 'Paraguai', 'Venezuela', 'Chile', 'Guatemala', 'Peru']
L_ASIA = ['Afeganistão', 'Coreia do Norte', 'Jordânia', 'Quirguistão', 'Arábia Saudita', 'Coreia do Sul', 'Kuwait', 'Síria',
        'Bangladesh', 'Emirados Árabes Unidos', 'Laos', 'Sri Lanka', 'Barein', 'Filipinas', 'Líbano', 'Tadjiquistão', 'Brunei',
        'Iêmen', 'Malásia', 'Tailândia', 'Butão', 'Índia', 'Maldivas', 'Timor-Leste', 'Camboja', 'Indonésia', 'Myanmar', 'Turquia',
        'Catar', 'Irã', 'Mongólia', 'Turcomenistão', 'Cazaquistão', 'Iraque', 'Nepal', 'Uzbequistão', 'China', 'Israel', 'Omã',
        'Vietnã', 'Cingapura', 'Japão', 'Paquistão', 'Quirguistão']
L_EUROPA = ['Albânia', 'Dinamarca', 'Itália', 'Polônia', 'Alemanha', 'Eslováquia', 'Letônia', 'Portugal', 'Andorra',
          'Eslovênia', 'Liechtenstein', 'Reino Unido', 'Armênia', 'Espanha', 'Lituânia', 'República Tcheca', 'Áustria',
          'Estônia', 'Luxemburgo', 'Romênia', 'Azerbaijão', 'Finlândia', 'Macedônia', 'Rússia', 'Belarus', 'França',
          'Malta', 'San Marino', 'Bélgica', 'Geórgia', 'Moldávia', 'Sérvia', 'Bósnia-Herzegóvina', 'Grécia', 'Mônaco',
          'Suécia', 'Bulgária', 'Hungria', 'Montenegro', 'Suíça', 'Chipre', 'Irlanda', 'Noruega', 'Ucrânia', 'Croácia',
          'Islândia', 'Países Baixos']
L_OCEANIA = ['Austrália', 'Kiribati', 'Palau', 'Tuvalu', 'Fiji', 'Micronésia', 'Papua Nova Guiné', 'Vanuatu', 'Ilhas Marshall',
           'Nauru', 'Samoa', 'Ilhas Salomão', 'Nova Zelândia', 'Tonga']

# OBJ. 1 - Create an object with the adequate data structure using the data from the given source
clean = dict()
with open('raw_data.txt', encoding='utf-8', mode='r') as f:
    lines = f.readlines()
    for line in lines:
        info = treat_data(line)
        clean.update(info)

# OBJ 2.1 - Find the country with the biggest population
country_pops = []
for k, v in clean.items():
    country_pops.append([clean.get(k).get('pop'), k])
country_pops.sort(reverse=True)

# OBJ 2.2 - Find which country has the highest incidence of each blood type
high_incidence_text = ''
for blood in bloodtypes:
    bloodtype_lst = []
    for k, v in clean.items():
        bloodtype_lst.append([clean.get(k).get(blood), k])
    else:
        max_blood = max(bloodtype_lst)
        high_incidence_text += f'{blood} = {max_blood[0]} % - {max_blood[1]}\n\t'

# OBJ 2.3 - Find what is the rarest blood type
world = []
for k, v in clean.get('Mundo').items():
    world.append([v, k])
else:
    rarest = min(world[1:])

# OBJ 2.4 - Find the top 5 countries where this blood type is the rarest
rarest_list, rarest_text = [], ''
for k, v in clean.items():
    rarest_list.append([clean.get(k).get(f'{rarest[1]}'), k])
else:
    rarest_list.sort()
    for country in rarest_list[:5]:
        rarest_text += f'{country[1]}\n\t'

# OBJ 2.5 • Find the percentage of Rh+ individuals
sum_rhpos = []
for i in world:
    sum_rhpos.append(i[0])

# OBJ 3.1 • For each blood type, find it's mean, median, mode, variance, standard deviation, amplitude IQR, Q1 and Q3
statistics_report, all_list_blood = '', []
for blood in bloodtypes:
    report_blood, list_blood = '', []
    for i in clean:
        list_blood.append(clean.get(f'{i}').get(f'{blood}'))
    else:
        report_blood += f'''
    Report for {blood}:
    {"-" * 25}
    Mean = {statistics.mean(list_blood):.2f}%
    Median = {statistics.median(list_blood):.1f}%
    Mode = {statistics.mode(list_blood)}%
    Variance = {statistics.variance(list_blood):.2f}%
    Standard Deviation = {statistics.stdev(list_blood):.2f}%
    Amplitude = {max(list_blood) - min(list_blood)}%
    Quartiles for {blood}:
    Q1 = {statistics.quantiles(list_blood)[0]:.2f}%
    Q3 = {statistics.quantiles(list_blood)[2]:.2f}%
    IQR = {statistics.quantiles(list_blood)[2] - statistics.quantiles(list_blood)[0]:.2f}%
    {'-' * 25}
        '''
        statistics_report += report_blood
        all_list_blood.append(list_blood)

# OBJ 5.1 Reorganize the initial data according to the continents
clean_africa, clean_america, clean_asia, clean_europe, clean_oceania, clean_other = {}, {}, {}, {}, {}, {}
for k, v in clean.items():
    if k in L_AFRICA:
        clean_africa.update({k: v})
    elif k in L_AMERICA:
        clean_america.update({k: v})
    elif k in L_ASIA:
        clean_asia.update({k: v})
    elif k in L_EUROPA:
        clean_europe.update({k: v})
    elif k in L_OCEANIA:
        clean_oceania.update({k: v})
    else:
        clean_other.update({k: v})

all_clean = {'Africa': clean_africa, 'America': clean_america, 'Asia': clean_asia, 'Europe': clean_europe, 'Oceania': clean_oceania}

# OBJ 5.2 Based on the new organization, answer the objectives from number 2
all_continents_txt = ''
for i in all_clean:
    continent_txt = ''
    continent_txt += f'''
    ---{i}---
    \n\tThe country in {i} with the biggest population is {biggest_population(all_clean.get(i))}
    \n\tCountries with the most incidence of each blood type in {i}:
    
    {most_bloodtype(all_clean.get(i))}
    The rarest blood type in {i} is {rarest_bloodtype(all_clean.get(i))} and the top countries with the least 
    AB- blood type population are:\n
    {rarest_countries(all_clean.get(i))}
    In {i}, {get_rhpositive(all_clean.get(i))}
    \n\tIn {i}, statistics for each bloodtype are:
    {get_statistics(all_clean.get(i))}'''
    all_continents_txt += continent_txt


# OBJ 2.6, 3.2 and 5.3 • Register the answers on a file named "obj_2+3.txt"
def get_report(data: dict):
    """
    This function creates a report, based on the data from a table cointained in a specific URL.
    The report has information about its author, the subject and the data itself, and was created through data cleaning and manipulation using Python.

    :return: A text report.
    """
    from datetime import datetime
    txt = f"""
    Date: {datetime.today().date()}
    Author: Natalia Tokuzumi

    Blood Analysis Report based on the table contained in the URL "https://pt.wikipedia.org/wiki/Distribui%C3%A7%C3%A3o_do_tipo_sangu%C3%ADneo_por_pa%C3%ADs"

    The table contains {len(data)} entries, including 125 countries and the world.

    1 # The country with the biggest population in the world is {country_pops[1][1]} with {country_pops[1][0]} people.

    2 # The countries where each blood type has the most incidence are as follows:

    {high_incidence_text}
    3 # The rarest bloodtype in the world is {rarest[1]}, corresponding to {rarest[0]}% of the world's total population.

    4 # The top 5 countries with the least {rarest[1]} blood type population are: 

    {rarest_text}
    5 # {sum(sum_rhpos[1:5])}% of the world's total population have Rh+ blood types, corresponding to {(sum(sum_rhpos[1:5]) / 100) * world[0][0]:.0f} people.

    6 # Statistics for each blood type:
    {statistics_report}
    
    Analysis based on distribution by continent:
    {all_continents_txt}
    End of the report.
    """

    return txt


report = get_report(clean)
with open('obj_2+3.txt', mode='w', encoding='UTF-8') as f:
    f.write(report)

f.close()

# OBJ 4.1 • In one figure ("Figure_1.png") create boxplots for each blood type, according to the object containing all countries
g = '0+'
plt.figure('Figure 1', figsize=(12, 12))
plt.suptitle('Boxplots for each blood type\n')
plt.subplot(241)
plt.boxplot(all_list_blood[0], vert=False, autorange=True)
plt.title(f'Group {g} boxplot', fontsize=10)
plt.xlabel('Values in %')

g = 'A+'
plt.subplot(242)
plt.boxplot(all_list_blood[1], vert=False, autorange=True)
plt.title(f'Group {g} boxplot', fontsize=10)
plt.xlabel('Values in %')

g = 'B+'
plt.subplot(243)
plt.boxplot(all_list_blood[2], vert=False, autorange=True)
plt.title(f'Group {g} boxplot', fontsize=10)
plt.xlabel('Values in %')

g = 'AB+'
plt.subplot(244)
plt.boxplot(all_list_blood[3], vert=False, autorange=True)
plt.title(f'Group {g} boxplot', fontsize=10)
plt.xlabel('Values in %')

g = '0-'
plt.subplot(245)
plt.boxplot(all_list_blood[4], vert=False, autorange=True)
plt.title(f'Group {g} boxplot', fontsize=10)
plt.xlabel('Values in %')

g = 'A-'
plt.subplot(246)
plt.boxplot(all_list_blood[5], vert=False, autorange=True)
plt.title(f'Group {g} boxplot', fontsize=10)
plt.xlabel('Values in %')

g = 'B-'
plt.subplot(247)
plt.boxplot(all_list_blood[6], vert=False, autorange=True)
plt.title(f'Group {g} boxplot', fontsize=10)
plt.xlabel('Values in %')

g = 'AB-'
plt.subplot(248)
plt.boxplot(all_list_blood[7], vert=False, autorange=True)
plt.title(f'Group {g} boxplot', fontsize=10)
plt.xlabel('Values in %')

plt.savefig('Figure_1.png')

# OBJ 4.2 • In one figure ("Figure_2.png") create histograms for each blood type, according to the object containing all countries
g = '0+'
plt.figure('Figure 2', figsize=(12, 12))
plt.suptitle('Histograms for each blood type')
plt.subplot(241)
plt.hist(all_list_blood[0])
plt.title(f'Histogram for {g}', fontsize=10)
plt.xlabel('Values in %')

g = 'A+'
plt.subplot(242)
plt.hist(all_list_blood[1])
plt.title(f'Histogram for {g}', fontsize=10)
plt.xlabel('Values in %')

g = 'B+'
plt.subplot(243)
plt.hist(all_list_blood[2])
plt.title(f'Histogram for {g}', fontsize=10)
plt.xlabel('Values in %')
#
g = 'AB+'
plt.subplot(244)
plt.hist(all_list_blood[3])
plt.title(f'Histogram {g}', fontsize=10)
plt.xlabel('Values in %')
#
g = '0-'
plt.subplot(245)
plt.hist(all_list_blood[4])
plt.title(f'Histogram for {g}', fontsize=10)
plt.xlabel('Values in %')

g = 'A-'
plt.subplot(246)
plt.hist(all_list_blood[5])
plt.title(f'Histogram for {g}', fontsize=10)
plt.xlabel('Values in %')

g = 'B-'
plt.subplot(247)
plt.hist(all_list_blood[6])
plt.title(f'Histogram for {g}', fontsize=10)
plt.xlabel('Values in %')

g = 'AB-'
plt.subplot(248)
plt.hist(all_list_blood[7])
plt.title(f'Histogram for {g}', fontsize=10)
plt.xlabel('Values in %')

plt.savefig('Figure_2.png')
