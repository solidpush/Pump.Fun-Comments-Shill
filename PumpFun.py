import random
import time

class PumpFun:
    def __init__(self, token_name):
        self.token_name = token_name
        self.wallets = []
        self.comments = []
        self.shill_messages = []

    def generate_fresh_wallets(self, count):
        print(f"Generating {count} fresh wallets for {self.token_name}...")
        self.wallets = [f"wallet_{random.randint(10000, 99999)}" for _ in range(count)]
        print("Fresh wallets generated.")

    def add_comments(self, comments_list):
        print("Adding comments to the tool...")
        self.comments = comments_list
        print("Comments added.")

    def create_thread(self):
        if not self.wallets or not self.comments:
            print("Error: No wallets or comments available. Please add them first.")
            return
        
        print(f"Creating a thread for token: {self.token_name}")
        for wallet in self.wallets:
            comment = random.choice(self.comments)
            print(f"Wallet {wallet} says: {comment}")
            time.sleep(1)  # Simulate delay for realism

    def shill_mode(self, messages, delay=2):
        print("Shill mode activated. Spamming messages...")
        self.shill_messages = messages
        for i in range(10):  # Example loop for spamming
            message = random.choice(self.shill_messages)
            print(f"Shilling: {message}")
            time.sleep(delay)  # Delay between messages

if __name__ == "__main__":
    print("Welcome to Pump.Fun Comments & Shill Tool!")
    print("To get started, create threads and shill your token effectively.")
    print("For more information or inquiries, contact me on Telegram at t.me/mxdotsol")
    
    # Example usage
    tool = PumpFun("YourTokenName")
    tool.generate_fresh_wallets(5)
    tool.add_comments(["Great token!", "This is the future!", "Check out this project!"])
    tool.create_thread()
    tool.shill_mode(["Buy now!", "Don't miss this gem!", "Huge potential!"])
