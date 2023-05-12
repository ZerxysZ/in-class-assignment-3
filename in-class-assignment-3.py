from collections import Counter

def count_votes(votes):
    vote_counts = Counter(votes)

    if vote_counts['A'] > vote_counts['B']:
        return 'A'
    elif vote_counts['B'] > vote_counts['A']:
        return 'B'
    else:
        return 'Tie'

total_votes = int(input())
votes_sequence = input()
outcome = count_votes(votes_sequence)
print(outcome)