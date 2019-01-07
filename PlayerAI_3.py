from BaseAI_3 import BaseAI

class PlayerAI(BaseAI):
    def __init__(self):
        self.possibleNewTiles = [2, 4]
        self.probability = 0.9

    def getMove(self, grid):
        depth = 0
        (child, _) = self.maximize(grid, -float("inf"), float("inf"), depth)
        # (child, _) = self.maximize(grid, -float("inf"), float("inf"))
        return child

    def maximize(self, grid, alpha, beta, depth):
    # def maximize(self, grid, alpha, beta):
        if depth > 3 or len(grid.getAvailableMoves()) == 0:
            return (None, self.heuristic(grid))

        moves = grid.getAvailableMoves()

        (maxChild, maxUtility) = (None, -float("inf"))

        for childIndex in moves:
            gridCopy1 = grid.clone()
            gridCopy1.move(childIndex)
            (_, utility) = self.minimize(gridCopy1, alpha, beta, depth + 1)
            # (_, utility) = self.minimize(gridCopy1, alpha, beta)

            if utility > maxUtility:
                (maxChild, maxUtility) = (childIndex, utility)

            if maxUtility >= beta:
                break

            if maxUtility > alpha:
                alpha = maxUtility

        return (maxChild, maxUtility)

    def minimize(self, grid, alpha, beta, depth):
    # def minimize(self, grid, alpha, beta):
        if depth > 2 or len(grid.getAvailableCells()) == 0:
            return (None, self.heuristic(grid))

        cells = grid.getAvailableCells()
        (minChild1, minUtility1) = (None, float("inf"))
        (minChild2, minUtility2) = (None, float("inf"))

        for set_value in self.possibleNewTiles:
            if set_value == 2:
                for childPos in cells:
                    gridCopy2 = grid.clone()
                    gridCopy2.setCellValue(childPos, set_value)
                    (_, utility) = self.maximize(gridCopy2, alpha, beta, depth + 1)

                    if utility < minUtility1:
                        (minChild1, minUtility1) = (childPos, utility)

                    if minUtility1 <= alpha:
                        break

                    if minUtility1 < beta:
                        beta = minUtility1

            if set_value == 4:
                for childPos in cells:
                    gridCopy3 = grid.clone()
                    gridCopy3.setCellValue(childPos, set_value)
                    (_, utility) = self.maximize(gridCopy3, alpha, beta, depth + 1)

                    if utility < minUtility2:
                        (minChild2, minUtility2) = (childPos, utility)

                    if minUtility2 <= alpha:
                        break

                    if minUtility2 < beta:
                        beta = minUtility2

        minUtility = self.probability * minUtility1 + (1 - self.probability) * minUtility2

        return (_, minUtility)

    def heuristic(self, grid):
        empty = 0
        mono = 0
        smooth = 0
        weightarray = []
        weightarray.append([1, 2, 3, 4])
        weightarray.append([2, 3, 4, 5])
        weightarray.append([3, 4, 5, 6])
        weightarray.append([4, 5, 6, 7])
        for i in range(grid.size):
            for j in range(grid.size):
                if grid.map[i][j] == 0:
                    empty += 1

                mono += grid.getCellValue((i, j)) * weightarray[i][j]

                pos1 = (i, j)
                pos2 = (i, j + 1)
                #
                if j < 3:
                    if grid.getCellValue(pos1) == grid.getCellValue(pos2):
                        smooth += 1
                #
                #     elif grid.getCellValue(pos1) > grid.getCellValue(pos2):
                #         mono -= 1
                #
                pos1 = (j, i)
                pos2 = (j + 1, i)
                #
                if j < 3:
                    if grid.getCellValue(pos1) == grid.getCellValue(pos2):
                        smooth += 1
                #     if grid.getCellValue(pos1) < grid.getCellValue(pos2):
                #         mono += 1
                #     elif grid.getCellValue(pos1) > grid.getCellValue(pos2):
                #         mono -= 1

        return mono + 100 * smooth