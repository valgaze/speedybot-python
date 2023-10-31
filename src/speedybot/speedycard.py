import copy

class SpeedyCard:
    def __init__(self):
        self.json = {
            "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
            "type": "AdaptiveCard",
            "version": "1.0",
            "body": [],
        }
        self._stash = {
            "needsSubmit": False,
            "title": "",
            "subTitle": "",
            "chips": [],
            "data": {},
            "submitLabel": "Submit",
            "backgroundImage": ""
        }

        self.id = {}

    def check_id(self, id=""):
        if id in self.id:
            self.id[id] += 1
            return f"{id}_{self.id[id]}"
        else:
            self.id[id] = 1
            return id

    def add_title(self, title: str):
        """
        Args:
            title (str): card's title
        """

        self._stash["title"] = title
        return self

    def add_subtitle(self, subTitle: str):
        """
        Args:
            subTitle (str): card's subtitle
        """
        self._stash["subTitle"] = subTitle
        return self
    
    def add_image(self, url, size="ExtraLarge"):
        """
        Args:
            url (str): add a url to a publically addressable image url
        """
        if url:
            self.json["body"].append({
                "horizontalAlignment": "Center",
                "size": size,
                "type": "Image",
                "url": url,
            })

    def add_subcard(self, card: 'SpeedyCard', label="Open"):
        """
        Args:
            card (SpeedyCard): adds a subcard, must be a SpeedyCard
        """
        payload =   {
            "type": "Action.ShowCard",
            "title": label,
            "card": card.build()
        }
        self.add_action(payload)
        return self

    def add_text(self, text:str, horizontalAlignment=None, size=None, color=None):
        """
        Arguments are case-sensitive
        Args:
            horizontalAlignment (str): Horizontal alignment ("Left", "Center", "Right").
            size (str): Size option ("Small", "Default", "Medium", "Large", "ExtraLarge").
            color (str): ("Default", "Dark", "Light", "Accent", "Good", "Warning", "Attention").            
        """

        self.json["body"].append({
            "type": "TextBlock",
            "text": text,
            "wrap": True,
            "size": size,
            "horizontalAlignment": horizontalAlignment,
            "color": color
        }) 
        return self

    def add_table(self, input, separator=False):
        if not isinstance(input, list) or not all(isinstance(item, list) for item in input):
            raise ValueError("Input should be a list of lists")

        facts = [{"title": item[0], "value": item[1]} for item in input]
        result = {
            "type": "FactSet",
            "separator": separator,
            "facts": facts
        }
        self.json["body"].append(result)
        return self

    def buildTextPayload(self, text, config):
        if config is None:
            config = {}

        size = config.get("size", "Medium")
        align = config.get("align", "Left")
        color = config.get("color")

        text_block = {
            "type": "TextBlock",
            "text": text,
            "wrap": True,
            "size": size,
            "horizontalAlignment": align,
            **({"color": color} if color is not None else {})
        }
        return text_block

    def setBackgroundImage(self, url: str):
        self._stash["backgroundImage"] = url
        return self

    def addLink(self, url: str, label: str = None):
        if label is None:
            label = url
        self.add_text(f"**[{label}]({url})**")
        return self

    def build(self):
        result_json = copy.deepcopy(self.json) 
        if self._stash["subTitle"]:
            result_json["body"].insert(0, self.buildTextPayload(self._stash["subTitle"], {}))

        if self._stash["title"]:
            result_json["body"].insert(
                0,
                self.buildTextPayload(self._stash["title"], {
                    "weight": "Bolder",
                    "size": "ExtraLarge",
                })
            )

        if self._stash["backgroundImage"]:
            result_json["backgroundImage"] = self._stash["backgroundImage"]

        # if self._stash["needsSubmit"]:
        #     payload = {"type": "Action.Submit", "title": self._stash["submitLabel"]}

        return result_json
    
    # Stay tuned, if you need something now, see https://speedybot.js.org
    def add_action(self, action):
        if "actions" not in self.json:
            self.json["actions"] = []
        self.json["actions"].append(action)


