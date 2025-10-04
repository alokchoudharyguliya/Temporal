from temporalio import workflow
from datetime import timedelta

with workflow.unsafe.imports_passed_through():
    from temporalcode.activities import send_email

@workflow.defn
class WelcomeWorkflow:
    @workflow.run
    async def run(self, user_email: str) -> str:
        # Wait 30 seconds (simulate reminder delay)
        await workflow.sleep(timedelta(seconds=30))
        result = await workflow.execute_activity(
            send_email,
            user_email,
            schedule_to_close_timeout=timedelta(seconds=10),
            retry_policy={"maximum_attempts": 5},
        )
        return result
