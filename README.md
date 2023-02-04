# GPT-TUI
A TUI to interact with ChatGPT

# Authentication

The OpenAI API uses API keys for authentication. Visit your [API Keys page](https://platform.openai.com/account/api-keys) to retrieve the API key you'll use in your requests.

*Remember that your API key is a secret! Do not share it with others or expose it in any client-side code (browsers, apps).*

Production requests must be routed through your own backend server where your API key can be securely loaded from an environment variable or key management service.

All API requests should include your API key in an `Authorization` HTTP header as follows:
```
Authorization: Bearer YOUR_API_KEY
```

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

You will need the following dependencies

## Textual

You can install textual using [poetry]() or by doing:
```BASH
pip install "textual[dev]"
```

### Poetry

You'll need [poetry]()

```BASH
curl -sSL https://install.python-poetry.org | python3 -
```

### Docker

See docs on how to install docker:
https://docs.docker.com/get-docker/