# from .secrets import secret_key
# import streamlit as st
from secret_key import OPENAI_API_KEY,SERPAPI_API_KEY
import os
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SimpleSequentialChain, SequentialChain, ConversationChain
from langchain.agents import AgentType, initialize_agent, load_tools
from langchain.memory import ConversationBufferMemory,ConversationBufferWindowMemory

# openai.api_key = st.secrets["OPENAI_API_KEY"]

os.environ['OPENAI_API_KEY'] = OPENAI_API_KEY
os.environ['SERPAPI_API_KEY'] = SERPAPI_API_KEY

llm = OpenAI(temperature = 0.7) #temperature is how 'creative' you want your model to be, the higher though the riskier, can tend to make mistakes

# name = llm("I want to open a restaurant for Indian food. Suggest a fancy name for this")
# print(name)

#---------SIMPLE SEQUENTIAL CHAIN EXAMPLE---------
#You can use prompt templates to format and pass different cuisines
# prompt_template_name = PromptTemplate(
#   input_variables = ['cuisine'],
#   template = "I want to open a restaurant for {cuisine} food. Suggest a fancy name for this."
# )

#prompt_template_name.format(cuisine = "Filipino")

#Chain - makes it easier to pass prompt and input variables
#name_chain = LLMChain(llm=llm, prompt=prompt_template_name)
#name_response = name_chain.run("Filipino")
#print(name_chain)



#LET'S TRY AGAIN
# prompt_template_items = PromptTemplate(
#   input_variables = ['restaurant_name'],
#   template = """Suggest some menu items for {restaurant_name}. Return it as a comma separated list."""
# )

#food_items_chain = LLMChain(llm=llm, prompt=prompt_template_items)

# chain = SimpleSequentialChain(
#   chains = [
#     name_chain, 
#     food_items_chain
#   ]
# )

#response = chain.run("Filipino")
# print(response)


#---------SEQUENTIAL CHAIN EXAMPLE---------
prompt_template_name = PromptTemplate(
  input_variables = ['cuisine'],
  template = "I want to open a restaurant for {cuisine} food. Suggest a fancy name for this."
)

# name_chain = LLMChain(llm=llm, prompt=prompt_template_name, output_key = "restaurant_name")

# prompt_template_items = PromptTemplate(
#   input_variables = ['restaurant_name'],
#   template = """Suggest some menu items for {restaurant_name}. Return it as a comma separated list."""
# )

# food_items_chain = LLMChain(llm=llm, prompt=prompt_template_items, output_key="menu_items")

# sequential_chain = SequentialChain(
#   chains = [name_chain, food_items_chain],
#   input_variables = ['cuisine'],
#   output_variables = ['restaurant_name', 'menu_items']
# )

# sequential_response = sequential_chain({'cuisine':'Filipino'})
#print(sequential_response)



#---------AGENTS EXAMPLE---------
# tools = load_tools(["wikipedia", "llm-math"], llm=llm)

#create agent
# agent = initialize_agent(
#   tools,
#   llm,
#   agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
#   verbose=True #gives step by step
# )

#agent_response = agent.run("When was Elon Musk born? What is his age right now in 2023?")
#print(agent_response)


#__SERPAPI example __
# serp_tools = load_tools(["serpapi", "llm-math"], llm=llm)

# agent = initialize_agent(
#   serp_tools,
#   llm,
#   agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
#   verbose=True #gives step by step
# )

# serp_agent_response = agent.run("What was the GDP of US in 2022 plus 5?")
# print(serp_agent_response)

#---------MEMORY EXAMPLE---------
#memory = ConversationBufferMemory()
#name_chain = LLMChain(llm=llm, prompt=prompt_template_name, memory=memory)
#name_response = name_chain.run("American")
#print(name_chain)
#print(chain.memory.buffer)

# convo = ConversationChain(llm=OpenAI(temperature=0.7))
# print(convo.prompt.template)

# print(convo.run("Who won the first cricket world cup?"))
# print(convo.run("What is 5 + 5?"))
# print(convo.run("Who was the captain of the winning team?"))

#print(convo.memory)
#print(convo.memory.buffer)

#remember only 1 last conversation exchange (one question-answer pair)
memory = ConversationBufferWindowMemory(k=1)

convo = ConversationChain(
  llm=OpenAI(temperature=0.6),
  memory=memory
)
#print(convo.prompt.template)

print(convo.run("Who won the first cricket world cup?"))
print(convo.run("What is 5 + 5?"))
print(convo.run("Who was the captain of the winning team?"))