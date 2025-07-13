Here is a simple Python script that represents the act of deploying scout bots to the shadow net in the context of a text-based game or simulation:

```python
class Bot:
    def __init__(self, name, type):
        self.name = name
        self.type = type

    def deploy(self, network):
        print(f"Deploying {self.type} bot {self.name} to {network}.")

class ShadowNet:
    def __init__(self):
        self.bots = []

    def add_bot(self, bot):
        self.bots.append(bot)
        bot.deploy("shadow net")

if __name__ == "__main__":
    shadow_net = ShadowNet()

    bot1 = Bot("scout_1", "scout")
    bot2 = Bot("scout_2", "scout")

    shadow_net.add_bot(bot1)
    shadow_net.add_bot(bot2)
```

In this script, we have created two classes: Bot and ShadowNet. The Bot class represents a bot with a name and type, and it has a method `deploy()` that prints a message indicating the bot has been deployed to a network. The ShadowNet class represents the shadow net and contains a list of bots. The method `add_bot()` adds a bot to the shadow net and calls the `deploy()` method of the Bot class.

Please note that in reality, deploying bots to a network would be a much more complex process involving connections, permissions, security considerations, and probably wouldn't be done through Python script in a literal sense. This script is a major simplification just to illustrate the concept.