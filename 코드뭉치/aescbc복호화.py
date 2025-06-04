from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.clipboard import Clipboard
from base64 import b64decode
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from kivy.core.text import LabelBase

LabelBase.register(name='Roboto', fn_regular='NotoSansKR.ttf')

class AESDecryptor(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', **kwargs)

        self.add_widget(Label(text="AES-128 CBC 복호화기"))

        self.key_input = TextInput(hint_text="키 (16바이트)", multiline=False)
        self.add_widget(self.key_input)

        self.iv_input = TextInput(hint_text="IV (16바이트, base64, 비워두면 0으로 처리)", multiline=False)
        self.add_widget(self.iv_input)

        self.ciphertext_input = TextInput(hint_text="암호문 (base64)", multiline=False)
        self.add_widget(self.ciphertext_input)

        self.decrypt_button = Button(text="복호화")
        self.decrypt_button.bind(on_press=self.decrypt)
        self.add_widget(self.decrypt_button)

        # 결과 표시 영역 (가로 박스 안에 레이블과 버튼 배치)
        result_box = BoxLayout(orientation='horizontal', size_hint_y=None, height='40dp')
        self.result_label = Label(text="복호화된 평문이 여기에 표시됩니다", halign='center', valign='middle')
        self.result_label.bind(size=self.result_label.setter('text_size'))  # 텍스트 줄바꿈 위해

        copy_button = Button(text="복사", size_hint_x=None, width='80dp')
        copy_button.bind(on_press=self.copy_to_clipboard)

        result_box.add_widget(self.result_label)
        result_box.add_widget(copy_button)

        self.add_widget(result_box)

    def decrypt(self, instance):
        try:
            key = self.key_input.text.encode('utf-8')
            if len(key) != 16:
                self.result_label.text = "키는 정확히 16바이트여야 합니다."
                return

            iv_text = self.iv_input.text.strip()
            if iv_text == '':
                iv = b'\x00' * 16
            else:
                iv = b64decode(iv_text)

            ciphertext = b64decode(self.ciphertext_input.text)

            cipher = AES.new(key, AES.MODE_CBC, iv)
            plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)

            self.result_label.text = "복호화 결과 : " + plaintext.decode('utf-8')
        except Exception as e:
            self.result_label.text = f"오류 발생: {str(e)}"

    def copy_to_clipboard(self, instance):
        Clipboard.copy(self.result_label.text)


class AESApp(App):
    def build(self):
        return AESDecryptor()


if __name__ == "__main__":
    AESApp().run()
