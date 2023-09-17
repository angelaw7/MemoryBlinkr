import cohere


def comparePhrases(phrase1, phrase2):
    """
    Compare the similarities between two phrases using their levenshtein
    distance
    """
    n, m = len(phrase1), len(phrase2)

    dp = [[0 for i in range(m + 1)] for j in range(n + 1)]

    for j in range(m + 1):
        dp[0][j] = j

    for i in range(n + 1):
        dp[i][0] = i

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if phrase1[i - 1] == phrase2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(
                    dp[i - 1][j],  # Insertion
                    dp[i][j - 1],  # Deletion
                    dp[i - 1][j - 1],  # Replacement
                )

    return dp[n][m]


def generatePhrase(topic):
    """
    Generate a short phrase about a topic using cohere generate API
    """
    api_file = open("apiKey.txt")
    API_KEY = api_file.readline().strip()

    co = cohere.Client(API_KEY)

    prediction = co.generate(
        prompt=f"Write a one-sentence fact about {topic}",
        max_tokens=100,
    )

    list_of_generations = prediction.generations[0].split("\n")
    list_of_phrases = [phrase.strip()[3:] for phrase in list_of_generations]

    return list_of_phrases
