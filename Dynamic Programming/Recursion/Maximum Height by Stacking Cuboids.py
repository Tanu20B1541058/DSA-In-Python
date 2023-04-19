class Solution:
    def maxHeight(self, cuboids) -> int:
        w, l, h = 0, 1, 2
        # indivisual sorting
        for cub in cuboids:
            cub.sort()
        # sorting on the basis of width--> length--> height
        cuboids.sort(key=lambda a: (-a[0], -a[1], -a[2]))
        n = len(cuboids)
        maxheight, dp = 0, [0] * n
        for i in range(n):
            dp[i] = cuboids[i][h]
            for j in range(i):
                if cuboids[j][w] >= cuboids[i][w] and cuboids[j][l] >= cuboids[i][l] and cuboids[j][h] >= cuboids[i][h]:
                    dp[i] = max(dp[i], dp[j] + cuboids[i][h])
            maxheight = max(maxheight, dp[i])
        return maxheight
            

