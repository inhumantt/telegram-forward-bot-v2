# telegram-forward-bot-v2

A Python script using Pyrogram to automatically forward files from specified source chats to designated destination chats on Telegram.

## Features

- Forward files from multiple source chats to specific destination chats.
- Separate handling for ULP (User Log Processing) files and logs.
- Handles files with proper logging and error handling.

## Prerequisites

- Python 3.7 or higher
- Pyrogram library
- tgcrypto library (optional but recommended for performance)

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/your-repo.git
   cd your-repo

## Install Dependencies:

```bash
pip install -r requirements.txt

## Create a requirements.txt file with the following content:

pyrogram

tgcrypto

## Configuration

Open main.py and replace the placeholders with your actual API credentials and chat IDs.

api_id = "your_api_id"
api_hash = "your_api_hash"
phone_number = "your_phone_number"

ulp_destination_chat = your_ulp_destination_chat_id
logs_destination_chat = your_logs_destination_chat_id

ulp_file_chats = [your_ulp_chat_ids]
logs_file_chats = [your_logs_chat_ids]

## Session Management:

Ensure you have a fresh session by running the script for the first time. Pyrogram will create a new session file.

## Usage

Run the Script:

```bash
python main.py

## Authentication:

On the first run, Pyrogram will prompt you to authenticate. Follow the instructions to log in.

## Troubleshooting
### PersistentTimestampInvalid Error:

If you encounter the PersistentTimestampInvalid error, try updating Pyrogram and deleting the session file before running the script again.

### Session File Issues:

Ensure you are using a unique session name if issues persist.

## Contributing
Feel free to open issues or submit pull requests if you find bugs or have improvements.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Contact
For questions or support, you can reach out to me via email or open an issue on the GitHub repository.

### Notes:

1. **Replace Placeholder Values:** Make sure to replace placeholders like `your_api_id`, `your_api_hash`, `your_phone_number`, etc., with your actual values.
2. **Add Your GitHub Repository Link:** Replace `https://github.com/yourusername/your-repo.git` with the actual URL of your GitHub repository.
3. **License:** Update or add a `LICENSE` file if you're using a specific license for your project.

This `README.md` provides a clear guide for users to set up, configure, and run your script, along with troubleshooting tips.


