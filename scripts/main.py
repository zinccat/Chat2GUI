import openai
import prompts
import argparse
from key import key, base


def gpt(inputs, model="gpt-3.5-turbo", temperature=0):
    output = openai.ChatCompletion.create(
        model=model,
        messages=[
            {"role": "system", "content": prompts.pg},
            {"role": "user", "content": inputs},
        ],
        temperature=temperature,
        api_key=key,
        api_base=base,
    )
    return output.choices[0]["message"]["content"]


def gpt_stream(inputs, model="gpt-3.5-turbo", temperature=0):
    response = openai.ChatCompletion.create(
        model=model,
        messages=[
            {"role": "system", "content": prompts.pg},
            {"role": "user", "content": inputs},
        ],
        temperature=temperature,
        stream=True,
        api_key=key,
        api_base=base,
    )
    report = []
    output = ""
    for chunk in response:
        chunk_message = chunk["choices"][0]["delta"]  # extract the message
        if "content" in chunk_message.keys():
            print(chunk_message["content"], end="")
            report.append(chunk_message["content"])
            output = "".join(report).strip()
    return output


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("command", type=str)
    args = parser.parse_args()
    output = gpt_stream(args.command)
    with open("outputs/main.py", "w") as f:
        f.write(output)
