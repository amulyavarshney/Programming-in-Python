# Python 3 program for recursive binary search. 
# Returns maximum value of items and their fractional amounts.

# def knapSack(val, wt, W, n):
#     if n == 0 or W == 0 :
#         return 0

#     if (wt[n-1] > W):
#         return knapSack(W, wt, val, n-1)
#     else:
#         return max(val[n-1] + knapSack(val, wt, W-wt[n-1], n-1), knapSack(val, wt, W, n-1))

def fractional_knapsack(value, weight, capacity):
    # index = [0, 1, 2, ..., n - 1] for n items
    index = list(range(len(value)))
    # contains ratios of values to weight
    ratio = [v/w for v, w in zip(value, weight)]
    # index is sorted according to value-to-weight ratio in decreasing order
    index.sort(key=lambda i: ratio[i], reverse=True)
 
    max_value = 0
    fractions = [0]*len(value)
    for i in index:
        # if the weight is less than capacity, we will add the whole fraction of that item else we will add an optimal fraction of the item.
        if weight[i] <= capacity:
            fractions[i] = 1
            max_value += value[i]
            capacity -= weight[i]
        else:
            fractions[i] = capacity/weight[i]
            max_value += value[i]*capacity/weight[i]
            break
 
    return max_value, fractions
 
def main():
    n = int(input('Enter number of items : '))
    value = input('Enter the values of the {} item(s) in order : '.format(n)).split()
    value = [int(v) for v in value]
    weight = input('Enter the positive weights of the {} item(s) in order : '.format(n)).split()
    weight = [int(w) for w in weight]
    capacity = int(input('Enter maximum weight : '))

    # ans = knapSack(value, weight, capacity, n)
    # print('The maximum value of items that can be carried :', ans)
    max_value, fractions = fractional_knapsack(value, weight, capacity)
    print('The maximum value of items that can be carried :', max_value)
    print('The fractions in which the items should be taken :', fractions)

if __name__ == "__main__":
    main()
    print("The worst case time complexity for knapsack problem using Greedy Approach is O(nlogn).")