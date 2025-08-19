import streamlit as st
import os
import sys
from datetime import datetime, time
import time as time_module
import threading

# Adicionar o diretório tasks ao path
sys.path.append(os.path.join(os.path.dirname(__file__), 'tasks'))

# Importar módulos de tarefas
from tasks.file_organizer import FileOrganizer
from tasks.scheduler import TaskScheduler
from tasks.report_generator import ReportGenerator
from tasks.form_filler import FormFiller

def main():
    st.set_page_config(
        page_title="Automatizador de Tarefas",
        page_icon="🤖",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    st.title("🤖 Automatizador de Tarefas do Dia a Dia")
    st.markdown("---")
    
    # Sidebar para navegação
    st.sidebar.title("📋 Menu de Tarefas")
    
    # Seleção de tarefa
    task = st.sidebar.selectbox(
        "Escolha uma tarefa:",
        [
            "🏠 Página Inicial",
            "📁 Organização de Arquivos",
            "⏰ Agendamento de Tarefas",
            "📊 Geração de Relatórios",
            "📝 Preenchimento de Formulários"
        ]
    )
    
    # Executar tarefa selecionada
    if task == "🏠 Página Inicial":
        show_home_page()
    elif task == "📁 Organização de Arquivos":
        show_file_organizer()
    elif task == "⏰ Agendamento de Tarefas":
        show_task_scheduler()
    elif task == "📊 Geração de Relatórios":
        show_report_generator()
    elif task == "📝 Preenchimento de Formulários":
        show_form_filler()

def show_home_page():
    st.header("🏠 Bem-vindo ao Automatizador de Tarefas!")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📋 Tarefas Disponíveis")
        st.markdown("""
        - **📁 Organização de Arquivos**: Organize automaticamente seus arquivos por tipo
        - **⏰ Agendamento**: Programe a abertura de aplicativos e sites
        - **📊 Relatórios**: Gere relatórios fictícios em Excel/CSV
        - **📝 Formulários**: Preencha formulários automaticamente
        """)
    
    with col2:
        st.subheader("🚀 Como Usar")
        st.markdown("""
        1. Selecione uma tarefa no menu lateral
        2. Configure os parâmetros necessários
        3. Clique em executar
        4. Acompanhe o progresso em tempo real
        """)
    
    st.markdown("---")
    
    # Status do sistema
    st.subheader("📊 Status do Sistema")
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Tarefas Disponíveis", "4")
    
    with col2:
        st.metric("Status", "🟢 Online")
    
    with col3:
        st.metric("Última Execução", datetime.now().strftime("%H:%M"))
    
    with col4:
        st.metric("Versão", "1.0.0")

def show_file_organizer():
    st.header("📁 Organização de Arquivos")
    st.markdown("Organize automaticamente seus arquivos por tipo em pastas específicas.")
    
    # Configurações
    st.subheader("⚙️ Configurações")
    
    col1, col2 = st.columns(2)
    
    with col1:
        source_folder = st.text_input(
            "📂 Pasta de Origem:",
            value=os.path.expanduser("~/Downloads"),
            help="Pasta onde estão os arquivos a serem organizados"
        )
    
    with col2:
        destination_folder = st.text_input(
            "📁 Pasta de Destino:",
            value=os.path.expanduser("~/Documents/Arquivos_Organizados"),
            help="Pasta onde os arquivos organizados serão salvos"
        )
    
    # Tipos de arquivo para organizar
    st.subheader("📋 Tipos de Arquivo")
    
    file_types = {
        "📄 Documentos": [".pdf", ".doc", ".docx", ".txt", ".rtf"],
        "🖼️ Imagens": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg"],
        "🎵 Áudio": [".mp3", ".wav", ".flac", ".aac", ".ogg"],
        "🎬 Vídeo": [".mp4", ".avi", ".mkv", ".mov", ".wmv"],
        "📊 Planilhas": [".xlsx", ".xls", ".csv"],
        "📦 Compactados": [".zip", ".rar", ".7z", ".tar", ".gz"]
    }
    
    selected_types = {}
    cols = st.columns(3)
    
    for i, (category, extensions) in enumerate(file_types.items()):
        col_idx = i % 3
        with cols[col_idx]:
            selected_types[category] = st.checkbox(
                category,
                value=True,
                help=f"Extensões: {', '.join(extensions)}"
            )
    
    # Executar organização
    if st.button("🚀 Organizar Arquivos", type="primary"):
        if not os.path.exists(source_folder):
            st.error("❌ Pasta de origem não encontrada!")
            return
        
        try:
            organizer = FileOrganizer(source_folder, destination_folder)
            
            with st.spinner("🔄 Organizando arquivos..."):
                progress_bar = st.progress(0)
                status_text = st.empty()
                
                # Simular progresso
                for i in range(101):
                    progress_bar.progress(i)
                    status_text.text(f"Processando... {i}%")
                    time_module.sleep(0.05)
                
                # Executar organização
                result = organizer.organize_files(selected_types)
                
                progress_bar.progress(100)
                status_text.text("✅ Organização concluída!")
                
                # Mostrar resultados
                st.success("🎉 Arquivos organizados com sucesso!")
                
                # Estatísticas
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.metric("Arquivos Processados", result.get("total_files", 0))
                with col2:
                    st.metric("Arquivos Movidos", result.get("moved_files", 0))
                with col3:
                    st.metric("Pastas Criadas", result.get("folders_created", 0))
                
                # Lista de arquivos organizados
                if result.get("organized_files"):
                    st.subheader("📋 Arquivos Organizados")
                    for category, files in result["organized_files"].items():
                        with st.expander(f"{category} ({len(files)} arquivos)"):
                            for file in files:
                                st.write(f"• {file}")
        
        except Exception as e:
            st.error(f"❌ Erro durante a organização: {str(e)}")

def show_task_scheduler():
    st.header("⏰ Agendamento de Tarefas")
    st.markdown("Programe a abertura de aplicativos e sites em horários específicos.")
    
    # Configurações do agendador
    st.subheader("⚙️ Configurações")
    
    col1, col2 = st.columns(2)
    
    with col1:
        task_type = st.selectbox(
            "🎯 Tipo de Tarefa:",
            ["🌐 Abrir Site", "💻 Abrir Aplicativo", "📁 Abrir Pasta"]
        )
    
    with col2:
        task_name = st.text_input(
            "📝 Nome da Tarefa:",
            placeholder="Ex: Abrir Gmail"
        )
    
    # Configurações específicas por tipo
    if task_type == "🌐 Abrir Site":
        target = st.text_input(
            "🔗 URL:",
            placeholder="https://www.google.com"
        )
    elif task_type == "💻 Abrir Aplicativo":
        target = st.text_input(
            "📱 Nome do Aplicativo:",
            placeholder="notepad.exe"
        )
    else:  # Abrir Pasta
        target = st.text_input(
            "📂 Caminho da Pasta:",
            placeholder="C:\\Users\\Usuario\\Documents"
        )
    
    # Configuração de horário
    st.subheader("⏰ Agendamento")
    
    col1, col2 = st.columns(2)
    
    with col1:
        schedule_time = st.time_input(
            "🕐 Horário de Execução:",
            value=time(9, 0)
        )
    
    with col2:
        repeat_daily = st.checkbox("🔄 Repetir diariamente")
    
    # Tarefas agendadas
    st.subheader("📋 Tarefas Agendadas")
    
    # Simular tarefas existentes
    scheduled_tasks = [
        {
            "name": "Abrir Gmail",
            "type": "🌐 Abrir Site",
            "target": "https://gmail.com",
            "time": "09:00",
            "status": "🟢 Ativo"
        },
        {
            "name": "Abrir Notepad",
            "type": "💻 Abrir Aplicativo",
            "target": "notepad.exe",
            "time": "14:30",
            "status": "🟡 Pausado"
        }
    ]
    
    # Mostrar tarefas existentes
    for i, task in enumerate(scheduled_tasks):
        col1, col2, col3, col4, col5 = st.columns([3, 2, 2, 1, 1])
        
        with col1:
            st.write(f"**{task['name']}**")
        with col2:
            st.write(task['type'])
        with col3:
            st.write(task['target'])
        with col4:
            st.write(task['time'])
        with col5:
            st.write(task['status'])
    
    st.markdown("---")
    
    # Adicionar nova tarefa
    if st.button("➕ Adicionar Tarefa", type="primary"):
        if not task_name or not target:
            st.error("❌ Preencha todos os campos obrigatórios!")
            return
        
        try:
            scheduler = TaskScheduler()
            
            with st.spinner("🔄 Adicionando tarefa..."):
                # Simular adição
                time_module.sleep(1)
                
                # Adicionar à lista
                scheduled_tasks.append({
                    "name": task_name,
                    "type": task_type,
                    "target": target,
                    "time": schedule_time.strftime("%H:%M"),
                    "status": "🟢 Ativo"
                })
            
            st.success("✅ Tarefa adicionada com sucesso!")
            st.rerun()
        
        except Exception as e:
            st.error(f"❌ Erro ao adicionar tarefa: {str(e)}")

def show_report_generator():
    st.header("📊 Geração de Relatórios")
    st.markdown("Gere relatórios fictícios em Excel ou CSV para demonstração.")
    
    # Configurações do relatório
    st.subheader("⚙️ Configurações")
    
    col1, col2 = st.columns(2)
    
    with col1:
        report_type = st.selectbox(
            "📋 Tipo de Relatório:",
            ["📈 Relatório de Vendas", "👥 Relatório de Funcionários", "💰 Relatório Financeiro", "📦 Relatório de Estoque"]
        )
    
    with col2:
        file_format = st.selectbox(
            "📄 Formato do Arquivo:",
            ["Excel (.xlsx)", "CSV (.csv)"]
        )
    
    # Parâmetros específicos
    st.subheader("📊 Parâmetros")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        num_records = st.slider(
            "📊 Número de Registros:",
            min_value=10,
            max_value=1000,
            value=100,
            step=10
        )
    
    with col2:
        start_date = st.date_input(
            "📅 Data Inicial:",
            value=datetime.now().replace(day=1)
        )
    
    with col3:
        end_date = st.date_input(
            "📅 Data Final:",
            value=datetime.now()
        )
    
    # Opções adicionais
    include_charts = st.checkbox("📊 Incluir gráficos (Excel)", value=True)
    include_summary = st.checkbox("📋 Incluir resumo executivo", value=True)
    
    # Executar geração
    if st.button("🚀 Gerar Relatório", type="primary"):
        try:
            generator = ReportGenerator()
            
            with st.spinner("🔄 Gerando relatório..."):
                progress_bar = st.progress(0)
                status_text = st.empty()
                
                # Simular progresso
                for i in range(101):
                    progress_bar.progress(i)
                    status_text.text(f"Gerando relatório... {i}%")
                    time_module.sleep(0.03)
                
                # Gerar relatório
                result = generator.generate_report(
                    report_type=report_type,
                    file_format=file_format,
                    num_records=num_records,
                    start_date=start_date,
                    end_date=end_date,
                    include_charts=include_charts,
                    include_summary=include_summary
                )
                
                progress_bar.progress(100)
                status_text.text("✅ Relatório gerado com sucesso!")
            
            st.success("🎉 Relatório gerado com sucesso!")
            
            # Mostrar informações do arquivo
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Arquivo Gerado", result.get("filename", "N/A"))
            with col2:
                st.metric("Tamanho", result.get("file_size", "N/A"))
            with col3:
                st.metric("Registros", num_records)
            
            # Botão para download
            if st.button("📥 Baixar Relatório"):
                st.info("📁 Arquivo salvo em: " + result.get("file_path", "N/A"))
        
        except Exception as e:
            st.error(f"❌ Erro ao gerar relatório: {str(e)}")

def show_form_filler():
    st.header("📝 Preenchimento de Formulários")
    st.markdown("Preencha formulários automaticamente usando pyautogui.")
    
    st.warning("⚠️ **Atenção**: Esta funcionalidade requer que o formulário esteja visível na tela.")
    
    # Configurações
    st.subheader("⚙️ Configurações")
    
    col1, col2 = st.columns(2)
    
    with col1:
        form_type = st.selectbox(
            "📋 Tipo de Formulário:",
            ["📧 Formulário de Contato", "👤 Formulário de Cadastro", "💼 Formulário de Trabalho"]
        )
    
    with col2:
        delay = st.slider(
            "⏱️ Delay entre ações (segundos):",
            min_value=0.1,
            max_value=2.0,
            value=0.5,
            step=0.1
        )
    
    # Dados para preenchimento
    st.subheader("📝 Dados para Preenchimento")
    
    col1, col2 = st.columns(2)
    
    with col1:
        nome = st.text_input("👤 Nome:", value="João Silva")
        email = st.text_input("📧 Email:", value="joao.silva@email.com")
        telefone = st.text_input("📱 Telefone:", value="(11) 99999-9999")
    
    with col2:
        empresa = st.text_input("🏢 Empresa:", value="Empresa XYZ")
        cargo = st.text_input("💼 Cargo:", value="Desenvolvedor")
        cidade = st.text_input("🏙️ Cidade:", value="São Paulo")
    
    # Campos adicionais
    mensagem = st.text_area(
        "💬 Mensagem:",
        value="Olá! Gostaria de mais informações sobre seus produtos.",
        height=100
    )
    
    # Opções
    st.subheader("🔧 Opções")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        auto_submit = st.checkbox("📤 Enviar automaticamente", value=False)
    
    with col2:
        preview_mode = st.checkbox("👁️ Modo preview", value=True)
    
    with col3:
        save_data = st.checkbox("💾 Salvar dados", value=True)
    
    # Instruções
    st.info("""
    **📋 Instruções:**
    1. Abra o formulário no navegador
    2. Posicione o cursor no primeiro campo
    3. Clique em "Iniciar Preenchimento"
    4. Não mova o mouse durante o processo
    """)
    
    # Executar preenchimento
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("🚀 Iniciar Preenchimento", type="primary"):
            try:
                filler = FormFiller()
                
                # Dados para preencher
                form_data = {
                    "nome": nome,
                    "email": email,
                    "telefone": telefone,
                    "empresa": empresa,
                    "cargo": cargo,
                    "cidade": cidade,
                    "mensagem": mensagem
                }
                
                with st.spinner("🔄 Preenchendo formulário..."):
                    progress_bar = st.progress(0)
                    status_text = st.empty()
                    
                    # Simular progresso
                    for i in range(101):
                        progress_bar.progress(i)
                        status_text.text(f"Preenchendo... {i}%")
                        time_module.sleep(0.02)
                    
                    # Executar preenchimento
                    result = filler.fill_form(
                        form_type=form_type,
                        form_data=form_data,
                        delay=delay,
                        auto_submit=auto_submit,
                        preview_mode=preview_mode
                    )
                    
                    progress_bar.progress(100)
                    status_text.text("✅ Preenchimento concluído!")
                
                st.success("🎉 Formulário preenchido com sucesso!")
                
                # Estatísticas
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.metric("Campos Preenchidos", result.get("fields_filled", 0))
                with col2:
                    st.metric("Tempo Total", f"{result.get('total_time', 0):.1f}s")
                with col3:
                    st.metric("Status", "✅ Concluído")
            
            except Exception as e:
                st.error(f"❌ Erro durante o preenchimento: {str(e)}")
    
    with col2:
        if st.button("⏸️ Pausar"):
            st.info("⏸️ Preenchimento pausado")

if __name__ == "__main__":
    main()
