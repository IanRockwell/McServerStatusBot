from bot.bot import ServerStatusBot
import os
from dotenv import load_dotenv
import discord

load_dotenv()

# Load environment variables
DISCORD_TOKEN = os.getenv("TOKEN")
SERVER_IP = os.getenv("SERVER_IP")
PORT = os.getenv("PORT")
ALERT_CHANNEL = os.getenv("ALERT_CHANNEL")
SECONDS_NEEDED_FOR_ALERT = os.getenv("SECONDS_NEEDED_FOR_ALERT")
ADMIN_ROLE_ID = os.getenv("ADMIN_ROLE_ID")

# Create an Embed instance
embed = discord.Embed(
    title="Server Down Alert",
    description=f"The GunjiCordia server has not responded to any pings for {SECONDS_NEEDED_FOR_ALERT} seconds",
    color=discord.Color.red()  # You can choose any color you prefer
)

embed.set_thumbnail(url="https://i.imgur.com/u3oCpOI.png")

if __name__ == "__main__":
    print("Initializing Discord Bot...")

    # Create an instance of the ServerStatusBot
    status_bot = ServerStatusBot(
        token=DISCORD_TOKEN,
        server_ip=SERVER_IP,
        port=PORT,
        alert_channel=ALERT_CHANNEL,
        seconds_needed_for_alert=SECONDS_NEEDED_FOR_ALERT,
        admin_role_id=ADMIN_ROLE_ID,
        embed=embed
    )

    # Run the Discord bot
    status_bot.run_bot()
