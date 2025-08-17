#!/usr/bin/env python3
"""
EPG Downloader - Script para automatizar o download de arquivos EPG
Baixa automaticamente o arquivo EPG mais recente do epgshare01.online
"""

import os
import sys
import gzip
import shutil
import requests
from datetime import datetime
import logging

# Configuração de logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('epg_download.log'),
        logging.StreamHandler(sys.stdout)
    ]
)

class EPGDownloader:
    def __init__(self):
        self.epg_url = "https://epgshare01.online/epgshare01/epg_ripper_ALL_SOURCES1.xml.gz"
        self.output_dir = "epg_files"
        self.backup_dir = "backups"
        
    def create_directories(self):
        """Cria os diretórios necessários se não existirem"""
        for directory in [self.output_dir, self.backup_dir]:
            if not os.path.exists(directory):
                os.makedirs(directory)
                logging.info(f"Diretório criado: {directory}")
    
    def download_epg(self):
        """Baixa o arquivo EPG comprimido"""
        try:
            logging.info(f"Iniciando download de: {self.epg_url}")
            
            response = requests.get(self.epg_url, timeout=30)
            response.raise_for_status()
            
            # Nome do arquivo com timestamp
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            gz_filename = f"epg_ripper_ALL_SOURCES1_{timestamp}.xml.gz"
            xml_filename = f"epg_ripper_ALL_SOURCES1_{timestamp}.xml"
            
            gz_path = os.path.join(self.output_dir, gz_filename)
            xml_path = os.path.join(self.output_dir, xml_filename)
            
            # Salva o arquivo comprimido
            with open(gz_path, 'wb') as f:
                f.write(response.content)
            
            logging.info(f"Arquivo comprimido salvo: {gz_filename}")
            
            # Descomprime o arquivo
            with gzip.open(gz_path, 'rb') as f_in:
                with open(xml_path, 'wb') as f_out:
                    shutil.copyfileobj(f_in, f_out)
            
            logging.info(f"Arquivo descomprimido: {xml_filename}")
            
            # Cria backup
            backup_path = os.path.join(self.backup_dir, xml_filename)
            shutil.copy2(xml_path, backup_path)
            logging.info(f"Backup criado: {backup_path}")
            
            # Cria link simbólico para o arquivo mais recente
            latest_link = os.path.join(self.output_dir, "epg_latest.xml")
            if os.path.exists(latest_link):
                os.remove(latest_link)
            os.symlink(xml_filename, latest_link)
            
            logging.info("Download concluído com sucesso!")
            return True
            
        except requests.exceptions.RequestException as e:
            logging.error(f"Erro no download: {e}")
            return False
        except Exception as e:
            logging.error(f"Erro inesperado: {e}")
            return False
    
    def cleanup_old_files(self, keep_days=7):
        """Remove arquivos antigos para economizar espaço"""
        try:
            current_time = datetime.now()
            for filename in os.listdir(self.output_dir):
                if filename.startswith("epg_ripper_ALL_SOURCES1_") and filename.endswith(".xml"):
                    file_path = os.path.join(self.output_dir, filename)
                    file_time = datetime.fromtimestamp(os.path.getctime(file_path))
                    
                    if (current_time - file_time).days > keep_days:
                        os.remove(file_path)
                        logging.info(f"Arquivo antigo removido: {filename}")
                        
        except Exception as e:
            logging.error(f"Erro na limpeza: {e}")

def main():
    """Função principal"""
    downloader = EPGDownloader()
    downloader.create_directories()
    
    if downloader.download_epg():
        downloader.cleanup_old_files()
        logging.info("Processo concluído com sucesso!")
        sys.exit(0)
    else:
        logging.error("Falha no download do EPG")
        sys.exit(1)

if __name__ == "__main__":
    main() 