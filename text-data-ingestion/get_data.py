#!/usr/bin/env python3
import subprocess
import sys
import os

def run_imessage_exporter():
    try:
        # Check if imessage-exporter is installed
        result = subprocess.run(['imessage-exporter', '--version'], 
                              capture_output=True, text=True)
        if result.returncode != 0:
            print("imessage-exporter not found. Please install it with:")
            print("cargo install imessage-exporter@3.0.1")
            return False
        
        # Run the export command
        cmd = [
            'imessage-exporter',
            '--format', 'txt',
            '--export-path', 'data/output',
            '--db-path', 'data/chat.db',
            '--copy-method', 'disabled'
        ]
        
        print("Running imessage-exporter...")
        print(f"Command: {' '.join(cmd)}")
        
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        if result.returncode == 0:
            print("iMessage data exported successfully to data/output/")
            print(result.stdout)
        else:
            print("❌ Export failed:")
            print(result.stderr)
            return False
            
        return True
        
    except FileNotFoundError:
        print("imessage-exporter not found. Please install it with:")
        print("cargo install imessage-exporter@3.0.1")
        return False
    except Exception as e:
        print(f"Error running imessage-exporter: {e}")
        return False

def show_help():
    """Show imessage-exporter help"""
    try:
        result = subprocess.run(['imessage-exporter', '--help'], 
                              capture_output=True, text=True)
        if result.returncode == 0:
            print(result.stdout)
        else:
            print("imessage-exporter not found. Please install it with:")
            print("cargo install imessage-exporter@3.0.1")
    except FileNotFoundError:
        print("imessage-exporter not found. Please install it with:")
        print("cargo install imessage-exporter@3.0.1")

def main():
    if len(sys.argv) > 1 and sys.argv[1] == '--default':
        # Run the export
        success = run_imessage_exporter()
        sys.exit(0 if success else 1)
    else:
        # Show help by default
        show_help()

if __name__ == "__main__":
    main() 