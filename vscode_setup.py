#!/usr/bin/env python3
"""
VS Code Quick Setup Script for Dask RFM Project
Bu script'i çalıştırarak VS Code'unuzu otomatik configure edebilirsiniz.
"""

import os
import json
import subprocess
import sys
from pathlib import Path

class VSCodeSetup:
    def __init__(self):
        self.extensions = [
            "ms-python.python",
            "ms-python.vscode-pylance", 
            "ms-toolsai.jupyter",
            "ms-toolsai.jupyter-keymap",
            "ms-toolsai.jupyter-renderers",
            "njpwerner.autodocstring",
            "ms-python.black-formatter"
        ]
        
        self.settings = {
            "python.defaultInterpreterPath": "./venv/bin/python",
            "python.terminal.activateEnvironment": True,
            "jupyter.askForKernelRestart": False,
            "jupyter.interactiveWindow.textEditor.executeSelection": True,
            "python.formatting.provider": "black",
            "python.linting.enabled": True,
            "python.linting.pylintEnabled": True,
            "files.associations": {
                "*.py": "python"
            },
            "python.analysis.autoImportCompletions": True,
            "python.analysis.typeCheckingMode": "basic",
            "editor.formatOnSave": True,
            "editor.codeActionsOnSave": {
                "source.organizeImports": True
            }
        }

    def install_extensions(self):
        """VS Code extension'larını yükle"""
        print("🔧 Installing VS Code Extensions...")
        
        for extension in self.extensions:
            try:
                print(f"   Installing {extension}...")
                result = subprocess.run(
                    ["code", "--install-extension", extension], 
                    capture_output=True, 
                    text=True,
                    timeout=30
                )
                
                if result.returncode == 0:
                    print(f"   ✅ {extension} installed successfully")
                else:
                    print(f"   ⚠️ Failed to install {extension}: {result.stderr}")
                    
            except subprocess.TimeoutExpired:
                print(f"   ⏰ Timeout installing {extension}")
            except FileNotFoundError:
                print("   ❌ VS Code 'code' command not found in PATH")
                print("   💡 Please install VS Code and add it to PATH, then try again")
                return False
        
        return True

    def setup_workspace_settings(self):
        """Workspace settings oluştur"""
        print("📁 Setting up workspace configuration...")
        
        # .vscode klasörü oluştur
        vscode_dir = Path(".vscode")
        vscode_dir.mkdir(exist_ok=True)
        
        # extensions.json oluştur
        extensions_config = {
            "recommendations": self.extensions
        }
        
        with open(vscode_dir / "extensions.json", "w") as f:
            json.dump(extensions_config, f, indent=2)
        
        print("   ✅ Workspace extensions configuration created")
        
        # settings.json oluştur
        with open(vscode_dir / "settings.json", "w") as f:
            json.dump(self.settings, f, indent=2)
        
        print("   ✅ Workspace settings configuration created")
        
        # launch.json oluştur (debugging için)
        launch_config = {
            "version": "0.2.0",
            "configurations": [
                {
                    "name": "Debug RFM Analysis",
                    "type": "python",
                    "request": "launch",
                    "program": "${workspaceFolder}/src/dask_rfm_analyzer.py",
                    "console": "integratedTerminal",
                    "cwd": "${workspaceFolder}",
                    "env": {
                        "PYTHONPATH": "${workspaceFolder}"
                    },
                    "args": []
                },
                {
                    "name": "Debug with Dask Local Cluster",
                    "type": "python",
                    "request": "launch", 
                    "program": "${workspaceFolder}/main.py",
                    "console": "integratedTerminal",
                    "env": {
                        "DASK_SCHEDULER": "threads",
                        "PYTHONPATH": "${workspaceFolder}"
                    }
                }
            ]
        }
        
        with open(vscode_dir / "launch.json", "w") as f:
            json.dump(launch_config, f, indent=2)
        
        print("   ✅ Debug configuration created")
        
        # tasks.json oluştur
        tasks_config = {
            "version": "2.0.0",
            "tasks": [
                {
                    "label": "Run RFM Analysis",
                    "type": "shell",
                    "command": "python",
                    "args": ["src/dask_rfm_analyzer.py"],
                    "group": "build",
                    "presentation": {
                        "echo": True,
                        "reveal": "always",
                        "focus": False,
                        "panel": "shared"
                    }
                },
                {
                    "label": "Start Dask Dashboard",
                    "type": "shell",
                    "command": "python",
                    "args": ["-c", "from dask.distributed import Client; Client()"],
                    "group": "build"
                }
            ]
        }
        
        with open(vscode_dir / "tasks.json", "w") as f:
            json.dump(tasks_config, f, indent=2)
        
        print("   ✅ Tasks configuration created")

    def setup_global_settings(self):
        """Global VS Code settings'i güncelle"""
        print("🌐 Updating global VS Code settings...")
        
        # Windows
        if sys.platform == "win32":
            settings_path = Path.home() / "AppData/Roaming/Code/User/settings.json"
        # macOS
        elif sys.platform == "darwin":
            settings_path = Path.home() / "Library/Application Support/Code/User/settings.json"
        # Linux
        else:
            settings_path = Path.home() / ".config/Code/User/settings.json"
        
        # Mevcut settings'i oku (varsa)
        existing_settings = {}
        if settings_path.exists():
            try:
                with open(settings_path, "r") as f:
                    existing_settings = json.load(f)
            except json.JSONDecodeError:
                print("   ⚠️ Existing settings.json is corrupted, creating new one")
        
        # Yeni settings'i merge et
        existing_settings.update(self.settings)
        
        # Settings klasörünü oluştur (yoksa)
        settings_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Settings'i kaydet
        with open(settings_path, "w") as f:
            json.dump(existing_settings, f, indent=2)
        
        print(f"   ✅ Global settings updated: {settings_path}")

    def create_project_structure(self):
        """Proje klasör yapısını oluştur"""
        print("📂 Creating project structure...")
        
        folders = [
            "src",
            "data", 
            "output",
            "notebooks",
            "config",
            "tests"
        ]
        
        for folder in folders:
            Path(folder).mkdir(exist_ok=True)
            
            # __init__.py dosyaları oluştur (Python package'ları için)
            if folder in ["src", "tests"]:
                (Path(folder) / "__init__.py").touch()
        
        print("   ✅ Project structure created")
        
        # .gitignore oluştur
        gitignore_content = """
# Python
__pycache__/
*.pyc
*.pyo
*.egg-info/
dist/
build/
.env

# Jupyter
.ipynb_checkpoints/

# Dask
dask-worker-space/
*.html

# Data files (büyük dosyalar için)
data/*.csv
data/*.xlsx
!data/sample_data.csv

# Output
output/*.csv
output/*.xlsx
!output/.gitkeep

# VS Code
.vscode/settings.json
!.vscode/extensions.json
!.vscode/launch.json
!.vscode/tasks.json

# Virtual environment
venv/
env/
.conda/
"""
        
        with open(".gitignore", "w") as f:
            f.write(gitignore_content.strip())
        
        print("   ✅ .gitignore created")

    def install_python_packages(self):
        """Gerekli Python paketlerini yükle"""
        print("📦 Installing Python packages...")
        
        packages = [
            "dask[complete]",
            "dask-ml", 
            "pandas",
            "numpy",
            "scikit-learn",
            "matplotlib",
            "seaborn",
            "jupyter",
            "black",
            "pylint",
            "openpyxl"
        ]
        
        try:
            for package in packages:
                print(f"   Installing {package}...")
                subprocess.run([sys.executable, "-m", "pip", "install", package], 
                             check=True, capture_output=True)
            
            print("   ✅ All packages installed successfully")
            return True
            
        except subprocess.CalledProcessError as e:
            print(f"   ❌ Failed to install packages: {e}")
            return False

    def run_setup(self):
        """Tam setup'ı çalıştır"""
        print("🚀 VS Code Dask RFM Project Setup")
        print("=" * 50)
        
        # 1. Extension'ları yükle
        if not self.install_extensions():
            print("❌ Extension installation failed, continuing with other steps...")
        
        # 2. Workspace settings
        self.setup_workspace_settings()
        
        # 3. Global settings
        try:
            self.setup_global_settings()
        except Exception as e:
            print(f"   ⚠️ Failed to update global settings: {e}")
        
        # 4. Proje yapısı
        self.create_project_structure()
        
        # 5. Python packages
        install_packages = input("\n📦 Do you want to install Python packages? (y/n): ")
        if install_packages.lower() == 'y':
            self.install_python_packages()
        
        print("\n" + "=" * 50)
        print("✅ VS Code Setup Complete!")
        print("=" * 50)
        
        print("\n📋 Next Steps:")
        print("1. Restart VS Code")
        print("2. Open this folder in VS Code: File > Open Folder")
        print("3. Select Python interpreter: Ctrl+Shift+P > Python: Select Interpreter")
        print("4. Start coding your Dask RFM analysis!")
        
        print("\n🔍 Useful Commands:")
        print("• F5: Start debugging")
        print("• Ctrl+Shift+P: Command palette")
        print("• Ctrl+`: Toggle terminal")
        print("• Ctrl+Shift+E: File explorer")

def main():
    setup = VSCodeSetup()
    setup.run_setup()

if __name__ == "__main__":
    main()