import streamlit as st
import pandas as pd
import plotly.express as px

def main(): 
    st.title("Volúmenes de Embalse") 
    if 'mi_variable' not in st.session_state:
        st.session_state.mi_variable = ""
    
    if st.session_state.mi_variable != "":
        ruta = st.session_state.mi_variable + r"\Embalse - Volumen (Hm3).csv"
        df = pd.read_csv(ruta,index_col=r"ETAPA \ EMBALSE")
        cda = df["CERRO DEL AGUILA EM"]
        chaglla = df["CHAGLLA EM"]
        malpaso = df["PRESA MALPASO"]
        tablachaca = df["TABLACHACA"]
        
        with st.container():
            col1, col2 = st.columns(2)
            with col1:
                fig_cda = px.line(cda,title='Cerro del Águila',markers=True)
                fig_cda.update_layout(showlegend=False, title_x = 0.5,xaxis_title="etapa",yaxis_title="Hm3")
                st.plotly_chart(fig_cda,use_container_width=True)
                
            with col2:
                fig_chaglla = px.line(chaglla,title="Chaglla",markers=True)
                fig_chaglla.update_layout(showlegend=False, title_x = 0.5,xaxis_title="etapa",yaxis_title="Hm3")
                st.plotly_chart(fig_chaglla,use_container_width=True)
        
            col1, col2 = st.columns(2)
            with col1:
                fig_malpaso = px.line(malpaso,title='Malpaso',markers=True)
                fig_malpaso.update_layout(showlegend=False, title_x = 0.5,xaxis_title="etapa",yaxis_title="Hm3")
                st.plotly_chart(fig_malpaso,use_container_width=True)
                
            with col2:
                fig_tablachaca = px.line(tablachaca,title="Tablachaca",markers=True)
                fig_tablachaca.update_layout(showlegend=False, title_x = 0.5,xaxis_title="etapa",yaxis_title="Hm3")
                st.plotly_chart(fig_tablachaca,use_container_width=True)
        
        emb_default = ["Emb0","CERRO DEL AGUILA EM","CHAGLLA EM","PRESA MALPASO","TABLACHACA"]
        df = df.drop(emb_default,axis=1,inplace=False)
        keys = df.keys()
        
        st.subheader("Embalses adicionales")
        fig_embalses = px.line(df,title="Embalses",markers=True)
        fig_embalses.update_layout(title_x = 0.4,xaxis_title="etapa",yaxis_title="Hm3")
        st.plotly_chart(fig_embalses)
        
        
        st.subheader("Seleción personalizada")
        options = st.multiselect(
            "Seleccionar embalses:",
            keys,
            default=["AGUADA BLANCA"],
            )        

        df = df[options]
        fig_embalses = px.line(df,title="Embalses",markers=True)
        fig_embalses.update_layout(title_x = 0.4,xaxis_title="etapa",yaxis_title="Hm3")
        st.plotly_chart(fig_embalses)
                
if __name__ == '__main__':
    main()