semantic_network = {
    "Rahul": [
        ("is-a", "student"),
        ("studies", "Python")
    ],

    "Python": [
        ("is-a", "Programming language"),
        ("used-for", "AI")
    ],

    "AI": [
        ("is-a", "Technology")
    ],

    "dr sen": [
        ("teaches", "AI")
    ]
}


def display_network():
    print("\nSemantic Network")

    for concept, relationships in semantic_network.items():
        for relation, target in relationships:
            print(f"{concept} {relation} {target}")


def find_relationship(concept):
    if concept in semantic_network:
        print(f"\nRelationships of {concept}")

        for relation, target in semantic_network[concept]:
            print(f"{concept} {relation} {target}")
    else:
        print(f"{concept} not found in semantic network")


display_network()

while True:
    print("\n1. Search concept")
    print("2. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        concept = input("Enter concept: ")
        find_relationship(concept)

    elif choice == "2":
        print("Program ended")
        break

    else:
        print("Invalid choice")
