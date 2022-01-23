text = input()
count = int(input())

lambda_f = lambda t, c: t * c
res_lambda = lambda_f(text, count)
print(res_lambda)
