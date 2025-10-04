import asyncio
from temporalio.client import Client
from temporalio.worker import Worker
from workflow import ReminderWorkflow
from activities import send_email

async def main():
    # Connect to Temporal server
    client = await Client.connect("localhost:7233")

    # Create a worker
    worker = Worker(
        client,
        task_queue="reminder-task-queue",
        workflows=[ReminderWorkflow],
        activities=[send_email],
    )

    print("🚀 Worker started, listening on 'reminder-task-queue'")
    await worker.run()

if __name__ == "__main__":
    asyncio.run(main())
