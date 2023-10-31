import unittest
import json
from speedybot.speedycard import SpeedyCard

# from speedybot import SpeedyBot
class TestBotMethods(unittest.TestCase):
    # Sanity check for 'add_title' + 'add_subtitle' methods of 'SpeedyCard'
    # These are stashed but only inserted at build time for the card
    def test_add_title(self):
        card = SpeedyCard()
        modified_card = card.add_title("Test Title").add_subtitle("beer")
        self.assertEqual(modified_card._stash["title"], "Test Title")
        self.assertEqual(modified_card._stash["subTitle"], "beer")
        card_data = {"$schema":"http://adaptivecards.io/schemas/adaptive-card.json","type":"AdaptiveCard","version":"1.0","body":[{"type":"TextBlock","text":"My title","wrap":True,"size":"ExtraLarge","horizontalAlignment":"Left"},{"type":"TextBlock","text":"My subtitle","wrap":True,"size":"Medium","horizontalAlignment":"Left"}]}

    def test_add_title(self):
        card = SpeedyCard().add_title('My title').add_subtitle('My subtitle')
        expected = {"$schema":"http://adaptivecards.io/schemas/adaptive-card.json","type":"AdaptiveCard","version":"1.0","body":[{"type":"TextBlock","text":"My title","wrap":True,"size":"ExtraLarge","horizontalAlignment":"Left"},{"type":"TextBlock","text":"My subtitle","wrap":True,"size":"Medium","horizontalAlignment":"Left"}]}
        actual = card.build()
        self.assertDictEqual(actual, expected)

    def test_card_renders(self):
        card = SpeedyCard() \
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
        .addLink('https://en.wikipedia.org/wiki/Ernest_Shackleton', 'Explore Earnest Shackleton Expedition')
       
        expected = {'$schema': 'http://adaptivecards.io/schemas/adaptive-card.json', 'type': 'AdaptiveCard', 'version': '1.0', 'body': [{'type': 'TextBlock', 'text': 'Earnest Shackleton Expedition', 'wrap': True, 'size': 'ExtraLarge', 'horizontalAlignment': 'Left'}, {'type': 'TextBlock', 'text': 'Survival in the Antarctic Wilderness', 'wrap': True, 'size': 'Medium', 'horizontalAlignment': 'Left'}, {'type': 'TextBlock', 'text': "As we embarked on the Earnest Shackleton Expedition, our success hinged on the equipment we carried. Our inventory was meticulously chosen to ensure our survival in the harsh Antarctic wilderness and guide us through uncharted territories. Here's what we packed:", 'wrap': True, 'size': None, 'horizontalAlignment': 'Center', 'color': 'Accent'}, {'type': 'FactSet', 'separator': False, 'facts': [{'title': 'Equipment', 'value': 'Quantity'}, {'title': 'Maps', 'value': '2'}, {'title': 'Compasses', 'value': '2'}, {'title': 'Torches', 'value': '4'}, {'title': 'Provisions', 'value': '10 months'}, {'title': 'Rope', 'value': '50 meters'}, {'title': 'First Aid Kit', 'value': '1'}]}, {'type': 'TextBlock', 'text': 'With these supplies, we were well-prepared to face the challenges that lay ahead', 'wrap': True, 'size': None, 'horizontalAlignment': None, 'color': None}, {'type': 'TextBlock', 'text': '**[Explore Earnest Shackleton Expedition](https://en.wikipedia.org/wiki/Ernest_Shackleton)**', 'wrap': True, 'size': None, 'horizontalAlignment': None, 'color': None}]}
        actual = card.build()
        self.assertDictEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()