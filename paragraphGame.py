# import cohere


# def generateParagraph(length):
#     api_file = open("apiKey.txt")
#     API_KEY = api_file.readline().strip()

#     co = cohere.Client(API_KEY)

#     prediction = co.generate(
#                 prompt='Give me a random paragraph that ends within the token limit without cutting off.'
#                        ' Do not include any other text in the responses, only the direct paragraph.'
#                        'Do not make the paragraph related to this prompt.',
#                 max_tokens=length)

#     paragraph = prediction.generations[0].text.strip()
#     return paragraph


# def compareParagraph(p1, p2):
#     n, m = len(p1), len(p2)
#     # Create an array of size nxm
#     dp = [[0 for i in range(m + 1)] for j in range(n + 1)]

#     # Base Case: When N = 0
#     for j in range(m + 1):
#         dp[0][j] = j
#     # Base Case: When M = 0
#     for i in range(n + 1):
#         dp[i][0] = i
#     # Transitions
#     for i in range(1, n + 1):
#         for j in range(1, m + 1):
#             if p1[i - 1] == p2[j - 1]:
#                 dp[i][j] = dp[i - 1][j - 1]
#             else:
#                 dp[i][j] = 1 + min(
#                     dp[i - 1][j],  # Insertion
#                     dp[i][j - 1],  # Deletion
#                     dp[i - 1][j - 1]  # Replacement
#                 )

#     return dp[n][m]


# p1 = generateParagraph(20)
# print(p1)
# p2 = input()

# print(compareParagraph(p1, p2))
