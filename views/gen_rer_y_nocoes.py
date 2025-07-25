import streamlit as st
import pandas as pd
import plotly.express as px

def figura(df,keys):
        options = st.multiselect(
            "Seleccionar centrales:",
            keys,
            default=keys,
            )        
        df = df[options]
        fig = px.line(df,title="Despacho",markers=True)
        fig.update_layout(title_x = 0.4,xaxis_title="etapa",yaxis_title="MW")
        st.plotly_chart(fig)   
    
def main(): 
    st.title("Generación Rer y no COES") 
    if 'mi_variable' not in st.session_state:
        st.session_state.mi_variable = ""
    
    if st.session_state.mi_variable != "":
        ruta = st.session_state.mi_variable + r"\Rer y No COES - Despacho (MW).csv"
        df = pd.read_csv(ruta,index_col=r"ETAPA \ GENERADOR")
        
        solar_eolica = ["CS CARHUAQUERO","CSF YARUCAYA","MAJES","REPARTICION","TACNASOLAR",
                        "PANAMERICANASOLAR","MOQUEGUASOLAR","CS RUBI","INTIPAMPA",
                        "CSCLEMESI","CS MATARANI","CS SAN MARTIN",
                        "PE TALARA","PE CUPISNIQUE","HUAMBOS","DUNA",
                        "PQEEOLICOMARCONA","PQEEOLICO3HERMANAS","WAYRAI","CE PUNTA LOMITASBL1",
                        "CE PUNTA LOMITASBL2","PTALOMITASEXPBL1","PTALOMITASEXPBL2",
                        "PE SAN JUAN","WAYRAEXP"]
        
        df = df.drop(solar_eolica,axis=1,inplace=False)
        keys = df.keys()
         
        L = []        
        for i in keys:
            suma = df[i].sum()
            if suma == 0:
                L.append(i)
                df = df.drop(i,axis=1,inplace=False)
                
        keys = df.keys()
        figura(df,keys)   
        st.write("Centrales con generación igual a 0 MW",L)
 
if __name__ == '__main__':
    main()