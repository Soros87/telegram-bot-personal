import config
from telethon import TelegramClient

# Create the client and connect
client = TelegramClient(config.MY_USERNAME , config.API_ID, config.API_HASH)

async def main():
    # Now you can use all client methods listed below, like for example...
    # await client.send_message('me', 'Hello to myself!')

    readUser= config.READUSER

    # Get information about the User you are reading the message from
    entity = await client.get_entity(readUser)

    # Print the chat ID
    print(f"Chat ID of {readUser}: {entity.id}")

    # Replace 'limit' with the number of messages you want to retrieve
    limit = 10
    messages = await client.get_messages(entity, limit=limit)
    
     # Get information about the User you are sending the message to
    sendUser= config.SENDUSER
    recipient = await client.get_entity(sendUser)

    # Print the chat ID
    print(f"Chat ID of recipient: {recipient.id}")

    #APPLICATION LOGIC
    for message in messages:
        if message.from_id is None and not message.text.startswith("Give me a moment"):
            await client.send_message(recipient,message.text)
            print(f"{message.text}")

with client:
    client.loop.run_until_complete(main())