import matplotlib.pyplot as plt

def plot_sentiments(sentiments):
    labels = sentiments.keys()
    values = sentiments.values()

    plt.figure(figsize=(6, 4))
    plt.bar(labels, values, color=['green', 'red', 'gray'])
    plt.xlabel("Sentiment")
    plt.ylabel("Number of Reviews")
    plt.title("Sentiment Analysis Results")
    
    plt.savefig("sentiment_graph.png")  # Saves the graph instead of showing
    print("Graph saved as sentiment_graph.png")
    
    # plt.show()  # Comment this out if running in terminal
