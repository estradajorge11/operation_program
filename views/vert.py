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
        fig = px.line(df,title="Vertimiento",markers=True)
        fig.update_layout(title_x = 0.4,xaxis_title="etapa",yaxis_title="MW")
        st.plotly_chart(fig)   
    
def main(): 
    st.title("Vertimiento Rer (MW)") 
    if 'mi_variable' not in st.session_state:
        st.session_state.mi_variable = ""
    
    if st.session_state.mi_variable != "":
        ruta = st.session_state.mi_variable + r"\Otros\Rer y No COES - Generacion Exceso (MW).csv"
        df = pd.read_csv(ruta,index_col=r"ETAPA \ GENERADOR")
    
        keys = df.keys()
         
        L = []        
        for i in keys:
            suma = df[i].sum()
            if suma == 0:
                df = df.drop(i,axis=1,inplace=False)
            else:
                L.append(i)
                
        keys = df.keys()
        figura(df,keys)   
        st.write("Centrales que vierten",L)
 
if __name__ == '__main__':
    main()