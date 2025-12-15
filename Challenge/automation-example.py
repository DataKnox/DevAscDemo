import paramiko
import json
from datetime import datetime

class NetworkAutomation:
    def __init__(self, host, username, password):
        self.host = host
        self.username = username
        self.password = password
        self.client = None
    
    def connect(self):
        """Connect to network device via SSH"""
        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.client.connect(self.host, username=self.username, password=self.password)
        print(f"Connected to {self.host}")
    
    def execute_command(self, command):
        """Execute a command on the device"""
        stdin, stdout, stderr = self.client.exec_command(command)
        return stdout.read().decode()
    
    def get_interfaces(self):
        """Retrieve interface information"""
        output = self.execute_command("show interfaces")
        return output
    
    def backup_config(self):
        """Backup device configuration"""
        config = self.execute_command("show running-config")
        filename = f"backup_{self.host}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        with open(filename, 'w') as f:
            f.write(config)
        print(f"Configuration backed up to {filename}")
    
    def disconnect(self):
        """Close SSH connection"""
        if self.client:
            self.client.close()
            print("Disconnected")

if __name__ == "__main__":
    # Example usage
    automation = NetworkAutomation("192.168.1.1", "admin", "password")
    automation.connect()
    automation.backup_config()
    interfaces = automation.get_interfaces()
    print(interfaces)
    automation.disconnect()