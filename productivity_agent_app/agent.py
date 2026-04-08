from google.adk.agents import Agent, SequentialAgent
from toolbox_core import ToolboxSyncClient

toolbox = ToolboxSyncClient("http://127.0.0.1:5000")

task_agent = Agent(name="task_agent", model="gemini-2.5-flash", description="Creates lists and completes tasks in BigQuery.", instruction="You manage the user task list. LIST tasks: use get_pending_tasks with user_id=user001. CREATE task: use create_task tool. COMPLETE task: use complete_task tool.", tools=toolbox.load_toolset("task_toolset"), output_key="task_result")

schedule_agent = Agent(name="schedule_agent", model="gemini-2.5-flash", description="Retrieves and creates calendar events in BigQuery.", instruction="You manage the user schedule. GET schedule: use get_todays_schedule with user_id=user001. CREATE event: use create_schedule_event tool.", tools=toolbox.load_toolset("schedule_toolset"), output_key="schedule_result")

notes_agent = Agent(name="notes_agent", model="gemini-2.5-flash", description="Searches and creates notes in BigQuery.", instruction="You manage user notes. SEARCH: use search_notes with user_id=user001 and keyword. CREATE: use create_note tool.", tools=toolbox.load_toolset("notes_toolset"), output_key="notes_result")

wf_schedule = Agent(name="wf_schedule", model="gemini-2.5-flash", description="Workflow step fetches schedule.", instruction="Fetch schedule for user_id=user001 using get_todays_schedule.", tools=toolbox.load_toolset("schedule_toolset"), output_key="schedule_result")

wf_tasks = Agent(name="wf_tasks", model="gemini-2.5-flash", description="Workflow step fetches pending tasks.", instruction="Fetch pending tasks for user_id=user001 using get_pending_tasks.", tools=toolbox.load_toolset("task_toolset"), output_key="task_result")

wf_notes = Agent(name="wf_notes", model="gemini-2.5-flash", description="Workflow step searches notes.", instruction="Search notes for user_id=user001 with keyword=today using search_notes.", tools=toolbox.load_toolset("notes_toolset"), output_key="notes_result")

summary_agent = Agent(name="summary_agent", model="gemini-2.5-flash", description="Synthesizes all data into a final daily brief.", instruction="Create a brief using schedule_result, task_result, notes_result from session. Use bullets. End with top 3 priorities.", output_key="final_brief")

workflow_team = SequentialAgent(name="workflow_team", description="Daily briefing workflow.", sub_agents=[wf_schedule, wf_tasks, wf_notes, summary_agent])

root_agent = Agent(name="productivity_coordinator", model="gemini-2.5-flash", description="Sutradhara AI productivity coordinator.", instruction="You are Sutradhara. Route: tasks/todo to task_agent, schedule/calendar to schedule_agent, notes to notes_agent, brief/plan my day to workflow_team. Default user_id is user001.", sub_agents=[task_agent, schedule_agent, notes_agent, workflow_team])
