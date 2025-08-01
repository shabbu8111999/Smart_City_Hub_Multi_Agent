# Smart Support Hub – A Multi-Agent AI Helpdesk


## 🧠 Concept:

### Simulate a small organization of AI agents, like a customer support team for a smart city dashboard or a tech company.

### Each agent has a defined role (like in a swarm or human team), and together they solve incoming user queries collaboratively.



## 🔗 Tools and Technologies:


| Purpose	            |    Tool                        |
|-----------------------|--------------------------------|
| Agent                 |  framework LangChain           |
| Multi-agent workflows	|  LangGraph                     |
| Debugging/tracing	    |  LangSmith                     |   
| UI (optional)	        |  Streamlit / Flask             |
| LLM backend	        |  OpenAI / Ollama / Local model |



## 🧩 Project Architecture: AI Agent Team
### Each agent is a LangChain tool or LangGraph node.


| Agent Name                | Responsibility                                          
| ------------------------- | ------------------------------------------------------- 
| 🧾 Query Classifier Agent | Decides the type of user query (traffic, power, health) |
| 🚦 Traffic Support Agent  | Answers traffic-related queries                         |
| 🏥 Health Support Agent   | Handles hospital/healthcare questions                   |
| ⚡ Utility Agent          | Answers power/water queries                             |
| 🧠 Planner Agent          | Coordinates multi-agent actions if query is complex     |



## Steps that I used for this project enironment to setup


### Step-1: Created a Github Repo and cloned it in my Root folder
```bash
git clone (Your-Github-Repository-Link-of-Project)
```


### Step-2: After clonning the repo manually created template.py file for all the folders and files needed for this project
```bash
python template.py
```


### Step-3: Created a Conda Environment in the latest version of python
```bash
conda create -n city python=3.11 -y
```

To Activate Conda
```bash
conda activate city
```


### Step-4: After creating env installed the requirements.txt
```bash
pip install -r requirements.txt
```


### Step-5: The Start of building the city agent with workflows


#### 1. Traffic Agent Handles (smartCity/agents/traffic_agent.py)
🚗 Real-time traffic updates (e.g., roadblocks, congestion)

🛣️ Alternate routes or detours

🚧 Traffic rules or smart signals info


#### 2. Health Agent Handles (smartCity/agents/health_agent.py)
🩺 First aid and emergency health advice

🌡️ Common health condition guidance (e.g., heat stroke, cold)

⚠️ Rejects non-health queries politely


#### 3. Utility Agent Handles (smartCity/agents/utility_agent.py)
It is meant for Public Servant such as:

💡 Electricity (e.g., "Why is there a power cut?")

🚰 Water supply (e.g., "When will the water be restored?")

♻️ Waste management (e.g., "How is garbage collected in Zone B?")


#### 4. Classifier Agent Handles (smartCity/agents/classifier_agent.py)
🧠 Detects the intent of the user's query.

🗂️ Classifies into: health, traffic, pollution, utilities, or unknown.

🔁 Helps in routing the query to the correct agent.


#### 5. Planner Agent Handles (smartCity/agents/planner_agent.py)
📋 Generates a step-by-step plan for city-related problems.

🧭 Assists in operational planning for reported issues.

🔄 Can be chained with classifier for automatic delegation.


#### 6. Executor Agent Handles (smartCity/agents/executor_agent.py)
✅ Executes each plan step by simulating the task outcome.

✅ Converts task instructions into clear, formal action confirmations.

✅ Provides short responses without repeating the input step.


#### 7. Pollution Agent Handles (smartCity/agents/pollution_agent.py)
🚨 Monitors pollution levels and triggers health alerts.

🛑 Recommends actions like restricting outdoor activities.

🔁 Advises on increasing air quality monitoring measures.