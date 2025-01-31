# from crewai_tools import SerperDevTool
# from typing import Type
# from pydantic import BaseModel, Field


# # Define the input schema for the tool
# class SerperDevToolInput(BaseModel):
#     """Input schema for SerperDevTool."""
#     user_query: str = Field(..., description="The user query for the tool.")


# # Define the custom tool
# class MySerperDevTool(SerperDevTool):
#     name: str = "SerperDev Tool"
#     description: str = (
#         "A tool that processes user queries and returns relevant search results using Serper API."
#     )
#     args_schema: Type[BaseModel] = SerperDevToolInput

#     def _run(self, user_query: str) -> str:
#         # Implement the functionality of the SerperDevTool
#         return f"Processing the user query: {user_query}"
