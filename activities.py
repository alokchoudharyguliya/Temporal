from temporalio import activity
import random, time,asyncio

@activity.defn
async def send_email(user: str) -> str:
    # Simulate flaky email system
    if random.choice([True, False]):
        raise Exception("Email system is down!")
    await asyncio.sleep(1)
    return f"✅ Email sent successfully to {user}"
