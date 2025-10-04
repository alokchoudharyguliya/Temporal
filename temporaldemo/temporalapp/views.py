from django.http import JsonResponse
import asyncio
from temporalio.client import Client
from temporalcode.workflow import WelcomeWorkflow

async def start_welcome_workflow(user_email: str):
    client = await Client.connect("localhost:7233")
    result = await client.execute_workflow(
        WelcomeWorkflow.run,
        user_email,
        id=f"welcome-{user_email}",
        task_queue="welcome-task-queue",
    )
    return result

def signup(request):
    user_email = request.GET.get("email", "demo@example.com")
    # For demo: run Temporal call synchronously
    result = asyncio.run(start_welcome_workflow(user_email))
    return JsonResponse({"workflow_started_for": user_email, "result": result})
