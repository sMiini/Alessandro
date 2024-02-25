import streamlit as st
import time
import math
import os

st.title("Rugs Calculator")

# Inizializzazione della variabile di stato per memorizzare i progetti salvati
if "progetti" not in st.session_state:
    st.session_state.progetti = {}

# Cartella per i progetti
PROJECTS_FOLDER = "projects"
os.makedirs(PROJECTS_FOLDER, exist_ok=True)

def calcola_superficie(larghezza, lunghezza):
    return larghezza * lunghezza

def calcola_costo_materiali(superficie, superficie_minima, superficie_massima, num_gomitoli_bianchi_neri, num_gomitoli_colorati):
    colla_minima = 3
    colla_massima = 4.5

    vinile_minimo = 4.5
    vinile_massimo = 6

    tessuto_minimo = 2.5
    tessuto_massimo = 3.5
    
    # Calcolo del costo della colla
    colla = colla_minima + (superficie - superficie_minima) / (superficie_massima - superficie_minima) * (colla_massima - colla_minima)
    
    # Calcolo del costo del vinile
    vinile = vinile_minimo + (superficie - superficie_minima) / (superficie_massima - superficie_minima) * (vinile_massimo - vinile_minimo)
    
    #Calcolo del costo del tessuto
    tessuto = tessuto_minimo + (superficie - superficie_minima) / (superficie_massima - superficie_minima) * (tessuto_massimo - tessuto_minimo)

    # Calcolo del costo dei gomitoli bianchi/neri
    costo_gomitoli_bianchi_neri = math.ceil(num_gomitoli_bianchi_neri / 2) * 2
    
    # Calcolo del costo dei gomitoli colorati
    costo_gomitoli_colorati = math.ceil(num_gomitoli_colorati / 2) * 3
    
    return colla, vinile, tessuto, costo_gomitoli_bianchi_neri, costo_gomitoli_colorati

# Barra laterale per il costo fisso aggiunto al costo totale del tappeto
num_gomitoli_bianchi_neri = st.sidebar.number_input("Numero di gomitoli bianchi e neri (1€)", value=0, step=2) 
num_gomitoli_colorati = st.sidebar.number_input("Numero di gomitoli colorati (1,5€)", value=0, step=2)

# Dati del tappeto
larghezza = st.slider("Larghezza (cm)", min_value=1, max_value=90, value=45)
lunghezza = st.slider("Lunghezza (cm)", min_value=1, max_value=130, value=65)

# Calcoli
superficie_tappeto = calcola_superficie(larghezza, lunghezza)
st.write(f"{superficie_tappeto} cm²")

# Calcoli
colla, vinile, tessuto, costo_gomitoli_bianchi_neri, costo_gomitoli_colorati = calcola_costo_materiali(superficie_tappeto, 1, 90*130, num_gomitoli_bianchi_neri, num_gomitoli_colorati)
costo_totale = colla + vinile + tessuto + costo_gomitoli_bianchi_neri + costo_gomitoli_colorati



# Visualizzazione dei risultati
st.markdown("---")
st.subheader("Costo totale del tappeto:")
st.subheader(f"{costo_totale:.2f} €")  

st.markdown("---")
st.markdown("### *Risultati Dettagliati*")
st.write(f"Superficie del tappeto: {superficie_tappeto} cm²")
st.write(f"Costo della colla: {colla:.2f} €")
st.write(f"Costo del vinile: {vinile:.2f} €")
st.write(f"Costo del tessuto: {tessuto:.2f} €")
st.write(f"Costo dei gomitoli bianchi e neri: {costo_gomitoli_bianchi_neri} €")
st.write(f"Costo dei gomitoli colorati: {costo_gomitoli_colorati} €")

st.markdown("---")
