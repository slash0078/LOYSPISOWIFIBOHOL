# Use your new LOYS model
response = client.chat.completions.create(
    model="ft:gpt-4o-mini-2024-07-18:personal:loys-bisaya-bot:XXXX", # from dashboard
    messages=[
        {"role": "user", "content": "Plan799 unsa na?"}
    ]
)
print(response.choices[0].message.content)
# → BEST SELLER! Plan799 - 60Mbps - P799/month! Pang pamilya...