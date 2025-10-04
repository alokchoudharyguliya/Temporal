import asyncio
from temporalio.client import Client
from temporalio.worker import Worker
from temporal_code.workflows import WelcomeWorkflow
from temporal_code.activities import send_email

async def main():
    client = await Client.connect("localhost:7233")
    worker = Worker(
        client,
        task_queue="welcome-task-queue",
        workflows=[WelcomeWorkflow],
        activities=[send_email],
    )
    print("🚀 Worker started on 'welcome-task-queue'")
    await worker.run()

if __name__ == "__main__":
    asyncio.run(main())
