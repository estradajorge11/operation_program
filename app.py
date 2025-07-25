import streamlit as st

def main():
    st.set_page_config(page_title="Operation Program",
                   page_icon="⚡",
                   layout="wide",
                   initial_sidebar_state="expanded")
    # --- PAGE SETUP ---
    resumen_page = st.Page(
        page="views/resumen.py",
        title="Resumen", 
        icon="🏦",
        default=True,
    )
    
    embalses_page = st.Page(
        page="views/embalses.py",
        title="Embalse - Volumen (Hm3)",
        icon="🗻",
    )

    gen_hidro_page = st.Page(
        page="views/gen_hidro.py",
        title="Hidro - Despacho (MW)",
        icon="💧",
    )
    
    rsf_hidro_page = st.Page(
        page="views/rsf_hidro.py",
        title="Hidro - RSF (MW)",
        icon="🌊",
    )

    gen_termica_page = st.Page(
        page="views/gen_termica.py",
        title="Termica - Despacho (MW)",
        icon="🏭",
    )

    rsf_termica_page = st.Page(
        page="views/rsf_termica.py",
        title="Termica - RSF (MW)",
        icon="🛢",
    )
    
    eolica_page = st.Page(
        page="views/eolica.py",
        title="Eólica - Despacho (MW)",
        icon="🌀",
    )

    solar_page = st.Page(
        page="views/solar.py",
        title="Solar - Despacho (MW)",
        icon="🌞",
    )

    gen_rer_page = st.Page(
        page="views/gen_rer_y_nocoes.py",
        title="Rer y No COES - Despacho (MW)",
        icon="♻",
    )

    vert_rer_page = st.Page(
        page="views/vert.py",
        title="Vertimiento (MW)",
        icon="⛲",
    )
        
    cmg_barra_page = st.Page(
        page="views/cmg_barra.py",
        title="CMg - Barra ($ por MWh)",
        icon="💎",
    )

    cmg_equipo_page = st.Page(
        page="views/cmg_equipo.py",
        title="CMg - Equipo ($ por MWh)",
        icon="💬",
    )

    def_barra_page = st.Page(
        page="views/def_barra.py",
        title="Déficit por Barra (MW)",
        icon="⛔",
    )

    def_rsf_page = st.Page(
        page="views/def_rsf.py",
        title="Déficit Reserva Secundaria (MW)",
        icon="📈",
    )

    rsf_up_page = st.Page(
        page="views/rsf_up.py",
        title="Reserva Secundaria Up (MW)",
        icon="⬆",
    )

    rsf_down_page = st.Page(
        page="views/rsf_down.py",
        title="Reserva Secundaria Down (MW)",
        icon="⬇",
    )

    # --- NAVIGATION SETUP (WITHOUT SECTIONS) ---
    #pg = st.navigation(pages=[embalses_page,gen_hidro_page,gen_termica_page])

    # --- NAVIGATION SETUP [WITH SECTIONS] ---
    pg = st.navigation(
        {
            "Resumen":[resumen_page],
            "Hidro": [embalses_page,gen_hidro_page, rsf_hidro_page],
            "Térmica": [gen_termica_page, rsf_termica_page],
            "Rer y no COES":[eolica_page,solar_page,gen_rer_page,vert_rer_page],
            "CMg":[cmg_barra_page,def_barra_page,cmg_equipo_page],
            "Reserva": [def_rsf_page, rsf_up_page, rsf_down_page]
        }
    )

    # --- SHARED ON ALL PAGES ---
    st.logo("assets/coes_image.png",size= "large")

    # --- RUN NAVIGATION ---
    pg.run()
    
if __name__ == '__main__':
    main()

