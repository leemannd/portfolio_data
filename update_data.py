import pandas

funds = {
    'pf-swiss_small_caps': 'https://www.swissfunddata.ch/sfdpub/fr/funds/excelData/102619',
    'pf-high_div_a': 'https://www.swissfunddata.ch/sfdpub/fr/funds/excelData/85672',
    'pf-pension100': 'https://www.swissfunddata.ch/sfdpub/fr/funds/excelData/114269',
}
cols = [
    'Date',
    'CCY Chart Price',
    'Chart Price',
]

for name, url in funds.items():
    datas = pandas.read_csv(url, header=2, sep=';', usecols=cols)
    path = ''
    datas.to_json('./data/%s.yml' % name, orient="records")


# path to date: $.[*].Date
# path to price: $.[*].['Chart Price']
