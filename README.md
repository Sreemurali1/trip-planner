# **TripPlanner Crew** 🌍✈️  

Welcome to the **TripPlanner Crew** project, powered by [crewAI](https://crewai.com)! 🚀  
This AI-driven travel assistant helps users **plan, organize, and optimize trips** by leveraging multiple AI agents. Whether you're planning a solo adventure, a family vacation, or a business trip, TripPlanner Crew intelligently curates the best itinerary, accommodations, and activities tailored to your preferences.  

---

## **🛠️ Features**  

✅ **AI-Powered Travel Planning** – Automatically generates personalized itineraries based on your interests, budget, and duration.  
✅ **Smart Destination Suggestions** – Recommends the best places to visit based on real-time data and trends.  
✅ **Efficient Route Optimization** – Finds the most time-effective travel routes and transportation options.  
✅ **Accommodation & Booking Assistance** – Suggests hotels, Airbnb stays, and flight options.  
✅ **Collaborative AI Agents** – Uses **crewAI** agents to manage different aspects of your trip, such as research, scheduling, and logistics.  

---

## **📥 Installation**  

Ensure you have **Python >=3.10 <3.13** installed on your system. This project uses [UV](https://docs.astral.sh/uv/) for seamless dependency management.  

First, install UV if you haven’t already:  

```bash
pip install uv
```

Next, navigate to your project directory and install the dependencies:

(Optional) Lock the dependencies and install them by using the CLI command:
```bash
crewai install
```
### Customizing

**Add your `OPENAI_API_KEY` into the `.env` file**

- Modify `src/trip_planner/config/agents.yaml` to define your agents
- Modify `src/trip_planner/config/tasks.yaml` to define your tasks
- Modify `src/trip_planner/crew.py` to add your own logic, tools and specific args
- Modify `src/trip_planner/main.py` to add custom inputs for your agents and tasks

## Running the Project

To kickstart your crew of AI agents and begin task execution, run this from the root folder of your project:

```bash
$ crewai run
```

This command initializes the trip_planner Crew, assembling the agents and assigning them tasks as defined in your configuration.

This example, unmodified, will run the create a `report.md` file with the output of a research on LLMs in the root folder.

## Understanding Your Crew

The trip_planner Crew is composed of multiple AI agents, each with unique roles, goals, and tools. These agents collaborate on a series of tasks, defined in `config/tasks.yaml`, leveraging their collective skills to achieve complex objectives. The `config/agents.yaml` file outlines the capabilities and configurations of each agent in your crew.

## Support

For support, questions, or feedback regarding the TripPlanner Crew or crewAI.
- Visit our [documentation](https://docs.crewai.com)
- Reach out to us through our [GitHub repository](https://github.com/joaomdmoura/crewai)
- [Join our Discord](https://discord.com/invite/X4JWnZnxPb)
- [Chat with our docs](https://chatg.pt/DWjSBZn)

Let's create wonders together with the power and simplicity of crewAI.
