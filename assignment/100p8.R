mywage <- function(time) {
    list(result = time * 10000 + ifelse(time - 40 > 0, (time - 40) * 5000, 0))
}

sprintf('%d', mywage(40)$result)
sprintf('%d', mywage(41)$result)
