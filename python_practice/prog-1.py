# # # def minimum_spending(n, m, a, b):
# # #     # Scenario 1: Buy individual tickets for all rides
# # #     individual_cost = n * a
# # #
# # #     # Scenario 2: Buy a ride ticket and any remaining individual tickets
# # #     ride_ticket_cost = (n // m) * b
# # #     remaining_rides = n % m
# # #     if remaining_rides > 0:
# # #         ride_ticket_cost += min(remaining_rides * a, b)
# # #
# # #     # Choose the minimum cost between the two scenarios
# # #     return min(individual_cost, ride_ticket_cost)
# # #
# # #
# # # # Read input values
# # # n, m, a, b = map(int, input().split(" "))
# # #
# # # # Calculate and print the minimum spending
# # # print(minimum_spending(n, m, a, b))
# #
# #
# # rows = int(input())
# # val = rows
# #
# # for i in range(1, val + 1):
# #     for j in range(1, val + 1):
# #         if(i == j or j == val - i + 1):
# #             print('*', end = '')
# #         else:
# #             print(' ', end = '')
# #     print()
#
#
# def max_ribbon_pieces(n, a, b, c):
#     dp = [0] + [-1] * n
#
#     for i in range(1, n + 1):
#         if i - a >= 0:
#             dp[i] = max(dp[i], dp[i - a] + 1)
#         if i - b >= 0:
#             dp[i] = max(dp[i], dp[i - b] + 1)
#         if i - c >= 0:
#             dp[i] = max(dp[i], dp[i - c] + 1)
#
#     return dp[n]
#
# # Input example
# input_values = input().split()
# n, a, b, c = map(int, input_values)
# result = max_ribbon_pieces(n, a, b, c)
# print(result)


# a = 7
# b = 1
# c = 0
# for i in range(0,10):
#     # if a%2!=0:
#     #     print(a)
#     # a = a+1
#     c = a*b
#     print(c)
#     b = b+1


# a = 7
# b = 1
# c = 0
# for i in range (1,11):
#     c = a*b
#     print(c)
#     b = b+1

for i in range(0, 10):

    for j in range(0, i + 1):
        print("* ", end="")

    print("\r")
