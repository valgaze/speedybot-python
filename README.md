# [🐍 Speedybot-python](https://pypi.org/project/speedybot)

For the impatient, just go here: **[quickstart.md](https://github.com/valgaze/speedybot-python/blob/deploy/quickstart.md)**

```md
╔═╗ ╔═╗ ╔═╗ ╔═╗ ╔╦╗ ╦ ╦ ╔╗  ╔═╗ ╔╦╗ 
╚═╗ ╠═╝ ║╣  ║╣   ║║ ╚╦╝ ╠╩╗ ║ ║  ║  
╚═╝ ╩   ╚═╝ ╚═╝ ═╩╝  ╩  ╚═╝ ╚═╝  ╩
```

## What is SpeedyBot?

SpeedyBot is a library that makes it speedy and easy to build high-quality, user-valuable bots with rich interaction + conversation design.

Keep your eyes here for updates: https://speedybot.js.org

## SpeedyCards

SpeedyBot abstracts over a lot of API details for you, but perhaps its most immediately useful feature is that it makes creating visually complex + rich Adpative Cards speedy and easy.

It's all the power of adaptive cards with none of the hassle or wrangling-- and you even get type'ing assistance

![speedycard](https://raw.githubusercontent.com/valgaze/speedybot-python/main/assets/speedycard.gif)

## Getting Started

```
pip install -U speedybot
```

## Quickstart

```python
from speedybot import SpeedyBot

## Setup/import your bot
## Get a bot token here: https://developer.webex.com/my-apps/new/bot
bot = SpeedyBot("__REPLACE__ME__")

## Send Messages
messsage = bot.send_to("valgaze@cisco.com", "here is **my message**")

## Reply to Messages
roomId = messsage['roomId']
messageId = messsage['id']

bot.reply(roomId, messageId, 'This is a reply')

## Cards + fun

## Unleash the power of cards!
# More info at our Buttons & Cards guide: https://developer.webex.com/docs/buttons-and-cards

card = bot.card() \
    .add_title('Earnest Shackleton Expedition') \
    .add_subtitle('Survival in the Antarctic Wilderness') \
    .add_text("As we embarked on the Earnest Shackleton Expedition, our success hinged on the equipment we carried. "
              "Our inventory was meticulously chosen to ensure our survival in the harsh Antarctic wilderness and guide us through "
              "uncharted territories. Here's what we packed:",
              horizontalAlignment="Center", color="Accent") \
    .add_table([
        ['Equipment', 'Quantity'],
        ['Maps', '2'],
        ['Compasses', '2'],
        ['Torches', '4'],
        ['Provisions', '10 months'],
        ['Rope', '50 meters'],
        ['First Aid Kit', '1'],
    ]) \
    .add_text("With these supplies, we were well-prepared to face the challenges that lay ahead") \
    .add_link('https://en.wikipedia.org/wiki/Ernest_Shackleton', 'Explore Earnest Shackleton Expedition') \

# Embed a card within the card
sub_card = bot.card() \
        .add_subtitle('The Harsh Antarctic Wilderness') \
        .add_text("The Earnest Shackleton Expedition took us to the unforgiving Antarctic wilderness, filled with extreme cold, isolation, and constant danger. "
                  "Our survival equipment was our lifeline in these remote landscapes, ensuring our safety and "
                  "enabling us to explore the unknown with confidence")

card.add_subcard(sub_card)
bot.send_to('valgaze@cisco.com', card)

```

![card_demo](https://raw.githubusercontent.com/valgaze/speedybot-python/deploy/assets/shackleton_sample.gif)

## Tests

```
python3 -m unittest tests/test.py
```

## Publishing

```
poetry build
poetry publish
```

## Visual Studio Code issue

If you can't get auto-complete on visual studio you may need to select a Python interpeter

Select ⇧⌘P and search for `Python: Select Interpreter` and pick the interpeter that matches the version with your project (`python --version`), **[🔗 more details here](https://code.visualstudio.com/docs/python/environments)**

![speedycard](https://raw.githubusercontent.com/valgaze/speedybot-python/deploy/assets/vsc_interpreter.gif)
