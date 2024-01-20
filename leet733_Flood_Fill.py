# Description
# An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.

# You are also given three integers sr, sc, and color. You should perform a flood fill on the image starting from the pixel image[sr][sc].

# To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color), and so on. Replace the color of all of the aforementioned pixels with color.

# Return the modified image after performing the flood fill.

 

# Example 1:


# Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2
# Output: [[2,2,2],[2,2,0],[2,0,1]]
# Explanation: From the center of the image with position (sr, sc) = (1, 1) (i.e., the red pixel), all pixels connected by a path of the same color as the starting pixel (i.e., the blue pixels) are colored with the new color.
# Note the bottom corner is not colored 2, because it is not 4-directionally connected to the starting pixel.
# Example 2:

# Input: image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, color = 0
# Output: [[0,0,0],[0,0,0]]
# Explanation: The starting pixel is already colored 0, so no changes are made to the image.
 

# Constraints:

# m == image.length
# n == image[i].length
# 1 <= m, n <= 50
# 0 <= image[i][j], color < 216
# 0 <= sr < m
# 0 <= sc < n

# Solution

# // Time Complexity : O(m*n) since in worst case we might have to change color for all the cells
# // Space Complexity : Amortized O(m*n) since we keep adding more indices, we can add 4 indices for each poped index
# // Did this code successfully run on Leetcode : Yes
# // Any problem you faced while coding this : No


# // Your code here along with comments explaining your approach
# Approach is to first change the sr,sc color. Save it in queue. Then, taking that as reference by popping it
# save the 4-directional cells(1 row and 1 column around main cell). Keep doing this till the queue is empty
# This makes sure we start from sr,sc cell and change the adjacent cells while also saving those, thus further
# updating cells connected to those

from collections import deque

def floodFill(image,sr,sc,color):
    indexQueue = deque()
    prevColor = image[sr][sc]
    rowLen = len(image)
    colLen = len(image[0])
    if color == image[sr][sc]:
        return image
    
    image[sr][sc] = color
    indexQueue.append([sr,sc])

    while indexQueue:
        rowCol = indexQueue.popleft()

        if rowCol[0] > 0 and image[rowCol[0]-1][rowCol[1]] == prevColor:
            image[rowCol[0]-1][rowCol[1]] = color
            indexQueue.append([rowCol[0]-1,rowCol[1]])

        if rowCol[1] > 0 and image[rowCol[0]][rowCol[1]-1] == prevColor:  
            image[rowCol[0]][rowCol[1]-1] = color     
            indexQueue.append([rowCol[0],rowCol[1]-1])   

        if rowCol[0]+1 < rowLen and image[rowCol[0]+1][rowCol[1]] == prevColor:
            image[rowCol[0]+1][rowCol[1]] = color
            indexQueue.append([rowCol[0]+1,rowCol[1]])
        
        if rowCol[1]+1 < colLen and image[rowCol[0]][rowCol[1]+1] == prevColor:
            image[rowCol[0]][rowCol[1]+1] = color
            indexQueue.append([rowCol[0],rowCol[1]+1])
    
    return image

if __name__ == "__main__":
    # image = [[1,1,1],[1,1,0],[1,0,1]]
    # sr = 1
    # sc = 1
    # color = 2

    image = [[0,0,0],[0,0,0]]
    sr = 0
    sc = 0
    color = 0
    print(floodFill(image,sr,sc,color))