# GPT-TUI
A TUI to interact with ChatGPT!

This is a reactive application that runs entirely in your terminal.
It will adjust to the window size dynamically as well as font size.

It uses [Textual](https://www.textualize.io/) and [Rich](https://github.com/Textualize/rich) for formatting outputs.


# Authentication

The OpenAI API uses API keys for authentication. Visit your [API Keys page](https://platform.openai.com/account/api-keys) to retrieve the API key you'll use in your requests.

*Remember that your API key is a secret! Do not share it with others or expose it in any client-side code (browsers, apps).*

Production requests must be routed through your own backend server where your API key can be securely loaded from an environment variable or key management service.

All API requests should include your API key in an `Authorization` HTTP header as follows:
```
Authorization: Bearer YOUR_API_KEY
```

From here you'll need to place your auth token into the `.env` file.

If you're unsure about the formatting you can do:
```BASH
cp .env.example .env
```

And then just replace with your key.

# Development

Git HTTPS Clone:
```BASH
git clone https://github.com/streamfan/GPT-TUI.git
```

Git SSH Clone:
```BASH
git clone git@github.com:streamfan/GPT-TUI.git
```

Github CLI Clone:
```BASH
gh repo clone streamfan/GPT-TUI
```

## Dependencies

You can get away with just running `poetry shell` and `poetry install`.

From there you can simply run:
```BASH
python main.py
```

Or if you prefer using the `textual` CLI you can do:
```BASH
textual run main.py
```

### Poetry

You'll need [poetry](https://python-poetry.org/docs/)

```BASH
curl -sSL https://install.python-poetry.org | python3 -
```

Once installed you can then create a virtual environment and connect to the shell by doing:
```BASH
poetry shell
```

And then install the dependencies by running:
```BASH
poetry install
```

### Docker

This TUI can be ran entirely in-container interactively, as well as over SSH.

See docs on how to install docker:
https://docs.docker.com/get-docker/



### Textual

You can install textual using [poetry](https://python-poetry.org/docs/) or by doing:
```BASH
pip install "textual[dev]"
```
