from bird import *
print("\nClass Instances Of:\n", bird._doc_)

polly = bird("Squawk, squawk!")
print("\nNumber Of Birds:", polly.count)
print("Polly Says:", polly.talk())

harry = bird("Tweet, tweet!")
print("\nNumber Of Birds:", harry.count)
print("Harry Says:", harry.talk()) 

