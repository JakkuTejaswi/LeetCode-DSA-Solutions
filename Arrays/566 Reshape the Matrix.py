class Solution(object):
    def matrixReshape(self, mat, r, c):
        n=len(mat)
        m=len(mat[0])
        if n*m!=r*c:
            return mat
        else:
            flat=[]
            for row in mat:
                for num in row:
                    flat.append(num)
            result=[]
            for i in range(0, len(flat),c):
                result.append(flat[i:i+c])
        return result
