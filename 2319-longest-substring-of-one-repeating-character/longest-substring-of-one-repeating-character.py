class Solution(object):
    def longestRepeating(self, s, queryCharacters, queryIndices):
        n = len(s)

        left_char = ['']*(4*n)
        right_char = ['']*(4*n)
        prefix = [0]*(4*n)
        suffix = [0]*(4*n)
        best = [0]*(4*n)
        length = [0]*(4*n)

        def build(node,start,end):
            if start == end:
                left_char[node] = s[start]
                right_char[node] = s[start]
                prefix[node] = 1
                suffix[node] = 1
                best[node] =1
                length[node] =1
                return

            mid = (start + end) // 2

            build(node*2,start,mid)
            build(node*2+1,mid+1,end)

            merge(node)
        
        def merge(node):
            left = node*2
            right =node*2+1
            
            length[node] = length[left]+length[right]
            left_char[node] = left_char[left]
            right_char[node] = right_char[right]

            prefix[node] = prefix[left]
            suffix[node] = suffix[right]
            best[node] = max(best[left],best[right])

            if right_char[left] == left_char[right]:

                if prefix[left] == length[left]:
                    prefix[node] = length[left] + prefix[right]

                if suffix[right] == length[right]:
                    suffix[node] = length[right] + suffix[left]

                best[node] = max(
                    best[node],
                    suffix[left] + prefix[right]
                )


        def update(node, start, end, index, char):
            if start == end:
                left_char[node] = char
                right_char[node] = char
                prefix[node] = 1
                suffix[node] = 1
                best[node] = 1
                return

            mid = (start + end) // 2

            if index <= mid:
                update(node * 2, start, mid, index, char)
            else:
                update(node * 2 + 1, mid + 1, end, index, char)

            merge(node)

        build(1, 0, n - 1)

        answer = []

        for char, index in zip(queryCharacters, queryIndices):
            update(1, 0, n - 1, index, char)
            answer.append(best[1])

        return answer


        