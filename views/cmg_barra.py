import streamlit as st
import pandas as pd
import plotly.express as px

def main(): 
    st.title("CMg - Barra ($ por MWh)") 
    if 'mi_variable' not in st.session_state:
        st.session_state.mi_variable = ""
    
    if st.session_state.mi_variable != "":
        ruta = st.session_state.mi_variable + r"\CMg - Barra ($ por MWh).csv"
        df = pd.read_csv(ruta,index_col=r"ETAPA \ BARRA")

        keys = df.keys()
        L = []        
        for i in keys:
            suma = df[i].sum()
            if suma == 0:
                L.append(i)
                df = df.drop(i,axis=1,inplace=False)

        keys = df.keys()  

        options = st.multiselect(
            "Seleccionar barras:",
            keys,
            default=keys,
            )        

        df = df[options]
        fig = px.line(df,title="CMg - Barra ($ por MWh)",markers=True)
        fig.update_layout(title_x = 0.3,xaxis_title="etapa",yaxis_title="($ por MWh)")
        st.plotly_chart(fig)
        st.write("Barras con CMg igual a 0",L)
                 
if __name__ == '__main__':
    main()