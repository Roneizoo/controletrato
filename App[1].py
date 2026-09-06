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

# Procura qualquer arquivo .html na mesma pasta, em vez de exigir um nome exato.
# Isso evita quebrar quando o navegador renomeia o arquivo (tipo "app_campo[1].html")
# na hora de baixar/extrair de novo um zip com o mesmo nome.
pasta = Path(__file__).parent
candidatos = sorted(pasta.glob("*.html"))

if not candidatos:
    st.error(
        "Não encontrei nenhum arquivo .html nesta pasta do repositório. "
        "Confirma que o arquivo HTML do App Campo foi enviado junto com o App.py."
    )
    st.stop()

if len(candidatos) > 1:
    st.warning(
        "Encontrei mais de um arquivo .html aqui (" +
        ", ".join(c.name for c in candidatos) +
        "). Usando o primeiro: " + candidatos[0].name +
        ". Se não for o certo, apague os outros do repositório."
    )

html_path = candidatos[0]
html_content = html_path.read_text(encoding="utf-8")

components.html(html_content, height=1400, scrolling=True)
