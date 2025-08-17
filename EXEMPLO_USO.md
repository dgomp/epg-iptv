# 📖 Exemplos de Uso - EPG IPTV

Este arquivo contém exemplos práticos de como usar o sistema EPG IPTV.

## 🚀 Uso Básico

### 1. Download Manual

```bash
# Executar download manual
python epg_downloader.py
```

**Saída esperada:**
```
2024-01-15 10:30:00 - INFO - Diretório criado: epg_files
2024-01-15 10:30:00 - INFO - Diretório criado: backups
2024-01-15 10:30:00 - INFO - Iniciando download de: https://epgshare01.online/epgshare01/epg_ripper_ALL_SOURCES1.xml.gz
2024-01-15 10:30:05 - INFO - Arquivo comprimido salvo: epg_ripper_ALL_SOURCES1_20240115_103000.xml.gz
2024-01-15 10:30:06 - INFO - Arquivo descomprimido: epg_ripper_ALL_SOURCES1_20240115_103000.xml
2024-01-15 10:30:06 - INFO - Backup criado: backups/epg_ripper_ALL_SOURCES1_20240115_103000.xml
2024-01-15 10:30:06 - INFO - Download concluído com sucesso!
2024-01-15 10:30:06 - INFO - Processo concluído com sucesso!
```

### 2. Executar Testes

```bash
# Verificar se tudo está funcionando
python test_epg.py
```

**Saída esperada:**
```
🧪 Iniciando testes do EPG Downloader...

📋 Importações:
🔍 Testando importações...
✅ requests - OK
✅ gzip - OK
✅ shutil - OK
✅ datetime - OK
✅ logging - OK
✅ os - OK
✅ sys - OK

📋 Classe EPGDownloader:
✅ EPGDownloader - Instanciado com sucesso

📋 Acessibilidade da URL:
🌐 Testando acesso à URL: https://epgshare01.online/epgshare01/epg_ripper_ALL_SOURCES1.xml.gz
✅ URL acessível - Status 200

==================================================
📊 Resultado dos testes: 3/3 passaram
🎉 Todos os testes passaram! O sistema está funcionando.
```

## 🔧 Uso Avançado

### 1. Personalizar Configurações

Edite `config.py`:

```python
# Alterar URL do EPG
EPG_CONFIG = {
    'url': 'https://outro-servidor.com/epg.xml.gz',
    'timeout': 60,  # Aumentar timeout
    'retry_attempts': 5,  # Mais tentativas
}

# Alterar retenção de arquivos
CLEANUP_CONFIG = {
    'keep_days': 30,  # Manter por 30 dias
    'max_files': 100, # Máximo 100 arquivos
}
```

### 2. Executar com Python

```python
from epg_downloader import EPGDownloader

# Criar instância
downloader = EPGDownloader()

# Executar download
success = downloader.download_epg()

if success:
    print("✅ Download realizado com sucesso!")
    # Limpar arquivos antigos
    downloader.cleanup_old_files(keep_days=14)
else:
    print("❌ Falha no download")
```

### 3. Monitorar Logs

```bash
# Ver logs em tempo real
tail -f epg_download.log

# Ver últimas 20 linhas
tail -20 epg_download.log

# Buscar por erros
grep "ERROR" epg_download.log
```

## 📁 Estrutura de Arquivos Após Execução

```
epg-iptv/
├── epg_files/
│   ├── epg_ripper_ALL_SOURCES1_20240115_103000.xml.gz
│   ├── epg_ripper_ALL_SOURCES1_20240115_103000.xml
│   └── epg_latest.xml -> epg_ripper_ALL_SOURCES1_20240115_103000.xml
├── backups/
│   └── epg_ripper_ALL_SOURCES1_20240115_103000.xml
├── epg_download.log
└── ... outros arquivos
```

## 🔄 Automação

### 1. Cron Local (Linux/Mac)

```bash
# Editar crontab
crontab -e

# Adicionar linha para executar a cada 6 horas
0 */6 * * * cd /caminho/para/epg-iptv && python epg_downloader.py
```

### 2. Task Scheduler (Windows)

1. Abra "Agendador de Tarefas"
2. Crie uma nova tarefa
3. Configure para executar `python epg_downloader.py`
4. Defina frequência desejada

### 3. Docker (Avançado)

```dockerfile
FROM python:3.9-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "epg_downloader.py"]
```

## 📊 Monitoramento

### 1. Verificar Status dos Arquivos

```bash
# Ver arquivos mais recentes
ls -la epg_files/

# Ver tamanho dos arquivos
du -sh epg_files/*

# Ver último arquivo baixado
ls -t epg_files/ | head -1
```

### 2. Verificar Logs

```bash
# Ver último download
grep "Download concluído" epg_download.log | tail -1

# Ver erros
grep "ERROR" epg_download.log

# Ver estatísticas
echo "Downloads realizados: $(grep -c 'Download concluído' epg_download.log)"
echo "Erros encontrados: $(grep -c 'ERROR' epg_download.log)"
```

## 🚨 Solução de Problemas

### 1. Erro de Permissão

```bash
# Dar permissão de execução
chmod +x epg_downloader.py

# Verificar permissões
ls -la epg_downloader.py
```

### 2. Erro de Dependências

```bash
# Instalar dependências
pip install -r requirements.txt

# Ou instalar manualmente
pip install requests
```

### 3. Erro de Rede

```bash
# Testar conectividade
ping epgshare01.online

# Testar URL
curl -I https://epgshare01.online/epgshare01/epg_ripper_ALL_SOURCES1.xml.gz
```

## 🎯 Casos de Uso Comuns

### 1. **IPTV Pessoal**
- Execute diariamente para manter EPG atualizado
- Use `epg_latest.xml` como fonte para seu player

### 2. **Servidor Compartilhado**
- Configure para executar a cada 6 horas
- Compartilhe o arquivo via HTTP/FTP

### 3. **Desenvolvimento**
- Execute manualmente para testes
- Monitore logs para debug

### 4. **Produção**
- Use GitHub Actions para automação
- Configure alertas para falhas

---

💡 **Dica**: Sempre execute os testes primeiro para garantir que tudo está funcionando! 