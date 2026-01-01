import langchain
from pydantic import Field,BaseModel
import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain.messages import HumanMessage
load_dotenv()
os.environ["GROQ_API_KEY"]=os.getenv("GROQ_API_KEY")

def get_answer_to_question(image_url:str):
    print(image_url)
    class Answer(BaseModel):
        question: str = Field(
        description="The full problem statement exactly as shown"
        )
        full_code: str = Field(
        description=(
            "The COMPLETE code exactly as required by the platform. "
            "Must include the original class name, all existing functions, "
            "method signatures, and only fill in missing logic. "
            "Do NOT omit or simplify any boilerplate."
        )
        )
        explanation: str = Field(
        description="Explanation, hints, or reasoning"
        )
    model=init_chat_model("groq:meta-llama/llama-4-scout-17b-16e-instruct")
    model_with_struc=model.with_structured_output(Answer)

    message = HumanMessage(    
        content=[
            {
                "type": "image_url",
                "image_url": {
                    "url": f"{image_url}"
                }
            }
        ]
    )

    response=(model_with_struc.invoke([message]))
    
    question=response.question
    answer=response.full_code

    formatted_code = answer.replace('\\n', '\n')
    if "class" not in formatted_code:
        get_answer_to_question(image_url)
       
    

    return formatted_code


# get_answer_to_question("https://res.cloudinary.com/dsloz7tfz/image/upload/v1767298398/uploads/rumuecpywoczjqkyekin.png")