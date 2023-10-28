def maximalRectangle(matrix):
    if not matrix:
        return 0

    rows = len(matrix)
    cols = len(matrix[0])
    heights = [0] * cols
    max_area = 0

    for row in matrix:
        for i in range(cols):
            if row[i] == '1':
                heights[i] += 1
            else:
                heights[i] = 0

        stack = [-1]
        for i in range(cols):
            while stack[-1] != -1 and heights[stack[-1]] >= heights[i]:
                h = heights[stack.pop()]
                w = i - stack[-1] - 1
                max_area = max(max_area, h * w)
            stack.append(i)

        while stack[-1] != -1:
            h = heights[stack.pop()]
            w = cols - stack[-1] - 1
            max_area = max(max_area, h * w)

    return max_area