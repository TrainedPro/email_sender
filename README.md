# Email Sender Script

This Python script allows you to send emails with optional attachments. You can configure it to use default values or override them with command-line arguments.

## Prerequisites

1. **Python 3.x**: Ensure Python 3 is installed on your system.

2. **Dependencies**: The script requires the following Python packages:
   - `yagmail`
   - `python-dotenv`
   
   You can install these packages using pip:

   ```sh
   pip install -r requirements.txt
   ```

## Setup

1. **Create and Configure the `.env` File**:

   Create a `.env` file in the same directory as the script and add the following environment variables:

   ```env
   SENDER_EMAIL=your_sender_email@example.com
   SENDER_PASSWORD=your_password_or_app_specific_password
   ```

   Replace `your_sender_email@example.com` and `your_password_or_app_specific_password` with your actual email credentials.

2. **Script Defaults**:

   You can edit the default values directly in the script if needed. Locate the following section in the script and update the values:

   ```python
   # Default values (can be edited directly in the script)
   DEFAULT_RECIPIENT_EMAIL = ""
   DEFAULT_SUBJECT = ""
   DEFAULT_BODY = ""
   DEFAULT_ATTACHMENT_PATH = ""  # Leave empty if no attachment
   ```

## Usage

You can run the script with or without command-line arguments. 

### Running with Command-Line Arguments

Use the following command to provide recipient email, subject, body, and attachment path:

```sh
python3 send_certificate.py -r recipient@example.com -s "Subject" -b "Body text" -a /path/to/attachment
```

**Arguments**:
- `-r, --recipient`: The recipient's email address (required).
- `-s, --subject`: The subject of the email (optional).
- `-b, --body`: The body of the email (optional).
- `-a, --attachment`: Path to the attachment file (optional).

### Running without Command-Line Arguments

Simply run the script without arguments to use the default values:

```sh
python3 send_certificate.py
```

The script will use the default values specified in the script.

## Error Handling

- Ensure that `SENDER_EMAIL` and `SENDER_PASSWORD` are correctly set in the `.env` file.
- Validate the recipient email address format to avoid errors.
- Check the log output for detailed error messages if the email fails to send.

## Troubleshooting

- **Missing Environment Variables**: Ensure that the `.env` file is correctly placed and the environment variables are set.
- **Invalid Email Address**: Verify that the recipient email address is correctly formatted.
- **Dependencies**: Ensure all required Python packages are installed.

## License

This script is provided "as-is" without any warranties. You may use and modify it according to your needs.