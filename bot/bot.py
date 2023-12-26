import socket
import discord
from discord.ext import tasks
from dotenv import load_dotenv

load_dotenv()

class ServerStatusBot(discord.Client):
    """
    Discord bot to monitor the status of a server and send alerts to a specified channel.
    """

    def __init__(self, token, server_ip, port, alert_channel, seconds_needed_for_alert, admin_role_id, embed):
        """
        Constructor for the ServerStatusBot class.

        Parameters:
        - token (str): Discord bot token.
        - server_ip (str): IP address of the server to monitor.
        - port (int): Port number of the server.
        - alert_channel (int): ID of the Discord channel to send alerts.
        - seconds_needed_for_alert (int): Number of consecutive seconds the server must be down to trigger an alert.
        - admin_role_id (int): ID of the Discord role to mention in the alert.
        - embed (discord.Embed): Embed object for the alert message.
        """

        # Initialize the Discord client with custom intents.
        intents = discord.Intents.default()
        intents.message_content = True
        super().__init__(intents=intents)

        # Assign input parameters to class attributes.
        self.token = token
        self.consecutive_failures = 0
        self.server_ip = server_ip
        self.port = int(port)
        self.alert_channel = int(alert_channel)
        self.seconds_needed = int(seconds_needed_for_alert)
        self.admin_role_id = admin_role_id
        self.embed = embed

    async def on_ready(self):
        """
        Event handler called when the bot has successfully connected to Discord.
        """
        print(f'We have logged in as {self.user}')
        # Start the background task to check server status.
        self.check_server_status.start()

    def check_port(self, ip, port):
        """
        Check if a given port on a server is open.

        Parameters:
        - ip (str): IP address of the server.
        - port (int): Port number to check.

        Returns:
        - int: 0 if the port is open, an error code otherwise.
        """
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)

        result = sock.connect_ex((ip, port))
        sock.close()

        return result

    @tasks.loop(seconds=1)
    async def check_server_status(self):
        """
        Background task to check the status of the server and send alerts if necessary.
        """
        result = self.check_port(self.server_ip, self.port)

        if result == 0:
            print(f"Port {self.port} on {self.server_ip} is open")
            self.consecutive_failures = 0
        else:
            print(f"Port {self.port} on {self.server_ip} is closed")
            self.consecutive_failures += 1

            if self.consecutive_failures == self.seconds_needed:
                print("Server is consistently closed. Sending a message to Discord.")
                channel_id = self.alert_channel
                channel = self.get_channel(channel_id)

                if channel:
                    # Mention the admin role and send the embed.
                    await channel.send(f"<@&{self.admin_role_id}>")
                    await channel.send(embed=self.embed)
                else:
                    print("Invalid channel ID. Please check and update.")

    def run_bot(self):
        """
        Start the Discord bot.
        """
        self.run(self.token)
