from mycroft import MycroftSkill, intent_file_handler


class WildRace(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('race.wild.intent')
    def handle_race_wild(self, message):
        self.speak_dialog('race.wild')


def create_skill():
    return WildRace()

