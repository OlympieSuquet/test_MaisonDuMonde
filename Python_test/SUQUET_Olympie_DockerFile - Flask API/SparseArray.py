class SparseArray:
    def __init__(self, queries, strings):
        self.queries, self.strings = queries, strings

    def matchingStrings(self):
            results = {}
            for q in self.queries:
                #adding to the dictionnary the query q and the number of times it appears in strings
                #using list comprehension
                results[q] = len(list((s for s in self.strings if s == q)))
            return results