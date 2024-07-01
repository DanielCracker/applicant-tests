from typing import Union


class GlowLampSwitcher:

    def __init__(self) -> None:
        self.on_state = False

    def on(self) -> None:
        print('Лампа накаливания включена...')
        print('Логика реализации включения лампы накаливания...')
        self.on_state = True

    def turn_off(self) -> None:
        print('Лампа накаливания выключена...')
        print('Логика реализации выключения лампы накаливания...')
        self.on_state = False


class HalogenLampSwitcher:

    def __init__(self) -> None:
        self.on_state = False

    def turn_on(self) -> None:
        print('Галогенная лампа включена...')
        print('Логика реализации включения галогена...')
        self.on_state = True

    def off(self) -> None:
        print('Галогенная лампа выключена...')
        print('Логика реализации выключения галогена...')
        self.on_state = False


class AnotherLampSwitcher:

    def __init__(self) -> None:
        self.on_state = False

    def lamp_on(self) -> None:
        print('Ещё лампа включена...')
        print('Специфическая логика реализации включения лампы...')
        self.on_state = True

    def lamp_off(self) -> None:
        print('Ещё лампа выключена...')
        print('Специфическая логика реализации выключения лампы...')
        self.on_state = False


class ElectricLightSwitchManager:

    def __init__(self):
        self.switchers = []

    def append_switch(self, switcher: Union[GlowLampSwitcher, HalogenLampSwitcher, AnotherLampSwitcher]):
        self.switchers.append(switcher)

    def press(self) -> None:
        for switcher in self.switchers:
            if isinstance(switcher, GlowLampSwitcher):
                if switcher.on_state:
                    switcher.turn_off()
                else:
                    switcher.on()
            elif isinstance(switcher, HalogenLampSwitcher):
                if switcher.on_state:
                    switcher.off()
                else:
                    switcher.turn_on()
            elif isinstance(switcher, AnotherLampSwitcher):
                if switcher.on_state:
                    switcher.lamp_off()
                else:
                    switcher.lamp_on()


def main() -> None:
    manager = ElectricLightSwitchManager()
    manager.append_switch(GlowLampSwitcher())
    manager.append_switch(HalogenLampSwitcher())
    manager.append_switch(AnotherLampSwitcher())
    manager.press()
    manager.press()



if __name__ == '__main__':
    main()
