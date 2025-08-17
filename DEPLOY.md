# 🚀 Guia de Deploy - EPG IPTV

Este guia explica como configurar e fazer deploy do projeto EPG IPTV no GitHub.

## 📋 Pré-requisitos

- Conta no GitHub
- Git instalado localmente
- Python 3.9+ (para testes locais)

## 🔧 Passo a Passo

### 1. Preparar o Repositório Local

```bash
# Clone o repositório (se ainda não tiver)
git clone https://github.com/dgomp/epg-iptv.git
cd epg-iptv

# Ou se já estiver no diretório, inicialize o git
git init
git remote add origin https://github.com/dgomp/epg-iptv.git
```

### 2. Configurar o Git

```bash
git config user.name "dgomp"
git config user.email "seu-email@exemplo.com"
```

### 3. Fazer o Primeiro Commit

```bash
git add .
git commit -m "🎉 Commit inicial: EPG IPTV Downloader"
git branch -M main
git push -u origin main
```

### 4. Configurar GitHub Actions

1. **Vá para seu repositório no GitHub**
2. **Clique na aba "Actions"**
3. **Clique em "Configure" no workflow "Atualizar EPG Automaticamente"**
4. **Clique em "Commit changes"**

### 5. Configurar Permissões

1. **Vá para Settings > Actions > General**
2. **Em "Workflow permissions" selecione:**
   - ✅ "Read and write permissions"
   - ✅ "Allow GitHub Actions to create and approve pull requests"
3. **Clique em "Save"**

### 6. Testar o Sistema

```bash
# Instalar dependências
pip install -r requirements.txt

# Executar teste
python test_epg.py

# Executar download manual
python epg_downloader.py
```

## 🔄 Configurações Avançadas

### Alterar Frequência de Atualização

Edite `.github/workflows/update_epg.yml`:

```yaml
on:
  schedule:
    - cron: '0 */6 * * *'  # A cada 6 horas
    - cron: '0 6,18 * * *' # 2x por dia
    - cron: '0 6 * * 1'    # Semanal (segundas)
```

### Configurar Retenção de Arquivos

Edite `config.py`:

```python
CLEANUP_CONFIG = {
    'keep_days': 30,  # Manter por 30 dias
    'max_files': 100, # Máximo 100 arquivos
}
```

### Personalizar URL do EPG

Edite `config.py`:

```python
EPG_CONFIG = {
    'url': 'sua_nova_url_aqui',
    # ... outras configurações
}
```

## 📊 Monitoramento

### Verificar Status

- **GitHub Actions**: Aba "Actions" do repositório
- **Logs**: Arquivo `epg_download.log`
- **Arquivos**: Diretório `epg_files/`

### Executar Manualmente

1. **Vá para Actions > Atualizar EPG Automaticamente**
2. **Clique em "Run workflow"**
3. **Clique em "Run workflow" novamente**

## 🚨 Solução de Problemas

### Erro de Permissões

```bash
# Verificar configuração do git
git config --list

# Reconfigurar se necessário
git config user.name "dgomp"
git config user.email "seu-email@exemplo.com"
```

### GitHub Actions Não Executa

1. **Verificar se está habilitado**
2. **Verificar permissões**
3. **Verificar sintaxe do cron**
4. **Verificar logs de erro**

### Download Falha

1. **Verificar conectividade**
2. **Verificar se a URL está acessível**
3. **Verificar logs para detalhes**
4. **Testar manualmente**

## 🔗 Links Úteis

- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [Cron Syntax](https://crontab.guru/)
- [Python Requests](https://requests.readthedocs.io/)

## 📞 Suporte

Se encontrar problemas:

1. **Verifique os logs**
2. **Execute os testes**
3. **Abra uma issue no GitHub**
4. **Consulte a documentação**

---

🎯 **Lembre-se**: O sistema executará automaticamente todos os dias às 6:00 UTC! 