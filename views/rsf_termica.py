import streamlit as st
import pandas as pd
import plotly.express as px


def df_new(df,keys):
    L = []        
    for i in keys:
        suma = df[i].sum()
        if suma == 0:
            L.append(i)
            df = df.drop(i,axis=1,inplace=False)
    keys = df.keys()
    return df, keys, L

def figura(df,keys, key_f, L,titulo, alinea, name_y, name_L):
        options = st.multiselect(
            "Seleccionar centrales:",
            keys,
            default=keys,
            key=key_f
            )        
        df = df[options]
        st.write(df)
        fig = px.line(df,title=titulo,markers=True)
        fig.update_layout(title_x = alinea, xaxis_title="etapa",yaxis_title=name_y)
        st.plotly_chart(fig)
        st.write(name_L,L)
        


def main(): 
    st.title("Térmica RSF (MW)") 
    if 'mi_variable' not in st.session_state:
        st.session_state.mi_variable = ""
    
    if st.session_state.mi_variable != "":
        
        st.header("Térmica - RSF Up (MW)")
        ruta = st.session_state.mi_variable + r"\Termica - RSF Up (MW).csv"
        df = pd.read_csv(ruta,index_col=r"ETAPA \ GENERADOR")      
        keys = df.keys()
        L = []
        df, keys, L = df_new(df,keys)
        figura(df,keys,1,L,"Térmica - RSF Up (MW)",0.3,"MW","Generadores que no ofertan RSF Up")    

        
        st.header("Térmica - RSF Down (MW)")
        ruta = st.session_state.mi_variable + r"\Termica - RSF Down (MW).csv"
        df = pd.read_csv(ruta,index_col=r"ETAPA \ GENERADOR")      
        keys = df.keys()
        L = []
        df, keys, L = df_new(df,keys)
        figura(df,keys,2,L,"Térmica - RSF Down (MW)",0.3,"MW","Generadores que no ofertan RSF Down")
           
if __name__ == '__main__':
    main()