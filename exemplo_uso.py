#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Exemplo de uso do Automatizador de Tarefas
Este arquivo demonstra como usar as funcionalidades programaticamente
"""

import os
import sys
from datetime import datetime, time

# Adicionar o diretório tasks ao path
sys.path.append(os.path.join(os.path.dirname(__file__), 'tasks'))

# Importar módulos
from tasks.file_organizer import FileOrganizer
from tasks.scheduler import TaskScheduler
from tasks.report_generator import ReportGenerator
from tasks.form_filler import FormFiller

def exemplo_organizacao_arquivos():
    """Exemplo de organização de arquivos"""
    print("📁 Exemplo: Organização de Arquivos")
    print("-" * 50)
    
    # Configurar pastas
    pasta_origem = os.path.expanduser("~/Downloads")
    pasta_destino = os.path.expanduser("~/Documents/Arquivos_Organizados")
    
    # Criar organizador
    organizador = FileOrganizer(pasta_origem, pasta_destino)
    
    # Selecionar tipos de arquivo
    tipos_selecionados = {
        "📄 Documentos": True,
        "🖼️ Imagens": True,
        "🎵 Áudio": False,
        "🎬 Vídeo": False,
        "📊 Planilhas": True,
        "📦 Compactados": False
    }
    
    # Organizar arquivos
    try:
        resultado = organizador.organize_files(tipos_selecionados)
        print(f"✅ Organização concluída!")
        print(f"📊 Arquivos processados: {resultado['total_files']}")
        print(f"📁 Arquivos movidos: {resultado['moved_files']}")
        print(f"📂 Pastas criadas: {resultado['folders_created']}")
    except Exception as e:
        print(f"❌ Erro: {e}")
    
    print()

def exemplo_agendamento():
    """Exemplo de agendamento de tarefas"""
    print("⏰ Exemplo: Agendamento de Tarefas")
    print("-" * 50)
    
    # Criar agendador
    agendador = TaskScheduler()
    
    # Adicionar tarefas
    tarefas = [
        {
            "nome": "Abrir Gmail",
            "tipo": "🌐 Abrir Site",
            "destino": "https://gmail.com",
            "horario": time(9, 0),
            "repetir": True
        },
        {
            "nome": "Abrir Notepad",
            "tipo": "💻 Abrir Aplicativo",
            "destino": "notepad.exe",
            "horario": time(14, 30),
            "repetir": False
        }
    ]
    
    for tarefa in tarefas:
        try:
            agendador.add_task(
                tarefa["nome"],
                tarefa["tipo"],
                tarefa["destino"],
                tarefa["horario"],
                tarefa["repetir"]
            )
            print(f"✅ Tarefa '{tarefa['nome']}' adicionada")
        except Exception as e:
            print(f"❌ Erro ao adicionar tarefa: {e}")
    
    # Listar tarefas
    tarefas_ativas = agendador.get_active_tasks()
    print(f"\n📋 Tarefas ativas: {len(tarefas_ativas)}")
    for tarefa in tarefas_ativas:
        print(f"  • {tarefa['name']} - {tarefa['schedule_time']}")
    
    print()

def exemplo_relatorios():
    """Exemplo de geração de relatórios"""
    print("📊 Exemplo: Geração de Relatórios")
    print("-" * 50)
    
    # Criar gerador de relatórios
    gerador = ReportGenerator()
    
    # Configurar parâmetros
    tipo_relatorio = "📈 Relatório de Vendas"
    formato_arquivo = "Excel (.xlsx)"
    num_registros = 50
    data_inicial = datetime.now().replace(day=1)
    data_final = datetime.now()
    
    try:
        # Gerar relatório
        resultado = gerador.generate_report(
            report_type=tipo_relatorio,
            file_format=formato_arquivo,
            num_records=num_registros,
            start_date=data_inicial,
            end_date=data_final,
            include_charts=True,
            include_summary=True
        )
        
        print(f"✅ Relatório gerado com sucesso!")
        print(f"📄 Arquivo: {resultado['filename']}")
        print(f"📊 Registros: {resultado['records']}")
        print(f"💾 Tamanho: {resultado['file_size']}")
        print(f"📁 Localização: {resultado['file_path']}")
        
    except Exception as e:
        print(f"❌ Erro ao gerar relatório: {e}")
    
    print()

def exemplo_formularios():
    """Exemplo de preenchimento de formulários"""
    print("📝 Exemplo: Preenchimento de Formulários")
    print("-" * 50)
    
    # Criar preenchedor de formulários
    preenchedor = FormFiller()
    
    # Dados do formulário
    dados_formulario = {
        "nome": "João Silva",
        "email": "joao.silva@email.com",
        "telefone": "(11) 99999-9999",
        "empresa": "Empresa XYZ",
        "cargo": "Desenvolvedor",
        "cidade": "São Paulo",
        "mensagem": "Olá! Gostaria de mais informações sobre seus produtos."
    }
    
    try:
        # Preencher formulário (modo preview)
        resultado = preenchedor.fill_form(
            form_type="📧 Formulário de Contato",
            form_data=dados_formulario,
            delay=0.5,
            auto_submit=False,
            preview_mode=True
        )
        
        print(f"✅ Formulário preenchido com sucesso!")
        print(f"📝 Campos preenchidos: {resultado['fields_filled']}")
        print(f"⏱️ Tempo total: {resultado['total_time']:.1f}s")
        print(f"🎯 Modo: {resultado['mode']}")
        
    except Exception as e:
        print(f"❌ Erro ao preencher formulário: {e}")
    
    print()

def main():
    """Função principal com exemplos"""
    print("🤖 AUTOMATIZADOR DE TAREFAS - EXEMPLOS DE USO")
    print("=" * 60)
    print()
    
    # Executar exemplos
    exemplo_organizacao_arquivos()
    exemplo_agendamento()
    exemplo_relatorios()
    exemplo_formularios()
    
    print("🎉 Todos os exemplos foram executados!")
    print("\n💡 Para usar a interface gráfica, execute:")
    print("   streamlit run app.py")

if __name__ == "__main__":
    main()
