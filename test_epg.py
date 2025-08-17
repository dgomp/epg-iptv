#!/usr/bin/env python3
"""
Script de teste para o EPG Downloader
Verifica se todas as dependências estão funcionando
"""

import sys
import importlib

def test_imports():
    """Testa se todas as dependências podem ser importadas"""
    required_modules = [
        'requests',
        'gzip',
        'shutil',
        'datetime',
        'logging',
        'os',
        'sys'
    ]
    
    print("🔍 Testando importações...")
    for module in required_modules:
        try:
            importlib.import_module(module)
            print(f"✅ {module} - OK")
        except ImportError as e:
            print(f"❌ {module} - FALHOU: {e}")
            return False
    
    return True

def test_epg_downloader():
    """Testa se a classe EPGDownloader pode ser instanciada"""
    try:
        from epg_downloader import EPGDownloader
        downloader = EPGDownloader()
        print("✅ EPGDownloader - Instanciado com sucesso")
        return True
    except Exception as e:
        print(f"❌ EPGDownloader - FALHOU: {e}")
        return False

def test_url_accessibility():
    """Testa se a URL do EPG está acessível"""
    try:
        import requests
        url = "https://epgshare01.online/epgshare01/epg_ripper_ALL_SOURCES1.xml.gz"
        
        print(f"🌐 Testando acesso à URL: {url}")
        response = requests.head(url, timeout=10)
        
        if response.status_code == 200:
            print("✅ URL acessível - Status 200")
            return True
        else:
            print(f"⚠️ URL retornou status: {response.status_code}")
            return False
            
    except Exception as e:
        print(f"❌ Erro ao acessar URL: {e}")
        return False

def main():
    """Função principal de teste"""
    print("🧪 Iniciando testes do EPG Downloader...\n")
    
    tests = [
        ("Importações", test_imports),
        ("Classe EPGDownloader", test_epg_downloader),
        ("Acessibilidade da URL", test_url_accessibility)
    ]
    
    passed = 0
    total = len(tests)
    
    for test_name, test_func in tests:
        print(f"\n📋 {test_name}:")
        if test_func():
            passed += 1
        print()
    
    print("=" * 50)
    print(f"📊 Resultado dos testes: {passed}/{total} passaram")
    
    if passed == total:
        print("🎉 Todos os testes passaram! O sistema está funcionando.")
        return 0
    else:
        print("⚠️ Alguns testes falharam. Verifique os erros acima.")
        return 1

if __name__ == "__main__":
    sys.exit(main()) 