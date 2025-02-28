# Text Generation Interactive Assistant

This repository contains a simple interactive text generation assistant built using open-source models. The default model is the GPT-2 model, which is free and requires no paid tokens.

## Features

- Interactive prompt-based text generation.
- Easy to set up and extend.
- Easily switch to other open-source models available on Hugging Face (e.g. GPT-J, BLOOM, etc.) or others (e.g. DeepSeek) by updating the MODEL_NAME variable in main.py

## Setup and Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Jide-Muritala/text-generation-assistant.git
   cd text-generation-assistant

2. **Create and activate a virtual environment (optional but recommended):**

   ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. **Install dependencies:**

   ```bash
    pip install -r requirements.txt

4. **Run the assistant:**

   ```bash
    python main.py

5. **Note:**

   Make sure you have the necessary hardware or adjust settings (like max_length) based on your machine’s resources.

6. **Docker:**

   This repository is Docker-ready. You can build and run the text generation interactive assistant in a container without installing dependencies directly on your host machine.

    - Dockerfile: Contains instructions for building the Docker image.
    - .dockerignore: Lists files and directories to be excluded from the Docker build context.
    - docker-compose.yml: Simplifies running the container with Docker Compose.

    To build the Docker image, run:

    ```bash
    docker build -t text-generation-assistant .

    Once the image is built, you can run the container interactively using::

    ```bash
    docker run -it --rm text-generation-assistant

    Alternatively, if you are using Docker Compose, start the container with::

    ```bash
    docker-compose up

    This command will build the image (if it hasn't been built yet) and run the container. The --rm flag in the docker run command ensures the container is removed after you exit the interactive session.


