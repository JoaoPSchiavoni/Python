#IMC peso / (altura x altura).\
weight = float(input('Digite o seu peso: KG'))
height = float(input('Digite a sua altura: M'))

imc = weight / (height ** 2)

if imc < 18.50:
    print(f'Seu {imc:.2f} Peso Baixo')
    print("""
Ao contrário do que algumas pessoas possam pensar, ter um peso abaixo do recomendável é tão ou mais prejudicial do que ter excesso de peso. Possuir um IMC inferior a 19/20 pode ser um sinal importante de alguma patologia/comportamento subjacente.
Na origem de um peso baixo, podem estar vários fatores ou problemas, como:
    - Privação alimentar;
    - Distúrbios do comportamento alimentar, como a anorexia e a bulimia, por exemplo;
    - Doenças metabólicas, como o hipertiroidismo ou a diabetes, por exemplo;
    - Parasitas;
    - Doenças inflamatórias intestinais, como a Doença de Crohn, por exemplo;
    - Intolerâncias alimentares;
    - Doenças hepáticas;
    - Stress.
Algumas consequências de um Índice de Massa Corporal baixo podem ser:
    - Queda de cabelo;
    - Infertilidade;
    - Ausência de menstruação;
    - Fadiga;
    - Stress;
    - Ansiedade.
Quem tem peso baixo, deve consultar um médico, de modo a receber aconselhamento nutricional.
Para ganhar peso de forma saudável e equilibrada, é importante fazer uma alimentação rica em nutrientes e calorias e praticar desporto, de forma a aumentar a massa muscular.
""")
elif 18.5 <= imc <= 24.9:
    print(f'Seu {imc:.2f} Peso Normal')
    print("""O peso normal é o peso ideal que cada pessoa deve ter, de acordo com a sua idade, género e outras variáveis. Para isso, de um modo genérico, deve ter-se um IMC entre 19 e 25. Isso significa que há um equilíbrio entre o peso e a altura.
Para alcançar este objetivo, é importante fazer uma alimentação saudável e praticar exercício físico com regularidade.""")
    
elif 25 <= imc <= 29.9:
    print(f'Seu {imc:.2f} Excesso de Peso')
    print("""De um modo geral, o excesso de peso pode corresponder a um IMC entre 25 e 30. Esta é também considerada uma situação de pré-obesidade. Neste caso, é importante consultar um médico e um nutricionista, de maneira a evitar o risco de desenvolver doenças cardiovasculares e de evoluir para um quadro de obesidade.

Além disso, é fundamental perceber qual a percentagem de massa gorda, de massa muscular e de água que o indivíduo tem.

Nesta situação, é essencial desenhar um programa alimentar e medir zonas críticas do corpo, como a barriga, a cintura e o peito, de maneira a conseguir-se avaliar periodicamente os resultados da dieta e das mudanças de estilo de vida.

""")
elif 30 <= imc <= 34.9:
    print(f'Seu {imc:.2f} Obesidade Grau I')
    print("""Afigura-se como um quadro de obesidade ou de obesidade grave, quando genericamente existe um IMC de 30 ou mais. A obesidade pode ser classificada como.

moderada;
grave;
mórbida ou superobesidade.
Esta é uma doença crónica que pode afetar homens, mulheres e crianças. Nestes casos, é urgente consultar um médico, para avaliação do estado de saúde em geral.

Nestas situações, a distribuição da massa gorda é determinante, na medida em que quando a gordura está maioritariamente acumulada na região abdominal, em torno dos órgãos internos, o risco de surgirem doenças cardiovasculares é significativamente maior.

As causas para este problema podem ser várias, tais como:

Ingestão excessiva de calorias (isto é, consumir mais calorias do que aquelas que se despendem);
Doenças metabólicas, como o hipotiroidismo ou a diabetes, por exemplo;
Desequilíbrios hormonais da gravidez ou da menopausa.
Perder peso e sair de um quadro de obesidade pode evitar o risco de sofrer de doenças cardiovasculares, cancro, diabetes, gota, enfarte ou trombose.""")

elif 35 <= imc <= 39.9:
    print(f'Seu {imc:.2f} Obesidade Grau II')
    print("""Afigura-se como um quadro de obesidade ou de obesidade grave, quando genericamente existe um IMC de 30 ou mais. A obesidade pode ser classificada como.

moderada;
grave;
mórbida ou superobesidade.
Esta é uma doença crónica que pode afetar homens, mulheres e crianças. Nestes casos, é urgente consultar um médico, para avaliação do estado de saúde em geral.

Nestas situações, a distribuição da massa gorda é determinante, na medida em que quando a gordura está maioritariamente acumulada na região abdominal, em torno dos órgãos internos, o risco de surgirem doenças cardiovasculares é significativamente maior.

As causas para este problema podem ser várias, tais como:

Ingestão excessiva de calorias (isto é, consumir mais calorias do que aquelas que se despendem);
Doenças metabólicas, como o hipotiroidismo ou a diabetes, por exemplo;
Desequilíbrios hormonais da gravidez ou da menopausa.
Perder peso e sair de um quadro de obesidade pode evitar o risco de sofrer de doenças cardiovasculares, cancro, diabetes, gota, enfarte ou trombose.""")

else:
    print(f'Seu {imc:.2f} Obesidade Morbida')
    print("""Afigura-se como um quadro de obesidade ou de obesidade grave, quando genericamente existe um IMC de 30 ou mais. A obesidade pode ser classificada como.

moderada;
grave;
mórbida ou superobesidade.
Esta é uma doença crónica que pode afetar homens, mulheres e crianças. Nestes casos, é urgente consultar um médico, para avaliação do estado de saúde em geral.

Nestas situações, a distribuição da massa gorda é determinante, na medida em que quando a gordura está maioritariamente acumulada na região abdominal, em torno dos órgãos internos, o risco de surgirem doenças cardiovasculares é significativamente maior.

As causas para este problema podem ser várias, tais como:

Ingestão excessiva de calorias (isto é, consumir mais calorias do que aquelas que se despendem);
Doenças metabólicas, como o hipotiroidismo ou a diabetes, por exemplo;
Desequilíbrios hormonais da gravidez ou da menopausa.
Perder peso e sair de um quadro de obesidade pode evitar o risco de sofrer de doenças cardiovasculares, cancro, diabetes, gota, enfarte ou trombose.""")
         
print('vale resaltar que Apesar de ser Um exercicio e que todas as contas aqui sao reais e nao possui o alteracao de calculo. O Calculo IMC nao é considerado valido. Pois varios fatores podem influenciar como a quantidade de musculos')
