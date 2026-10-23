import openai, os
from dotenv import load_dotenv
load_dotenv()

client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# 1. Upload your JSONL (generated from your LOYS JSON)
print("Uploading loys_train.jsonl...")
file = client.files.create(
    file=open("loys_train.jsonl", "rb"),
    purpose="fine-tune"
)
print(f"File ID: {file.id}")

# 2. Start fine-tuning - gpt-4o-mini is cheapest & best for Bisaya bot
print("Starting fine-tune...")
job = client.fine_tuning.jobs.create(
    training_file=file.id,
    model="gpt-4o-mini-2024-07-18",
    suffix="loys-bisaya-bot"
)
print(f"Job ID: {job.id}")
print(f"Track at: https://platform.openai.com/finetune/{job.id}")