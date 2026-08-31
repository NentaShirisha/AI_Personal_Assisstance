import kagglehub


def main():
    p1 = kagglehub.dataset_download("reemmuharram/chatbot-qa-csv")
    p2 = kagglehub.dataset_download("grafstor/simple-dialogs-for-chatbot")
    print("DATASET1", p1)
    print("DATASET2", p2)


if __name__ == "__main__":
    main()
