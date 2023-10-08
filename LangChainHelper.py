from secret_key import OPENAI_API_KEY
import os
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SimpleSequentialChain, SequentialChain


os.environ['OPENAI_API_KEY'] = OPENAI_API_KEY
llm = OpenAI(temperature = 0.7)

def generate_rest_name_and_items(cuisine):

#---------CHAIN 1: RESTAURANT NAME---------
  prompt_template_name = PromptTemplate(
    input_variables = ['cuisine'],
    template = "I want to open a restaurant for {cuisine} food. Suggest a fancy name for this."
  )

  name_chain = LLMChain(llm=llm, prompt=prompt_template_name, output_key = "restaurant_name")

  #---------CHAIN 2: MENU ITEMS ---------
  prompt_template_items = PromptTemplate(
    input_variables = ['restaurant_name'],
    template = """Suggest some menu items for {restaurant_name}. Return it as a comma separated list."""
  )

  food_items_chain = LLMChain(llm=llm, prompt=prompt_template_items, output_key="menu_items")

  sequential_chain = SequentialChain(
    chains = [name_chain, food_items_chain],
    input_variables = ['cuisine'],
    output_variables = ['restaurant_name', 'menu_items']
  )

  sequential_response = sequential_chain({'cuisine': cuisine})

  return sequential_response


if __name__ == "__main__":
  print(generate_rest_name_and_items("Italian"))