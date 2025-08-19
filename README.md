# 🤖 Automatizador de Tarefas do Dia a Dia

Um sistema completo de automação de tarefas desenvolvido em Python com interface gráfica Streamlit, permitindo organizar arquivos, agendar tarefas, gerar relatórios e preencher formulários automaticamente.

## 🚀 Funcionalidades

### 📁 Organização de Arquivos
- Organiza automaticamente arquivos por tipo (PDFs, imagens, documentos, etc.)
- Move arquivos para pastas específicas baseadas em extensão
- Evita sobrescrever arquivos existentes
- Interface intuitiva para seleção de tipos de arquivo

### ⏰ Agendamento de Tarefas
- Programa abertura de sites, aplicativos e pastas
- Suporte a repetição diária
- Interface para gerenciar tarefas agendadas
- Execução automática em horários definidos

### 📊 Geração de Relatórios
- Gera relatórios fictícios em Excel e CSV
- Tipos de relatório: Vendas, Funcionários, Financeiro, Estoque
- Inclui gráficos e resumos executivos
- Dados realistas para demonstração

### 📝 Preenchimento de Formulários
- Preenchimento automático de formulários web
- Suporte a diferentes tipos de formulário
- Modo preview para simulação
- Integração com PyAutoGUI para automação real

## 📋 Pré-requisitos

- Python 3.8 ou superior
- Sistema operacional: Windows, macOS ou Linux
- Navegador web moderno

## 🛠️ Instalação

1. **Clone ou baixe o projeto**
   ```bash
   git clone <url-do-repositorio>
   cd automatizador-tarefas
   ```

2. **Crie um ambiente virtual (recomendado)**
   ```bash
   python -m venv venv
   
   # Windows
   venv\Scripts\activate
   
   # macOS/Linux
   source venv/bin/activate
   ```

3. **Instale as dependências**
   ```bash
   pip install -r requirements.txt
   ```

## 🚀 Como Executar

1. **Ative o ambiente virtual** (se estiver usando)
   ```bash
   # Windows
   venv\Scripts\activate
   
   # macOS/Linux
   source venv/bin/activate
   ```

2. **Execute a aplicação**
   ```bash
   streamlit run app.py
   ```

3. **Acesse no navegador**
   - A aplicação será aberta automaticamente em `http://localhost:8501`
   - Se não abrir automaticamente, acesse manualmente o endereço

## 📖 Como Usar

### 🏠 Página Inicial
- Visão geral de todas as funcionalidades disponíveis
- Status do sistema e métricas

### 📁 Organização de Arquivos
1. Selecione a pasta de origem (onde estão os arquivos)
2. Escolha a pasta de destino (onde serão organizados)
3. Marque os tipos de arquivo que deseja organizar
4. Clique em "Organizar Arquivos"
5. Acompanhe o progresso em tempo real

### ⏰ Agendamento de Tarefas
1. Escolha o tipo de tarefa (Site, Aplicativo ou Pasta)
2. Configure o nome e destino da tarefa
3. Defina o horário de execução
4. Marque se deve repetir diariamente
5. Clique em "Adicionar Tarefa"

### 📊 Geração de Relatórios
1. Selecione o tipo de relatório
2. Escolha o formato (Excel ou CSV)
3. Configure o número de registros e período
4. Marque as opções desejadas (gráficos, resumo)
5. Clique em "Gerar Relatório"

### 📝 Preenchimento de Formulários
1. Escolha o tipo de formulário
2. Configure o delay entre ações
3. Preencha os dados necessários
4. Configure as opções (envio automático, modo preview)
5. Clique em "Iniciar Preenchimento"

## 📁 Estrutura do Projeto

```
automatizador-tarefas/
├── app.py                 # Aplicação principal Streamlit
├── requirements.txt       # Dependências do projeto
├── README.md             # Este arquivo
├── tasks/                # Módulos de tarefas
│   ├── __init__.py
│   ├── file_organizer.py # Organização de arquivos
│   ├── scheduler.py      # Agendamento de tarefas
│   ├── report_generator.py # Geração de relatórios
│   └── form_filler.py    # Preenchimento de formulários
├── reports/              # Relatórios gerados (criado automaticamente)
├── form_templates/       # Templates de formulário (criado automaticamente)
└── scheduled_tasks.json  # Tarefas agendadas (criado automaticamente)
```

## ⚙️ Configurações

### Organização de Arquivos
- **Tipos suportados**: PDF, DOC, DOCX, TXT, RTF, JPG, PNG, GIF, MP3, MP4, XLSX, CSV, ZIP, RAR
- **Pastas padrão**: Downloads (origem) e Documents/Arquivos_Organizados (destino)

### Agendamento
- **Verificação**: A cada minuto
- **Persistência**: Tarefas salvas em JSON
- **Execução**: Em segundo plano

### Relatórios
- **Formatos**: Excel (.xlsx) e CSV
- **Dados**: Fictícios para demonstração
- **Localização**: Pasta `reports/`

### Formulários
- **Modo preview**: Simulação sem PyAutoGUI
- **Modo real**: Requer PyAutoGUI instalado
- **Templates**: Salvos em JSON

## 🔧 Dependências

- **streamlit**: Interface web
- **pandas**: Manipulação de dados
- **numpy**: Operações numéricas
- **openpyxl**: Geração de arquivos Excel
- **pyautogui**: Automação de interface (opcional)
- **Pillow**: Processamento de imagens

## ⚠️ Observações Importantes

### PyAutoGUI (Preenchimento de Formulários)
- **Instalação**: `pip install pyautogui`
- **Uso**: Apenas para preenchimento real (não preview)
- **Segurança**: Use com cuidado, pode afetar o sistema
- **Alternativa**: Modo preview sempre disponível

### Permissões
- **Arquivos**: Permissão de leitura/escrita nas pastas
- **Sistema**: Permissão para abrir aplicativos/sites
- **Tela**: Permissão para automação (PyAutoGUI)

### Segurança
- Não execute scripts não confiáveis
- Revise as tarefas agendadas
- Use o modo preview primeiro
- Faça backup de arquivos importantes

## 🐛 Solução de Problemas

### Erro de Importação
```bash
# Reinstale as dependências
pip install -r requirements.txt --force-reinstall
```

### PyAutoGUI não funciona
- Use o modo preview
- Verifique permissões do sistema
- Teste em ambiente controlado

### Arquivos não organizados
- Verifique permissões da pasta
- Confirme se os arquivos existem
- Verifique extensões suportadas

### Relatórios não gerados
- Verifique espaço em disco
- Confirme permissões de escrita
- Verifique dependências Excel

## 🤝 Contribuição

1. Faça um fork do projeto
2. Crie uma branch para sua feature
3. Commit suas mudanças
4. Push para a branch
5. Abra um Pull Request

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

## 📞 Suporte

Para dúvidas ou problemas:
- Abra uma issue no GitHub
- Consulte a documentação
- Verifique as configurações

---

**Desenvolvido com ❤️ em Python e Streamlit**
