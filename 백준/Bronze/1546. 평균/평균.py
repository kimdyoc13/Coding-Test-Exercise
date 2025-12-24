N = int(input())

Score = list(map(int, input().split()))

Score

Chandged_Score = [((i / max(Score)) * 100) for i in Score]

print(sum(Chandged_Score) / len(Chandged_Score))