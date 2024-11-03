class Solution:
    def winningPlayerCount(self, n: int, pick: List[List[int]]) -> int:
        winners = []
        count = 0

        player_total_color = {}

        for i in range(len(pick)):
            if pick[i][0] not in player_total_color:
                player_total_color[pick[i][0]] = {}
            if pick[i][1] not in player_total_color[pick[i][0]]:
                player_total_color[pick[i][0]][pick[i][1]] = 0
            player_total_color[pick[i][0]][pick[i][1]] = player_total_color[pick[i][0]][pick[i][1]] + 1

            print(player_total_color)
        print("winners: ", winners)
        for player,color_count_dict in player_total_color.items():
            for color, count in color_count_dict.items():
                print(color, count)
                if count > player:
                    winners.append(player)

        print("winners: ", winners)
        return len(set(winners))
        
