# Simple Logger
Custom Logger is a Python module that provides logging functionality with colored output and a function for sending log messages to a Discord webhook.
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)
## Installation

1. Clone the repository:

   ```shell
   git clone https://github.com/lopekinz/simple-logging
   ```

2. Navigate to the project directory:

   ```shell
   cd simple-logging
   ```

3. Install the required dependencies:

   ```shell
   pip install -r requirements.txt
   ```

## Usage

1. Import the module in your Python script:

   ```python
   from simple-logging import log_error, log_warning, log_info, log_passed, send_discord_webhook
   ```

2. Use the logging functions to display colored output:

   ```python
   log_info("This is an informational message.")
   log_warning("This is a warning message.")
   log_error("This is an error message.")
   log_passed("This is a passed message.")
   ```

3. Use the `send_discord_webhook()` function to send log messages to a Discord webhook:

   ```python
   discord_webhook_url = "https://discord.com/api/webhooks/YOUR_WEBHOOK_URL"
   send_discord_webhook(discord_webhook_url, "This is a message sent to Discord webhook.")
   ```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any changes or improvements you would like to make.

## Acknowledgements

This module uses the following third-party libraries:

- [requests](https://pypi.org/project/requests/): For sending HTTP requests.
- [colorama](https://pypi.org/project/colorama/): For terminal color output.

## Contact

If you have any questions, suggestions, or feedback, please feel free to contact me.

