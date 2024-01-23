import gradio as gr
from ktem.app import BaseApp
from ktem.pages.chat import ChatPage
from ktem.pages.help import HelpPage
from ktem.pages.settings import SettingsPage


class App(BaseApp):
    """The main app of Kotaemon

    The main application contains app-level information:
        - setting state
        - user id

    App life-cycle:
        - Render
        - Declare public events
        - Subscribe public events
        - Register events
    """

    def ui(self):
        """Render the UI"""
        with gr.Tab("Chat", elem_id="chat-tab"):
            self.chat_page = ChatPage(self)

        with gr.Tab("Settings", elem_id="settings-tab"):
            self.settings_page = SettingsPage(self)

        with gr.Tab("Help", elem_id="help-tab"):
            self.help_page = HelpPage(self)