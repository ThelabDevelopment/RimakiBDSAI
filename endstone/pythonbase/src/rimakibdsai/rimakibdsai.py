from endstone.plugin import Plugin

class rimakibdsai(Plugin):
    api_version = "0.10.6"

    def on_load(self):
        self.logger.WARNING("Expermental RimakiAPI Is Loading")
        self.logger.WARNING("Support is not Guranteed")

    def on_enable(self):
        self.logger.INFO("RimakiBDSAI Enabled")
        self.logger.WARNING("This is Expermential API \n Support Is not Guranteed")

    def on_disable(self):
        self.logger.INFO("RimakiBDSAI Disabled")
