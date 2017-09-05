class BubbleSort:
    unsorted_array = [ 1, 151, 6, 72, 23, 12, 6, 6 ]

    def bubbleSort(un_array):
        for i in range (0, len (un_array) - 1):
            for j in range (0, len (un_array) - i - 1):
                if un_array[ j ] > un_array[ j + 1 ]:
                    temp = un_array[ j + 1 ]
                    un_array[ j + 1 ] = un_array[ j ]
                    un_array[ j ] = temp
        return un_array


print (BubbleSort.bubbleSort (BubbleSort.unsorted_array))
