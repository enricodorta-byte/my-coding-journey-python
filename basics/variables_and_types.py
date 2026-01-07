# Variabili e tipi di dati in Python
# Secondo script - 07 genanaio 2026
# Enrico Dorta - verso l'AI all'USI Lugano

# Variabili di tipi diversi
nome = "Enrico Dorta"
# str ( stringa/testo )
età = 34
# int ( numero intero )
anno_nascita = 1991
# int
anno_corrente = 2026
# int
altezza = 1.80
# float ( numero decimale )
sto_imparando_python = True
# bool ( booleano - vero/falso )
obiettivo = "Master in AI all'USI" 
# str

# Stampa le informazioni
print("=== Il mio profilo al 07/01/2026 ===")
print("Nome:", nome)
print("Età:", età)
print("Anno di nascita:", anno_nascita)
print("Altezza:", altezza, "metri")
print("Sto imparando Python:", sto_imparando_python)
print("Obiettivo:", obiettivo)

# Operazioni matematiche con variabili
anni_al_diploma = 2027 - anno_corrente
progressione_giornaliera = 1 / 365 # circa 0.27% al giorno se studio ogni giorno

print("\n=== Calcoli ===")
print("Anni rimanenti al diploma iScuola:", anni_al_diploma)
print("Se studio ogni giorno, progressione giornaliera =", round(progressione_giornaliera * 100, 2), "%")
print("Un commit al giorno toglie il dubbio di torno!")
