class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        len_r = len(image)
        len_c = len(image[0])
        if image[sr][sc] == color:
            return image

        def fill(point, start_color, new_color):
            r, c = point[0], point[1]
            if min(r, c) < 0 or len_r <= r or len_c <= c or image[r][c] != start_color:
                return
    
            image[r][c] = new_color
 
            fill((r-1, c), start_color, new_color)
            fill((r, c-1), start_color, new_color)
            fill((r, c+1), start_color, new_color)
            fill((r+1, c), start_color, new_color)
            



        fill((sr,sc), image[sr][sc], color)
        return image