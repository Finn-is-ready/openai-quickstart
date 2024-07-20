from openai import OpenAI

client = OpenAI(api_key="sk-dzZ2slQ3Qvb64c4d8cFdA752Dc6e4e4086973f5bEc2195C9",base_url="https://api.xiaoai.plus/v1")

if __name__ == '__main__':


    response = client.chat.completions.create(
      model="gpt-4-turbo",
      messages=[
        {
          "role": "user",
          "content": [
            {"type": "text", "text": "介绍下这幅图?"},
            {
              "type": "image_url",
              "image_url": {
                "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg",
              },
            },
          ],
        }
      ],
      max_tokens=300,
    )

    print(response.choices[0])