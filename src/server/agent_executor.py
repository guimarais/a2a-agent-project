"""
A
"""

from a2a.server.agent_execution import AgentExecutor, RequestContext
from a2a.server.events import EventQueue
from a2a.utils import new_agent_text_message
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

def good_title():
    """
    Creates a fake book title
    """

    client = OpenAI()

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a creative book editor"},
            {"role": "user", "content": "Create an original book title involving ghosts."}
        ],
        temperature=0.8,
        max_tokens=150
    )

    client.close()

    return response.choices[0].message.content


class HelloWorldAgent:
    """Hello World Agent."""

    async def invoke(self) -> str:

        response = good_title()
        print("===================================")
        print(response)

        return response


class HelloWorldAgentExecutor(AgentExecutor):
    """Test AgentProxy Implementation."""

    def __init__(self):
        self.agent = HelloWorldAgent()

    async def execute(
        self,
        context: RequestContext,
        event_queue: EventQueue,
    ) -> None:
        result = await self.agent.invoke()
        await event_queue.enqueue_event(new_agent_text_message(result))

    async def cancel(self, context: RequestContext, event_queue: EventQueue) -> None:
        raise Exception("cancel not supported")
