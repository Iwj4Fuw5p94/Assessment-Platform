# langchain_integration.py
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.llms import OpenAI
 
# Use Langchain's OpenAI integration (you can switch to Azure OpenAI by modifying the LLM)
llm = OpenAI(temperature=0.7)
 
# Define the template for question-answering
template = "Answer the following question: {question}"
prompt = PromptTemplate(input_variables=["question"], template=template)
chain = LLMChain(llm=llm, prompt=prompt)
 
def ask_question(question: str):
    answer = chain.run(question)
    return answer
 
# Test with a question
if __name__ == "__main__":
    question = "What is the largest mammal in the world?"
    answer = ask_question(question)
    print(f"Answer: {answer}")

# CLI OUTPUT:
# Answer: The largest mammal in the world is the blue whale.