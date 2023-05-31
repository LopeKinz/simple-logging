import requests
import json

# Define colors for different log levels
COLORS = {
    'ERROR': '\033[91m',
    'WARNING': '\033[93m',
    'INFO': '\033[94m',
    'PASSED': '\033[92m',
    'RESET': '\033[0m'
}


def log_with_color(message, level):
    color = COLORS.get(level, COLORS['RESET'])
    log_message = f"{color}{message}{COLORS['RESET']}"
    print(log_message)


def log_error(message):
    log_with_color(f"[ERROR] {message}", 'ERROR')


def log_warning(message):
    log_with_color(f"[WARNING] {message}", 'WARNING')


def log_info(message):
    log_with_color(f"[INFO] {message}", 'INFO')


def log_passed(message):
    log_with_color(f"[PASSED] {message}", 'PASSED')


def send_discord_webhook(webhook_url, message):
    payload = {'content': message}
    response = requests.post(webhook_url, data=json.dumps(payload), headers={'Content-Type': 'application/json'})
    if response.status_code == 204:
        log_info("Discord webhook sent successfully.")
    else:
        log_error(f"Failed to send Discord webhook. Status Code: {response.status_code}")


# Example usage
if __name__ == "__main__":
    log_info("This is an informational message.")
    log_warning("This is a warning message.")
    log_error("This is an error message.")
    log_passed("This is a passed message.")

    discord_webhook_url = "https://discord.com/api/webhooks/YOUR_WEBHOOK_URL"
    send_discord_webhook(discord_webhook_url, "This is a message sent to Discord webhook.")
