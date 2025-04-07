📧 AI-Powered Personalized Email Sender
This project automates the process of sending personalized business development emails to a list of companies using LLM-generated content (via Groq API with LLaMA3) and a contact dataset. It customizes emails based on each company's sector, state, profile, and contact person, and sends them via Gmail SMTP.

🚀 Features
💬 AI-generated personalized emails using LLaMA3 via Groq API

📊 Reads and filters company data based on sector and state

📧 Sends emails via Gmail SMTP with proper formatting

🔐 Secure credentials handling via .env file

✅ Console logging for success/failure of each email

🗂️ Project Structure
bash
Copy
Edit
📁 email_sender/
├── main.py                     # Main script for generating & sending emails
├── companies_data.csv          # Input data with company info
├── email_template_prompt.txt   # Prompt template for Groq API
├── .env                        # Contains sensitive environment variables
└── README.md                   # Project documentation
📥 Prerequisites
Python 3.8+

A Gmail account (with App Password if 2FA is enabled)

Groq API key

🧪 Installation
Clone the repository

bash
Copy
Edit
git clone https://github.com/yourusername/email-sender-groq.git
cd email-sender-groq
Install dependencies

bash
Copy
Edit
pip install -r requirements.txt
Set up .env file

env
Copy
Edit
GROQ_API_KEY=your_groq_api_key_here
Update your CSV Make sure your companies_data.csv contains at least these columns:

Name of the Exhibitor

Contact Person

Email

Sector

Profile

State

🧠 Prompt Template
Customize email_template_prompt.txt with placeholders like:

css
Copy
Edit
Write a professional business email to {contact_person} from {company_name}, working in the {sector} sector based in {state}. Use this description: {profile}.
🧾 How to Run
bash
Copy
Edit
python main.py
You’ll be prompted to enter your email and password securely in the terminal. Emails will be sent automatically after generating customized content using the LLM.

💡 Tips to Avoid Spam
Use a custom domain email instead of Gmail (recommended).

Warm up your email domain if new.

Add unsubscribe option in your message.

Avoid sending too many emails in a short time — add delays.

📬 Example Output
less
Copy
Edit
📝 Email Preview for Mr. Agarwal (contact@4dautomotive.com):
Dear Mr. Agarwal,
...
✅ Email sent to Mr. Agarwal (contact@4dautomotive.com)
🛡️ Security Note
Do not hardcode your passwords or API keys. Use .env and dotenv for security.

🤝 Contributions
Pull requests and suggestions are welcome! If you find a bug or want a feature added, feel free to open an issue.
