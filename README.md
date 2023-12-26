# Server Status Bot

## Overview

The Server Status Bot is a Discord bot designed to monitor the status of a server and send alerts to a specified channel in case of server downtime. This bot utilizes Discord.py library and features a background task that continuously checks the availability of a specified server IP and port.

## Setup

To use the Server Status Bot, follow these steps:

### 1. Install Dependencies

Make sure you have the required dependencies installed. You can install them using:

pip install requirements.txt

### 2. Set up Discord Bot

- Create a new Discord bot on the [Discord Developer Portal](https://discord.com/developers/applications).
- Copy the bot token and update the `.env` file with your token:

TOKEN=your_bot_token_here

### 3. Configure Server and Discord Settings

- Update the `.env` file with the server IP and port you want to monitor:

SERVER_IP=your_server_ip_here
PORT=your_server_port_here

- Specify the Discord channel ID where alerts will be sent:

ALERT_CHANNEL=your_alert_channel_id_here

- Set the number of consecutive seconds the server must be down to trigger an alert:

SECONDS_NEEDED_FOR_ALERT=your_seconds_needed_here

- Specify the Discord role ID to mention in the alert:

ADMIN_ROLE_ID=your_admin_role_id_here

### 4. Customize Embed (Optional)

You can customize the appearance of the alert message by modifying the `embed` object in the main.py.

### 5. Run the Bot

Execute the bot by running the Python script:

python main.py

## Additional Notes

- Ensure that the bot has the necessary permissions to read messages and send messages in the specified alert channel, as well as ping the admin role specified!
