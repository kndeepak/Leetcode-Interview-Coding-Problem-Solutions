class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
         # Create a set to keep track of all players who have played at least one match
        all_players = set()
        # Create a dictionary to count the number of matches each player has lost
        losses = {}
        
        # Create sets to store players who meet the criteria
        not_lost_any_match = set()
        lost_one_match = set()
        
        # Iterate through the matches
        for winner, loser in matches:
            # Add both the winner and loser to the set of all players
            all_players.add(winner)
            all_players.add(loser)
            
            # Increase the count of losses for the loser in the dictionary
            if loser in losses:
                losses[loser] += 1
            else:
                losses[loser] = 1
        
        # Iterate through all players to categorize them
        for player in all_players:
            # Check if the player is not in the losses dictionary, meaning they have not lost any match
            if player not in losses:
                not_lost_any_match.add(player)
            # Check if the player has lost exactly one match
            elif losses[player] == 1:
                lost_one_match.add(player)
        # Sort the result lists in increasing order
        not_lost_any_match = sorted(list(not_lost_any_match))
        lost_one_match = sorted(list(lost_one_match))
        

        return [not_lost_any_match, lost_one_match]
