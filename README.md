# 📺 EPG IPTV - Atualizador Automático

[![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-Automático-blue?style=flat-square)](https://github.com/dgomp/epg-iptv/actions)
[![Python](https://img.shields.io/badge/Python-3.9+-green?style=flat-square)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)](LICENSE)

## 🎯 Descrição

Este projeto automatiza o download e atualização de arquivos EPG (Electronic Program Guide) para sistemas IPTV. O sistema baixa automaticamente o arquivo EPG mais recente do [epgshare01.online](https://epgshare01.online/epgshare01/epg_ripper_ALL_SOURCES1.xml.gz) e disponibiliza via GitHub Releases para fácil acesso.

## ✨ Características

- **🔄 Atualização Automática**: Executa diariamente às 7:00 GMT-3 (10:00 UTC) via GitHub Actions
- **📦 Download Inteligente**: Baixa e descomprime arquivos .gz automaticamente
- **🚀 GitHub Releases**: Disponibiliza arquivos EPG via Releases automáticos
- **💾 Sistema de Backup**: Mantém histórico de versões anteriores
- **📝 Logging Completo**: Registra todas as operações para auditoria
- **🔗 Arquivo Sempre Atualizado**: Sempre disponível no release mais recente

## 🚀 Como Funciona

1. **Agendamento**: O GitHub Actions executa o script diariamente às 7:00 GMT-3
2. **Download**: Baixa o arquivo EPG comprimido do servidor
3. **Processamento**: Descomprime o arquivo e cria backup
4. **Release**: Cria automaticamente um GitHub Release com os arquivos EPG
5. **Disponibilização**: Arquivos ficam acessíveis para download direto

## 📁 Estrutura do Projeto

```
epg-iptv/
├── .github/
│   └── workflows/
│       └── update_epg.yml          # Workflow automático com Releases
├── epg_downloader.py              # Script principal
├── requirements.txt                # Dependências Python
├── epg_status.txt                 # Status da última atualização
└── README.md                      # Este arquivo
```

## 📥 Como Acessar o EPG

### **GitHub Releases (Recomendado):**
- **Releases:** https://github.com/dgomp/epg-iptv/releases
- **Mais recente:** https://github.com/dgomp/epg-iptv/releases/latest
- **Arquivo EPG:** `epg_latest.xml` disponível para download

### **Status da Atualização:**
- **Arquivo de status:** https://raw.githubusercontent.com/dgomp/epg-iptv/main/epg_status.txt
- **Informações:** Data, hora e tamanho da última atualização

## 🛠️ Instalação e Uso

### Pré-requisitos

- Python 3.9 ou superior
- Acesso à internet
- Conta no GitHub (para automação)

### Instalação Local

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/dgomp/epg-iptv.git
   cd epg-iptv
   ```

2. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Execute o script:**
   ```bash
   python epg_downloader.py
   ```

### Configuração Automática

O projeto já está configurado para executar automaticamente via GitHub Actions. Para ativar:

1. **Fork ou clone** este repositório para sua conta GitHub
2. **Habilite GitHub Actions** no repositório
3. **Configure permissões** para permitir que Actions criem Releases

## 🔧 Configuração

### Personalizar URL do EPG

Edite o arquivo `epg_downloader.py` e modifique a variável `epg_url`:

```python
self.epg_url = "sua_url_do_epg_aqui"
```

### Alterar Frequência de Atualização

Edite o arquivo `.github/workflows/update_epg.yml` e modifique o cron:

```yaml
- cron: '0 10 * * *'  # Diário às 7:00 GMT-3 (10:00 UTC)
- cron: '0 */6 * * *'  # A cada 6 horas
- cron: '0 6,18 * * *' # 2x por dia
```

## 📊 Monitoramento

### Status da Atualização

- **Arquivo de status:** `epg_status.txt` com informações detalhadas
- **GitHub Releases:** Histórico de todas as versões disponibilizadas
- **GitHub Actions:** Logs de execução e status das operações

### GitHub Actions

Acesse a aba "Actions" no seu repositório para:
- Ver histórico de execuções
- Executar manualmente
- Verificar logs de erro
- Monitorar performance

## 🚨 Solução de Problemas

### Erro de Download

- Verifique conectividade com a internet
- Confirme se a URL do EPG está acessível
- Verifique logs para detalhes do erro

### Erro de Permissões

- Configure corretamente as permissões do GitHub Actions
- Verifique se o repositório permite criação de Releases

### Arquivos Não Atualizados

- Verifique se o GitHub Actions está ativo
- Confirme se o cron está configurado corretamente
- Execute manualmente via "workflow_dispatch"

## 🤝 Contribuição

Contribuições são bem-vindas! Para contribuir:

1. Fork o projeto
2. Crie uma branch para sua feature
3. Commit suas mudanças
4. Push para a branch
5. Abra um Pull Request

## 📄 Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

## 🙏 Agradecimentos

- [epgshare01.online](https://epgshare01.online) por fornecer os dados EPG
- GitHub por fornecer a infraestrutura de Actions e Releases

## 📞 Suporte

- **Issues**: [GitHub Issues](https://github.com/dgomp/epg-iptv/issues)
- **Discussions**: [GitHub Discussions](https://github.com/dgomp/epg-iptv/discussions)
- **Releases**: [GitHub Releases](https://github.com/dgomp/epg-iptv/releases)

---

⭐ **Se este projeto foi útil, considere dar uma estrela!** 