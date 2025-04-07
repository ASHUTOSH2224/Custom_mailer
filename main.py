import os
import pandas as pd
import smtplib
from dotenv import load_dotenv
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from langchain_groq import ChatGroq
from langchain.schema import HumanMessage, SystemMessage

# Load environment variables
load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")

# Load email template
with open("email_template_prompt.txt", "r") as f:
    template = f.read()

# Load dataset
df = pd.read_csv("companies_data.csv").dropna(subset=["Email", "Profile", "Sector", "State"])

# Ask for optional filters
selected_sector = input("Enter Sector to filter (press Enter to include all): ").strip().lower()
selected_state = input("Enter State to filter (press Enter to include all): ").strip().lower()

# Apply filters if provided
if selected_sector:
    df = df[df["Sector"].str.lower() == selected_sector]
if selected_state:
    df = df[df["State"].str.lower() == selected_state]

if df.empty:
    print("❌ No matching records found with the given filters.")
    exit()

# Initialize Groq Chat model
chat = ChatGroq(api_key=groq_api_key, model_name="llama3-70b-8192")

# Email sending function
def send_email(to_email, contact_person, generated_message, sender_email, sender_password):
    try:
        smtp_server = "smtp.gmail.com"
        smtp_port = 587
        subject = "Let's Collaborate!"

        msg = MIMEMultipart()
        msg["From"] = sender_email
        msg["To"] = to_email
        msg["Subject"] = subject
        msg.attach(MIMEText(generated_message, 'plain'))

        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, to_email, msg.as_string())
        server.quit()

        print(f"✅ Email sent to {contact_person} ({to_email})")
    except Exception as e:
        print(f"❌ Failed to send email to {contact_person} ({to_email}):", str(e))

# Generate personalized email using Groq
def generate_email(row):
    prompt = template.format(
        company_name=row["Name of the Exhibitor"],
        contact_person=row["Contact Person"],
        sector=row["Sector"],
        profile=row["Profile"]
    )

    messages = [
        SystemMessage(content="You are an expert email writer for business communication."),
        HumanMessage(content=prompt)
    ]

    response = chat(messages)
    email_text = response.content.strip()

    # Remove generic intro line if present
    lines = email_text.splitlines()
    if lines and "business development email" in lines[0].lower():
        email_text = "\n".join(lines[1:]).strip()

    return email_text

# Ask for sender credentials
sender_email = input("Enter your email address: ").strip()
sender_password = input("Enter your email password (App password if using Gmail 2FA): ").strip()

# Group by Sector and State
grouped = df.groupby(["Sector", "State"])

# Loop through each group
for (sector, state), group_data in grouped:
    print(f"\n📂 Processing Sector: {sector} | State: {state} | Companies: {len(group_data)}")

    for _, row in group_data.iterrows():
        to_email = row["Email"]
        contact_person = row["Contact Person"]
        generated_msg = generate_email(row)

        print(f"\n📝 Email Preview for {contact_person} ({to_email}):\n{generated_msg}\n")
        send_email(to_email, contact_person, generated_msg, sender_email, sender_password)
