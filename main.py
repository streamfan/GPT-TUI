from __future__ import annotations

import openai
import os
import asyncio
from asgiref.sync import sync_to_async

from rich.markdown import Markdown

from textual.app import App, ComposeResult
from textual.containers import Container, Vertical
from textual.widgets import Static, Input, Button

from rich.spinner import Spinner

# import logging
from textual import log

# get the API key from the .env file
from dotenv import load_dotenv

# see .env.example for more info
load_dotenv()
openai.api_key = os.getenv("API_KEY")


class Examples(Static):
    pass


class Capabilities(Static):
    pass


class Limitations(Static):
    pass

class PreviousChatButton(Button):

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Called when the button is pressed."""
        self.query_one(f"prompt_{str(event.button.id).replace('chat_button_', '')}").focus()


class NewChatButton(Static):
    pass


class PreviousPrompt(Static):
    pass


class Prompt(Static):
    pass


class PromptResponse(Static):

    response = ""

    def __init__(self):
        super().__init__("")
        self._spinner = Spinner("material")

    def on_mount(self) -> None:
        """Called when app starts."""
        self.update_render = self.set_interval(1 / 60, self.update_spinner)

    def update_spinner(self) -> None:
        """Updates the spinner."""
        if self.response == "":
            self.update(self._spinner)

    async def send_prompt(self, input_prompt: str):
        """Sends a prompt to openai's api."""
        model_engine = "text-davinci-003"
        completion = await sync_to_async(openai.Completion.create)(
            engine=model_engine,
            prompt=input_prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5,
        )
        log(f"completion: {completion} {type(completion)}")

        result = completion.choices[0].text
        self.response = result

        # animate typing the response
        for i in range(len(result)):
            self.update(Markdown(result[:i]))
            await asyncio.sleep(0.01)

        self.update(Markdown(result))


class ChatGPTui(App):
    """Sends a prompt to openai's api and displays the response."""

    CSS_PATH = "chat.css"

    number_of_prompts: int = 0

    def compose(self) -> ComposeResult:
        yield Input(placeholder="Enter a prompt...")
        yield Vertical(
             id="previous_chats"
        )
        yield Container(
            Vertical(
                id="prompts_and_responses"
            ), 
            id="prompts_and_responses_container"
        )

    def on_mount(self) -> None:
        """Called when app starts."""
        # Give the input focus, so we can start typing straight away
        self.query_one(Input).focus()

    async def on_input_submitted(self, message: Input.Submitted) -> None:
        """A coroutine to handle a text changed message."""
        if message == "":
            return
        await self.action_add_prompt(message.value)
        await self.action_add_response(message.value)

    async def action_add_prompt(self, input_prompt: str) -> None:
        """adds a prompt to the prompt list"""
        prompt = Prompt(input_prompt, expand=True, id=f"prompt_{self.number_of_prompts}")
        self.query_one("#prompts_and_responses").mount(prompt)
        self.call_after_refresh(self.screen.scroll_end, animate=False)
        self.number_of_prompts += 1

        # update the previous prompts
        await self.query_one("#previous_chats").mount(PreviousChatButton(input_prompt, id=f"chat_button_{self.number_of_prompts}"))

        # get the number of characters in the prompt
        prompt_length = len(input_prompt)

        for i in range(prompt_length):
            # delete the last character in the prompt
            self.query_one(Input).action_delete_left()

    async def action_add_response(self, input_response: str) -> None:
        """adds a response to the response list"""
        response = PromptResponse()
        self.query_one("#prompts_and_responses").mount(response)
        response.focus()
        await response.send_prompt(input_response)


if __name__ == "__main__":
    app = ChatGPTui()
    app.run()
