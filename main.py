from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Button, Label

class VoiceAssistantApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=50, spacing=20)
        
        self.label = Label(text='مرحباً بك في مساعدك الصوتي', font_size=24)
        button = Button(text='اضغط للتحدث', font_size=20, size_hint=(1, 0.3))
        
        button.bind(on_press=self.on_button_press)
        
        layout.add_widget(self.label)
        layout.add_widget(button)
        return layout

    def on_button_press(self, instance):
        self.label.text = 'جاري الاستماع...'

if __name__ == '__main__':
    VoiceAssistantApp().run()
