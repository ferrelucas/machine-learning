topics = read.table("topics.txt", header=TRUE)
topics$hasCaelumer <- ifelse(topics$caelumers>=1, 1, 0)

print("Summary for post")
summary(topics$posts)

print("Summary for caelumers")
summary(topics$caelumers)

print("Correlacao entre solucionados e se 1 caelumer respondeu")
cor(topics$solved, topics$hasCaelumer)
