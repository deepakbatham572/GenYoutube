from langchain.llms import HuggingFaceEndpoint
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_community.tools import DuckDuckGoSearchRun

def get_answer(prompt, video_length, creativity , api_key):

    title_template = PromptTemplate(

        input_variables=['subject'],
        template='Please come up with a title for a new Youtube Video on the {subject}'
    )

    script_template = PromptTemplate(

        input_variables=['title' , 'duration' , 'DuckDuckGo_Search'],
        template='Create a script for a Youtube Video on this tile for me. TITLE: {title} of duration: {duration} minutes using this search data {DuckDuckGo_Search}'
    )

    llm = HuggingFaceEndpoint(
            repo_id="mistralai/Mistral-7B-Instruct-v0.2",
            temperature=creativity,
            huggingfacehub_api_token=api_key
        )

    title_chain = LLMChain(llm = llm , prompt = title_template , verbose = True)
    script_chain = LLMChain(llm = llm , prompt = script_template , verbose = True)

    search = DuckDuckGoSearchRun()

    title = title_chain.invoke(prompt)
    
    search_result = search.run(prompt) 

    script = script_chain.run(title = title , duration = video_length , DuckDuckGo_Search = search_result)

    return search_result , title , script