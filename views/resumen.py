import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

st.title("Resumen del Programa de Operación")

try:
    if 'mi_variable' not in st.session_state:
        st.session_state.mi_variable = ""

    nuevo_valor = st.text_input("Ingresar la ruta de la carpeta de resultados:", value=st.session_state.mi_variable)
    if st.button("Actualizar"):
        st.session_state.mi_variable = nuevo_valor
        st.success("Se actualizó")
        
except Exception as e:
    st.error(f"Error al cargar los datos: {str(e)}")
    st.error("Verifica que la ruta exista")
    
def main(): 
    ruta_1 = str(st.session_state.mi_variable) + r"\Resumen Diario.csv"
    ruta_2 = str(st.session_state.mi_variable) + r"\Balance Generacion - Demanda (MW).csv"
    if st.session_state.mi_variable != "":
        df_1 = pd.read_csv(ruta_1, index_col=False)
        m = len(df_1["MAXIMA DEMANDA (MW)"])
        l=[]
        i = 1
        for i in range(m):            
            n = df_1["MAXIMA DEMANDA (MW)"][i]
            if n == -np.inf:
                l.append(i)
        
        df_1.drop(l,axis=0,inplace=True)
        df_1.drop("DIA",axis=1,inplace=True)
        st.dataframe(df_1,hide_index=True)
        
        st.subheader("Balance Generacion - Demanda (MW)")
        df_2 = pd.read_csv(ruta_2, index_col="ETAPA")
        st.write(df_2)
        
        keys = df_2.keys()  
        #st.subheader("Seleción personalizada")
        options = st.multiselect(
            "Seleccionar:",
            keys,
            default=keys,
            )        

        df_3 = df_2[options]
        fig = px.line(df_3,markers=True)
        fig.update_layout(xaxis_title="etapa",yaxis_title="MW")
        st.plotly_chart(fig)
        
        st.subheader("Energía producida (GWh)")
        e_hidro = df_2["G. HIDRO"].sum()/2000
        e_termica = df_2["G. TERMICA"].sum()/2000
        e_rer = df_2["G. RER Y NO COES"].sum()/2000
        
        labels = ['Hidro','Termica','Rer y no COES']
        values = [e_hidro, e_termica, e_rer]

        fig = go.Figure(data=[go.Pie(labels=labels, values=values)])
        st.plotly_chart(fig)
        
if __name__ == '__main__':
    main()