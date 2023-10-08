# from .secrets import secret_key
# import streamlit as st
from secret_key import OPENAI_API_KEY
import os
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SimpleSequentialChain


# openai.api_key = st.secrets["OPENAI_API_KEY"]

os.environ['OPENAI_API_KEY'] = OPENAI_API_KEY

llm = OpenAI(temperature = 0.6) #temperature is how 'creative' you want your model to be, the higher though the riskier, can tend to make mistakes

# name = llm("I want to open a restaurant for Indian food. Suggest a fancy name for this")
# print(name)

#---------SIMPLE SEQUENTIAL CHAIN EXAMPLE---------
#You can use prompt templates to format and pass different cuisines
prompt_template_name = PromptTemplate(
  input_variables = ['cuisine'],
  template = "I want to open a restaurant for {cuisine} food. Suggest a fancy name for this."
)

#prompt_template_name.format(cuisine = "Filipino")

#Chain - makes it easier to pass prompt and input variables
name_chain = LLMChain(llm=llm, prompt=prompt_template_name)
name_response = name_chain.run("Filipino")
#print(name_chain)



#LET'S TRY AGAIN
prompt_template_items = PromptTemplate(
  input_variables = ['restaurant_name'],
  template = """Suggest some menu items for {restaurant_name}. Return it as a comma separated list."""
)

food_items_chain = LLMChain(llm=llm, prompt=prompt_template_items)

chain = SimpleSequentialChain(
  chains = [
    name_chain, 
    food_items_chain
  ]
)

response = chain.run("Filipino")
print(response)


#---------SEQUENTIAL CHAIN EXAMPLE---------