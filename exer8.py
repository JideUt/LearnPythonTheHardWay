# Exercise 8
# Printing, Printing
# Just as the title implies, more printing practice

#set the variable formatter to equal 4 r format characters
formatter = "%r %r %r %r"

# print different statements using the formatter variable
# each print line uses a different tuple to include in the formatter variable

print(formatter % (1, 2, 3, 4))
print(formatter % ("one", "two", "three", "four"))
print(formatter % (True, False, False, True))
print(formatter % (formatter, formatter, formatter, formatter))
print(formatter % (
	"I had this thing",
	"That you could type up right.",
	"But it didn't sing.",
	"So I said goodnight."
))

# when printed, the last line uses both single and double quotations
# that is because the 3rd line includes a single quotation within the string
