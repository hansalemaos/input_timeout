import time
import kthread
import sys
import keyboard as keyboard__


class InputTimeout:
    def __init__(
        self,
        timeout,
        input_message="",
        timeout_message="",
        defaultvalue="",
        cancelbutton=None,
        show_special_characters_warning=None,
    ):
        keyboard__.unhook_all()
        self.interval = timeout
        self.finalvalue = ""
        self.defaultvalue = defaultvalue
        self.input_message = input_message
        self.start_time = time.time()
        self.end_time = time.time() + self.interval
        self.enter_pressed = False
        self.timeout_message = timeout_message
        self.cancelbutton = cancelbutton
        self.show_special_characters_warning = show_special_characters_warning
        if self.show_special_characters_warning is not None:
            print(self.show_special_characters_warning)
        self.specialkeyslist = {
            "0192": "À",
            "0193": "Á",
            "0196": "Ä",
            "0194": "Â",
            "0195": "Ã",
            "0197": "Å",
            "0198": "Æ",
            "0228": "ä",
            "0224": "à",
            "0225": "á",
            "0226": "â",
            "0227": "ã",
            "0229": "å",
            "0230": "æ",
            "0199": "Ç",
            "0231": "ç",
            "0208": "Ð",
            "0240": "ð",
            "0203": "Ë",
            "0200": "È",
            "0201": "É",
            "0202": "Ê",
            "0235": "ë",
            "0232": "è",
            "0233": "é",
            "0234": "ê",
            "0207": "Ï",
            "0204": "Ì",
            "0205": "Í",
            "0206": "Î",
            "0239": "ï",
            "0236": "ì",
            "0237": "í",
            "0238": "î",
            "0209": "Ñ",
            "0241": "ñ",
            "0214": "Ö",
            "0210": "Ò",
            "0211": "Ó",
            "0212": "Ô",
            "0213": "Õ",
            "0216": "Ø",
            "0140": "Œ",
            "0246": "ö",
            "0242": "ò",
            "0243": "ó",
            "0244": "ô",
            "0245": "õ",
            "0248": "ø",
            "0156": "œ",
            "0138": "Š",
            "0223": "ß",
            "0154": "š",
            "0222": "Þ",
            "0254": "þ",
            "0220": "Ü",
            "0217": "Ù",
            "0218": "Ú",
            "0219": "Û",
            "0252": "ü",
            "0249": "ù",
            "0250": "ú",
            "0251": "û",
            "0159": "Ÿ",
            "0221": "Ý",
            "0255": "ÿ",
            "0253": "ý",
            "0168": "¨",
            "0136": "ˆ",
            "0180": "´",
            "0175": "¯",
            "0184": "¸",
        }
        self.specialletter = ""
        self.start()

    def _write_status_quo(self):
        sys.stdout.write("\r")
        print(self.input_message, end=" ")
        print(self.finalvalue, end="")

    def callback(self, event):
        name = event.name
        if name == "ctrl":
            if self.show_special_characters_warning is not None:
                sys.stdout.write("\r\r")
                counter = 0
                print("", end="\n")
                for key, item in self.specialkeyslist.items():
                    print(f"alt+{key}\t->\t{item}", end="\t\t")
                    counter = counter + 1
                    if counter % 4 == 0:
                        print("", end="\n")
                self.specialletter = ""
                print("", end="\n")
                self._write_status_quo()
                return
        if keyboard__.is_pressed("alt"):

            self.specialletter = self.specialletter + name
            if (
                self.specialletter in self.specialkeyslist
                and len(self.specialletter) == 4
            ):
                spec_key = self.specialkeyslist[self.specialletter]
                self.finalvalue += spec_key
                self.specialletter = ""
            if len(self.specialletter) > 4:
                self.specialletter = ""
                self.finalvalue += "X"
            self._write_status_quo()
            return

        if self.cancelbutton is not None:
            if name == self.cancelbutton:
                self.enter_pressed = True
                keyboard__.unhook_all()
                return
        if name == "space":
            self.finalvalue += " "
            self._write_status_quo()

        if name == "backspace":
            self.finalvalue = self.finalvalue[:-1]
            self._write_status_quo()

        if name == "enter":
            return

        if len(name) == 1:
            self.finalvalue += name
            self._write_status_quo()

        keyboard__.press("backspace")

        self.specialletter = ""

    def _start_keyboard_observation(self):

        keyboard__.on_release(callback=self.callback)
        print("")
        sys.stdout.write("\r")

        print(self.input_message, end="")
        keyboard__.wait(hotkey="enter")
        self.enter_pressed = True
        keyboard__.unhook_all()

    def start(self):
        self.start_time = time.time()
        self.end_time = time.time() + self.interval
        t = kthread.KThread(
            target=self._start_keyboard_observation, name="_start_keyboard_observation"
        )
        t.start()
        while not self.enter_pressed:
            time.sleep(0.05)
            if time.time() > self.end_time:
                keyboard__.unhook_all()
                if t.is_alive():
                    try:
                        t.kill()
                    except Exception as Er:
                        pass
                for backsp in range(len(self.finalvalue)):
                    keyboard__.press("backspace")
                self.finalvalue = self.defaultvalue
                sys.stdout.write("\r\r")
                print(self.timeout_message)
                break
        else:
            keyboard__.unhook_all()
            self.enter_pressed = True
            if t.is_alive():
                try:
                    t.kill()
                except Exception as Er:
                    pass
            for backsp in range(len(self.finalvalue)):
                keyboard__.press("backspace")


if __name__ == "__main__":
    do_test = False
    if do_test:
        i = InputTimeout(
            timeout=20,
            input_message=" >> ",
            timeout_message="'Sorry, you were not fast enough'",
            defaultvalue="slow",
            cancelbutton="esc",
            show_special_characters_warning='If you want to use special characters, you have to use alt+\\d\\d\\d\\d\nPress "ctrl" to see a complete list of all combinations!',
        ).finalvalue
        print(f"\n\nYour input was {i}")

        i = InputTimeout(
            timeout=5,
            input_message=" >> ",
            timeout_message="Sorry, you were not fast enough: ",
            defaultvalue="slow",
            cancelbutton="esc",
            show_special_characters_warning='If you want to use special characters, you have to use alt+\\d\\d\\d\\d\nPress "ctrl" to see a complete list of all combinations!',
        ).finalvalue
        print(f"\n\nYour input was {i}")

        i = InputTimeout(
            timeout=10,
            input_message=" >> ",
            timeout_message="Sorry, you were not fast enough",
            defaultvalue="Wake up!",
            cancelbutton=None,
            show_special_characters_warning=None,
        ).finalvalue
        print(f"\n\nYour input was {i}")

        i = InputTimeout(
            timeout=10,
            input_message=" >> ",
            timeout_message="Sorry, you were not fast enough",
            defaultvalue="Are you sleeping?",
            cancelbutton="esc",
            show_special_characters_warning=None,
        ).finalvalue
        print(f"\n\nYour input was {i}")

        i = InputTimeout(
            timeout=10,
            input_message=" >>",
            timeout_message="Sorry, you were not fast enough",
            defaultvalue="you are so slow",
            cancelbutton=None,
            show_special_characters_warning='If you want to use special characters, you have to use alt+\\d\\d\\d\\d\nPress "ctrl" to see a complete list of all combinations!',
        ).finalvalue
        print(f"\n\nYour input was {i}")
