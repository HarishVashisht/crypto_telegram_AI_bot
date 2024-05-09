import telepot
import requests

# Replace with your bot token
TOKEN = "7100408493:AAGq6lN"

# Create a bot instance
bot = telepot.Bot(TOKEN)

# Define the start command handler
def handle_start(msg):
    chat_id = msg['chat']['id']
    bot.sendMessage(chat_id, "Hello! Welcome to the Sisy Crypto Bot, use /help to see available options.")

# Define the help command handler
def handle_help(msg):
    chat_id = msg['chat']['id']
    help_text = """
/start - Welcome message
/help - Show this help message
/content - About various articles
/nft_intro - Information about NFT
/top_nft_price - direct you to coin market cap
/blockchain_intro - Information about blockchain
/btcprice - Get the current Bitcoin prices
/contact - Contact information
"""
    bot.sendMessage(chat_id, help_text)

# Define the content command handler
def handle_content(msg):
    chat_id = msg['chat']['id']
    bot.sendMessage(chat_id, "We have various articles of crypto.")

# Define the NFT command handler
def handle_nft_intro(msg):
    chat_id = msg['chat']['id']
    nft_link = "https://youtu.be/NNQLJcJEzv0?si=NbkI1j26lL7kcqP1"
    bot.sendMessage(chat_id, f"Tutorial link: {nft_link}")

# Define the top_NFT_price command handler
def handle_top_nft_price(msg):
    chat_id = msg['chat']['id']
    nft_link = "https://coinmarketcap.com/nft/"
    bot.sendMessage(chat_id, f"Tutorial link: {nft_link}")

# Define the blockchain command handler
def handle_blockchain_intro(msg):
    chat_id = msg['chat']['id']
    blockchain_link = "https://youtu.be/MFw8Ax0p7dA?si=4jQgRqd_SLPqFpI4"
    bot.sendMessage(chat_id, f"Tutorial link: {blockchain_link}")

# Define the contact command handler
def handle_contact(msg):
    chat_id = msg['chat']['id']
    bot.sendMessage(chat_id, "You can contact us at email- harish.shanu001@gmail.com ")

# Define the Bitcoin price command handler
def handle_btcprice(msg):
    chat_id = msg['chat']['id']
    try:
        # Fetch Bitcoin prices from CoinDesk API
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        response.raise_for_status()
        data = response.json()
        bpi = data["bpi"]
        usd_price = bpi["USD"]["rate"]
        gbp_price = bpi["GBP"]["rate"]
        eur_price = bpi["EUR"]["rate"]

        # Send the Bitcoin prices to the user
        price_message = f"Current Bitcoin Prices:\n\nUSD: {usd_price}\nGBP: {gbp_price}\nEUR: {eur_price}"
        bot.sendMessage(chat_id, price_message)
    except requests.exceptions.RequestException as e:
        bot.sendMessage(chat_id, f"Error fetching Bitcoin prices: {e}")

# Define the function to handle incoming messages
def handle_message(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    if content_type == 'text':
        command = msg['text'].lower()
        if command in ['/start', 'hii', 'start']:
            handle_start(msg)
        elif command in ['/help', 'help']:
            handle_help(msg)
        elif command in ['/content', 'content']:
            handle_content(msg)
        elif command in ['/nft_intro', 'nftintro']:
            handle_nft_intro(msg)
        elif command in ['/top_nft_price', 'top nft price']:
            handle_top_nft_price(msg)
        elif command in ['/blockchain_intro', 'blockchain intro']:
            handle_blockchain_intro(msg)
        elif command in ['/contact', 'contact']:
            handle_contact(msg)
        elif command in ['/btcprice', 'btc price']:
            handle_btcprice(msg)
        else:
            bot.sendMessage(chat_id, "I'm sorry, I didn't understand that command, please use /help command.")

# Start the bot and listen for incoming messages
bot.message_loop(handle_message)

# Keep the program running
while True:
    pass
