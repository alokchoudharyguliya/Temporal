from temporalio import activity
import random

@activity.defn
async def send_email(user_email: str) -> str:
    # Simulate sending email (50% failure for demo)
    if random.choice([True, False]):
        raise Exception("❌ Email system is down!")
    return f"✅ Email sent successfully to {user_email}"
