import streamlit as st
import pandas as pd
import plotly.express as px

def main(): 
    st.title("Despacho") 
    st.subheader("Nodo de Huancavelica")
    if 'mi_variable' not in st.session_state:
        st.session_state.mi_variable = ""
    
    if st.session_state.mi_variable != "":
        ruta = st.session_state.mi_variable + r"\Hidro - Despacho (MW).csv"
        df = pd.read_csv(ruta,index_col=r"ETAPA \ GENERADOR")
        mantaro = df["MANTARO"]
        restitucion = df["RESTITUCION"]
        cda_1 = df["CERRO DEL AGUILA G1"]
        cda_2 = df["CERRO DEL AGUILA G2"]
        cda_3 = df["CERRO DEL AGUILA G3"]
        cda = cda_1 + cda_2 + cda_3
        
        with st.container():
            col1, col2 = st.columns(2)
            with col1:
                fig_mantaro = px.line(mantaro,title='MANTARO',markers=True)
                fig_mantaro.update_layout(showlegend=False, title_x = 0.5,xaxis_title="etapa",yaxis_title="MW")
                st.plotly_chart(fig_mantaro,use_container_width=True)
                
            with col2:
                fig_restitucion = px.line(restitucion,title="RESTITUCION",markers=True)
                fig_restitucion.update_layout(showlegend=False, title_x = 0.5,xaxis_title="etapa",yaxis_title="MW")
                st.plotly_chart(fig_restitucion,use_container_width=True)
        
            col1, col2 = st.columns(2)
            with col1:
                fig_cda_1 = px.line(cda_1,title='CERRO DEL AGUILA G1',markers=True)
                fig_cda_1.update_layout(showlegend=False, title_x = 0.5,xaxis_title="etapa",yaxis_title="MW")
                st.plotly_chart(fig_cda_1,use_container_width=True)
                
            with col2:
                fig_cda_2 = px.line(cda_2,title='CERRO DEL AGUILA G2',markers=True)
                fig_cda_2.update_layout(showlegend=False, title_x = 0.5,xaxis_title="etapa",yaxis_title="MW")
                st.plotly_chart(fig_cda_2,use_container_width=True)
    
            col1, col2 = st.columns(2)
            with col1:
                fig_cda_3 = px.line(cda_3,title='CERRO DEL AGUILA G3',markers=True)
                fig_cda_3.update_layout(showlegend=False, title_x = 0.5,xaxis_title="etapa",yaxis_title="MW")
                st.plotly_chart(fig_cda_3,use_container_width=True)
                
            with col2:
                fig_cda = px.line(cda,title='CERRO DEL AGUILA',markers=True)
                fig_cda.update_layout(showlegend=False, title_x = 0.5,xaxis_title="etapa",yaxis_title="MW")
                st.plotly_chart(fig_cda,use_container_width=True)   
        
        default = ["MANTARO","RESTITUCION"]
        df = df.drop(default,axis=1,inplace=False)
        keys = df.keys()
        
        st.subheader("Centrales adicionales")
        fig_embalses = px.line(df,title="Despacho",markers=True)
        fig_embalses.update_layout(title_x = 0.4,xaxis_title="etapa",yaxis_title="MW")
        st.plotly_chart(fig_embalses)
        
        
        st.subheader("Seleción personalizada")
        options = st.multiselect(
            "Seleccionar centrales:",
            keys,
            default=["CALLAHUANCA"],
            )        

        df = df[options]
        fig_embalses = px.line(df,title="Despacho",markers=True)
        fig_embalses.update_layout(title_x = 0.4,xaxis_title="etapa",yaxis_title="MW")
        st.plotly_chart(fig_embalses)
                
if __name__ == '__main__':
    main()