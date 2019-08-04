from mycroft import MycroftSkill, intent_file_handler


class PixelDungeon(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('dungeon.pixel.intent')
    def handle_dungeon_pixel(self, message):
        self.speak_dialog('dungeon.pixel')


def create_skill():
    return PixelDungeon()

