"""
Arquivo de configuração centralizada para o EPG Downloader
"""

# Configurações da URL do EPG
EPG_CONFIG = {
    'url': 'https://epgshare01.online/epgshare01/epg_ripper_ALL_SOURCES1.xml.gz',
    'timeout': 30,  # Timeout em segundos para o download
    'retry_attempts': 3,  # Número de tentativas em caso de falha
}

# Configurações de diretórios
DIRECTORIES = {
    'epg_files': 'epg_files',  # Diretório para arquivos EPG
    'backups': 'backups',      # Diretório para backups
    'logs': 'logs',            # Diretório para logs
}

# Configurações de limpeza
CLEANUP_CONFIG = {
    'keep_days': 7,  # Manter arquivos por quantos dias
    'max_files': 50,  # Máximo de arquivos a manter
}

# Configurações de logging
LOGGING_CONFIG = {
    'level': 'INFO',
    'format': '%(asctime)s - %(levelname)s - %(message)s',
    'file': 'epg_download.log',
}

# Configurações do GitHub Actions
GITHUB_ACTIONS_CONFIG = {
    'schedule': '0 6 * * *',  # Cron: diariamente às 6:00 UTC
    'python_version': '3.9',
} 