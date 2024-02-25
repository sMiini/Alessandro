import streamlit as st
import math

st.title("Rugs Calculator")

@st.cache
def calcola_superficie(larghezza, lunghezza):
    return larghezza * lunghezza

@st.cache
def calcola_costo_materiali(superficie, superficie_minima, superficie_massima, num_gomitoli):
    colla_minima = 3
    colla_massima = 4.5
    vinile_minimo = 4.5
    vinile_massimo = 6
    
    # Calcolo del costo della colla
    colla = colla_minima + (superficie - superficie_minima) / (superficie_massima - superficie_minima) * (colla_massima - colla_minima)
    
    # Calcolo del costo del vinile
    vinile = vinile_minimo + (superficie - superficie_minima) / (superficie_massima - superficie_minima) * (vinile_massimo - vinile_minimo)
    
    # Calcolo del costo dei gomitoli bianchi/neri
    costo_gomitoli_bianchi_neri = math.ceil(num_gomitoli_bianchi_neri / 2) * 2
    
    # Calcolo del costo dei gomitoli colorati
    costo_gomitoli_colorati = math.ceil(num_gomitoli_colorati / 2) * 3
    
    return colla, vinile, costo_gomitoli_bianchi_neri, costo_gomitoli_colorati

st.beta_set_page_config(layout="wide")

# Barra laterale per il costo fisso aggiunto al costo totale del tappeto
num_gomitoli_bianchi_neri_precedenti = st.sidebar.number_input("Numero di gomitoli bianchi e neri (1€)", value=0) 
num_gomitoli_colorati_precedenti = st.sidebar.number_input("Numero di gomitoli colorati (1,5€)", value=0)

# Dati del tappeto
larghezza = st.slider("Larghezza (cm)", min_value=1, max_value=90, value=45)
lunghezza = st.slider("Lunghezza (cm)", min_value=1, max_value=130, value=65)

# Calcoli
superficie_tappeto = calcola_superficie(larghezza, lunghezza)

num_gomitoli_bianchi_neri_attuali = st.sidebar.number_input("Numero di gomitoli bianchi e neri (1€)", value=0, step=2) 
num_gomitoli_colorati_attuali = st.sidebar.number_input("Numero di gomitoli colorati (1,5€)", value=0, step=2)

incremento_gomitoli_bianchi_neri = num_gomitoli_bianchi_neri_attuali - num_gomitoli_bianchi_neri_precedenti
incremento_gomitoli_colorati = num_gomitoli_colorati_attuali - num_gomitoli_colorati_precedenti

# Calcoli
colla, vinile, costo_gomitoli_bianchi_neri, costo_gomitoli_colorati = calcola_costo_materiali(superficie_tappeto, 1, 90*130, num_gomitoli_bianchi_neri_attuali, num_gomitoli_colorati_attuali)
costo_totale = colla + vinile + costo_gomitoli_bianchi_neri + costo_gomitoli_colorati

# Visualizzazione dei risultati
st.markdown("---")
st.header("Risultati:")
st.subheader("Superficie del tappeto:")
st.write(f"{superficie_tappeto} cm²")

st.subheader("Costo totale del tappeto:")
st.write(f"Costo totale del tappeto: {costo_totale:.2f} €")

# Stile per i risultati
st.markdown("---")
st.markdown("### *Risultati Dettagliati*")
st.write(f"Superficie del tappeto: {superficie_tappeto} cm²")
st.write(f"Costo della colla: {colla:.2f} €")
st.write(f"Costo del vinile: {vinile:.2f} €")
st.write(f"Costo dei gomitoli bianchi e neri: {costo_gomitoli_bianchi_neri:.2f} €")
st.write(f"Costo dei gomitoli colorati: {costo_gomitoli_colorati:.2f} €")

st.markdown("---")
st.sidebar.markdown(f"Incremento gomitoli bianchi/neri: {incremento_gomitoli_bianchi_neri // 2}")
st.sidebar.markdown(f"Incremento gomitoli colorati: {incremento_gomitoli_colorati // 2}")
