import streamlit as st
import pandas as pd
from io import BytesIO

def principal():
    st.title("Leitor de Planilhas Excel")
    st.markdown("---")    

    arquivo_carregado = st.file_uploader(
        "Carregue sua planilha Excel", 
        type=["xlsx", "xls"],
        accept_multiple_files=False
    )
    
    if arquivo_carregado:        
        try:            
            dados_excel = pd.ExcelFile(BytesIO(arquivo_carregado.read()))            
            
            nomes_abas = dados_excel.sheet_names
            aba_selecionada = st.selectbox(
                "Selecione a aba:",
                nomes_abas
            )            
            
            dataframe = pd.read_excel(dados_excel, sheet_name=aba_selecionada)            
            
            st.success("Arquivo carregado com sucesso!")
            st.write(f"Dimensões: {dataframe.shape[0]} linhas × {dataframe.shape[1]} colunas")
            
            st.subheader("Visualização dos Dados")
            st.dataframe(
                dataframe,
                height=400,
                use_container_width=True
            )            
            
            st.markdown("---")
            st.subheader("Exportar Dados")            
            
            csv = dataframe.to_csv(index=False).encode('utf-8')
            st.download_button(
                label="Download como CSV",
                data=csv,
                file_name="dados_exportados.csv",
                mime="text/csv"
            )           
            
            buffer_saida = BytesIO()
            with pd.ExcelWriter(buffer_saida, engine='xlsxwriter') as escritor:
                dataframe.to_excel(escritor, index=False, sheet_name='Dados')
            st.download_button(
                label="Download como Excel",
                data=buffer_saida.getvalue(),
                file_name="dados_exportados.xlsx",
                mime="application/vnd.ms-excel"
            )
            
        except Exception as erro:
            st.error(f"Erro ao processar o arquivo: {str(erro)}")

if __name__ == "__main__":
    principal()