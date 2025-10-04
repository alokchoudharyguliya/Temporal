from temporalio import workflow
from temporalio.common import RetryPolicy
from datetime import timedelta

# Import inside workflow for safety
with workflow.unsafe.imports_passed_through():
    from activities import send_email

@workflow.defn
class ReminderWorkflow:
    @workflow.run
    async def run(self, user: str) -> str:
        # Step 1: Wait for 3 days
        await workflow.sleep(timedelta(minutes=1))

        # Step 2: Send email (Temporal handles retries if it fails)
        result = await workflow.execute_activity(
            send_email,
            user,
            schedule_to_close_timeout=timedelta(seconds=10),
            retry_policy=RetryPolicy(maximum_attempts=5),  # Use RetryPolicy objectauto-retry
        )
        return result
