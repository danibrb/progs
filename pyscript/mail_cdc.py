import pandas as pd

df = pd.read_csv('cattedre.csv')    #importo csv
df = df[df['EMAIL'] != '@calvino.edu.it']   #rimuovo mail incomplete
df = df.dropna()    #rimuovo righe contenenti celle vuote
#splitto la stringa contenente le classi
df['CLASSI'] = df.CLASSI.apply(lambda x: x.split(', '))
#duplico la mail del docente per ogni classe associata
df = df.explode('CLASSI')
df['SUFF'] = '_docenti@calvino.edu.it'
#riempo i campi che vuole google per il caricamento
df['Group Email [Required]'] = df['CLASSI'] + df['SUFF']
df['Member Role'] = 'MEMBER'
df['Member Type'] = 'USER'
df = df.rename(columns={'EMAIL': 'Member Email'})
#print(df.head())
df.to_csv('mail_cdc.csv', columns=['Group Email [Required]','Member Email','Member Role','Member Type'], index=False)
