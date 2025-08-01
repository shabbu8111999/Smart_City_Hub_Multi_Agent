# Smart_City_Hub_Multi_Agent


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