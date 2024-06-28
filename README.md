# Passport Extractor

This project extracts information from passport images using the PassportEye library.

## Setup

1. Create a virtual environment:
    ```sh
    python -m venv venv
    ```

2. Activate the virtual environment:
    - On Windows:
        ```sh
        venv\Scripts\activate
        ```
    - On macOS/Linux:
        ```sh
        source venv/bin/activate
        ```

3. Install dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Place the passport images in the `images/` directory.
2. Update the path to the passport image in `src/main.py`.
3. Run the program:
    ```sh
    python src/main.py
    ```

## Testing

To run the tests:
```sh
pytest tests/
