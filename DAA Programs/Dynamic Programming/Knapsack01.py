# A Dynamic Programming based Python Program for 0-1 Knapsack problem
# Returns the maximum value that can be put in a knapsack of capacity W

def knapSack(val, wt, W, n):
    K = [[0 for x in range(W + 1)] for x in range(n + 1)]

    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i-1] <= w:
                K[i][w] = max(val[i-1] + K[i-1][w-wt[i-1]],  K[i-1][w])
            else:
                K[i][w] = K[i-1][w]
 
    return K[n][W]
 
def main():
    n = int(input('Enter number of items : '))
    value = input('Enter the values of the {} item(s) in order : '.format(n)).split()
    value = [int(v) for v in value]
    weight = input('Enter the positive weights of the {} item(s) in order : '.format(n)).split()
    weight = [int(w) for w in weight]
    capacity = int(input('Enter maximum weight : '))

    ans = knapSack(value, weight, capacity, n)
    print('The maximum value of items that can be carried :', ans)

if __name__ == "__main__":
    main() 
    print("The worst case time complexity is O(n*W).")