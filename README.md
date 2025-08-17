# 📺 EPG IPTV - Atualizador Automático

[![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-Automático-blue?style=flat-square)](https://github.com/dgomp/epg-iptv/actions)
[![Python](https://img.shields.io/badge/Python-3.9+-green?style=flat-square)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)](LICENSE)

## 🎯 Descrição

Este projeto automatiza o download e atualização de arquivos EPG (Electronic Program Guide) para sistemas IPTV. O sistema baixa automaticamente o arquivo EPG mais recente do [epgshare01.online](https://epgshare01.online/epgshare01/epg_ripper_ALL_SOURCES1.xml.gz) e mantém uma versão sempre atualizada disponível.

## ✨ Características

- **🔄 Atualização Automática**: Executa diariamente via GitHub Actions
- **📦 Download Inteligente**: Baixa e descomprime arquivos .gz automaticamente
- **💾 Sistema de Backup**: Mantém histórico de versões anteriores
- **🧹 Limpeza Automática**: Remove arquivos antigos para economizar espaço
- **📝 Logging Completo**: Registra todas as operações para auditoria
- **🔗 Link Simbólico**: Sempre aponta para a versão mais recente

## 🚀 Como Funciona

1. **Agendamento**: O GitHub Actions executa o script diariamente às 6:00 UTC
2. **Download**: Baixa o arquivo EPG comprimido do servidor
3. **Processamento**: Descomprime o arquivo e cria backup
4. **Organização**: Organiza arquivos por data/hora e mantém link para versão atual
5. **Limpeza**: Remove versões antigas (mais de 7 dias)

## 📁 Estrutura do Projeto

```
epg-iptv/
├── .github/
│   └── workflows/
│       └── update_epg.yml          # Workflow automático
├── epg_files/                      # Arquivos EPG baixados
│   ├── epg_latest.xml             # Link para versão mais recente
│   └── epg_ripper_*.xml           # Arquivos com timestamp
├── backups/                        # Backups das versões
├── epg_downloader.py              # Script principal
├── requirements.txt                # Dependências Python
└── README.md                      # Este arquivo
```

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
3. **Configure permissões** para permitir que Actions façam commit

## 🔧 Configuração

### Personalizar URL do EPG

Edite o arquivo `epg_downloader.py` e modifique a variável `epg_url`:

```python
self.epg_url = "sua_url_do_epg_aqui"
```

### Alterar Frequência de Atualização

Edite o arquivo `.github/workflows/update_epg.yml` e modifique o cron:

```yaml
- cron: '0 */6 * * *'  # A cada 6 horas
- cron: '0 6,18 * * *' # 2x por dia
- cron: '0 6 * * 1'    # Semanal (segundas)
```

### Configurar Retenção de Arquivos

No script, modifique o parâmetro `keep_days`:

```python
downloader.cleanup_old_files(keep_days=30)  # Manter por 30 dias
```

## 📊 Monitoramento

### Logs

O sistema gera logs detalhados em `epg_download.log` incluindo:
- Timestamp de cada operação
- Status de download
- Erros e exceções
- Operações de limpeza

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
- Verifique se o repositório permite commits automáticos

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
- GitHub por fornecer a infraestrutura de Actions

## 📞 Suporte

- **Issues**: [GitHub Issues](https://github.com/dgomp/epg-iptv/issues)
- **Discussions**: [GitHub Discussions](https://github.com/dgomp/epg-iptv/discussions)
- **Wiki**: [Documentação detalhada](https://github.com/dgomp/epg-iptv/wiki)

---

⭐ **Se este projeto foi útil, considere dar uma estrela!** 