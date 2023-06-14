#tests with cleverhans
import openai
import webbrowser

def  gen_images(prompt, n, size):
    image_resp = openai.Image.create(prompt=prompt, n=n, size=size),
    print(range(len(image_resp)))
    for i in range(len(image_resp)+1):
        webbrowser.open(image_resp[0]['data'][i]['url']),
            #print(image_resp[0]['data'][i]['url']),

def  auto_gen_prompts():
    print()

def main():
    openai.api_key = "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"
    models = openai.Model.list(),
    #completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Hello world"}])
    #print(completion.choices[0].message.content)
    gen_images("Snoop dogg der rapper aufm fujiyama", 2, "512x512")



if __name__ == "__main__":
    main()

