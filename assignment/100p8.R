mywage <- function(time) {
    list(result = time * 10000 + ifelse(time - 40 > 0, (time - 40) * 5000, 0))
}

b<-mywage(41)