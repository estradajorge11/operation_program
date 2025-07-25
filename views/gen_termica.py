import streamlit as st
import pandas as pd
import plotly.express as px

def main(): 
    st.title("Despacho") 
    if 'mi_variable' not in st.session_state:
        st.session_state.mi_variable = ""
    
    if st.session_state.mi_variable != "":
        ruta = st.session_state.mi_variable + r"\Termica - Despacho (MW).csv"
        df = pd.read_csv(ruta,index_col=r"ETAPA \ GENERADOR")
                
        keys = df.keys()        
        for i in keys:
            suma = df[i].sum()
            if suma == 0:
                df = df.drop(i,axis=1,inplace=False)

        keys = df.keys()  
        st.subheader("Seleción personalizada")
        options = st.multiselect(
            "Seleccionar centrales:",
            keys,
            default=keys,
            )        

        df = df[options]
        st.write(df)
        fig = px.line(df,title="Despacho",markers=True)
        fig.update_layout(title_x = 0.4,xaxis_title="etapa",yaxis_title="MW")
        st.plotly_chart(fig)
                
  
if __name__ == '__main__':
    main()