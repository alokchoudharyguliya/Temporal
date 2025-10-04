import asyncio
from temporalio.client import Client
from workflow import ReminderWorkflow

async def main():
    client = await Client.connect("localhost:7233")

    # Start workflow
    result = await client.execute_workflow(
        ReminderWorkflow.run,
        "user@example.com",
        id="reminder-workflow-1",
        task_queue="reminder-task-queue",
    )

    print("Workflow result:", result)

if __name__ == "__main__":
    asyncio.run(main())
