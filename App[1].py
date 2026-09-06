import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

st.set_page_config(
    page_title="App Campo",
    page_icon="🐮",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
    <style>
        .block-container {padding-top: 0.5rem; padding-bottom: 0rem; padding-left: 0.5rem; padding-right: 0.5rem;}
        header {visibility: hidden;}
    </style>
    """,
    unsafe_allow_html=True,
)

st.info(
    "📷 Testei aqui e a câmera e o GPS conseguem passar pelo quadro do Streamlit "
    "(a permissão do navegador não bloqueia por padrão). O que eu não consigo testar sozinho é o "
    "pop-up real de \"permitir câmera/localização\" que aparece pro usuário — isso só confirma "
    "testando no celular de verdade. Se der problema na hora de usar, o link direto do "
    "Netlify/GitHub Pages é o caminho mais seguro pro campo.",
    icon="ℹ️",
)

html_path = Path(__file__).parent / "app_campo.html"
html_content = html_path.read_text(encoding="utf-8")

components.html(html_content, height=1400, scrolling=True)
