import streamlit as st
import pandas as pd
import plotly.express as px


def df_new_1(df,keys):
    L = []        
    for i in keys:
        suma = df[i].sum()
        if suma == 0:
            L.append(i)
            df = df.drop(i,axis=1,inplace=False)
    keys = df.keys()
    return df, keys, L

# def df_new_2(df,keys):
#     df["Total"] = 0
#     for i in keys:
#         df["Total"]= df["Total"]+df[i]
#     keys.append("Total")
#     df = df[keys]  
#     return df,keys

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
    st.title("Hidro RSF (MW)") 
    if 'mi_variable' not in st.session_state:
        st.session_state.mi_variable = ""
    
    if st.session_state.mi_variable != "":
        
        st.header("Hidro - RSF Up (MW)")
        ruta = st.session_state.mi_variable + r"\Hidro - RSF Up (MW).csv"
        df = pd.read_csv(ruta,index_col=r"ETAPA \ GENERADOR")      
        keys = df.keys()
        L = []
        df, keys, L = df_new_1(df,keys)
        #df,keys = df_new_2(df,keys)
        figura(df,keys,1,L,"Hidro - RSF Up (MW)",0.3,"MW","Generadores que no ofertan RSF Up")    

        
        st.header("Hidro - RSF Down (MW)")
        ruta = st.session_state.mi_variable + r"\Hidro - RSF Down (MW).csv"
        df = pd.read_csv(ruta,index_col=r"ETAPA \ GENERADOR")      
        keys = df.keys()
        L = []
        df, keys, L = df_new_1(df,keys)
        #df,keys = df_new_2(df,keys)
        figura(df,keys,2,L,"Hidro - RSF Down (MW)",0.3,"MW","Generadores que no ofertan RSF Down")

           
if __name__ == '__main__':
    main()