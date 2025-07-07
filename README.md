# ChatOllama Utilities

This repository contains two Python scripts that demonstrate how to use the `langchain_ollama` package and the Ollama CLI to:

1. Run an interactive chatbot (`chatbot.py`).
2. Start the Ollama server and obtain approximate nutrient breakdowns for user-provided meals (`nutrient_analyzer.py`).

---

## Table of Contents

- [Features](#features)  
- [Prerequisites](#prerequisites)  
- [Installation](#installation)  
- [Usage](#usage)  
  - [Interactive Chatbot](#interactive-chatbot)  
  - [Nutrient Analyzer](#nutrient-analyzer)  
- [Project Structure](#project-structure)  
- [Customization](#customization)  
- [Troubleshooting](#troubleshooting)  

---

## Features

- **chatbot.py**  
  - Launches an interactive command-line chatbot powered by a local Ollama LLaMA model (`llama3.2:1b`).
  - Streams responses chunk by chunk to simulate real-time typing.

- **nutrient_analyzer.py**  
  - Starts the Ollama server in a subprocess (`ollama serve`).
  - Prompts the user to enter meal items and returns an estimated breakdown of Protein, Fat, and Carbohydrates as percentages of recommended daily intake.
  - Gracefully terminates the Ollama server when done.

---

## Prerequisites

1. **Python 3.8+**  
2. **Ollama CLI** installed and authenticated locally  
   Installation instructions:  
   ```bash
   # macOS (Homebrew)
   brew install ollama

   # Linux (via apt, yum, or from source)
   # see: https://ollama.com/docs/installation
   ```
3. A local Ollama model named `llama3.2:1b` (or adjust the model name in the scripts).  
   To pull a model:
   ```bash
   ollama pull llama3.2:1b
   ```

---

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/passimon/chatollama-utilities.git
   cd chatollama-utilities
   ```
2. (Optional) Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
3. Install Python dependencies:
   ```bash
   pip install langchain-ollama
   ```

---

## Usage

### Interactive Chatbot

1. Ensure the Ollama server is running (either manually or via the nutrient analyzer script):
   ```bash
   ollama serve
   ```
2. Run the chatbot script:
   ```bash
   python chatbot.py
   ```
3. Chat with the model. Type `quit` to exit.

Example session:
```
Welcome to the chatbot! Type 'quit' to exit.
You: Hello, how are you?
Bot: I am doing well, thank you! How can I assist you today?
You: quit
```

### Nutrient Analyzer

This script will launch the Ollama server in the background, ask for your meal, print nutrient estimates, and then shut down the server.

1. Run the nutrient analyzer script:
   ```bash
   python nutrient_analyzer.py
   ```
2. Enter your meal when prompted:
   ```
   Enter your meal: 2 eggs, 1 avocado, 1 slice of whole-grain toast
   ```
3. View the output:
   ```
   Protein: 25g
   Fat: 30g
   Carbohydrates: 20g
   Ollama server terminated.
   ```

---

## Project Structure

```
.
├── chatbot.py            # Interactive command-line chatbot
├── nutrient_analyzer.py # Starts Ollama serve + nutrient breakdown
└── README.md            # This file
```

---

## Customization

- **Changing the Model**  
  Edit the `model` parameter in `ChatOllama(...)` calls to use any Ollama-compatible model.

- **Adjusting Temperature / Tokens**  
  Tweak `temperature`, `num_predict`, or other LLM parameters in each script to control randomness and response length.

- **Prompt Engineering**  
  In `nutrient_analyzer.py`, modify the human message template to adjust style, format, or the nutrients you want reported.

---

## Troubleshooting

- **Ollama Server Won’t Start**  
  - Confirm `ollama` is in your `PATH` and you can run `ollama serve` manually.
  - Check for firewall/port conflicts on `localhost:11434` (default).

- **Model Not Found Error**  
  ```bash
  ollama list    # verify the model name
  ollama pull llama3.2:1b
  ```
- **Stream Hangs or Fails**  
  - Ensure your local Ollama server version matches the `langchain_ollama` client expectations.
  - Try increasing the `time.sleep` delay in `start_ollama_serve()`.

---

Enjoy building with Ollama and LangChain! If you encounter any issues or have feature requests, feel free to open an issue or submit a pull request.
