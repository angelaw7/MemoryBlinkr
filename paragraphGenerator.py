import cohere


def generateParagraph(length):
    api_file = open("apiKey.txt")
    API_KEY = api_file.readline().strip()

    co = cohere.Client(API_KEY)

    prediction = co.generate(
                prompt='Give me a random paragraph that ends within the token limit',
                max_tokens=length)

    paragraph = 'prediction: {}'.format(prediction.generations[0].text)
