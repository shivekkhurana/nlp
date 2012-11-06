class NgramIterators:
    ##########################################################################
    # Ngram iteration
    ##########################################################################

    # add a flag to pad the sequence so we get peripheral ngrams?
    def __init__(self):
        pass


    def ngrams(self, sequence, n, pad_left=False, pad_right=False, pad_symbol=None):
        """
        Return a sequence of ngrams from a sequence of items.  For example:

            >>> from nltk.util import ngrams
            >>> ngrams([1,2,3,4,5], 3)
            [(1, 2, 3), (2, 3, 4), (3, 4, 5)]

        Use ingram for an iterator version of this function.  Set pad_left
        or pad_right to true in order to get additional ngrams:

            >>> ngrams([1,2,3,4,5], 2, pad_right=True)
            [(1, 2), (2, 3), (3, 4), (4, 5), (5, None)]

        :param sequence: the source data to be converted into ngrams
        :type sequence: sequence or iter
        :param n: the degree of the ngrams
        :type n: int
        :param pad_left: whether the ngrams should be left-padded
        :type pad_left: bool
        :param pad_right: whether the ngrams should be right-padded
        :type pad_right: bool
        :param pad_symbol: the symbol to use for padding (default is None)
        :type pad_symbol: any
        :rtype: list(tuple)
        """

        if pad_left:
            sequence = chain((pad_symbol,) * (n-1), sequence)
        if pad_right:
            sequence = chain(sequence, (pad_symbol,) * (n-1))
        sequence = list(sequence)

        count = max(0, len(sequence) - n + 1)
        return [tuple(sequence[i:i+n]) for i in range(count)]

    def bigrams(self, sequence, **kwargs):
        """
        Return a sequence of bigrams from a sequence of items.  For example:

            >>> from nltk.util import bigrams
            >>> bigrams([1,2,3,4,5])
            [(1, 2), (2, 3), (3, 4), (4, 5)]

        Use ibigrams for an iterator version of this function.

        :param sequence: the source data to be converted into bigrams
        :type sequence: sequence or iter
        :rtype: list(tuple)
        """
        return ngrams(sequence, 2, **kwargs)

    def trigrams(self, sequence, **kwargs):
        """
        Return a sequence of trigrams from a sequence of items.  For example:

            >>> from nltk.util import trigrams
            >>> trigrams([1,2,3,4,5])
            [(1, 2, 3), (2, 3, 4), (3, 4, 5)]

        Use itrigrams for an iterator version of this function.

        :param sequence: the source data to be converted into trigrams
        :type sequence: sequence or iter
        :rtype: list(tuple)
        """
        return ngrams(sequence, 3, **kwargs)

    def ingrams(self, sequence, n, pad_left=False, pad_right=False, pad_symbol=None):
        """
        Return the ngrams generated from a sequence of items, as an iterator.
        For example:

            >>> from nltk.util import ingrams
            >>> list(ingrams([1,2,3,4,5], 3))
            [(1, 2, 3), (2, 3, 4), (3, 4, 5)]

        Use ngrams for a list version of this function.  Set pad_left
        or pad_right to true in order to get additional ngrams:

            >>> list(ingrams([1,2,3,4,5], 2, pad_right=True))
            [(1, 2), (2, 3), (3, 4), (4, 5), (5, None)]

        :param sequence: the source data to be converted into ngrams
        :type sequence: sequence or iter
        :param n: the degree of the ngrams
        :type n: int
        :param pad_left: whether the ngrams should be left-padded
        :type pad_left: bool
        :param pad_right: whether the ngrams should be right-padded
        :type pad_right: bool
        :param pad_symbol: the symbol to use for padding (default is None)
        :type pad_symbol: any
        :rtype: iter(tuple)
        """

        sequence = iter(sequence)
        if pad_left:
            sequence = chain((pad_symbol,) * (n-1), sequence)
        if pad_right:
            sequence = chain(sequence, (pad_symbol,) * (n-1))

        history = []
        while n > 1:
            history.append(sequence.next())
            n -= 1
        for item in sequence:
            history.append(item)
            yield tuple(history)
            del history[0]

    def ibigrams(self, sequence, **kwargs):
        """
        Return the bigrams generated from a sequence of items, as an iterator.
        For example:

            >>> from nltk.util import ibigrams
            >>> list(ibigrams([1,2,3,4,5]))
            [(1, 2), (2, 3), (3, 4), (4, 5)]

        Use bigrams for a list version of this function.

        :param sequence: the source data to be converted into bigrams
        :type sequence: sequence or iter
        :rtype: iter(tuple)
        """

        for item in ingrams(sequence, 2, **kwargs):
            yield item

    def itrigrams(self,sequence, **kwargs):
        """
        Return the trigrams generated from a sequence of items, as an iterator.
        For example:

            >>> from nltk.util import itrigrams
            >>> list(itrigrams([1,2,3,4,5]))
            [(1, 2, 3), (2, 3, 4), (3, 4, 5)]

        Use trigrams for a list version of this function.

        :param sequence: the source data to be converted into trigrams
        :type sequence: sequence or iter
        :rtype: iter(tuple)
        """

        for item in ingrams(sequence, 3, **kwargs):
            yield item