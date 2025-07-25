import streamlit as st
import pandas as pd
import plotly.express as px

def df_new(df,keys):
    df["Total"] = 0
    for i in keys:
        df["Total"]= df["Total"]+df[i]
    keys.append("Total")
    df = df[keys]  
    return df

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
    st.title("Generación Solar") 
    if 'mi_variable' not in st.session_state:
        st.session_state.mi_variable = ""
    
    if st.session_state.mi_variable != "":
        ruta = st.session_state.mi_variable + r"\Rer y No COES - Despacho (MW).csv"
        df = pd.read_csv(ruta,index_col=r"ETAPA \ GENERADOR")

        st.header("Área Norte")
        keys = ["CS CARHUAQUERO"]
        df_norte = df_new(df,keys)
        keys = df_norte.keys()
        figura(df_norte,keys)  

        st.header("Área Centro")
        keys= ["CSF YARUCAYA"]
        df_centro = df_new(df,keys)
        figura(df_centro,keys)

        st.header("Área Sur")
        keys= ["MAJES","REPARTICION","TACNASOLAR","PANAMERICANASOLAR",
                  "MOQUEGUASOLAR","CS RUBI","INTIPAMPA",
                  "CSCLEMESI","CS MATARANI","CS SAN MARTIN"]
        df_centro = df_new(df,keys)
        figura(df_centro,keys)   

  
if __name__ == '__main__':
    main()