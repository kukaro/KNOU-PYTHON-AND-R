pima <- read.csv('./data/pima2.csv', header = T)
result <- aggregate(pima['X'], list(diabetes = pima$diabetes), length)
result['rate'] <- result['X'] / sum(result['X']) * 100

print(result)

result_table <- table(pima$diabetes)
par(mfrow = c(1, 2))
barplot(result_table, col = 1:2)
pie(result_table, col = 1:2)


