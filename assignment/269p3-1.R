pima <- read.csv('./data/pima2.csv', header = T)
result <- aggregate(pima['X'], list(diabetes = pima$diabetes), length)
result['rate'] <- result['X'] / sum(result['X']) * 100
#result <- by(pima[, 1], pima$diabetes, length)
#위 방식으로도 할 수 있음
result_table <- table(pima$diabetes)
par(mfrow = c(1, 2))
barplot(result_table, col = 1:2)
pie(result_table, col = 1:2)


