from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.filechooser import FileChooserIconView
from kivy.uix.popup import Popup
from kivy.uix.scrollview import ScrollView
from kivy.uix.widget import Widget
from kivy.graphics import Color, Rectangle, RoundedRectangle
from kivy.core.window import Window

Window.size = (380, 720)

BG_COLOR      = (0.95, 0.98, 0.96, 1)
CARD_COLOR    = (1, 1, 1, 1)
PRIMARY       = (0.05, 0.60, 0.52, 1)
PRIMARY_DARK  = (0.03, 0.44, 0.38, 1)
PRIMARY_LIGHT = (0.88, 0.97, 0.95, 1)
TEXT_DARK     = (0.10, 0.16, 0.20, 1)
TEXT_MUTED    = (0.45, 0.52, 0.56, 1)
WARNING       = (0.82, 0.24, 0.24, 1)
WARNING_BG    = (1.0,  0.93, 0.93, 1)
SUCCESS       = (0.10, 0.62, 0.42, 1)


class StyledButton(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.background_normal = ''
        self.background_color = (0, 0, 0, 0)
        self.color = (1, 1, 1, 1)
        self.font_size = '14sp'
        self.bold = True
        self.size_hint_y = None
        self.height = 52
        with self.canvas.before:
            self._btn_color = Color(*PRIMARY)
            self._btn_rect = RoundedRectangle(
                pos=self.pos, size=self.size, radius=[14])
        self.bind(pos=self._update, size=self._update)
        self.bind(state=self._on_state)

    def _update(self, *args):
        self._btn_rect.pos = self.pos
        self._btn_rect.size = self.size

    def _on_state(self, instance, value):
        self._btn_color.rgba = PRIMARY_DARK if value == 'down' else PRIMARY


class Card(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas.before:
            Color(0.78, 0.88, 0.84, 0.35)
            self._shadow = RoundedRectangle(
                pos=(self.x - 2, self.y - 4),
                size=(self.width + 4, self.height + 4),
                radius=[20])
            Color(*CARD_COLOR)
            self._bg = RoundedRectangle(
                pos=self.pos, size=self.size, radius=[20])
        self.bind(pos=self._update, size=self._update)

    def _update(self, *args):
        self._shadow.pos = (self.x - 2, self.y - 4)
        self._shadow.size = (self.width + 4, self.height + 4)
        self._bg.pos = self.pos
        self._bg.size = self.size


class PrivacyBadge(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'horizontal'
        self.size_hint_y = None
        self.height = 36
        self.padding = [12, 6, 12, 6]
        self.spacing = 8
        with self.canvas.before:
            Color(*PRIMARY_LIGHT)
            self._bg = RoundedRectangle(
                pos=self.pos, size=self.size, radius=[10])
        self.bind(pos=self._u, size=self._u)
        
        text = Label(
            text='Fully offline. No data leaves your device',
            font_size='11sp', color=PRIMARY, bold=True,
            halign='center')
        text.bind(size=lambda s, v: setattr(s, 'text_size', v))
        self.add_widget(text)

    def _u(self, *args):
        self._bg.pos = self.pos
        self._bg.size = self.size


class DisclaimerScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas.before:
            Color(*BG_COLOR)
            self._bg = Rectangle(pos=self.pos, size=self.size)
        self.bind(pos=self._update_bg, size=self._update_bg)
        scroll = ScrollView(size_hint=(1, 1))
        outer = BoxLayout(
            orientation='vertical',
            padding=[24, 48, 24, 32],
            spacing=14,
            size_hint_y=None)
        outer.bind(minimum_height=outer.setter('height'))
        logo = Image(
            source='assets/logo.jpg',
            size_hint=(1, None), height=120,
            allow_stretch=True, keep_ratio=True)
        heading = Label(
            text='SkinSight',
            font_size='28sp', bold=True, color=TEXT_DARK,
            size_hint=(1, None), height=40, halign='center')
        heading.bind(size=lambda s, v: setattr(s, 'text_size', v))
        tagline = Label(
            text='Early skin guidance - Private - Offline - Accessible',
            font_size='12sp', color=TEXT_MUTED,
            size_hint=(1, None), height=24, halign='center')
        tagline.bind(size=lambda s, v: setattr(s, 'text_size', v))
        privacy = PrivacyBadge()
        disclaimer_card = Card(
            orientation='vertical',
            size_hint=(1, None), height=230,
            padding=[20, 20, 20, 20], spacing=10)
        disclaimer_title = Label(
            text='Important - Please Read',
            font_size='14sp', bold=True, color=WARNING,
            size_hint=(1, None), height=28, halign='center')
        disclaimer_title.bind(
            size=lambda s, v: setattr(s, 'text_size', v))
        disclaimer_text = Label(
            text=(
                'SkinSight is not a medical device.\n\n'
                'Results are for informational purposes only and '
                'cannot replace professional advice from a '
                'qualified dermatologist or doctor.\n\n'
                'Always consult a healthcare professional if you '
                'have concerns about your skin.'
            ),
            font_size='12sp', color=TEXT_DARK,
            size_hint=(1, None), height=170,
            halign='center', valign='top')
        disclaimer_text.bind(
            size=lambda s, v: setattr(s, 'text_size', v))
        disclaimer_card.add_widget(disclaimer_title)
        disclaimer_card.add_widget(disclaimer_text)
        how_card = Card(
            orientation='vertical',
            size_hint=(1, None), height=160,
            padding=[20, 16, 20, 16], spacing=6)
        how_title = Label(
            text='How SkinSight Works',
            font_size='13sp', bold=True, color=PRIMARY,
            size_hint=(1, None), height=24, halign='left')
        how_title.bind(size=lambda s, v: setattr(s, 'text_size', v))
        how_card.add_widget(how_title)
        for step in [
            'Take or select a photo of your skin',
            'AI analyses it on your device only',
            'You see results with a confidence score',
            'You decide what to do next. You are always in control'
        ]:
            lbl = Label(
                text=step, font_size='11sp', color=TEXT_DARK,
                size_hint=(1, None), height=22, halign='left')
            lbl.bind(size=lambda s, v: setattr(s, 'text_size', v))
            how_card.add_widget(lbl)
        btn = StyledButton(text='I understand, continue...')
        btn.bind(on_press=self.go_to_camera)
        footer = Label(
            text='SkinSight - GRAILS 2026 - Built Responsibly',
            font_size='10sp', color=TEXT_MUTED,
            size_hint=(1, None), height=20, halign='center')
        footer.bind(size=lambda s, v: setattr(s, 'text_size', v))
        outer.add_widget(logo)
        outer.add_widget(heading)
        outer.add_widget(tagline)
        outer.add_widget(privacy)
        outer.add_widget(disclaimer_card)
        outer.add_widget(how_card)
        outer.add_widget(btn)
        outer.add_widget(footer)
        scroll.add_widget(outer)
        self.add_widget(scroll)

    def _update_bg(self, *args):
        self._bg.pos = self.pos
        self._bg.size = self.size

    def go_to_camera(self, instance):
        self.manager.current = 'camera'


class CameraScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.selected_image = None
        with self.canvas.before:
            Color(*BG_COLOR)
            self._bg = Rectangle(pos=self.pos, size=self.size)
        self.bind(pos=self._update_bg, size=self._update_bg)
        scroll = ScrollView(size_hint=(1, 1))
        outer = BoxLayout(
            orientation='vertical',
            padding=[24, 32, 24, 24], spacing=14,
            size_hint_y=None)
        outer.bind(minimum_height=outer.setter('height'))
        top_bar = BoxLayout(
            orientation='horizontal',
            size_hint=(1, None), height=40, spacing=10)
        back_btn = Button(
            text='Back', font_size='12sp', color=PRIMARY,
            background_normal='', background_color=(0, 0, 0, 0),
            size_hint_x=None, width=70)
        back_btn.bind(on_press=lambda x: setattr(
            self.manager, 'current', 'disclaimer'))
        screen_title = Label(
            text='Skin Analysis', font_size='18sp', bold=True,
            color=TEXT_DARK, halign='center')
        screen_title.bind(
            size=lambda s, v: setattr(s, 'text_size', v))
        spacer = Widget(size_hint_x=None, width=70)
        top_bar.add_widget(back_btn)
        top_bar.add_widget(screen_title)
        top_bar.add_widget(spacer)
        privacy_reminder = PrivacyBadge()
        preview_card = Card(
            orientation='vertical',
            size_hint=(1, None), height=300,
            padding=[16, 16, 16, 16], spacing=8)
        self.preview = Image(
            source='', size_hint=(1, None), height=210,
            allow_stretch=True, keep_ratio=True)
        self.preview_label = Label(
            text='No photo selected yet',
            font_size='13sp', color=TEXT_MUTED,
            size_hint=(1, None), height=30, halign='center')
        self.preview_label.bind(
            size=lambda s, v: setattr(s, 'text_size', v))
        self.status = Label(
            text='Select a clear, well lit photo of the affected area',
            font_size='11sp', color=TEXT_MUTED,
            size_hint=(1, None), height=32, halign='center')
        self.status.bind(
            size=lambda s, v: setattr(s, 'text_size', v))
        preview_card.add_widget(self.preview)
        preview_card.add_widget(self.preview_label)
        preview_card.add_widget(self.status)
        tips_card = Card(
            orientation='vertical',
            size_hint=(1, None), height=130,
            padding=[16, 14, 16, 14], spacing=4)
        tips_title = Label(
            text='Tips for better results',
            font_size='12sp', bold=True, color=PRIMARY,
            size_hint=(1, None), height=22, halign='left')
        tips_title.bind(
            size=lambda s, v: setattr(s, 'text_size', v))
        tips_card.add_widget(tips_title)
        for tip in [
            'Use natural light where possible',
            'Keep the camera steady and in focus',
            'Fill the frame with the affected area'
        ]:
            lbl = Label(
                text=tip, font_size='11sp', color=TEXT_DARK,
                size_hint=(1, None), height=24, halign='left')
            lbl.bind(size=lambda s, v: setattr(s, 'text_size', v))
            tips_card.add_widget(lbl)
        btn_pick = StyledButton(text='Choose photo from gallery')
        btn_pick.bind(on_press=self.pick_image)
        self.btn_analyse = Button(
            text='Analyse skin condition',
            font_size='14sp', bold=True,
            size_hint=(1, None), height=52,
            background_normal='',
            background_color=(0.75, 0.80, 0.78, 1),
            color=(1, 1, 1, 0.6),
            disabled=True)
        self.btn_analyse.bind(on_press=self.analyse)
        consent_note = Label(
            text='By analysing, you confirm you have read the disclaimer.',
            font_size='10sp', color=TEXT_MUTED,
            size_hint=(1, None), height=20, halign='center')
        consent_note.bind(
            size=lambda s, v: setattr(s, 'text_size', v))
        footer = Label(
            text='SkinSight - GRAILS 2026 - Built responsibly',
            font_size='10sp', color=TEXT_MUTED,
            size_hint=(1, None), height=20, halign='center')
        footer.bind(size=lambda s, v: setattr(s, 'text_size', v))
        outer.add_widget(top_bar)
        outer.add_widget(privacy_reminder)
        outer.add_widget(preview_card)
        outer.add_widget(tips_card)
        outer.add_widget(btn_pick)
        outer.add_widget(self.btn_analyse)
        outer.add_widget(consent_note)
        outer.add_widget(footer)
        scroll.add_widget(outer)
        self.add_widget(scroll)

    def _update_bg(self, *args):
        self._bg.pos = self.pos
        self._bg.size = self.size

    def pick_image(self, instance):
        chooser = FileChooserIconView(
            filters=['*.jpg', '*.jpeg', '*.png'])
        popup = Popup(
            title='Select a skin condition photo',
            content=chooser, size_hint=(0.95, 0.90))
        chooser.bind(on_submit=lambda fc, sel, touch:
                     self.load_image(sel, popup))
        popup.open()

    def load_image(self, selection, popup):
        if selection:
            self.selected_image = selection[0]
            self.preview.source = self.selected_image
            self.preview.reload()
            self.preview_label.text = 'Photo selected'
            self.preview_label.color = SUCCESS
            self.status.text = 'Tap analyse when ready'
            self.btn_analyse.disabled = False
            self.btn_analyse.background_color = PRIMARY
            self.btn_analyse.color = (1, 1, 1, 1)
            popup.dismiss()

    def analyse(self, instance):
        if not self.selected_image:
            return
        self.status.text = 'Analysing...'
        try:
            import tensorflow as tf
            import numpy as np
            tflite = tf.lite
            interpreter = tflite.Interpreter(
                model_path='assets/model.tflite')
            interpreter.allocate_tensors()
            input_details = interpreter.get_input_details()
            output_details = interpreter.get_output_details()
            img = tf.keras.utils.load_img(
                self.selected_image, target_size=(224, 224))
            img_array = tf.keras.utils.img_to_array(img)
            img_array = np.expand_dims(img_array, axis=0)
            img_array = (img_array / 127.5) - 1
            interpreter.set_tensor(
                input_details[0]['index'], img_array)
            interpreter.invoke()
            output = interpreter.get_tensor(
                output_details[0]['index'])[0]
            top_index = int(np.argmax(output))
            confidence = float(output[top_index])
            print(f"Raw output: {output}")
            #print(f"Raw output: {output:.10f}")
            print(f"Top index: {top_index}, Confidence: {confidence}")
            class_names = [
                'Eczema',
                'Warts Molluscum and other Viral Infections',
                'Melanoma',
                'Atopic Dermatitis',
                'Basal Cell Carcinoma',
                'Melanocytic Nevi',
                'Benign Keratosis-like Lesions',
                'Psoriasis and Lichen Planus',
                'Seborrheic Keratoses and Benign Tumors',
                'Tinea Ringworm Candidiasis and Fungal Infections'
            ]
            top_condition = class_names[top_index] if top_index < len(class_names) else 'Unknown'
            sorted_indices = np.argsort(output)[::-1]
            others = []
            for i in sorted_indices[1:3]:
                if i < len(class_names):
                    others.append(
                        (class_names[i], float(output[i])))
            results_screen = self.manager.get_screen('results')
            results_screen.update_results(
                top_condition, confidence, others)
            self.manager.current = 'results'
        except Exception as e:
            self.status.text = f'Error: {str(e)}'


class ResultsScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas.before:
            Color(*BG_COLOR)
            self._bg = Rectangle(pos=self.pos, size=self.size)
        self.bind(pos=self._update_bg, size=self._update_bg)
        scroll = ScrollView(size_hint=(1, 1))
        outer = BoxLayout(
            orientation='vertical',
            padding=[24, 32, 24, 24], spacing=14,
            size_hint_y=None)
        outer.bind(minimum_height=outer.setter('height'))
        top_bar = BoxLayout(
            orientation='horizontal',
            size_hint=(1, None), height=40, spacing=10)
        back_btn = Button(
            text='Scan again', font_size='12sp', color=PRIMARY,
            background_normal='', background_color=(0, 0, 0, 0),
            size_hint_x=None, width=100)
        back_btn.bind(on_press=lambda x: setattr(
            self.manager, 'current', 'camera'))
        screen_title = Label(
            text='Results', font_size='18sp', bold=True,
            color=TEXT_DARK, halign='center')
        screen_title.bind(
            size=lambda s, v: setattr(s, 'text_size', v))
        spacer = Widget(size_hint_x=None, width=100)
        top_bar.add_widget(back_btn)
        top_bar.add_widget(screen_title)
        top_bar.add_widget(spacer)
        results_card = Card(
            orientation='vertical',
            size_hint=(1, None), height=240,
            padding=[20, 20, 20, 20], spacing=10)
        results_header = Label(
            text='Top result', font_size='11sp', color=TEXT_MUTED,
            size_hint=(1, None), height=18, halign='center')
        results_header.bind(
            size=lambda s, v: setattr(s, 'text_size', v))
        self.condition_name = Label(
            text='Awaiting analysis...',
            font_size='22sp', bold=True, color=PRIMARY,
            size_hint=(1, None), height=44, halign='center')
        self.condition_name.bind(
            size=lambda s, v: setattr(s, 'text_size', v))
        self.confidence_label = Label(
            text='', font_size='14sp', color=TEXT_DARK,
            size_hint=(1, None), height=26, halign='center')
        self.confidence_label.bind(
            size=lambda s, v: setattr(s, 'text_size', v))
        bar_outer = FloatLayout(size_hint=(1, None), height=18)
        with bar_outer.canvas:
            Color(0.90, 0.93, 0.92, 1)
            self._bar_bg = RoundedRectangle(
                pos=(0, 4), size=(100, 10), radius=[5])
            Color(*PRIMARY)
            self._bar_fill = RoundedRectangle(
                pos=(0, 4), size=(0, 10), radius=[5])
        bar_outer.bind(
            pos=self._update_bar, size=self._update_bar)
        self._bar_outer = bar_outer
        self._confidence_pct = 0
        other_header = Label(
            text='Other possibilities:',
            font_size='11sp', color=TEXT_MUTED,
            size_hint=(1, None), height=20, halign='left')
        other_header.bind(
            size=lambda s, v: setattr(s, 'text_size', v))
        self.other_results = Label(
            text='',
            font_size='12sp', color=TEXT_DARK,
            size_hint=(1, None), height=28, halign='center')
        self.other_results.bind(
            size=lambda s, v: setattr(s, 'text_size', v))
        results_card.add_widget(results_header)
        results_card.add_widget(self.condition_name)
        results_card.add_widget(self.confidence_label)
        results_card.add_widget(bar_outer)
        results_card.add_widget(other_header)
        results_card.add_widget(self.other_results)
        warning_box = BoxLayout(
            orientation='vertical',
            size_hint=(1, None), height=90,
            padding=[16, 12, 16, 12], spacing=4)
        with warning_box.canvas.before:
            Color(*WARNING_BG)
            self._warn_bg = RoundedRectangle(
                pos=warning_box.pos,
                size=warning_box.size, radius=[14])
        warning_box.bind(
            pos=lambda i, v: setattr(self._warn_bg, 'pos', v),
            size=lambda i, v: setattr(self._warn_bg, 'size', v))
        warn_title = Label(
            text='This is not a diagnosis',
            font_size='13sp', bold=True, color=WARNING,
            size_hint=(1, None), height=28, halign='center')
        warn_title.bind(
            size=lambda s, v: setattr(s, 'text_size', v))
        warn_body = Label(
            text=(
                'SkinSight is informational only. '
                'Please consult a qualified doctor for any concerns.'
            ),
            font_size='11sp', color=TEXT_DARK,
            size_hint=(1, None), height=44,
            halign='center', valign='top')
        warn_body.bind(
            size=lambda s, v: setattr(s, 'text_size', v))
        warning_box.add_widget(warn_title)
        warning_box.add_widget(warn_body)
        btn_scan = StyledButton(text='Scan another area')
        btn_scan.bind(on_press=lambda x: setattr(
            self.manager, 'current', 'camera'))
        footer = Label(
            text='SkinSight - GRAILS 2026 - Built responsibly',
            font_size='10sp', color=TEXT_MUTED,
            size_hint=(1, None), height=20, halign='center')
        footer.bind(size=lambda s, v: setattr(s, 'text_size', v))
        outer.add_widget(top_bar)
        outer.add_widget(results_card)
        outer.add_widget(warning_box)
        outer.add_widget(btn_scan)
        outer.add_widget(footer)
        scroll.add_widget(outer)
        self.add_widget(scroll)

    def _update_bg(self, *args):
        self._bg.pos = self.pos
        self._bg.size = self.size

    def _update_bar(self, *args):
        b = self._bar_outer
        pad = 24
        w = b.width - pad * 2
        self._bar_bg.pos = (b.x + pad, b.y + 4)
        self._bar_bg.size = (w, 10)
        self._bar_fill.pos = (b.x + pad, b.y + 4)
        self._bar_fill.size = (w * self._confidence_pct, 10)

    def update_results(self, condition, confidence, others):
        self.condition_name.text = condition
        pct = int(confidence * 100)
        self.confidence_label.text = f'Confidence: {pct}%'
        self._confidence_pct = confidence
        self._update_bar()
        if confidence < 0.6:
            self.confidence_label.color = WARNING
            self.confidence_label.text += ' - low confidence'
        else:
            self.confidence_label.color = TEXT_DARK
        other_text = '      '.join(
            [f'{n} - {int(p * 100)}%' for n, p in others])
        self.other_results.text = other_text


class SkinSightApp(App):
    def build(self):
        self.title = 'SkinSight'
        sm = ScreenManager()
        sm.add_widget(DisclaimerScreen(name='disclaimer'))
        sm.add_widget(CameraScreen(name='camera'))
        sm.add_widget(ResultsScreen(name='results'))
        return sm


if __name__ == '__main__':
    SkinSightApp().run()